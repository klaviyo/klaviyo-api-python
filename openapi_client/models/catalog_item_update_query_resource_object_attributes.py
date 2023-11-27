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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CatalogItemUpdateQueryResourceObjectAttributes(BaseModel):
    """
    CatalogItemUpdateQueryResourceObjectAttributes
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The title of the catalog item.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This field can be used to set the price on the catalog item, which is what gets displayed for the item when included in emails. For most price-update use cases, you will also want to update the `price` on any child variants, using the [Update Catalog Variant Endpoint](https://developers.klaviyo.com/en/reference/update_catalog_variant).")
    description: Optional[StrictStr] = Field(default=None, description="A description of the catalog item.")
    url: Optional[StrictStr] = Field(default=None, description="URL pointing to the location of the catalog item on your website.")
    image_full_url: Optional[StrictStr] = Field(default=None, description="URL pointing to the location of a full image of the catalog item.")
    image_thumbnail_url: Optional[StrictStr] = Field(default=None, description="URL pointing to the location of an image thumbnail of the catalog item")
    images: Optional[List[StrictStr]] = Field(default=None, description="List of URLs pointing to the locations of images of the catalog item.")
    custom_metadata: Optional[Union[str, Any]] = Field(default=None, description="Flat JSON blob to provide custom metadata about the catalog item. May not exceed 100kb.")
    published: Optional[StrictBool] = Field(default=None, description="Boolean value indicating whether the catalog item is published.")
    __properties: ClassVar[List[str]] = ["title", "price", "description", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published"]

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
        """Create an instance of CatalogItemUpdateQueryResourceObjectAttributes from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if image_full_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_full_url is None and "image_full_url" in self.model_fields_set:
            _dict['image_full_url'] = None

        # set to None if image_thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_thumbnail_url is None and "image_thumbnail_url" in self.model_fields_set:
            _dict['image_thumbnail_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CatalogItemUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "price": obj.get("price"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "image_full_url": obj.get("image_full_url"),
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "images": obj.get("images"),
            "custom_metadata": obj.get("custom_metadata"),
            "published": obj.get("published")
        })
        return _obj


