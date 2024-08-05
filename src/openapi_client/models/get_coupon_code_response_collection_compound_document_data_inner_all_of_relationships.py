# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-07-15
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
from openapi_client.models.get_coupon_code_response_collection_compound_document_data_inner_all_of_relationships_coupon import GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsCoupon
from openapi_client.models.get_photos_dto_collection_data_inner_all_of_relationships_test_photographers import GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers
from typing import Optional, Set
from typing_extensions import Self

class GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationships(BaseModel):
    """
    GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationships
    """ # noqa: E501
    coupon: Optional[GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsCoupon] = None
    profile: Optional[GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers] = None
    __properties: ClassVar[List[str]] = ["coupon", "profile"]

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
        """Create an instance of GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of coupon
        if self.coupon:
            _dict['coupon'] = self.coupon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "coupon": GetCouponCodeResponseCollectionCompoundDocumentDataInnerAllOfRelationshipsCoupon.from_dict(obj["coupon"]) if obj.get("coupon") is not None else None,
            "profile": GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers.from_dict(obj["profile"]) if obj.get("profile") is not None else None
        })
        return _obj


