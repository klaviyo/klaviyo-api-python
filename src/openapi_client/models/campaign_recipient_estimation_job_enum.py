# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CampaignRecipientEstimationJobEnum(str, Enum):
    """
    CampaignRecipientEstimationJobEnum
    """

    """
    allowed enum values
    """
    CAMPAIGN_MINUS_RECIPIENT_MINUS_ESTIMATION_MINUS_JOB = 'campaign-recipient-estimation-job'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CampaignRecipientEstimationJobEnum from a JSON string"""
        return cls(json.loads(json_str))


