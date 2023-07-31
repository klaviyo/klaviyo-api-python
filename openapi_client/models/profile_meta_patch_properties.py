# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-07-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class ProfileMetaPatchProperties(BaseModel):
    """
    ProfileMetaPatchProperties
    """
    append: Optional[Dict[str, Any]] = Field(None, description="Append a simple value or values to this property array")
    unappend: Optional[Dict[str, Any]] = Field(None, description="Remove a simple value or values from this property array")
    unset: Optional[Dict[str, Any]] = Field(None, description="Remove a key or keys (and their values) completely from properties")
    __properties = ["append", "unappend", "unset"]

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
    def from_json(cls, json_str: str) -> ProfileMetaPatchProperties:
        """Create an instance of ProfileMetaPatchProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfileMetaPatchProperties:
        """Create an instance of ProfileMetaPatchProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfileMetaPatchProperties.parse_obj(obj)

        _obj = ProfileMetaPatchProperties.parse_obj({
            "append": obj.get("append"),
            "unappend": obj.get("unappend"),
            "unset": obj.get("unset")
        })
        return _obj

