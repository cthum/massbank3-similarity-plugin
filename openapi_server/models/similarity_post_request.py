from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.peak_list_inner import PeakListInner
from openapi_server import util

from openapi_server.models.peak_list_inner import PeakListInner  # noqa: E501

class SimilarityPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, peak_list=None, reference_spectra_list=None):  # noqa: E501
        """SimilarityPostRequest - a model defined in OpenAPI

        :param peak_list: The peak_list of this SimilarityPostRequest.  # noqa: E501
        :type peak_list: List[PeakListInner]
        :param reference_spectra_list: The reference_spectra_list of this SimilarityPostRequest.  # noqa: E501
        :type reference_spectra_list: List[str]
        """
        self.openapi_types = {
            'peak_list': List[PeakListInner],
            'reference_spectra_list': List[str]
        }

        self.attribute_map = {
            'peak_list': 'peak_list',
            'reference_spectra_list': 'reference_spectra_list'
        }

        self._peak_list = peak_list
        self._reference_spectra_list = reference_spectra_list

    @classmethod
    def from_dict(cls, dikt) -> 'SimilarityPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _similarity_post_request of this SimilarityPostRequest.  # noqa: E501
        :rtype: SimilarityPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def peak_list(self) -> List[PeakListInner]:
        """Gets the peak_list of this SimilarityPostRequest.

        the peak list of the query spectrum  # noqa: E501

        :return: The peak_list of this SimilarityPostRequest.
        :rtype: List[PeakListInner]
        """
        return self._peak_list

    @peak_list.setter
    def peak_list(self, peak_list: List[PeakListInner]):
        """Sets the peak_list of this SimilarityPostRequest.

        the peak list of the query spectrum  # noqa: E501

        :param peak_list: The peak_list of this SimilarityPostRequest.
        :type peak_list: List[PeakListInner]
        """

        self._peak_list = peak_list

    @property
    def reference_spectra_list(self) -> List[str]:
        """Gets the reference_spectra_list of this SimilarityPostRequest.

        the reference spectra list, list of ACCESSION strings  # noqa: E501

        :return: The reference_spectra_list of this SimilarityPostRequest.
        :rtype: List[str]
        """
        return self._reference_spectra_list

    @reference_spectra_list.setter
    def reference_spectra_list(self, reference_spectra_list: List[str]):
        """Sets the reference_spectra_list of this SimilarityPostRequest.

        the reference spectra list, list of ACCESSION strings  # noqa: E501

        :param reference_spectra_list: The reference_spectra_list of this SimilarityPostRequest.
        :type reference_spectra_list: List[str]
        """

        self._reference_spectra_list = reference_spectra_list
