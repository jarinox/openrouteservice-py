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

class MatrixRequest(object):
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
        'destinations': 'list[str]',
        'id': 'str',
        'locations': 'list[list[float]]',
        'metrics': 'list[str]',
        'resolve_locations': 'bool',
        'sources': 'list[str]',
        'units': 'str'
    }

    attribute_map = {
        'destinations': 'destinations',
        'id': 'id',
        'locations': 'locations',
        'metrics': 'metrics',
        'resolve_locations': 'resolve_locations',
        'sources': 'sources',
        'units': 'units'
    }

    def __init__(self, destinations=None, id=None, locations=None, metrics=None, resolve_locations=False, sources=None, units='m'):  # noqa: E501
        """MatrixRequest - a model defined in Swagger"""  # noqa: E501
        self._destinations = None
        self._id = None
        self._locations = None
        self._metrics = None
        self._resolve_locations = None
        self._sources = None
        self._units = None
        self.discriminator = None
        if destinations is not None:
            self.destinations = destinations
        if id is not None:
            self.id = id
        self.locations = locations
        if metrics is not None:
            self.metrics = metrics
        if resolve_locations is not None:
            self.resolve_locations = resolve_locations
        if sources is not None:
            self.sources = sources
        if units is not None:
            self.units = units

    @property
    def destinations(self):
        """Gets the destinations of this MatrixRequest.  # noqa: E501

        A list of indices that refers to the list of locations (starting with `0`). `{index_1},{index_2}[,{index_N} ...]` or `all` (default). `[0,3]` for the first and fourth locations   # noqa: E501

        :return: The destinations of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this MatrixRequest.

        A list of indices that refers to the list of locations (starting with `0`). `{index_1},{index_2}[,{index_N} ...]` or `all` (default). `[0,3]` for the first and fourth locations   # noqa: E501

        :param destinations: The destinations of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._destinations = destinations

    @property
    def id(self):
        """Gets the id of this MatrixRequest.  # noqa: E501

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :return: The id of this MatrixRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MatrixRequest.

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :param id: The id of this MatrixRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def locations(self):
        """Gets the locations of this MatrixRequest.  # noqa: E501

        List of comma separated lists of `longitude,latitude` coordinates in WGS 84 (EPSG:4326)  # noqa: E501

        :return: The locations of this MatrixRequest.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this MatrixRequest.

        List of comma separated lists of `longitude,latitude` coordinates in WGS 84 (EPSG:4326)  # noqa: E501

        :param locations: The locations of this MatrixRequest.  # noqa: E501
        :type: list[list[float]]
        """
        if locations is None:
            raise ValueError("Invalid value for `locations`, must not be `None`")  # noqa: E501

        self._locations = locations

    @property
    def metrics(self):
        """Gets the metrics of this MatrixRequest.  # noqa: E501

        Specifies a list of returned metrics. \"* `distance` - Returns distance matrix for specified points in defined `units`. * `duration` - Returns duration matrix for specified points in **seconds**.   # noqa: E501

        :return: The metrics of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this MatrixRequest.

        Specifies a list of returned metrics. \"* `distance` - Returns distance matrix for specified points in defined `units`. * `duration` - Returns duration matrix for specified points in **seconds**.   # noqa: E501

        :param metrics: The metrics of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["distance", "duration"]  # noqa: E501
        if not set(metrics).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `metrics` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(metrics) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._metrics = metrics

    @property
    def resolve_locations(self):
        """Gets the resolve_locations of this MatrixRequest.  # noqa: E501

        Specifies whether given locations are resolved or not. If the parameter value set to `true`, every element in `destinations` and `sources` will contain a `name` element that identifies the name of the closest street. Default is `false`.   # noqa: E501

        :return: The resolve_locations of this MatrixRequest.  # noqa: E501
        :rtype: bool
        """
        return self._resolve_locations

    @resolve_locations.setter
    def resolve_locations(self, resolve_locations):
        """Sets the resolve_locations of this MatrixRequest.

        Specifies whether given locations are resolved or not. If the parameter value set to `true`, every element in `destinations` and `sources` will contain a `name` element that identifies the name of the closest street. Default is `false`.   # noqa: E501

        :param resolve_locations: The resolve_locations of this MatrixRequest.  # noqa: E501
        :type: bool
        """

        self._resolve_locations = resolve_locations

    @property
    def sources(self):
        """Gets the sources of this MatrixRequest.  # noqa: E501

        A list of indices that refers to the list of locations (starting with `0`). `{index_1},{index_2}[,{index_N} ...]` or `all` (default). example `[0,3]` for the first and fourth locations   # noqa: E501

        :return: The sources of this MatrixRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this MatrixRequest.

        A list of indices that refers to the list of locations (starting with `0`). `{index_1},{index_2}[,{index_N} ...]` or `all` (default). example `[0,3]` for the first and fourth locations   # noqa: E501

        :param sources: The sources of this MatrixRequest.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def units(self):
        """Gets the units of this MatrixRequest.  # noqa: E501

        Specifies the distance unit. Default: m.  # noqa: E501

        :return: The units of this MatrixRequest.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this MatrixRequest.

        Specifies the distance unit. Default: m.  # noqa: E501

        :param units: The units of this MatrixRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["m", "km", "mi"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

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
        if issubclass(MatrixRequest, dict):
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
        if not isinstance(other, MatrixRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
