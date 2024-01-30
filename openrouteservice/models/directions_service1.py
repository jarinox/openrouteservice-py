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

class DirectionsService1(object):
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
        'alternative_routes': 'AlternativeRoutes',
        'attributes': 'list[str]',
        'bearings': 'list[list[float]]',
        'continue_straight': 'bool',
        'coordinates': 'list[list[float]]',
        'elevation': 'bool',
        'extra_info': 'list[str]',
        'geometry': 'bool',
        'geometry_simplify': 'bool',
        'id': 'str',
        'ignore_transfers': 'bool',
        'instructions': 'bool',
        'instructions_format': 'str',
        'language': 'str',
        'maneuvers': 'bool',
        'maximum_speed': 'float',
        'options': 'RouteOptions',
        'preference': 'str',
        'radiuses': 'list[float]',
        'roundabout_exits': 'bool',
        'schedule': 'bool',
        'schedule_duration': 'V2directionsprofilegeojsonScheduleDuration',
        'schedule_rows': 'int',
        'skip_segments': 'list[int]',
        'suppress_warnings': 'bool',
        'units': 'str',
        'walking_time': 'V2directionsprofilegeojsonWalkingTime'
    }

    attribute_map = {
        'alternative_routes': 'alternative_routes',
        'attributes': 'attributes',
        'bearings': 'bearings',
        'continue_straight': 'continue_straight',
        'coordinates': 'coordinates',
        'elevation': 'elevation',
        'extra_info': 'extra_info',
        'geometry': 'geometry',
        'geometry_simplify': 'geometry_simplify',
        'id': 'id',
        'ignore_transfers': 'ignore_transfers',
        'instructions': 'instructions',
        'instructions_format': 'instructions_format',
        'language': 'language',
        'maneuvers': 'maneuvers',
        'maximum_speed': 'maximum_speed',
        'options': 'options',
        'preference': 'preference',
        'radiuses': 'radiuses',
        'roundabout_exits': 'roundabout_exits',
        'schedule': 'schedule',
        'schedule_duration': 'schedule_duration',
        'schedule_rows': 'schedule_rows',
        'skip_segments': 'skip_segments',
        'suppress_warnings': 'suppress_warnings',
        'units': 'units',
        'walking_time': 'walking_time'
    }

    def __init__(self, alternative_routes=None, attributes=None, bearings=None, continue_straight=False, coordinates=None, elevation=None, extra_info=None, geometry=True, geometry_simplify=False, id=None, ignore_transfers=False, instructions=True, instructions_format='text', language='en', maneuvers=False, maximum_speed=None, options=None, preference='recommended', radiuses=None, roundabout_exits=False, schedule=False, schedule_duration=None, schedule_rows=None, skip_segments=None, suppress_warnings=None, units='m', walking_time=None):  # noqa: E501
        """DirectionsService1 - a model defined in Swagger"""  # noqa: E501
        self._alternative_routes = None
        self._attributes = None
        self._bearings = None
        self._continue_straight = None
        self._coordinates = None
        self._elevation = None
        self._extra_info = None
        self._geometry = None
        self._geometry_simplify = None
        self._id = None
        self._ignore_transfers = None
        self._instructions = None
        self._instructions_format = None
        self._language = None
        self._maneuvers = None
        self._maximum_speed = None
        self._options = None
        self._preference = None
        self._radiuses = None
        self._roundabout_exits = None
        self._schedule = None
        self._schedule_duration = None
        self._schedule_rows = None
        self._skip_segments = None
        self._suppress_warnings = None
        self._units = None
        self._walking_time = None
        self.discriminator = None
        if alternative_routes is not None:
            self.alternative_routes = alternative_routes
        if attributes is not None:
            self.attributes = attributes
        if bearings is not None:
            self.bearings = bearings
        if continue_straight is not None:
            self.continue_straight = continue_straight
        self.coordinates = coordinates
        if elevation is not None:
            self.elevation = elevation
        if extra_info is not None:
            self.extra_info = extra_info
        if geometry is not None:
            self.geometry = geometry
        if geometry_simplify is not None:
            self.geometry_simplify = geometry_simplify
        if id is not None:
            self.id = id
        if ignore_transfers is not None:
            self.ignore_transfers = ignore_transfers
        if instructions is not None:
            self.instructions = instructions
        if instructions_format is not None:
            self.instructions_format = instructions_format
        if language is not None:
            self.language = language
        if maneuvers is not None:
            self.maneuvers = maneuvers
        if maximum_speed is not None:
            self.maximum_speed = maximum_speed
        if options is not None:
            self.options = options
        if preference is not None:
            self.preference = preference
        if radiuses is not None:
            self.radiuses = radiuses
        if roundabout_exits is not None:
            self.roundabout_exits = roundabout_exits
        if schedule is not None:
            self.schedule = schedule
        if schedule_duration is not None:
            self.schedule_duration = schedule_duration
        if schedule_rows is not None:
            self.schedule_rows = schedule_rows
        if skip_segments is not None:
            self.skip_segments = skip_segments
        if suppress_warnings is not None:
            self.suppress_warnings = suppress_warnings
        if units is not None:
            self.units = units
        if walking_time is not None:
            self.walking_time = walking_time

    @property
    def alternative_routes(self):
        """Gets the alternative_routes of this DirectionsService1.  # noqa: E501


        :return: The alternative_routes of this DirectionsService1.  # noqa: E501
        :rtype: AlternativeRoutes
        """
        return self._alternative_routes

    @alternative_routes.setter
    def alternative_routes(self, alternative_routes):
        """Sets the alternative_routes of this DirectionsService1.


        :param alternative_routes: The alternative_routes of this DirectionsService1.  # noqa: E501
        :type: AlternativeRoutes
        """

        self._alternative_routes = alternative_routes

    @property
    def attributes(self):
        """Gets the attributes of this DirectionsService1.  # noqa: E501

        List of route attributes  # noqa: E501

        :return: The attributes of this DirectionsService1.  # noqa: E501
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this DirectionsService1.

        List of route attributes  # noqa: E501

        :param attributes: The attributes of this DirectionsService1.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["avgspeed", "detourfactor", "percentage"]  # noqa: E501
        if not set(attributes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `attributes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(attributes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._attributes = attributes

    @property
    def bearings(self):
        """Gets the bearings of this DirectionsService1.  # noqa: E501

        Specifies a list of pairs (bearings and deviations) to filter the segments of the road network a waypoint can snap to. \"For example `bearings=[[45,10],[120,20]]`. \"Each pair is a comma-separated list that can consist of one or two float values, where the first value is the bearing and the second one is the allowed deviation from the bearing. \"The bearing can take values between `0` and `360` clockwise from true north. If the deviation is not set, then the default value of `100` degrees is used. \"The number of pairs must correspond to the number of waypoints. \"The number of bearings corresponds to the length of waypoints-1 or waypoints. If the bearing information for the last waypoint is given, then this will control the sector from which the destination waypoint may be reached. \"You can skip a bearing for a certain waypoint by passing an empty value for an array, e.g. `[30,20],[],[40,20]`.  # noqa: E501

        :return: The bearings of this DirectionsService1.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._bearings

    @bearings.setter
    def bearings(self, bearings):
        """Sets the bearings of this DirectionsService1.

        Specifies a list of pairs (bearings and deviations) to filter the segments of the road network a waypoint can snap to. \"For example `bearings=[[45,10],[120,20]]`. \"Each pair is a comma-separated list that can consist of one or two float values, where the first value is the bearing and the second one is the allowed deviation from the bearing. \"The bearing can take values between `0` and `360` clockwise from true north. If the deviation is not set, then the default value of `100` degrees is used. \"The number of pairs must correspond to the number of waypoints. \"The number of bearings corresponds to the length of waypoints-1 or waypoints. If the bearing information for the last waypoint is given, then this will control the sector from which the destination waypoint may be reached. \"You can skip a bearing for a certain waypoint by passing an empty value for an array, e.g. `[30,20],[],[40,20]`.  # noqa: E501

        :param bearings: The bearings of this DirectionsService1.  # noqa: E501
        :type: list[list[float]]
        """

        self._bearings = bearings

    @property
    def continue_straight(self):
        """Gets the continue_straight of this DirectionsService1.  # noqa: E501

        Forces the route to keep going straight at waypoints restricting uturns there even if it would be faster.  # noqa: E501

        :return: The continue_straight of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._continue_straight

    @continue_straight.setter
    def continue_straight(self, continue_straight):
        """Sets the continue_straight of this DirectionsService1.

        Forces the route to keep going straight at waypoints restricting uturns there even if it would be faster.  # noqa: E501

        :param continue_straight: The continue_straight of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._continue_straight = continue_straight

    @property
    def coordinates(self):
        """Gets the coordinates of this DirectionsService1.  # noqa: E501

        The waypoints to use for the route as an array of `longitude/latitude` pairs in WGS 84 (EPSG:4326)  # noqa: E501

        :return: The coordinates of this DirectionsService1.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this DirectionsService1.

        The waypoints to use for the route as an array of `longitude/latitude` pairs in WGS 84 (EPSG:4326)  # noqa: E501

        :param coordinates: The coordinates of this DirectionsService1.  # noqa: E501
        :type: list[list[float]]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

    @property
    def elevation(self):
        """Gets the elevation of this DirectionsService1.  # noqa: E501

        Specifies whether to return elevation values for points. Please note that elevation also gets encoded for json response encoded polyline.  # noqa: E501

        :return: The elevation of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this DirectionsService1.

        Specifies whether to return elevation values for points. Please note that elevation also gets encoded for json response encoded polyline.  # noqa: E501

        :param elevation: The elevation of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._elevation = elevation

    @property
    def extra_info(self):
        """Gets the extra_info of this DirectionsService1.  # noqa: E501

        The extra info items to include in the response  # noqa: E501

        :return: The extra_info of this DirectionsService1.  # noqa: E501
        :rtype: list[str]
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this DirectionsService1.

        The extra info items to include in the response  # noqa: E501

        :param extra_info: The extra_info of this DirectionsService1.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["steepness", "suitability", "surface", "waycategory", "waytype", "tollways", "traildifficulty", "osmid", "roadaccessrestrictions", "countryinfo", "green", "noise", "csv", "shadow"]  # noqa: E501
        if not set(extra_info).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `extra_info` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(extra_info) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._extra_info = extra_info

    @property
    def geometry(self):
        """Gets the geometry of this DirectionsService1.  # noqa: E501

        Specifies whether to return geometry.   # noqa: E501

        :return: The geometry of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this DirectionsService1.

        Specifies whether to return geometry.   # noqa: E501

        :param geometry: The geometry of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._geometry = geometry

    @property
    def geometry_simplify(self):
        """Gets the geometry_simplify of this DirectionsService1.  # noqa: E501

        Specifies whether to simplify the geometry. Simplify geometry cannot be applied to routes with more than **one segment** and when `extra_info` is required.  # noqa: E501

        :return: The geometry_simplify of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._geometry_simplify

    @geometry_simplify.setter
    def geometry_simplify(self, geometry_simplify):
        """Sets the geometry_simplify of this DirectionsService1.

        Specifies whether to simplify the geometry. Simplify geometry cannot be applied to routes with more than **one segment** and when `extra_info` is required.  # noqa: E501

        :param geometry_simplify: The geometry_simplify of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._geometry_simplify = geometry_simplify

    @property
    def id(self):
        """Gets the id of this DirectionsService1.  # noqa: E501

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :return: The id of this DirectionsService1.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DirectionsService1.

        Arbitrary identification string of the request reflected in the meta information.  # noqa: E501

        :param id: The id of this DirectionsService1.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ignore_transfers(self):
        """Gets the ignore_transfers of this DirectionsService1.  # noqa: E501

        Specifies if transfers as criterion should be ignored.  # noqa: E501

        :return: The ignore_transfers of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_transfers

    @ignore_transfers.setter
    def ignore_transfers(self, ignore_transfers):
        """Sets the ignore_transfers of this DirectionsService1.

        Specifies if transfers as criterion should be ignored.  # noqa: E501

        :param ignore_transfers: The ignore_transfers of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._ignore_transfers = ignore_transfers

    @property
    def instructions(self):
        """Gets the instructions of this DirectionsService1.  # noqa: E501

        Specifies whether to return instructions.  # noqa: E501

        :return: The instructions of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this DirectionsService1.

        Specifies whether to return instructions.  # noqa: E501

        :param instructions: The instructions of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._instructions = instructions

    @property
    def instructions_format(self):
        """Gets the instructions_format of this DirectionsService1.  # noqa: E501

        Select html for more verbose instructions.  # noqa: E501

        :return: The instructions_format of this DirectionsService1.  # noqa: E501
        :rtype: str
        """
        return self._instructions_format

    @instructions_format.setter
    def instructions_format(self, instructions_format):
        """Sets the instructions_format of this DirectionsService1.

        Select html for more verbose instructions.  # noqa: E501

        :param instructions_format: The instructions_format of this DirectionsService1.  # noqa: E501
        :type: str
        """
        allowed_values = ["html", "text"]  # noqa: E501
        if instructions_format not in allowed_values:
            raise ValueError(
                "Invalid value for `instructions_format` ({0}), must be one of {1}"  # noqa: E501
                .format(instructions_format, allowed_values)
            )

        self._instructions_format = instructions_format

    @property
    def language(self):
        """Gets the language of this DirectionsService1.  # noqa: E501

        Language for the route instructions.  # noqa: E501

        :return: The language of this DirectionsService1.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DirectionsService1.

        Language for the route instructions.  # noqa: E501

        :param language: The language of this DirectionsService1.  # noqa: E501
        :type: str
        """
        allowed_values = ["cs", "cs-cz", "de", "de-de", "en", "en-us", "eo", "eo-eo", "es", "es-es", "fr", "fr-fr", "gr", "gr-gr", "he", "he-il", "hu", "hu-hu", "id", "id-id", "it", "it-it", "ja", "ja-jp", "ne", "ne-np", "nl", "nl-nl", "pl", "pl-pl", "pt", "pt-pt", "ro", "ro-ro", "ru", "ru-ru", "tr", "tr-tr", "zh", "zh-cn"]  # noqa: E501
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def maneuvers(self):
        """Gets the maneuvers of this DirectionsService1.  # noqa: E501

        Specifies whether the maneuver object is included into the step object or not.   # noqa: E501

        :return: The maneuvers of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._maneuvers

    @maneuvers.setter
    def maneuvers(self, maneuvers):
        """Sets the maneuvers of this DirectionsService1.

        Specifies whether the maneuver object is included into the step object or not.   # noqa: E501

        :param maneuvers: The maneuvers of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._maneuvers = maneuvers

    @property
    def maximum_speed(self):
        """Gets the maximum_speed of this DirectionsService1.  # noqa: E501

        The maximum speed specified by user.  # noqa: E501

        :return: The maximum_speed of this DirectionsService1.  # noqa: E501
        :rtype: float
        """
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, maximum_speed):
        """Sets the maximum_speed of this DirectionsService1.

        The maximum speed specified by user.  # noqa: E501

        :param maximum_speed: The maximum_speed of this DirectionsService1.  # noqa: E501
        :type: float
        """

        self._maximum_speed = maximum_speed

    @property
    def options(self):
        """Gets the options of this DirectionsService1.  # noqa: E501


        :return: The options of this DirectionsService1.  # noqa: E501
        :rtype: RouteOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DirectionsService1.


        :param options: The options of this DirectionsService1.  # noqa: E501
        :type: RouteOptions
        """

        self._options = options

    @property
    def preference(self):
        """Gets the preference of this DirectionsService1.  # noqa: E501

        Specifies the route preference  # noqa: E501

        :return: The preference of this DirectionsService1.  # noqa: E501
        :rtype: str
        """
        return self._preference

    @preference.setter
    def preference(self, preference):
        """Sets the preference of this DirectionsService1.

        Specifies the route preference  # noqa: E501

        :param preference: The preference of this DirectionsService1.  # noqa: E501
        :type: str
        """
        allowed_values = ["fastest", "shortest", "recommended"]  # noqa: E501
        if preference not in allowed_values:
            raise ValueError(
                "Invalid value for `preference` ({0}), must be one of {1}"  # noqa: E501
                .format(preference, allowed_values)
            )

        self._preference = preference

    @property
    def radiuses(self):
        """Gets the radiuses of this DirectionsService1.  # noqa: E501

        A list of maximum distances (measured in metres) that limit the search of nearby road segments to every given waypoint. The values must be greater than 0, the value of -1 specifies using the maximum possible search radius. The number of radiuses correspond to the number of waypoints. If only a single value is given, it will be applied to all waypoints.  # noqa: E501

        :return: The radiuses of this DirectionsService1.  # noqa: E501
        :rtype: list[float]
        """
        return self._radiuses

    @radiuses.setter
    def radiuses(self, radiuses):
        """Sets the radiuses of this DirectionsService1.

        A list of maximum distances (measured in metres) that limit the search of nearby road segments to every given waypoint. The values must be greater than 0, the value of -1 specifies using the maximum possible search radius. The number of radiuses correspond to the number of waypoints. If only a single value is given, it will be applied to all waypoints.  # noqa: E501

        :param radiuses: The radiuses of this DirectionsService1.  # noqa: E501
        :type: list[float]
        """

        self._radiuses = radiuses

    @property
    def roundabout_exits(self):
        """Gets the roundabout_exits of this DirectionsService1.  # noqa: E501

        Provides bearings of the entrance and all passed roundabout exits. Adds the `exit_bearings` array to the step object in the response.   # noqa: E501

        :return: The roundabout_exits of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._roundabout_exits

    @roundabout_exits.setter
    def roundabout_exits(self, roundabout_exits):
        """Sets the roundabout_exits of this DirectionsService1.

        Provides bearings of the entrance and all passed roundabout exits. Adds the `exit_bearings` array to the step object in the response.   # noqa: E501

        :param roundabout_exits: The roundabout_exits of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._roundabout_exits = roundabout_exits

    @property
    def schedule(self):
        """Gets the schedule of this DirectionsService1.  # noqa: E501

        If true, return a public transport schedule starting at <departure> for the next <schedule_duration> minutes.  # noqa: E501

        :return: The schedule of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DirectionsService1.

        If true, return a public transport schedule starting at <departure> for the next <schedule_duration> minutes.  # noqa: E501

        :param schedule: The schedule of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._schedule = schedule

    @property
    def schedule_duration(self):
        """Gets the schedule_duration of this DirectionsService1.  # noqa: E501


        :return: The schedule_duration of this DirectionsService1.  # noqa: E501
        :rtype: V2directionsprofilegeojsonScheduleDuration
        """
        return self._schedule_duration

    @schedule_duration.setter
    def schedule_duration(self, schedule_duration):
        """Sets the schedule_duration of this DirectionsService1.


        :param schedule_duration: The schedule_duration of this DirectionsService1.  # noqa: E501
        :type: V2directionsprofilegeojsonScheduleDuration
        """

        self._schedule_duration = schedule_duration

    @property
    def schedule_rows(self):
        """Gets the schedule_rows of this DirectionsService1.  # noqa: E501

        The maximum amount of entries that should be returned when requesting a schedule.  # noqa: E501

        :return: The schedule_rows of this DirectionsService1.  # noqa: E501
        :rtype: int
        """
        return self._schedule_rows

    @schedule_rows.setter
    def schedule_rows(self, schedule_rows):
        """Sets the schedule_rows of this DirectionsService1.

        The maximum amount of entries that should be returned when requesting a schedule.  # noqa: E501

        :param schedule_rows: The schedule_rows of this DirectionsService1.  # noqa: E501
        :type: int
        """

        self._schedule_rows = schedule_rows

    @property
    def skip_segments(self):
        """Gets the skip_segments of this DirectionsService1.  # noqa: E501

        Specifies the segments that should be skipped in the route calculation. A segment is the connection between two given coordinates and the counting starts with 1 for the connection between the first and second coordinate.  # noqa: E501

        :return: The skip_segments of this DirectionsService1.  # noqa: E501
        :rtype: list[int]
        """
        return self._skip_segments

    @skip_segments.setter
    def skip_segments(self, skip_segments):
        """Sets the skip_segments of this DirectionsService1.

        Specifies the segments that should be skipped in the route calculation. A segment is the connection between two given coordinates and the counting starts with 1 for the connection between the first and second coordinate.  # noqa: E501

        :param skip_segments: The skip_segments of this DirectionsService1.  # noqa: E501
        :type: list[int]
        """

        self._skip_segments = skip_segments

    @property
    def suppress_warnings(self):
        """Gets the suppress_warnings of this DirectionsService1.  # noqa: E501

        Suppress warning messages in the response  # noqa: E501

        :return: The suppress_warnings of this DirectionsService1.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_warnings

    @suppress_warnings.setter
    def suppress_warnings(self, suppress_warnings):
        """Sets the suppress_warnings of this DirectionsService1.

        Suppress warning messages in the response  # noqa: E501

        :param suppress_warnings: The suppress_warnings of this DirectionsService1.  # noqa: E501
        :type: bool
        """

        self._suppress_warnings = suppress_warnings

    @property
    def units(self):
        """Gets the units of this DirectionsService1.  # noqa: E501

        Specifies the distance unit.  # noqa: E501

        :return: The units of this DirectionsService1.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this DirectionsService1.

        Specifies the distance unit.  # noqa: E501

        :param units: The units of this DirectionsService1.  # noqa: E501
        :type: str
        """
        allowed_values = ["m", "km", "mi"]  # noqa: E501
        if units not in allowed_values:
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}"  # noqa: E501
                .format(units, allowed_values)
            )

        self._units = units

    @property
    def walking_time(self):
        """Gets the walking_time of this DirectionsService1.  # noqa: E501


        :return: The walking_time of this DirectionsService1.  # noqa: E501
        :rtype: V2directionsprofilegeojsonWalkingTime
        """
        return self._walking_time

    @walking_time.setter
    def walking_time(self, walking_time):
        """Sets the walking_time of this DirectionsService1.


        :param walking_time: The walking_time of this DirectionsService1.  # noqa: E501
        :type: V2directionsprofilegeojsonWalkingTime
        """

        self._walking_time = walking_time

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
        if issubclass(DirectionsService1, dict):
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
        if not isinstance(other, DirectionsService1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
