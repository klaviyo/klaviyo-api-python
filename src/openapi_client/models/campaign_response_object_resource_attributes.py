# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.audiences_sub_object import AudiencesSubObject
from openapi_client.models.send_strategy_sub_object import SendStrategySubObject
from typing import Optional, Set
from typing_extensions import Self

class CampaignResponseObjectResourceAttributes(BaseModel):
    """
    CampaignResponseObjectResourceAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = Field(description="The campaign name")
    status: Optional[StrictStr] = Field(description="The current status of the campaign")
    archived: StrictBool = Field(description="Whether the campaign has been archived or not")
    audiences: AudiencesSubObject
    send_options: Dict[str, Any] = Field(description="Options to use when sending a campaign")
    tracking_options: Dict[str, Any] = Field(description="The tracking options associated with the campaign")
    send_strategy: SendStrategySubObject
    created_at: Optional[datetime] = Field(description="The datetime when the campaign was created")
    scheduled_at: Optional[datetime] = Field(default=None, description="The datetime when the campaign was scheduled for future sending")
    updated_at: Optional[datetime] = Field(description="The datetime when the campaign was last updated by a user or the system")
    send_time: Optional[datetime] = Field(default=None, description="The datetime when the campaign will be / was sent or None if not yet scheduled by a send_job.")
    __properties: ClassVar[List[str]] = ["name", "status", "archived", "audiences", "send_options", "tracking_options", "send_strategy", "created_at", "scheduled_at", "updated_at", "send_time"]

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
        """Create an instance of CampaignResponseObjectResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of send_strategy
        if self.send_strategy:
            _dict['send_strategy'] = self.send_strategy.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if scheduled_at (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_at is None and "scheduled_at" in self.model_fields_set:
            _dict['scheduled_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if send_time (nullable) is None
        # and model_fields_set contains the field
        if self.send_time is None and "send_time" in self.model_fields_set:
            _dict['send_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "status": obj.get("status"),
            "archived": obj.get("archived"),
            "audiences": AudiencesSubObject.from_dict(obj["audiences"]) if obj.get("audiences") is not None else None,
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "send_strategy": SendStrategySubObject.from_dict(obj["send_strategy"]) if obj.get("send_strategy") is not None else None,
            "created_at": obj.get("created_at"),
            "scheduled_at": obj.get("scheduled_at"),
            "updated_at": obj.get("updated_at"),
            "send_time": obj.get("send_time")
        })
        return _obj


