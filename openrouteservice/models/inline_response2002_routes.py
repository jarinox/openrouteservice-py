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

class InlineResponse2002Routes(object):
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
        'cost': 'float',
        'delivery': 'list[int]',
        'description': 'str',
        'distance': 'float',
        'duration': 'float',
        'geometry': 'str',
        'pickup': 'list[int]',
        'service': 'float',
        'steps': 'list[InlineResponse2002Steps]',
        'vehicle': 'int',
        'waiting_time': 'float'
    }

    attribute_map = {
        'cost': 'cost',
        'delivery': 'delivery',
        'description': 'description',
        'distance': 'distance',
        'duration': 'duration',
        'geometry': 'geometry',
        'pickup': 'pickup',
        'service': 'service',
        'steps': 'steps',
        'vehicle': 'vehicle',
        'waiting_time': 'waiting_time'
    }

    def __init__(self, cost=None, delivery=None, description=None, distance=None, duration=None, geometry=None, pickup=None, service=None, steps=None, vehicle=None, waiting_time=None):  # noqa: E501
        """InlineResponse2002Routes - a model defined in Swagger"""  # noqa: E501
        self._cost = None
        self._delivery = None
        self._description = None
        self._distance = None
        self._duration = None
        self._geometry = None
        self._pickup = None
        self._service = None
        self._steps = None
        self._vehicle = None
        self._waiting_time = None
        self.discriminator = None
        if cost is not None:
            self.cost = cost
        if delivery is not None:
            self.delivery = delivery
        if description is not None:
            self.description = description
        if distance is not None:
            self.distance = distance
        if duration is not None:
            self.duration = duration
        if geometry is not None:
            self.geometry = geometry
        if pickup is not None:
            self.pickup = pickup
        if service is not None:
            self.service = service
        if steps is not None:
            self.steps = steps
        if vehicle is not None:
            self.vehicle = vehicle
        if waiting_time is not None:
            self.waiting_time = waiting_time

    @property
    def cost(self):
        """Gets the cost of this InlineResponse2002Routes.  # noqa: E501

        cost for this route  # noqa: E501

        :return: The cost of this InlineResponse2002Routes.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this InlineResponse2002Routes.

        cost for this route  # noqa: E501

        :param cost: The cost of this InlineResponse2002Routes.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def delivery(self):
        """Gets the delivery of this InlineResponse2002Routes.  # noqa: E501

        Total delivery for tasks in this route  # noqa: E501

        :return: The delivery of this InlineResponse2002Routes.  # noqa: E501
        :rtype: list[int]
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this InlineResponse2002Routes.

        Total delivery for tasks in this route  # noqa: E501

        :param delivery: The delivery of this InlineResponse2002Routes.  # noqa: E501
        :type: list[int]
        """

        self._delivery = delivery

    @property
    def description(self):
        """Gets the description of this InlineResponse2002Routes.  # noqa: E501

        vehicle description, if provided in input   # noqa: E501

        :return: The description of this InlineResponse2002Routes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse2002Routes.

        vehicle description, if provided in input   # noqa: E501

        :param description: The description of this InlineResponse2002Routes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def distance(self):
        """Gets the distance of this InlineResponse2002Routes.  # noqa: E501

        total route distance. Only provided when using the `-g` flag  # noqa: E501

        :return: The distance of this InlineResponse2002Routes.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this InlineResponse2002Routes.

        total route distance. Only provided when using the `-g` flag  # noqa: E501

        :param distance: The distance of this InlineResponse2002Routes.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def duration(self):
        """Gets the duration of this InlineResponse2002Routes.  # noqa: E501

        total travel time for this route  # noqa: E501

        :return: The duration of this InlineResponse2002Routes.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse2002Routes.

        total travel time for this route  # noqa: E501

        :param duration: The duration of this InlineResponse2002Routes.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def geometry(self):
        """Gets the geometry of this InlineResponse2002Routes.  # noqa: E501

        polyline encoded route geometry. Only provided when using the `-g` flag  # noqa: E501

        :return: The geometry of this InlineResponse2002Routes.  # noqa: E501
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this InlineResponse2002Routes.

        polyline encoded route geometry. Only provided when using the `-g` flag  # noqa: E501

        :param geometry: The geometry of this InlineResponse2002Routes.  # noqa: E501
        :type: str
        """

        self._geometry = geometry

    @property
    def pickup(self):
        """Gets the pickup of this InlineResponse2002Routes.  # noqa: E501

        total pickup for tasks in this route  # noqa: E501

        :return: The pickup of this InlineResponse2002Routes.  # noqa: E501
        :rtype: list[int]
        """
        return self._pickup

    @pickup.setter
    def pickup(self, pickup):
        """Sets the pickup of this InlineResponse2002Routes.

        total pickup for tasks in this route  # noqa: E501

        :param pickup: The pickup of this InlineResponse2002Routes.  # noqa: E501
        :type: list[int]
        """

        self._pickup = pickup

    @property
    def service(self):
        """Gets the service of this InlineResponse2002Routes.  # noqa: E501

        total service time for this route  # noqa: E501

        :return: The service of this InlineResponse2002Routes.  # noqa: E501
        :rtype: float
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this InlineResponse2002Routes.

        total service time for this route  # noqa: E501

        :param service: The service of this InlineResponse2002Routes.  # noqa: E501
        :type: float
        """

        self._service = service

    @property
    def steps(self):
        """Gets the steps of this InlineResponse2002Routes.  # noqa: E501

        array of `step` objects  # noqa: E501

        :return: The steps of this InlineResponse2002Routes.  # noqa: E501
        :rtype: list[InlineResponse2002Steps]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this InlineResponse2002Routes.

        array of `step` objects  # noqa: E501

        :param steps: The steps of this InlineResponse2002Routes.  # noqa: E501
        :type: list[InlineResponse2002Steps]
        """

        self._steps = steps

    @property
    def vehicle(self):
        """Gets the vehicle of this InlineResponse2002Routes.  # noqa: E501

        id of the vehicle assigned to this route  # noqa: E501

        :return: The vehicle of this InlineResponse2002Routes.  # noqa: E501
        :rtype: int
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this InlineResponse2002Routes.

        id of the vehicle assigned to this route  # noqa: E501

        :param vehicle: The vehicle of this InlineResponse2002Routes.  # noqa: E501
        :type: int
        """

        self._vehicle = vehicle

    @property
    def waiting_time(self):
        """Gets the waiting_time of this InlineResponse2002Routes.  # noqa: E501

        total waiting time for this route  # noqa: E501

        :return: The waiting_time of this InlineResponse2002Routes.  # noqa: E501
        :rtype: float
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """Sets the waiting_time of this InlineResponse2002Routes.

        total waiting time for this route  # noqa: E501

        :param waiting_time: The waiting_time of this InlineResponse2002Routes.  # noqa: E501
        :type: float
        """

        self._waiting_time = waiting_time

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
        if issubclass(InlineResponse2002Routes, dict):
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
        if not isinstance(other, InlineResponse2002Routes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
