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
from pydantic import BaseModel, Field, StrictStr

class ProfileSuppressionCreateQueryResourceObjectAttributes(BaseModel):
    """
    ProfileSuppressionCreateQueryResourceObjectAttributes
    """
    email: Optional[StrictStr] = Field(None, description="The email of the profile to suppress.")
    __properties = ["email"]

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
    def from_json(cls, json_str: str) -> ProfileSuppressionCreateQueryResourceObjectAttributes:
        """Create an instance of ProfileSuppressionCreateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfileSuppressionCreateQueryResourceObjectAttributes:
        """Create an instance of ProfileSuppressionCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfileSuppressionCreateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = ProfileSuppressionCreateQueryResourceObjectAttributes.parse_obj({
            "email": obj.get("email")
        })
        return _obj


