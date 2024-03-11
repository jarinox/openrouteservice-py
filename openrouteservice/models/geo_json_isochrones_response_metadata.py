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

class GeoJSONIsochronesResponseMetadata(object):
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
        'attribution': 'str',
        'engine': 'GeoJSONIsochronesResponseMetadataEngine',
        'id': 'str',
        'osm_file_md5_hash': 'str',
        'query': 'IsochronesProfileBody',
        'service': 'str',
        'system_message': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'attribution': 'attribution',
        'engine': 'engine',
        'id': 'id',
        'osm_file_md5_hash': 'osm_file_md5_hash',
        'query': 'query',
        'service': 'service',
        'system_message': 'system_message',
        'timestamp': 'timestamp'
    }

    def __init__(self, attribution=None, engine=None, id=None, osm_file_md5_hash=None, query=None, service=None, system_message=None, timestamp=None):  # noqa: E501
        """GeoJSONIsochronesResponseMetadata - a model defined in Swagger"""  # noqa: E501
        self._attribution = None
        self._engine = None
        self._id = None
        self._osm_file_md5_hash = None
        self._query = None
        self._service = None
        self._system_message = None
        self._timestamp = None
        self.discriminator = None
        if attribution is not None:
            self.attribution = attribution
        if engine is not None:
            self.engine = engine
        if id is not None:
            self.id = id
        if osm_file_md5_hash is not None:
            self.osm_file_md5_hash = osm_file_md5_hash
        if query is not None:
            self.query = query
        if service is not None:
            self.service = service
        if system_message is not None:
            self.system_message = system_message
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def attribution(self):
        """Gets the attribution of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        Copyright and attribution information  # noqa: E501

        :return: The attribution of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this GeoJSONIsochronesResponseMetadata.

        Copyright and attribution information  # noqa: E501

        :param attribution: The attribution of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: str
        """

        self._attribution = attribution

    @property
    def engine(self):
        """Gets the engine of this GeoJSONIsochronesResponseMetadata.  # noqa: E501


        :return: The engine of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: GeoJSONIsochronesResponseMetadataEngine
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this GeoJSONIsochronesResponseMetadata.


        :param engine: The engine of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: GeoJSONIsochronesResponseMetadataEngine
        """

        self._engine = engine

    @property
    def id(self):
        """Gets the id of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        ID of the request (as passed in by the query)  # noqa: E501

        :return: The id of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeoJSONIsochronesResponseMetadata.

        ID of the request (as passed in by the query)  # noqa: E501

        :param id: The id of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def osm_file_md5_hash(self):
        """Gets the osm_file_md5_hash of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        The MD5 hash of the OSM planet file that was used for generating graphs  # noqa: E501

        :return: The osm_file_md5_hash of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._osm_file_md5_hash

    @osm_file_md5_hash.setter
    def osm_file_md5_hash(self, osm_file_md5_hash):
        """Sets the osm_file_md5_hash of this GeoJSONIsochronesResponseMetadata.

        The MD5 hash of the OSM planet file that was used for generating graphs  # noqa: E501

        :param osm_file_md5_hash: The osm_file_md5_hash of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: str
        """

        self._osm_file_md5_hash = osm_file_md5_hash

    @property
    def query(self):
        """Gets the query of this GeoJSONIsochronesResponseMetadata.  # noqa: E501


        :return: The query of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: IsochronesProfileBody
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this GeoJSONIsochronesResponseMetadata.


        :param query: The query of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: IsochronesProfileBody
        """

        self._query = query

    @property
    def service(self):
        """Gets the service of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        The service that was requested  # noqa: E501

        :return: The service of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this GeoJSONIsochronesResponseMetadata.

        The service that was requested  # noqa: E501

        :param service: The service of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def system_message(self):
        """Gets the system_message of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        System message  # noqa: E501

        :return: The system_message of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._system_message

    @system_message.setter
    def system_message(self, system_message):
        """Sets the system_message of this GeoJSONIsochronesResponseMetadata.

        System message  # noqa: E501

        :param system_message: The system_message of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: str
        """

        self._system_message = system_message

    @property
    def timestamp(self):
        """Gets the timestamp of this GeoJSONIsochronesResponseMetadata.  # noqa: E501

        Time that the request was made (UNIX Epoch time)  # noqa: E501

        :return: The timestamp of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GeoJSONIsochronesResponseMetadata.

        Time that the request was made (UNIX Epoch time)  # noqa: E501

        :param timestamp: The timestamp of this GeoJSONIsochronesResponseMetadata.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if issubclass(GeoJSONIsochronesResponseMetadata, dict):
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
        if not isinstance(other, GeoJSONIsochronesResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
