# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.0. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.0
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V2directionsprofilegeojsonScheduleDurationDuration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'nano': 'int',
        'negative': 'bool',
        'seconds': 'int',
        'zero': 'bool'
    }

    attribute_map = {
        'nano': 'nano',
        'negative': 'negative',
        'seconds': 'seconds',
        'zero': 'zero'
    }

    def __init__(self, nano=None, negative=None, seconds=None, zero=None):  # noqa: E501
        """V2directionsprofilegeojsonScheduleDurationDuration - a model defined in Swagger"""  # noqa: E501
        self._nano = None
        self._negative = None
        self._seconds = None
        self._zero = None
        self.discriminator = None
        if nano is not None:
            self.nano = nano
        if negative is not None:
            self.negative = negative
        if seconds is not None:
            self.seconds = seconds
        if zero is not None:
            self.zero = zero

    @property
    def nano(self):
        """Gets the nano of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501


        :return: The nano of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :rtype: int
        """
        return self._nano

    @nano.setter
    def nano(self, nano):
        """Sets the nano of this V2directionsprofilegeojsonScheduleDurationDuration.


        :param nano: The nano of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :type: int
        """

        self._nano = nano

    @property
    def negative(self):
        """Gets the negative of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501


        :return: The negative of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :rtype: bool
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this V2directionsprofilegeojsonScheduleDurationDuration.


        :param negative: The negative of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :type: bool
        """

        self._negative = negative

    @property
    def seconds(self):
        """Gets the seconds of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501


        :return: The seconds of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this V2directionsprofilegeojsonScheduleDurationDuration.


        :param seconds: The seconds of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

    @property
    def zero(self):
        """Gets the zero of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501


        :return: The zero of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :rtype: bool
        """
        return self._zero

    @zero.setter
    def zero(self, zero):
        """Sets the zero of this V2directionsprofilegeojsonScheduleDurationDuration.


        :param zero: The zero of this V2directionsprofilegeojsonScheduleDurationDuration.  # noqa: E501
        :type: bool
        """

        self._zero = zero

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V2directionsprofilegeojsonScheduleDurationDuration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2directionsprofilegeojsonScheduleDurationDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
