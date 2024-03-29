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

class ProfileIdentifierDTOResourceObjectAttributes(BaseModel):
    """
    ProfileIdentifierDTOResourceObjectAttributes
    """
    email: Optional[StrictStr] = Field(None, description="Individual's email address")
    phone_number: Optional[StrictStr] = Field(None, description="Individual's phone number in E.164 format")
    external_id: Optional[StrictStr] = Field(None, description="A unique identifier used by customers to associate Klaviyo profiles with profiles in an external system, such as a point-of-sale system. Format varies based on the external system.")
    anonymous_id: Optional[StrictStr] = None
    __properties = ["email", "phone_number", "external_id", "anonymous_id"]

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
    def from_json(cls, json_str: str) -> ProfileIdentifierDTOResourceObjectAttributes:
        """Create an instance of ProfileIdentifierDTOResourceObjectAttributes from a JSON string"""
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

        # set to None if phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.phone_number is None and "phone_number" in self.__fields_set__:
            _dict['phone_number'] = None

        # set to None if external_id (nullable) is None
        # and __fields_set__ contains the field
        if self.external_id is None and "external_id" in self.__fields_set__:
            _dict['external_id'] = None

        # set to None if anonymous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.anonymous_id is None and "anonymous_id" in self.__fields_set__:
            _dict['anonymous_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfileIdentifierDTOResourceObjectAttributes:
        """Create an instance of ProfileIdentifierDTOResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfileIdentifierDTOResourceObjectAttributes.parse_obj(obj)

        _obj = ProfileIdentifierDTOResourceObjectAttributes.parse_obj({
            "email": obj.get("email"),
            "phone_number": obj.get("phone_number"),
            "external_id": obj.get("external_id"),
            "anonymous_id": obj.get("anonymous_id")
        })
        return _obj


