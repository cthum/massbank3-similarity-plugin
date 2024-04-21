import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.similarity_post_request import SimilarityPostRequest  # noqa: E501
from openapi_server.models.similarity_score_list_inner import SimilarityScoreListInner  # noqa: E501
from openapi_server import util
from openapi_server.db import spectra

from matchms.importing import load_from_msp
from matchms import Spectrum, calculate_scores
from matchms.similarity import CosineGreedy

import numpy as np


def similarity_post(body):  # noqa: E501
    """Create a new similarity calculation.

     # noqa: E501

    :param similarity_post_request: a similarity job
    :type similarity_post_request: dict | bytes

    :rtype: Union[List[SimilarityScoreListInner], Tuple[List[SimilarityScoreListInner], int], Tuple[List[SimilarityScoreListInner], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        request = SimilarityPostRequest.from_dict(body)

        mz = []
        intensities = []

        for peak in request.peak_list:
            mz.append(peak.mz)
            intensities.append(peak.intensity)

        query = Spectrum(mz=np.array(mz), intensities=np.array(intensities))

        if len(request.reference_spectra_list) > 0:
            def filter_fn(spectrum):
                return spectrum.metadata['id'] in request.reference_spectra_list

            references = list(filter(filter_fn, spectra))

            scores = calculate_scores(references, [query], CosineGreedy())
        else:
            scores = calculate_scores(spectra, [query], CosineGreedy())
        matches = scores.scores_by_query(query, 'CosineGreedy_score', sort=True)

        match_list = []

        for match in matches:
            match_list.append(SimilarityScoreListInner(match[0].metadata['id'], match[1][0]))

        return match_list


def version_get():  # noqa: E501
    """Get the version string of the implementation.

     # noqa: E501


    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'cosine similarity 1.0.0'
