# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProfileMetaPatchProperties(BaseModel):
    """
    ProfileMetaPatchProperties
    """ # noqa: E501
    append: Optional[Union[str, Any]] = Field(default=None, description="Append a simple value or values to this property array")
    unappend: Optional[Union[str, Any]] = Field(default=None, description="Remove a simple value or values from this property array")
    unset: Optional[Any] = Field(default=None, description="Remove a key or keys (and their values) completely from properties")
    __properties: ClassVar[List[str]] = ["append", "unappend", "unset"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProfileMetaPatchProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if unset (nullable) is None
        # and model_fields_set contains the field
        if self.unset is None and "unset" in self.model_fields_set:
            _dict['unset'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProfileMetaPatchProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "append": obj.get("append"),
            "unappend": obj.get("unappend"),
            "unset": obj.get("unset")
        })
        return _obj


