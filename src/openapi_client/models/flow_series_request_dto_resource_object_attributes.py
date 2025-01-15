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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FlowSeriesRequestDTOResourceObjectAttributes(BaseModel):
    """
    FlowSeriesRequestDTOResourceObjectAttributes
    """ # noqa: E501
    statistics: List[StrictStr] = Field(description="List of statistics to query for. All rate statistics will be returned in fractional form [0.0, 1.0]")
    timeframe: Dict[str, Any] = Field(description="The timeframe to query for data within. The max length a timeframe can be is 1 year")
    interval: Optional[StrictStr] = Field(description="The interval used to aggregate data within the series request. If hourly is used, the timeframe cannot be longer than 7 days. If daily is used, the timeframe cannot be longer than 60 days. If monthly is used, the timeframe cannot be longer than 52 weeks.")
    conversion_metric_id: Optional[StrictStr] = Field(description="ID of the metric to be used for conversion statistics")
    filter: Optional[StrictStr] = Field(default=None, description="API filter string used to filter the query. Allowed filters are flow_id, send_channel, flow_message_id. Allowed operators are equals, contains-any. Only one filter can be used per attribute, only AND can be used as a combination operator. Max of 100 messages per ANY filter. When filtering on send_channel, allowed values are email, push-notification, sms, whatsapp.")
    __properties: ClassVar[List[str]] = ["statistics", "timeframe", "interval", "conversion_metric_id", "filter"]

    @field_validator('statistics')
    def statistics_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['average_order_value', 'bounce_rate', 'bounced', 'bounced_or_failed', 'bounced_or_failed_rate', 'click_rate', 'click_to_open_rate', 'clicks', 'clicks_unique', 'conversion_rate', 'conversion_uniques', 'conversion_value', 'conversions', 'delivered', 'delivery_rate', 'failed', 'failed_rate', 'open_rate', 'opens', 'opens_unique', 'recipients', 'revenue_per_recipient', 'spam_complaint_rate', 'spam_complaints', 'unsubscribe_rate', 'unsubscribe_uniques', 'unsubscribes']):
                raise ValueError("each list item must be one of ('average_order_value', 'bounce_rate', 'bounced', 'bounced_or_failed', 'bounced_or_failed_rate', 'click_rate', 'click_to_open_rate', 'clicks', 'clicks_unique', 'conversion_rate', 'conversion_uniques', 'conversion_value', 'conversions', 'delivered', 'delivery_rate', 'failed', 'failed_rate', 'open_rate', 'opens', 'opens_unique', 'recipients', 'revenue_per_recipient', 'spam_complaint_rate', 'spam_complaints', 'unsubscribe_rate', 'unsubscribe_uniques', 'unsubscribes')")
        return value

    @field_validator('interval')
    def interval_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['daily', 'hourly', 'monthly', 'weekly']):
            raise ValueError("must be one of enum values ('daily', 'hourly', 'monthly', 'weekly')")
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
        """Create an instance of FlowSeriesRequestDTOResourceObjectAttributes from a JSON string"""
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
        # set to None if interval (nullable) is None
        # and model_fields_set contains the field
        if self.interval is None and "interval" in self.model_fields_set:
            _dict['interval'] = None

        # set to None if conversion_metric_id (nullable) is None
        # and model_fields_set contains the field
        if self.conversion_metric_id is None and "conversion_metric_id" in self.model_fields_set:
            _dict['conversion_metric_id'] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowSeriesRequestDTOResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statistics": obj.get("statistics"),
            "timeframe": obj.get("timeframe"),
            "interval": obj.get("interval"),
            "conversion_metric_id": obj.get("conversion_metric_id"),
            "filter": obj.get("filter")
        })
        return _obj


