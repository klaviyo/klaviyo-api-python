# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CampaignSendJobEnum(str, Enum):
    """
    CampaignSendJobEnum
    """

    """
    allowed enum values
    """
    CAMPAIGN_MINUS_SEND_MINUS_JOB = 'campaign-send-job'

    @classmethod
    def from_json(cls, json_str: str) -> CampaignSendJobEnum:
        """Create an instance of CampaignSendJobEnum from a JSON string"""
        return CampaignSendJobEnum(json.loads(json_str))

