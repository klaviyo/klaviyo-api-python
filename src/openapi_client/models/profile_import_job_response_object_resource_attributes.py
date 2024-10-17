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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProfileImportJobResponseObjectResourceAttributes(BaseModel):
    """
    ProfileImportJobResponseObjectResourceAttributes
    """ # noqa: E501
    status: Optional[StrictStr] = Field(description="Status of the asynchronous job.")
    created_at: Optional[datetime] = Field(description="The date and time the job was created in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).")
    total_count: StrictInt = Field(description="The total number of operations to be processed by the job. See `completed_count` for the job's current progress.")
    completed_count: Optional[StrictInt] = Field(default=0, description="The total number of operations that have been completed by the job.")
    failed_count: Optional[StrictInt] = Field(default=0, description="The total number of operations that have failed as part of the job.")
    completed_at: Optional[datetime] = Field(default=None, description="Date and time the job was completed in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).")
    expires_at: Optional[datetime] = Field(default=None, description="Date and time the job expires in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).")
    started_at: Optional[datetime] = Field(default=None, description="Date and time the job started processing in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).")
    __properties: ClassVar[List[str]] = ["status", "created_at", "total_count", "completed_count", "failed_count", "completed_at", "expires_at", "started_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['cancelled', 'complete', 'processing', 'queued']):
            raise ValueError("must be one of enum values ('cancelled', 'complete', 'processing', 'queued')")
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
        """Create an instance of ProfileImportJobResponseObjectResourceAttributes from a JSON string"""
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
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if completed_count (nullable) is None
        # and model_fields_set contains the field
        if self.completed_count is None and "completed_count" in self.model_fields_set:
            _dict['completed_count'] = None

        # set to None if failed_count (nullable) is None
        # and model_fields_set contains the field
        if self.failed_count is None and "failed_count" in self.model_fields_set:
            _dict['failed_count'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['started_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileImportJobResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "total_count": obj.get("total_count"),
            "completed_count": obj.get("completed_count") if obj.get("completed_count") is not None else 0,
            "failed_count": obj.get("failed_count") if obj.get("failed_count") is not None else 0,
            "completed_at": obj.get("completed_at"),
            "expires_at": obj.get("expires_at"),
            "started_at": obj.get("started_at")
        })
        return _obj


