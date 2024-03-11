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

class GraphExportService(object):
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
        'bbox': 'list[list[float]]',
        'id': 'str'
    }

    attribute_map = {
        'bbox': 'bbox',
        'id': 'id'
    }

    def __init__(self, bbox=None, id=None):  # noqa: E501
        """GraphExportService - a model defined in Swagger"""  # noqa: E501
        self._bbox = None
        self._id = None
        self.discriminator = None
        self.bbox = bbox
        if id is not None:
            self.id = id

    @property
    def bbox(self):
        """Gets the bbox of this GraphExportService.  # noqa: E501

        The bounding box to use for the request as an array of `longitude/latitude` pairs  # noqa: E501

        :return: The bbox of this GraphExportService.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this GraphExportService.

        The bounding box to use for the request as an array of `longitude/latitude` pairs  # noqa: E501

        :param bbox: The bbox of this GraphExportService.  # noqa: E501
        :type: list[list[float]]
        """
        if bbox is None:
            raise ValueError("Invalid value for `bbox`, must not be `None`")  # noqa: E501

        self._bbox = bbox

    @property
    def id(self):
        """Gets the id of this GraphExportService.  # noqa: E501

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :return: The id of this GraphExportService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GraphExportService.

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :param id: The id of this GraphExportService.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(GraphExportService, dict):
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
        if not isinstance(other, GraphExportService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
