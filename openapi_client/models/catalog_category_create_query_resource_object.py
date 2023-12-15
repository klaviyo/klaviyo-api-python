# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-12-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from openapi_client.models.catalog_category_create_query_resource_object_attributes import CatalogCategoryCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_create_query_resource_object_relationships import CatalogCategoryCreateQueryResourceObjectRelationships
from openapi_client.models.catalog_category_enum import CatalogCategoryEnum

class CatalogCategoryCreateQueryResourceObject(BaseModel):
    """
    CatalogCategoryCreateQueryResourceObject
    """
    type: CatalogCategoryEnum = Field(...)
    attributes: CatalogCategoryCreateQueryResourceObjectAttributes = Field(...)
    relationships: Optional[CatalogCategoryCreateQueryResourceObjectRelationships] = None
    __properties = ["type", "attributes", "relationships"]

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
    def from_json(cls, json_str: str) -> CatalogCategoryCreateQueryResourceObject:
        """Create an instance of CatalogCategoryCreateQueryResourceObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationships
        if self.relationships:
            _dict['relationships'] = self.relationships.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogCategoryCreateQueryResourceObject:
        """Create an instance of CatalogCategoryCreateQueryResourceObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogCategoryCreateQueryResourceObject.parse_obj(obj)

        _obj = CatalogCategoryCreateQueryResourceObject.parse_obj({
            "type": obj.get("type"),
            "attributes": CatalogCategoryCreateQueryResourceObjectAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "relationships": CatalogCategoryCreateQueryResourceObjectRelationships.from_dict(obj.get("relationships")) if obj.get("relationships") is not None else None
        })
        return _obj


