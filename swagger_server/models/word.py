# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Word(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, value: str=None):  # noqa: E501
        """Word - a model defined in Swagger

        :param value: The value of this Word.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'value': str
        }

        self.attribute_map = {
            'value': 'value'
        }
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Word':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Word of this Word.  # noqa: E501
        :rtype: Word
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this Word.


        :return: The value of this Word.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Word.


        :param value: The value of this Word.
        :type value: str
        """

        self._value = value
