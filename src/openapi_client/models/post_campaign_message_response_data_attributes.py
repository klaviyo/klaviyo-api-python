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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.render_options_sub_object import RenderOptionsSubObject
from openapi_client.models.send_time_sub_object import SendTimeSubObject
from typing import Optional, Set
from typing_extensions import Self

class PostCampaignMessageResponseDataAttributes(BaseModel):
    """
    PostCampaignMessageResponseDataAttributes
    """ # noqa: E501
    label: StrictStr = Field(description="The label or name on the message")
    channel: StrictStr = Field(description="The channel the message is to be sent on")
    content: Dict[str, Any] = Field(description="Additional attributes relating to the content of the message")
    send_times: Optional[List[SendTimeSubObject]] = Field(default=None, description="The list of appropriate Send Time Sub-objects associated with the message")
    render_options: Optional[RenderOptionsSubObject] = None
    created_at: Optional[datetime] = Field(default=None, description="The datetime when the message was created")
    updated_at: Optional[datetime] = Field(default=None, description="The datetime when the message was last updated")
    __properties: ClassVar[List[str]] = ["label", "channel", "content", "send_times", "render_options", "created_at", "updated_at"]

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
        """Create an instance of PostCampaignMessageResponseDataAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in send_times (list)
        _items = []
        if self.send_times:
            for _item in self.send_times:
                if _item:
                    _items.append(_item.to_dict())
            _dict['send_times'] = _items
        # override the default output from pydantic by calling `to_dict()` of render_options
        if self.render_options:
            _dict['render_options'] = self.render_options.to_dict()
        # set to None if send_times (nullable) is None
        # and model_fields_set contains the field
        if self.send_times is None and "send_times" in self.model_fields_set:
            _dict['send_times'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostCampaignMessageResponseDataAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "channel": obj.get("channel"),
            "content": obj.get("content"),
            "send_times": [SendTimeSubObject.from_dict(_item) for _item in obj["send_times"]] if obj.get("send_times") is not None else None,
            "render_options": RenderOptionsSubObject.from_dict(obj["render_options"]) if obj.get("render_options") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


