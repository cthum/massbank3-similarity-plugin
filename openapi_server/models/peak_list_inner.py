from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class PeakListInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mz=None, intensity=None):  # noqa: E501
        """PeakListInner - a model defined in OpenAPI

        :param mz: The mz of this PeakListInner.  # noqa: E501
        :type mz: float
        :param intensity: The intensity of this PeakListInner.  # noqa: E501
        :type intensity: float
        """
        self.openapi_types = {
            'mz': float,
            'intensity': float
        }

        self.attribute_map = {
            'mz': 'mz',
            'intensity': 'intensity'
        }

        self._mz = mz
        self._intensity = intensity

    @classmethod
    def from_dict(cls, dikt) -> 'PeakListInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The peak_list_inner of this PeakListInner.  # noqa: E501
        :rtype: PeakListInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mz(self) -> float:
        """Gets the mz of this PeakListInner.

        m/z value  # noqa: E501

        :return: The mz of this PeakListInner.
        :rtype: float
        """
        return self._mz

    @mz.setter
    def mz(self, mz: float):
        """Sets the mz of this PeakListInner.

        m/z value  # noqa: E501

        :param mz: The mz of this PeakListInner.
        :type mz: float
        """

        self._mz = mz

    @property
    def intensity(self) -> float:
        """Gets the intensity of this PeakListInner.

        intensity value  # noqa: E501

        :return: The intensity of this PeakListInner.
        :rtype: float
        """
        return self._intensity

    @intensity.setter
    def intensity(self, intensity: float):
        """Sets the intensity of this PeakListInner.

        intensity value  # noqa: E501

        :param intensity: The intensity of this PeakListInner.
        :type intensity: float
        """

        self._intensity = intensity
