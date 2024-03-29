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


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.email_subscription_parameters import EmailSubscriptionParameters
from openapi_client.models.sms_subscription_parameters import SMSSubscriptionParameters

class SubscriptionChannels(BaseModel):
    """
    SubscriptionChannels
    """
    email: Optional[EmailSubscriptionParameters] = None
    sms: Optional[SMSSubscriptionParameters] = None
    __properties = ["email", "sms"]

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
    def from_json(cls, json_str: str) -> SubscriptionChannels:
        """Create an instance of SubscriptionChannels from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of email
        if self.email:
            _dict['email'] = self.email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sms
        if self.sms:
            _dict['sms'] = self.sms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionChannels:
        """Create an instance of SubscriptionChannels from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionChannels.parse_obj(obj)

        _obj = SubscriptionChannels.parse_obj({
            "email": EmailSubscriptionParameters.from_dict(obj.get("email")) if obj.get("email") is not None else None,
            "sms": SMSSubscriptionParameters.from_dict(obj.get("sms")) if obj.get("sms") is not None else None
        })
        return _obj


