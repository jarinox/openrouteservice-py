# coding: utf-8

"""
    Openrouteservice

    This is the openrouteservice API documentation for ORS Core-Version 7.1.0. Documentations for [older Core-Versions](https://github.com/GIScience/openrouteservice-docs/releases) can be rendered with the [Swagger-Editor](https://editor-next.swagger.io/).  # noqa: E501

    OpenAPI spec version: 7.1.0
    Contact: support@smartmobility.heigit.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest
import configparser

import openrouteservice
from openrouteservice.models.json_individual_route_response_summary import JSONIndividualRouteResponseSummary  # noqa: E501
from openrouteservice.rest import ApiException


class TestJSONIndividualRouteResponseSummary(unittest.TestCase):
    """JSONIndividualRouteResponseSummary unit test stubs"""

    def setUp(self):
        cfg = configparser.ConfigParser()
        cfg.read('tests-config.ini')
        configuration = openrouteservice.Configuration()
        configuration.api_key['Authorization'] = cfg['ORS']['apiKey']

    def tearDown(self):
        pass

    def testJSONIndividualRouteResponseSummary(self):
        """Test JSONIndividualRouteResponseSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openrouteservice.models.json_individual_route_response_summary.JSONIndividualRouteResponseSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
