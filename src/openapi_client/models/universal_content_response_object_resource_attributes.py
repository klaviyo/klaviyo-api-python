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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UniversalContentResponseObjectResourceAttributes(BaseModel):
    """
    UniversalContentResponseObjectResourceAttributes
    """ # noqa: E501
    name: StrictStr = Field(description="The name for this universal content")
    definition: Optional[Dict[str, Any]] = None
    created: datetime = Field(description="The datetime when this universal content was created")
    updated: datetime = Field(description="The datetime when this universal content was updated")
    screenshot_status: StrictStr = Field(description="The status of a universal content screenshot.")
    screenshot_url: StrictStr
    __properties: ClassVar[List[str]] = ["name", "definition", "created", "updated", "screenshot_status", "screenshot_url"]

    @field_validator('screenshot_status')
    def screenshot_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['completed', 'failed', 'generating', 'never_generated', 'not_renderable', 'stale']):
            raise ValueError("must be one of enum values ('completed', 'failed', 'generating', 'never_generated', 'not_renderable', 'stale')")
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
        """Create an instance of UniversalContentResponseObjectResourceAttributes from a JSON string"""
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
        # set to None if definition (nullable) is None
        # and model_fields_set contains the field
        if self.definition is None and "definition" in self.model_fields_set:
            _dict['definition'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UniversalContentResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "definition": obj.get("definition"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "screenshot_status": obj.get("screenshot_status"),
            "screenshot_url": obj.get("screenshot_url")
        })
        return _obj


