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

class JSONIndividualRouteResponseExtras(object):
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
        'summary': 'list[JSONExtraSummary]',
        'values': 'list[list[int]]'
    }

    attribute_map = {
        'summary': 'summary',
        'values': 'values'
    }

    def __init__(self, summary=None, values=None):  # noqa: E501
        """JSONIndividualRouteResponseExtras - a model defined in Swagger"""  # noqa: E501
        self._summary = None
        self._values = None
        self.discriminator = None
        if summary is not None:
            self.summary = summary
        if values is not None:
            self.values = values

    @property
    def summary(self):
        """Gets the summary of this JSONIndividualRouteResponseExtras.  # noqa: E501

        List representing the summary of the extra info items.  # noqa: E501

        :return: The summary of this JSONIndividualRouteResponseExtras.  # noqa: E501
        :rtype: list[JSONExtraSummary]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this JSONIndividualRouteResponseExtras.

        List representing the summary of the extra info items.  # noqa: E501

        :param summary: The summary of this JSONIndividualRouteResponseExtras.  # noqa: E501
        :type: list[JSONExtraSummary]
        """

        self._summary = summary

    @property
    def values(self):
        """Gets the values of this JSONIndividualRouteResponseExtras.  # noqa: E501

        A list of values representing a section of the route. The individual values are:  Value 1: Indice of the staring point of the geometry for this section, Value 2: Indice of the end point of the geoemetry for this sections, Value 3: [Value](https://GIScience.github.io/openrouteservice/documentation/extra-info/Extra-Info.html) assigned to this section.  # noqa: E501

        :return: The values of this JSONIndividualRouteResponseExtras.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this JSONIndividualRouteResponseExtras.

        A list of values representing a section of the route. The individual values are:  Value 1: Indice of the staring point of the geometry for this section, Value 2: Indice of the end point of the geoemetry for this sections, Value 3: [Value](https://GIScience.github.io/openrouteservice/documentation/extra-info/Extra-Info.html) assigned to this section.  # noqa: E501

        :param values: The values of this JSONIndividualRouteResponseExtras.  # noqa: E501
        :type: list[list[int]]
        """

        self._values = values

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
        if issubclass(JSONIndividualRouteResponseExtras, dict):
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
        if not isinstance(other, JSONIndividualRouteResponseExtras):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
