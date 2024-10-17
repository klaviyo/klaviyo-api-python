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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.collection_links import CollectionLinks
from openapi_client.models.get_bulk_profile_suppressions_remove_job_response_collection_data_inner import GetBulkProfileSuppressionsRemoveJobResponseCollectionDataInner
from typing import Optional, Set
from typing_extensions import Self

class GetBulkProfileSuppressionsRemoveJobResponseCollection(BaseModel):
    """
    GetBulkProfileSuppressionsRemoveJobResponseCollection
    """ # noqa: E501
    data: List[GetBulkProfileSuppressionsRemoveJobResponseCollectionDataInner]
    links: Optional[CollectionLinks] = None
    __properties: ClassVar[List[str]] = ["data", "links"]

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
        """Create an instance of GetBulkProfileSuppressionsRemoveJobResponseCollection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetBulkProfileSuppressionsRemoveJobResponseCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [GetBulkProfileSuppressionsRemoveJobResponseCollectionDataInner.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "links": CollectionLinks.from_dict(obj["links"]) if obj.get("links") is not None else None
        })
        return _obj


