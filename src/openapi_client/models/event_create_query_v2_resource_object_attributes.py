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

from datetime import datetime
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.event_create_query_v2_resource_object_attributes_metric import EventCreateQueryV2ResourceObjectAttributesMetric
from openapi_client.models.event_create_query_v2_resource_object_attributes_profile import EventCreateQueryV2ResourceObjectAttributesProfile

class EventCreateQueryV2ResourceObjectAttributes(BaseModel):
    """
    EventCreateQueryV2ResourceObjectAttributes
    """
    properties: Dict[str, Any] = Field(..., description="Properties of this event. Any top level property (that are not objects) can be used to create segments. The $extra property is a special property. This records any non-segmentable values that can be referenced later. For example, HTML templates are useful on a segment but are not used to create a segment. There are limits placed onto the size of the data present. This must not exceed 5 MB. This must not exceed 300 event properties. A single string cannot be larger than 100 KB. Each array must not exceed 4000 elements. The properties cannot contain more than 10 nested levels.")
    time: Optional[datetime] = Field(None, description="When this event occurred. By default, the time the request was received will be used. The time is truncated to the second. The time must be after the year 2000 and can only be up to 1 year in the future.")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="A numeric value to associate with this event. For example, the dollar amount of a purchase.")
    unique_id: Optional[StrictStr] = Field(None, description="A unique identifier for an event. If the unique_id is repeated for the same profile and metric, only the first processed event will be recorded. If this is not present, this will use the time to the second. Using the default, this limits only one event per profile per second.")
    metric: EventCreateQueryV2ResourceObjectAttributesMetric = Field(...)
    profile: EventCreateQueryV2ResourceObjectAttributesProfile = Field(...)
    __properties = ["properties", "time", "value", "unique_id", "metric", "profile"]

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
    def from_json(cls, json_str: str) -> EventCreateQueryV2ResourceObjectAttributes:
        """Create an instance of EventCreateQueryV2ResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        # set to None if time (nullable) is None
        # and __fields_set__ contains the field
        if self.time is None and "time" in self.__fields_set__:
            _dict['time'] = None

        # set to None if unique_id (nullable) is None
        # and __fields_set__ contains the field
        if self.unique_id is None and "unique_id" in self.__fields_set__:
            _dict['unique_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCreateQueryV2ResourceObjectAttributes:
        """Create an instance of EventCreateQueryV2ResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCreateQueryV2ResourceObjectAttributes.parse_obj(obj)

        _obj = EventCreateQueryV2ResourceObjectAttributes.parse_obj({
            "properties": obj.get("properties"),
            "time": obj.get("time"),
            "value": obj.get("value"),
            "unique_id": obj.get("unique_id"),
            "metric": EventCreateQueryV2ResourceObjectAttributesMetric.from_dict(obj.get("metric")) if obj.get("metric") is not None else None,
            "profile": EventCreateQueryV2ResourceObjectAttributesProfile.from_dict(obj.get("profile")) if obj.get("profile") is not None else None
        })
        return _obj


