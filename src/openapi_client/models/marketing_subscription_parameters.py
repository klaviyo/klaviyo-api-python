# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-02-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class MarketingSubscriptionParameters(BaseModel):
    """
    MarketingSubscriptionParameters
    """
    consent: StrictStr = Field(..., description="The Consent status to subscribe to for the \"Marketing\" type. Currently supports \"SUBSCRIBED\".")
    consented_at: Optional[datetime] = Field(None, description="The timestamp of when the profile's consent was gathered")
    __properties = ["consent", "consented_at"]

    @validator('consent')
    def consent_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SUBSCRIBED'):
            raise ValueError("must be one of enum values ('SUBSCRIBED')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MarketingSubscriptionParameters:
        """Create an instance of MarketingSubscriptionParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MarketingSubscriptionParameters:
        """Create an instance of MarketingSubscriptionParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MarketingSubscriptionParameters.parse_obj(obj)

        _obj = MarketingSubscriptionParameters.parse_obj({
            "consent": obj.get("consent"),
            "consented_at": obj.get("consented_at")
        })
        return _obj


