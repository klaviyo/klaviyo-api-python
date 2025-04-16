# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2025-04-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_profile_response_collection_compound_document_data_inner_all_of_relationships_push_tokens import GetProfileResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsPushTokens
from openapi_client.models.get_profile_response_compound_document_data_all_of_relationships_lists import GetProfileResponseCompoundDocumentDataAllOfRelationshipsLists
from openapi_client.models.get_profile_response_compound_document_data_all_of_relationships_segments import GetProfileResponseCompoundDocumentDataAllOfRelationshipsSegments
from typing import Optional, Set
from typing_extensions import Self

class GetProfileResponseCompoundDocumentDataAllOfRelationships(BaseModel):
    """
    GetProfileResponseCompoundDocumentDataAllOfRelationships
    """ # noqa: E501
    lists: Optional[GetProfileResponseCompoundDocumentDataAllOfRelationshipsLists] = None
    segments: Optional[GetProfileResponseCompoundDocumentDataAllOfRelationshipsSegments] = None
    push_tokens: Optional[GetProfileResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsPushTokens] = Field(default=None, alias="push-tokens")
    __properties: ClassVar[List[str]] = ["lists", "segments", "push-tokens"]

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
        """Create an instance of GetProfileResponseCompoundDocumentDataAllOfRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lists
        if self.lists:
            _dict['lists'] = self.lists.to_dict()
        # override the default output from pydantic by calling `to_dict()` of segments
        if self.segments:
            _dict['segments'] = self.segments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of push_tokens
        if self.push_tokens:
            _dict['push-tokens'] = self.push_tokens.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProfileResponseCompoundDocumentDataAllOfRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lists": GetProfileResponseCompoundDocumentDataAllOfRelationshipsLists.from_dict(obj["lists"]) if obj.get("lists") is not None else None,
            "segments": GetProfileResponseCompoundDocumentDataAllOfRelationshipsSegments.from_dict(obj["segments"]) if obj.get("segments") is not None else None,
            "push-tokens": GetProfileResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsPushTokens.from_dict(obj["push-tokens"]) if obj.get("push-tokens") is not None else None
        })
        return _obj


