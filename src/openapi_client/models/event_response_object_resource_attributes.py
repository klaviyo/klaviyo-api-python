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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EventResponseObjectResourceAttributes(BaseModel):
    """
    EventResponseObjectResourceAttributes
    """ # noqa: E501
    timestamp: Optional[StrictInt] = Field(default=None, description="Event timestamp in seconds")
    event_properties: Optional[Dict[str, Any]] = Field(default=None, description="Event properties, can include identifiers and extra properties")
    datetime_: Optional[datetime] = Field(default=None, description="Event timestamp in ISO8601 format (YYYY-MM-DDTHH:MM:SS+hh:mm)", alias="datetime")
    uuid: Optional[StrictStr] = Field(default=None, description="A unique identifier for the event, this can be used as a cursor in pagination")
    __properties: ClassVar[List[str]] = ["timestamp", "event_properties", "datetime", "uuid"]

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
        """Create an instance of EventResponseObjectResourceAttributes from a JSON string"""
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
        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if event_properties (nullable) is None
        # and model_fields_set contains the field
        if self.event_properties is None and "event_properties" in self.model_fields_set:
            _dict['event_properties'] = None

        # set to None if datetime_ (nullable) is None
        # and model_fields_set contains the field
        if self.datetime_ is None and "datetime_" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if uuid (nullable) is None
        # and model_fields_set contains the field
        if self.uuid is None and "uuid" in self.model_fields_set:
            _dict['uuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "event_properties": obj.get("event_properties"),
            "datetime": obj.get("datetime"),
            "uuid": obj.get("uuid")
        })
        return _obj


