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


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.server_bis_subscription_create_query_resource_object_relationships_variant import ServerBISSubscriptionCreateQueryResourceObjectRelationshipsVariant

class ServerBISSubscriptionCreateQueryResourceObjectRelationships(BaseModel):
    """
    ServerBISSubscriptionCreateQueryResourceObjectRelationships
    """
    variant: Optional[ServerBISSubscriptionCreateQueryResourceObjectRelationshipsVariant] = None
    __properties = ["variant"]

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
    def from_json(cls, json_str: str) -> ServerBISSubscriptionCreateQueryResourceObjectRelationships:
        """Create an instance of ServerBISSubscriptionCreateQueryResourceObjectRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of variant
        if self.variant:
            _dict['variant'] = self.variant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerBISSubscriptionCreateQueryResourceObjectRelationships:
        """Create an instance of ServerBISSubscriptionCreateQueryResourceObjectRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServerBISSubscriptionCreateQueryResourceObjectRelationships.parse_obj(obj)

        _obj = ServerBISSubscriptionCreateQueryResourceObjectRelationships.parse_obj({
            "variant": ServerBISSubscriptionCreateQueryResourceObjectRelationshipsVariant.from_dict(obj.get("variant")) if obj.get("variant") is not None else None
        })
        return _obj
