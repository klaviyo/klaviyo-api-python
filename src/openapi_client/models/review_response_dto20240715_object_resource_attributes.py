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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.review_product_dto import ReviewProductDTO
from openapi_client.models.review_public_reply import ReviewPublicReply
from typing import Optional, Set
from typing_extensions import Self

class ReviewResponseDTO20240715ObjectResourceAttributes(BaseModel):
    """
    ReviewResponseDTO20240715ObjectResourceAttributes
    """ # noqa: E501
    email: Optional[StrictStr] = Field(description="The email of the author of this review")
    status: Optional[StrictStr] = Field(default=None, description="The status of this review")
    verified: StrictBool = Field(description="The verification status of this review (aka whether or not we have confirmation that the customer bought the product)")
    review_type: Optional[StrictStr] = Field(description="The type of this review — either a review, question, or rating")
    created: Optional[datetime] = Field(description="The datetime when this review was created")
    updated: Optional[datetime] = Field(description="The datetime when this review was updated")
    images: List[StrictStr] = Field(description="The list of images submitted with this review (represented as a list of urls). If there are no images, this field will be an empty list.")
    product: Optional[ReviewProductDTO] = None
    rating: Optional[StrictInt] = Field(default=None, description="The rating of this review on a scale from 1-5. If the review type is \"question\", this field will be null.")
    author: Optional[StrictStr] = Field(default=None, description="The author of this review")
    content: Optional[StrictStr] = Field(default=None, description="The content of this review")
    title: Optional[StrictStr] = Field(default=None, description="The title of this review")
    smart_quote: Optional[StrictStr] = Field(default=None, description="A quote from this review that summarizes the content")
    public_reply: Optional[ReviewPublicReply] = None
    __properties: ClassVar[List[str]] = ["email", "status", "verified", "review_type", "created", "updated", "images", "product", "rating", "author", "content", "title", "smart_quote", "public_reply"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['featured', 'pending', 'published', 'rejected', 'unpublished']):
            raise ValueError("must be one of enum values ('featured', 'pending', 'published', 'rejected', 'unpublished')")
        return value

    @field_validator('review_type')
    def review_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['question', 'rating', 'review']):
            raise ValueError("must be one of enum values ('question', 'rating', 'review')")
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
        """Create an instance of ReviewResponseDTO20240715ObjectResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_reply
        if self.public_reply:
            _dict['public_reply'] = self.public_reply.to_dict()
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if review_type (nullable) is None
        # and model_fields_set contains the field
        if self.review_type is None and "review_type" in self.model_fields_set:
            _dict['review_type'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and "updated" in self.model_fields_set:
            _dict['updated'] = None

        # set to None if rating (nullable) is None
        # and model_fields_set contains the field
        if self.rating is None and "rating" in self.model_fields_set:
            _dict['rating'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if smart_quote (nullable) is None
        # and model_fields_set contains the field
        if self.smart_quote is None and "smart_quote" in self.model_fields_set:
            _dict['smart_quote'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReviewResponseDTO20240715ObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "status": obj.get("status"),
            "verified": obj.get("verified"),
            "review_type": obj.get("review_type"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "images": obj.get("images"),
            "product": ReviewProductDTO.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "rating": obj.get("rating"),
            "author": obj.get("author"),
            "content": obj.get("content"),
            "title": obj.get("title"),
            "smart_quote": obj.get("smart_quote"),
            "public_reply": ReviewPublicReply.from_dict(obj["public_reply"]) if obj.get("public_reply") is not None else None
        })
        return _obj

