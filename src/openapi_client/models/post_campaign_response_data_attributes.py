# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2025-04-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.audiences import Audiences
from typing import Optional, Set
from typing_extensions import Self

class PostCampaignResponseDataAttributes(BaseModel):
    """
    PostCampaignResponseDataAttributes
    """ # noqa: E501
    name: StrictStr = Field(description="The campaign name")
    status: StrictStr = Field(description="The current status of the campaign")
    archived: StrictBool = Field(description="Whether the campaign has been archived or not")
    audiences: Audiences
    send_options: Dict[str, Any] = Field(description="Options to use when sending a campaign")
    tracking_options: Optional[Dict[str, Any]] = Field(default=None, description="The tracking options associated with the campaign")
    send_strategy: Dict[str, Any] = Field(description="The send strategy the campaign will send with")
    created_at: datetime = Field(description="The datetime when the campaign was created")
    scheduled_at: Optional[datetime] = Field(default=None, description="The datetime when the campaign was scheduled for future sending")
    updated_at: datetime = Field(description="The datetime when the campaign was last updated by a user or the system")
    send_time: Optional[datetime] = Field(default=None, description="The datetime when the campaign will be / was sent or None if not yet scheduled by a send_job.")
    __properties: ClassVar[List[str]] = ["name", "status", "archived", "audiences", "send_options", "tracking_options", "send_strategy", "created_at", "scheduled_at", "updated_at", "send_time"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Adding Recipients', 'Cancelled', 'Cancelled: Account Disabled', 'Cancelled: Internal Error', 'Cancelled: No Recipients', 'Cancelled: Smart Sending', 'Draft', 'Preparing to schedule', 'Preparing to send', 'Queued without Recipients', 'Scheduled', 'Sending', 'Sending Segments', 'Sent', 'Unknown', 'Variations Sent']):
            raise ValueError("must be one of enum values ('Adding Recipients', 'Cancelled', 'Cancelled: Account Disabled', 'Cancelled: Internal Error', 'Cancelled: No Recipients', 'Cancelled: Smart Sending', 'Draft', 'Preparing to schedule', 'Preparing to send', 'Queued without Recipients', 'Scheduled', 'Sending', 'Sending Segments', 'Sent', 'Unknown', 'Variations Sent')")
        return value

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
        """Create an instance of PostCampaignResponseDataAttributes from a JSON string"""
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
        # set to None if tracking_options (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_options is None and "tracking_options" in self.model_fields_set:
            _dict['tracking_options'] = None

        # set to None if scheduled_at (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_at is None and "scheduled_at" in self.model_fields_set:
            _dict['scheduled_at'] = None

        # set to None if send_time (nullable) is None
        # and model_fields_set contains the field
        if self.send_time is None and "send_time" in self.model_fields_set:
            _dict['send_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostCampaignResponseDataAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "status": obj.get("status"),
            "archived": obj.get("archived"),
            "audiences": Audiences.from_dict(obj["audiences"]) if obj.get("audiences") is not None else None,
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "send_strategy": obj.get("send_strategy"),
            "created_at": obj.get("created_at"),
            "scheduled_at": obj.get("scheduled_at"),
            "updated_at": obj.get("updated_at"),
            "send_time": obj.get("send_time")
        })
        return _obj


