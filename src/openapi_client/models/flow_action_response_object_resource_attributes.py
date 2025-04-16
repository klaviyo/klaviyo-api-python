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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.send_options import SendOptions
from openapi_client.models.sms_render_options import SMSRenderOptions
from typing import Optional, Set
from typing_extensions import Self

class FlowActionResponseObjectResourceAttributes(BaseModel):
    """
    FlowActionResponseObjectResourceAttributes
    """ # noqa: E501
    action_type: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    settings: Optional[Dict[str, Any]] = None
    tracking_options: Optional[Dict[str, Any]] = None
    send_options: Optional[SendOptions] = None
    render_options: Optional[SMSRenderOptions] = None
    __properties: ClassVar[List[str]] = ["action_type", "status", "created", "updated", "settings", "tracking_options", "send_options", "render_options"]

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
        """Create an instance of FlowActionResponseObjectResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of send_options
        if self.send_options:
            _dict['send_options'] = self.send_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of render_options
        if self.render_options:
            _dict['render_options'] = self.render_options.to_dict()
        # set to None if action_type (nullable) is None
        # and model_fields_set contains the field
        if self.action_type is None and "action_type" in self.model_fields_set:
            _dict['action_type'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and "updated" in self.model_fields_set:
            _dict['updated'] = None

        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        # set to None if tracking_options (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_options is None and "tracking_options" in self.model_fields_set:
            _dict['tracking_options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowActionResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action_type": obj.get("action_type"),
            "status": obj.get("status"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "settings": obj.get("settings"),
            "tracking_options": obj.get("tracking_options"),
            "send_options": SendOptions.from_dict(obj["send_options"]) if obj.get("send_options") is not None else None,
            "render_options": SMSRenderOptions.from_dict(obj["render_options"]) if obj.get("render_options") is not None else None
        })
        return _obj


