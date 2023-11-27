# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CouponCodeEnum(str, Enum):
    """
    CouponCodeEnum
    """

    """
    allowed enum values
    """
    COUPON_MINUS_CODE = 'coupon-code'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CouponCodeEnum from a JSON string"""
        return cls(json.loads(json_str))


