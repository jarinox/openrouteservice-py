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

class JsonExportResponseEdgesExtra(object):
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
        'edge_id': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'edge_id': 'edgeId',
        'extra': 'extra'
    }

    def __init__(self, edge_id=None, extra=None):  # noqa: E501
        """JsonExportResponseEdgesExtra - a model defined in Swagger"""  # noqa: E501
        self._edge_id = None
        self._extra = None
        self.discriminator = None
        if edge_id is not None:
            self.edge_id = edge_id
        if extra is not None:
            self.extra = extra

    @property
    def edge_id(self):
        """Gets the edge_id of this JsonExportResponseEdgesExtra.  # noqa: E501

        Id of the corresponding edge in the graph  # noqa: E501

        :return: The edge_id of this JsonExportResponseEdgesExtra.  # noqa: E501
        :rtype: str
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this JsonExportResponseEdgesExtra.

        Id of the corresponding edge in the graph  # noqa: E501

        :param edge_id: The edge_id of this JsonExportResponseEdgesExtra.  # noqa: E501
        :type: str
        """

        self._edge_id = edge_id

    @property
    def extra(self):
        """Gets the extra of this JsonExportResponseEdgesExtra.  # noqa: E501

        Extra info stored on the edge  # noqa: E501

        :return: The extra of this JsonExportResponseEdgesExtra.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this JsonExportResponseEdgesExtra.

        Extra info stored on the edge  # noqa: E501

        :param extra: The extra of this JsonExportResponseEdgesExtra.  # noqa: E501
        :type: object
        """

        self._extra = extra

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
        if issubclass(JsonExportResponseEdgesExtra, dict):
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
        if not isinstance(other, JsonExportResponseEdgesExtra):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
