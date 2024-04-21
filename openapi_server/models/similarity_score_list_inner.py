from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class SimilarityScoreListInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accession=None, similarity_score=None):  # noqa: E501
        """SimilarityScoreListInner - a model defined in OpenAPI

        :param accession: The accession of this SimilarityScoreListInner.  # noqa: E501
        :type accession: str
        :param similarity_score: The similarity_score of this SimilarityScoreListInner.  # noqa: E501
        :type similarity_score: float
        """
        self.openapi_types = {
            'accession': str,
            'similarity_score': float
        }

        self.attribute_map = {
            'accession': 'accession',
            'similarity_score': 'similarity_score'
        }

        self._accession = accession
        self._similarity_score = similarity_score

    @classmethod
    def from_dict(cls, dikt) -> 'SimilarityScoreListInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The similarity_score_list_inner of this SimilarityScoreListInner.  # noqa: E501
        :rtype: SimilarityScoreListInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accession(self) -> str:
        """Gets the accession of this SimilarityScoreListInner.


        :return: The accession of this SimilarityScoreListInner.
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession: str):
        """Sets the accession of this SimilarityScoreListInner.


        :param accession: The accession of this SimilarityScoreListInner.
        :type accession: str
        """

        self._accession = accession

    @property
    def similarity_score(self) -> float:
        """Gets the similarity_score of this SimilarityScoreListInner.


        :return: The similarity_score of this SimilarityScoreListInner.
        :rtype: float
        """
        return self._similarity_score

    @similarity_score.setter
    def similarity_score(self, similarity_score: float):
        """Sets the similarity_score of this SimilarityScoreListInner.


        :param similarity_score: The similarity_score of this SimilarityScoreListInner.
        :type similarity_score: float
        """

        self._similarity_score = similarity_score