# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-02-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PushTokenEnum(str, Enum):
    """
    PushTokenEnum
    """

    """
    allowed enum values
    """
    PUSH_MINUS_TOKEN = 'push-token'

    @classmethod
    def from_json(cls, json_str: str) -> PushTokenEnum:
        """Create an instance of PushTokenEnum from a JSON string"""
        return PushTokenEnum(json.loads(json_str))


