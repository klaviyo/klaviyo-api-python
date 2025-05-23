# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from openapi_client.models.custom_metric_group import CustomMetricGroup
from typing import Optional, Set
from typing_extensions import Self

class CustomMetricDefinition(BaseModel):
    """
    CustomMetricDefinition
    """ # noqa: E501
    aggregation_method: StrictStr = Field(description="Method of aggregation for custom metric measurements. If a metric has a `value` aggregation method, it will be treated as a revenue metric, such as a Placed Order metric. If a metric has a `count` aggregation method, it will only be able to report on conversions like an Active on Site metric. ")
    metric_groups: List[CustomMetricGroup]
    __properties: ClassVar[List[str]] = ["aggregation_method", "metric_groups"]

    @field_validator('aggregation_method')
    def aggregation_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['count', 'value']):
            raise ValueError("must be one of enum values ('count', 'value')")
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
        """Create an instance of CustomMetricDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metric_groups (list)
        _items = []
        if self.metric_groups:
            for _item in self.metric_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metric_groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomMetricDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregation_method": obj.get("aggregation_method"),
            "metric_groups": [CustomMetricGroup.from_dict(_item) for _item in obj["metric_groups"]] if obj.get("metric_groups") is not None else None
        })
        return _obj


