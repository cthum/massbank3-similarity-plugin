import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.similarity_post_request import SimilarityPostRequest  # noqa: E501
from openapi_server import util
from openapi_server.db import spectra

from matchms.importing import load_from_msp
from matchms import Spectrum, calculate_scores
from matchms.similarity import CosineGreedy

import numpy as np

def similarity_post(similarity_post_request=None):  # noqa: E501
    """Create a new similarity calculation.

     # noqa: E501

    :param similarity_post_request: a similarity job
    :type similarity_post_request: dict | bytes

    :rtype: Union[List[float], Tuple[List[float], int], Tuple[List[float], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        request = SimilarityPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
        mz = request.peak_list.mz
        intensity = request.peak_list.intensity

        query = Spectrum(mz=np.array(mz), intensities=np.array(intensity))

        scores = calculate_scores(references=spectra, queries=[query], similarity_function=CosineGreedy())
        matches = scores.scores_by_query(query, "CosineGreedy_score", sort=True)

        # TODO: Convert to response according to openapi specs
        # return matches
        return 'TODO: Return matches'
    
    return 'TODO: Return some error'


def version_get():  # noqa: E501
    """Get the version string of the implementation.

     # noqa: E501


    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    # Is this supposed to be JSON?
    return 'v0.1.0'
