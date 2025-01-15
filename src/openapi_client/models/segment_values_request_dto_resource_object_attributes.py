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

class SegmentValuesRequestDTOResourceObjectAttributes(BaseModel):
    """
    SegmentValuesRequestDTOResourceObjectAttributes
    """ # noqa: E501
    statistics: List[StrictStr] = Field(description="List of statistics to query for.")
    timeframe: Dict[str, Any] = Field(description="The timeframe to query for data within. Data is unavailable before June 1st, 2023. Please use a timeframe after this date. The max length a timeframe can be is 1 year")
    filter: Optional[StrictStr] = Field(default=None, description="API filter string used to filter the query. Allowed filters are segment_id. Allowed operators are equals, any. Only one filter can be used per attribute. Max of 100 messages per ANY filter.")
    __properties: ClassVar[List[str]] = ["statistics", "timeframe", "filter"]

    @field_validator('statistics')
    def statistics_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['members_added', 'members_removed', 'net_members_changed', 'total_members']):
                raise ValueError("each list item must be one of ('members_added', 'members_removed', 'net_members_changed', 'total_members')")
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
        """Create an instance of SegmentValuesRequestDTOResourceObjectAttributes from a JSON string"""
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
        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SegmentValuesRequestDTOResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statistics": obj.get("statistics"),
            "timeframe": obj.get("timeframe"),
            "filter": obj.get("filter")
        })
        return _obj


