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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FormValuesRequestDTOResourceObjectAttributes(BaseModel):
    """
    FormValuesRequestDTOResourceObjectAttributes
    """ # noqa: E501
    statistics: List[StrictStr] = Field(description="List of statistics to query for. All rate statistics will be returned in fractional form [0.0, 1.0]")
    timeframe: Dict[str, Any] = Field(description="The time frame to pull data from (Max length: 1 year). See [available time frames](https://developers.klaviyo.com/en/reference/reporting_api_overview#available-time-frames).")
    group_by: Optional[List[StrictStr]] = Field(default=None, description="List of attributes to group the data by. Allowed group-bys are form_id, form_version_id. If not passed in, the data will be grouped by form_id. If a group by has prerequisites, they must be passed in together. The prerequisites for form_version_id is form_id")
    filter: Optional[StrictStr] = Field(default=None, description="API filter string used to filter the query. Allowed filters are form_id, form_version_id. Allowed operators are equals, any. Only one filter can be used per attribute, only AND can be used as a combination operator. Max of 100 messages per ANY filter.")
    __properties: ClassVar[List[str]] = ["statistics", "timeframe", "group_by", "filter"]

    @field_validator('statistics')
    def statistics_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['closed_form', 'closed_form_uniques', 'qualified_form', 'qualified_form_uniques', 'submit_rate', 'submits', 'submitted_form_step', 'submitted_form_step_uniques', 'viewed_form', 'viewed_form_step', 'viewed_form_step_uniques', 'viewed_form_uniques']):
                raise ValueError("each list item must be one of ('closed_form', 'closed_form_uniques', 'qualified_form', 'qualified_form_uniques', 'submit_rate', 'submits', 'submitted_form_step', 'submitted_form_step_uniques', 'viewed_form', 'viewed_form_step', 'viewed_form_step_uniques', 'viewed_form_uniques')")
        return value

    @field_validator('group_by')
    def group_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['form_id', 'form_version_id']):
                raise ValueError("each list item must be one of ('form_id', 'form_version_id')")
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
        """Create an instance of FormValuesRequestDTOResourceObjectAttributes from a JSON string"""
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
        # set to None if group_by (nullable) is None
        # and model_fields_set contains the field
        if self.group_by is None and "group_by" in self.model_fields_set:
            _dict['group_by'] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormValuesRequestDTOResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statistics": obj.get("statistics"),
            "timeframe": obj.get("timeframe"),
            "group_by": obj.get("group_by"),
            "filter": obj.get("filter")
        })
        return _obj


