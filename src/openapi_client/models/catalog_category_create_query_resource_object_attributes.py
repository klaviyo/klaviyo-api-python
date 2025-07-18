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

class CatalogCategoryCreateQueryResourceObjectAttributes(BaseModel):
    """
    CatalogCategoryCreateQueryResourceObjectAttributes
    """ # noqa: E501
    external_id: StrictStr = Field(description="The ID of the catalog category in an external system.")
    name: StrictStr = Field(description="The name of the catalog category.")
    integration_type: Optional[StrictStr] = Field(default='$custom', description="The integration type. Currently only \"$custom\" is supported.")
    catalog_type: Optional[StrictStr] = Field(default='$default', description="The type of catalog. Currently only \"$default\" is supported.")
    __properties: ClassVar[List[str]] = ["external_id", "name", "integration_type", "catalog_type"]

    @field_validator('integration_type')
    def integration_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['$custom']):
            raise ValueError("must be one of enum values ('$custom')")
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
        """Create an instance of CatalogCategoryCreateQueryResourceObjectAttributes from a JSON string"""
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
        # set to None if integration_type (nullable) is None
        # and model_fields_set contains the field
        if self.integration_type is None and "integration_type" in self.model_fields_set:
            _dict['integration_type'] = None

        # set to None if catalog_type (nullable) is None
        # and model_fields_set contains the field
        if self.catalog_type is None and "catalog_type" in self.model_fields_set:
            _dict['catalog_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CatalogCategoryCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "external_id": obj.get("external_id"),
            "name": obj.get("name"),
            "integration_type": obj.get("integration_type") if obj.get("integration_type") is not None else '$custom',
            "catalog_type": obj.get("catalog_type") if obj.get("catalog_type") is not None else '$default'
        })
        return _obj


