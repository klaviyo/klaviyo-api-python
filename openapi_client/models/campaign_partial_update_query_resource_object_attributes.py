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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.audiences_sub_object import AudiencesSubObject
from openapi_client.models.send_strategy_sub_object import SendStrategySubObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CampaignPartialUpdateQueryResourceObjectAttributes(BaseModel):
    """
    CampaignPartialUpdateQueryResourceObjectAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The campaign name")
    audiences: Optional[AudiencesSubObject] = None
    send_options: Optional[Dict[str, Any]] = Field(default=None, description="Options to use when sending a campaign")
    tracking_options: Optional[Dict[str, Any]] = Field(default=None, description="The tracking options associated with the campaign")
    send_strategy: Optional[SendStrategySubObject] = None
    __properties: ClassVar[List[str]] = ["name", "audiences", "send_options", "tracking_options", "send_strategy"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CampaignPartialUpdateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of audiences
        if self.audiences:
            _dict['audiences'] = self.audiences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of send_strategy
        if self.send_strategy:
            _dict['send_strategy'] = self.send_strategy.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignPartialUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "audiences": AudiencesSubObject.from_dict(obj.get("audiences")) if obj.get("audiences") is not None else None,
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "send_strategy": SendStrategySubObject.from_dict(obj.get("send_strategy")) if obj.get("send_strategy") is not None else None
        })
        return _obj


