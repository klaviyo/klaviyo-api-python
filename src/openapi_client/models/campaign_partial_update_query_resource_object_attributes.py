# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2025-01-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.audiences_update import AudiencesUpdate
from typing import Optional, Set
from typing_extensions import Self

class CampaignPartialUpdateQueryResourceObjectAttributes(BaseModel):
    """
    CampaignPartialUpdateQueryResourceObjectAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The campaign name")
    audiences: Optional[AudiencesUpdate] = None
    send_options: Optional[Dict[str, Any]] = Field(default=None, description="Options to use when sending a campaign")
    tracking_options: Optional[Dict[str, Any]] = Field(default=None, description="The tracking options associated with the campaign")
    send_strategy: Optional[Dict[str, Any]] = Field(default=None, description="The send strategy the campaign will send with")
    __properties: ClassVar[List[str]] = ["name", "audiences", "send_options", "tracking_options", "send_strategy"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
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
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of audiences
        if self.audiences:
            _dict['audiences'] = self.audiences.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if send_options (nullable) is None
        # and model_fields_set contains the field
        if self.send_options is None and "send_options" in self.model_fields_set:
            _dict['send_options'] = None

        # set to None if tracking_options (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_options is None and "tracking_options" in self.model_fields_set:
            _dict['tracking_options'] = None

        # set to None if send_strategy (nullable) is None
        # and model_fields_set contains the field
        if self.send_strategy is None and "send_strategy" in self.model_fields_set:
            _dict['send_strategy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignPartialUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "audiences": AudiencesUpdate.from_dict(obj["audiences"]) if obj.get("audiences") is not None else None,
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "send_strategy": obj.get("send_strategy")
        })
        return _obj


