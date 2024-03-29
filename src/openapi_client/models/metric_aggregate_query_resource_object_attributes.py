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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class MetricAggregateQueryResourceObjectAttributes(BaseModel):
    """
    MetricAggregateQueryResourceObjectAttributes
    """
    metric_id: Optional[StrictStr] = Field(..., description="The metric ID used in the aggregation.")
    page_cursor: Optional[StrictStr] = Field(None, description="Optional pagination cursor to iterate over large result sets")
    measurements: conlist(StrictStr) = Field(..., description="Measurement key, e.g. `unique`, `sum_value`, `count`")
    interval: Optional[StrictStr] = Field('day', description="Aggregation interval, e.g. \"hour\", \"day\", \"week\", \"month\"")
    page_size: Optional[StrictInt] = Field(500, description="Alter the maximum number of returned rows in a single page of aggregation results")
    by: Optional[conlist(StrictStr)] = Field(None, description="Optional attribute(s) used for partitioning by the aggregation function")
    return_fields: Optional[conlist(StrictStr)] = Field(None, description="Provide fields to limit the returned data")
    filter: conlist(StrictStr) = Field(..., description="List of filters, must include time range using ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).             These filters follow a similar format to those in `GET` requests, the primary difference is that this endpoint asks for a list.             The time range can be filtered by providing a `greater-or-equal` and a `less-than` filter on the `datetime` field.")
    timezone: Optional[StrictStr] = Field('UTC', description="The timezone used for processing the query, e.g. `'America/New_York'`.             This field is validated against a list of common timezones from the [IANA Time Zone Database](https://www.iana.org/time-zones).             While most are supported, a few notable exceptions are `Factory`, `Europe/Kyiv` and `Pacific/Kanton`. This field is case-sensitive.")
    sort: Optional[StrictStr] = Field(None, description="Provide a sort key (e.g. -$message)")
    __properties = ["metric_id", "page_cursor", "measurements", "interval", "page_size", "by", "return_fields", "filter", "timezone", "sort"]

    @validator('measurements')
    def measurements_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('count', 'sum_value', 'unique'):
                raise ValueError("each list item must be one of ('count', 'sum_value', 'unique')")
        return value

    @validator('interval')
    def interval_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('day', 'hour', 'month', 'week'):
            raise ValueError("must be one of enum values ('day', 'hour', 'month', 'week')")
        return value

    @validator('by')
    def by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('$attributed_channel', '$attributed_flow', '$attributed_message', '$attributed_variation', '$campaign_channel', '$flow', '$flow_channel', '$message', '$message_send_cohort', '$variation', '$variation_send_cohort', 'Bounce Type', 'Campaign Name', 'Client Canonical', 'Client Name', 'Client Type', 'Email Domain', 'Failure Source', 'Failure Type', 'From Number', 'From Phone Region', 'List', 'Message Name', 'Message Type', 'Method', 'Subject', 'To Number', 'To Phone Region', 'URL', 'form_id'):
                raise ValueError("each list item must be one of ('$attributed_channel', '$attributed_flow', '$attributed_message', '$attributed_variation', '$campaign_channel', '$flow', '$flow_channel', '$message', '$message_send_cohort', '$variation', '$variation_send_cohort', 'Bounce Type', 'Campaign Name', 'Client Canonical', 'Client Name', 'Client Type', 'Email Domain', 'Failure Source', 'Failure Type', 'From Number', 'From Phone Region', 'List', 'Message Name', 'Message Type', 'Method', 'Subject', 'To Number', 'To Phone Region', 'URL', 'form_id')")
        return value

    @validator('sort')
    def sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('$attributed_channel', '-$attributed_channel', '$attributed_flow', '-$attributed_flow', '$attributed_message', '-$attributed_message', '$attributed_variation', '-$attributed_variation', '$campaign_channel', '-$campaign_channel', '$flow', '-$flow', '$flow_channel', '-$flow_channel', '$message', '-$message', '$message_send_cohort', '-$message_send_cohort', '$variation', '-$variation', '$variation_send_cohort', '-$variation_send_cohort', 'Bounce Type', '-Bounce Type', 'Campaign Name', '-Campaign Name', 'Client Canonical', '-Client Canonical', 'Client Name', '-Client Name', 'Client Type', '-Client Type', 'Email Domain', '-Email Domain', 'Failure Source', '-Failure Source', 'Failure Type', '-Failure Type', 'From Number', '-From Number', 'From Phone Region', '-From Phone Region', 'List', '-List', 'Message Name', '-Message Name', 'Message Type', '-Message Type', 'Method', '-Method', 'Subject', '-Subject', 'To Number', '-To Number', 'To Phone Region', '-To Phone Region', 'URL', '-URL', 'count', '-count', 'form_id', '-form_id', 'sum_value', '-sum_value', 'unique', '-unique'):
            raise ValueError("must be one of enum values ('$attributed_channel', '-$attributed_channel', '$attributed_flow', '-$attributed_flow', '$attributed_message', '-$attributed_message', '$attributed_variation', '-$attributed_variation', '$campaign_channel', '-$campaign_channel', '$flow', '-$flow', '$flow_channel', '-$flow_channel', '$message', '-$message', '$message_send_cohort', '-$message_send_cohort', '$variation', '-$variation', '$variation_send_cohort', '-$variation_send_cohort', 'Bounce Type', '-Bounce Type', 'Campaign Name', '-Campaign Name', 'Client Canonical', '-Client Canonical', 'Client Name', '-Client Name', 'Client Type', '-Client Type', 'Email Domain', '-Email Domain', 'Failure Source', '-Failure Source', 'Failure Type', '-Failure Type', 'From Number', '-From Number', 'From Phone Region', '-From Phone Region', 'List', '-List', 'Message Name', '-Message Name', 'Message Type', '-Message Type', 'Method', '-Method', 'Subject', '-Subject', 'To Number', '-To Number', 'To Phone Region', '-To Phone Region', 'URL', '-URL', 'count', '-count', 'form_id', '-form_id', 'sum_value', '-sum_value', 'unique', '-unique')")
        return value

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
    def from_json(cls, json_str: str) -> MetricAggregateQueryResourceObjectAttributes:
        """Create an instance of MetricAggregateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if metric_id (nullable) is None
        # and __fields_set__ contains the field
        if self.metric_id is None and "metric_id" in self.__fields_set__:
            _dict['metric_id'] = None

        # set to None if page_cursor (nullable) is None
        # and __fields_set__ contains the field
        if self.page_cursor is None and "page_cursor" in self.__fields_set__:
            _dict['page_cursor'] = None

        # set to None if interval (nullable) is None
        # and __fields_set__ contains the field
        if self.interval is None and "interval" in self.__fields_set__:
            _dict['interval'] = None

        # set to None if timezone (nullable) is None
        # and __fields_set__ contains the field
        if self.timezone is None and "timezone" in self.__fields_set__:
            _dict['timezone'] = None

        # set to None if sort (nullable) is None
        # and __fields_set__ contains the field
        if self.sort is None and "sort" in self.__fields_set__:
            _dict['sort'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetricAggregateQueryResourceObjectAttributes:
        """Create an instance of MetricAggregateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetricAggregateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = MetricAggregateQueryResourceObjectAttributes.parse_obj({
            "metric_id": obj.get("metric_id"),
            "page_cursor": obj.get("page_cursor"),
            "measurements": obj.get("measurements"),
            "interval": obj.get("interval") if obj.get("interval") is not None else 'day',
            "page_size": obj.get("page_size") if obj.get("page_size") is not None else 500,
            "by": obj.get("by"),
            "return_fields": obj.get("return_fields"),
            "filter": obj.get("filter"),
            "timezone": obj.get("timezone") if obj.get("timezone") is not None else 'UTC',
            "sort": obj.get("sort")
        })
        return _obj


