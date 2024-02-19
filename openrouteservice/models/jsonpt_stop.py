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

class JSONPtStop(object):
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
        'arrival_cancelled': 'bool',
        'arrival_time': 'datetime',
        'departure_cancelled': 'bool',
        'departure_time': 'datetime',
        'location': 'list[float]',
        'name': 'str',
        'planned_arrival_time': 'datetime',
        'planned_departure_time': 'datetime',
        'predicted_arrival_time': 'datetime',
        'predicted_departure_time': 'datetime',
        'stop_id': 'str'
    }

    attribute_map = {
        'arrival_cancelled': 'arrival_cancelled',
        'arrival_time': 'arrival_time',
        'departure_cancelled': 'departure_cancelled',
        'departure_time': 'departure_time',
        'location': 'location',
        'name': 'name',
        'planned_arrival_time': 'planned_arrival_time',
        'planned_departure_time': 'planned_departure_time',
        'predicted_arrival_time': 'predicted_arrival_time',
        'predicted_departure_time': 'predicted_departure_time',
        'stop_id': 'stop_id'
    }

    def __init__(self, arrival_cancelled=None, arrival_time=None, departure_cancelled=None, departure_time=None, location=None, name=None, planned_arrival_time=None, planned_departure_time=None, predicted_arrival_time=None, predicted_departure_time=None, stop_id=None):  # noqa: E501
        """JSONPtStop - a model defined in Swagger"""  # noqa: E501
        self._arrival_cancelled = None
        self._arrival_time = None
        self._departure_cancelled = None
        self._departure_time = None
        self._location = None
        self._name = None
        self._planned_arrival_time = None
        self._planned_departure_time = None
        self._predicted_arrival_time = None
        self._predicted_departure_time = None
        self._stop_id = None
        self.discriminator = None
        if arrival_cancelled is not None:
            self.arrival_cancelled = arrival_cancelled
        if arrival_time is not None:
            self.arrival_time = arrival_time
        if departure_cancelled is not None:
            self.departure_cancelled = departure_cancelled
        if departure_time is not None:
            self.departure_time = departure_time
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if planned_arrival_time is not None:
            self.planned_arrival_time = planned_arrival_time
        if planned_departure_time is not None:
            self.planned_departure_time = planned_departure_time
        if predicted_arrival_time is not None:
            self.predicted_arrival_time = predicted_arrival_time
        if predicted_departure_time is not None:
            self.predicted_departure_time = predicted_departure_time
        if stop_id is not None:
            self.stop_id = stop_id

    @property
    def arrival_cancelled(self):
        """Gets the arrival_cancelled of this JSONPtStop.  # noqa: E501

        Whether arrival at the stop was cancelled.  # noqa: E501

        :return: The arrival_cancelled of this JSONPtStop.  # noqa: E501
        :rtype: bool
        """
        return self._arrival_cancelled

    @arrival_cancelled.setter
    def arrival_cancelled(self, arrival_cancelled):
        """Sets the arrival_cancelled of this JSONPtStop.

        Whether arrival at the stop was cancelled.  # noqa: E501

        :param arrival_cancelled: The arrival_cancelled of this JSONPtStop.  # noqa: E501
        :type: bool
        """

        self._arrival_cancelled = arrival_cancelled

    @property
    def arrival_time(self):
        """Gets the arrival_time of this JSONPtStop.  # noqa: E501

        Arrival time of the stop.  # noqa: E501

        :return: The arrival_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """Sets the arrival_time of this JSONPtStop.

        Arrival time of the stop.  # noqa: E501

        :param arrival_time: The arrival_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._arrival_time = arrival_time

    @property
    def departure_cancelled(self):
        """Gets the departure_cancelled of this JSONPtStop.  # noqa: E501

        Whether departure at the stop was cancelled.  # noqa: E501

        :return: The departure_cancelled of this JSONPtStop.  # noqa: E501
        :rtype: bool
        """
        return self._departure_cancelled

    @departure_cancelled.setter
    def departure_cancelled(self, departure_cancelled):
        """Sets the departure_cancelled of this JSONPtStop.

        Whether departure at the stop was cancelled.  # noqa: E501

        :param departure_cancelled: The departure_cancelled of this JSONPtStop.  # noqa: E501
        :type: bool
        """

        self._departure_cancelled = departure_cancelled

    @property
    def departure_time(self):
        """Gets the departure_time of this JSONPtStop.  # noqa: E501

        Departure time of the stop.  # noqa: E501

        :return: The departure_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        """Sets the departure_time of this JSONPtStop.

        Departure time of the stop.  # noqa: E501

        :param departure_time: The departure_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._departure_time = departure_time

    @property
    def location(self):
        """Gets the location of this JSONPtStop.  # noqa: E501

        The location of the stop.  # noqa: E501

        :return: The location of this JSONPtStop.  # noqa: E501
        :rtype: list[float]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this JSONPtStop.

        The location of the stop.  # noqa: E501

        :param location: The location of this JSONPtStop.  # noqa: E501
        :type: list[float]
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this JSONPtStop.  # noqa: E501

        The name of the stop.  # noqa: E501

        :return: The name of this JSONPtStop.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JSONPtStop.

        The name of the stop.  # noqa: E501

        :param name: The name of this JSONPtStop.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def planned_arrival_time(self):
        """Gets the planned_arrival_time of this JSONPtStop.  # noqa: E501

        Planned arrival time of the stop.  # noqa: E501

        :return: The planned_arrival_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._planned_arrival_time

    @planned_arrival_time.setter
    def planned_arrival_time(self, planned_arrival_time):
        """Sets the planned_arrival_time of this JSONPtStop.

        Planned arrival time of the stop.  # noqa: E501

        :param planned_arrival_time: The planned_arrival_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._planned_arrival_time = planned_arrival_time

    @property
    def planned_departure_time(self):
        """Gets the planned_departure_time of this JSONPtStop.  # noqa: E501

        Planned departure time of the stop.  # noqa: E501

        :return: The planned_departure_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._planned_departure_time

    @planned_departure_time.setter
    def planned_departure_time(self, planned_departure_time):
        """Sets the planned_departure_time of this JSONPtStop.

        Planned departure time of the stop.  # noqa: E501

        :param planned_departure_time: The planned_departure_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._planned_departure_time = planned_departure_time

    @property
    def predicted_arrival_time(self):
        """Gets the predicted_arrival_time of this JSONPtStop.  # noqa: E501

        Predicted arrival time of the stop.  # noqa: E501

        :return: The predicted_arrival_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._predicted_arrival_time

    @predicted_arrival_time.setter
    def predicted_arrival_time(self, predicted_arrival_time):
        """Sets the predicted_arrival_time of this JSONPtStop.

        Predicted arrival time of the stop.  # noqa: E501

        :param predicted_arrival_time: The predicted_arrival_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._predicted_arrival_time = predicted_arrival_time

    @property
    def predicted_departure_time(self):
        """Gets the predicted_departure_time of this JSONPtStop.  # noqa: E501

        Predicted departure time of the stop.  # noqa: E501

        :return: The predicted_departure_time of this JSONPtStop.  # noqa: E501
        :rtype: datetime
        """
        return self._predicted_departure_time

    @predicted_departure_time.setter
    def predicted_departure_time(self, predicted_departure_time):
        """Sets the predicted_departure_time of this JSONPtStop.

        Predicted departure time of the stop.  # noqa: E501

        :param predicted_departure_time: The predicted_departure_time of this JSONPtStop.  # noqa: E501
        :type: datetime
        """

        self._predicted_departure_time = predicted_departure_time

    @property
    def stop_id(self):
        """Gets the stop_id of this JSONPtStop.  # noqa: E501

        The ID of the stop.  # noqa: E501

        :return: The stop_id of this JSONPtStop.  # noqa: E501
        :rtype: str
        """
        return self._stop_id

    @stop_id.setter
    def stop_id(self, stop_id):
        """Sets the stop_id of this JSONPtStop.

        The ID of the stop.  # noqa: E501

        :param stop_id: The stop_id of this JSONPtStop.  # noqa: E501
        :type: str
        """

        self._stop_id = stop_id

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
        if issubclass(JSONPtStop, dict):
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
        if not isinstance(other, JSONPtStop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
