# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.1. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.1
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2007(object):
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
        'locations': 'list[SnappingResponseLocations]',
        'metadata': 'GeoJSONSnappingResponseMetadata'
    }

    attribute_map = {
        'locations': 'locations',
        'metadata': 'metadata'
    }

    def __init__(self, locations=None, metadata=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._locations = None
        self._metadata = None
        self.discriminator = None
        if locations is not None:
            self.locations = locations
        if metadata is not None:
            self.metadata = metadata

    @property
    def locations(self):
        """Gets the locations of this InlineResponse2007.  # noqa: E501

        The snapped locations as coordinates and snapping distance.  # noqa: E501

        :return: The locations of this InlineResponse2007.  # noqa: E501
        :rtype: list[SnappingResponseLocations]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this InlineResponse2007.

        The snapped locations as coordinates and snapping distance.  # noqa: E501

        :param locations: The locations of this InlineResponse2007.  # noqa: E501
        :type: list[SnappingResponseLocations]
        """

        self._locations = locations

    @property
    def metadata(self):
        """Gets the metadata of this InlineResponse2007.  # noqa: E501


        :return: The metadata of this InlineResponse2007.  # noqa: E501
        :rtype: GeoJSONSnappingResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineResponse2007.


        :param metadata: The metadata of this InlineResponse2007.  # noqa: E501
        :type: GeoJSONSnappingResponseMetadata
        """

        self._metadata = metadata

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
