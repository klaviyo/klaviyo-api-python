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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.segment_definition import SegmentDefinition
from typing import Optional, Set
from typing_extensions import Self

class SegmentRetrieveResponseObjectResourceAttributes(BaseModel):
    """
    SegmentRetrieveResponseObjectResourceAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="A helpful name to label the segment")
    definition: Optional[SegmentDefinition] = None
    created: Optional[datetime] = Field(default=None, description="Date and time when the segment was created, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)")
    updated: Optional[datetime] = Field(default=None, description="Date and time when the segment was last updated, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)")
    is_active: StrictBool
    is_processing: StrictBool
    is_starred: StrictBool
    __properties: ClassVar[List[str]] = ["name", "definition", "created", "updated", "is_active", "is_processing", "is_starred"]

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
        """Create an instance of SegmentRetrieveResponseObjectResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and "updated" in self.model_fields_set:
            _dict['updated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SegmentRetrieveResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "definition": SegmentDefinition.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "is_active": obj.get("is_active"),
            "is_processing": obj.get("is_processing"),
            "is_starred": obj.get("is_starred")
        })
        return _obj


