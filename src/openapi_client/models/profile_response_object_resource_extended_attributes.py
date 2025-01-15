# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2025-01-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.predictive_analytics import PredictiveAnalytics
from openapi_client.models.profile_location import ProfileLocation
from openapi_client.models.subscriptions import Subscriptions
from typing import Optional, Set
from typing_extensions import Self

class ProfileResponseObjectResourceExtendedAttributes(BaseModel):
    """
    ProfileResponseObjectResourceExtendedAttributes
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="Individual's email address")
    phone_number: Optional[StrictStr] = Field(default=None, description="Individual's phone number in E.164 format")
    external_id: Optional[StrictStr] = Field(default=None, description="A unique identifier used by customers to associate Klaviyo profiles with profiles in an external system, such as a point-of-sale system. Format varies based on the external system.")
    first_name: Optional[StrictStr] = Field(default=None, description="Individual's first name")
    last_name: Optional[StrictStr] = Field(default=None, description="Individual's last name")
    organization: Optional[StrictStr] = Field(default=None, description="Name of the company or organization within the company for whom the individual works")
    locale: Optional[StrictStr] = Field(default=None, description="The locale of the profile, in the IETF BCP 47 language tag format like (ISO 639-1/2)-(ISO 3166 alpha-2)")
    title: Optional[StrictStr] = Field(default=None, description="Individual's job title")
    image: Optional[StrictStr] = Field(default=None, description="URL pointing to the location of a profile image")
    created: Optional[datetime] = Field(default=None, description="Date and time when the profile was created, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)")
    updated: Optional[datetime] = Field(default=None, description="Date and time when the profile was last updated, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)")
    last_event_date: Optional[datetime] = Field(default=None, description="Date and time of the most recent event the triggered an update to the profile, in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm)")
    location: Optional[ProfileLocation] = None
    properties: Optional[Dict[str, Any]] = Field(default=None, description="An object containing key/value pairs for any custom properties assigned to this profile")
    subscriptions: Optional[Subscriptions] = None
    predictive_analytics: Optional[PredictiveAnalytics] = None
    __properties: ClassVar[List[str]] = ["email", "phone_number", "external_id", "first_name", "last_name", "organization", "locale", "title", "image", "created", "updated", "last_event_date", "location", "properties", "subscriptions", "predictive_analytics"]

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
        """Create an instance of ProfileResponseObjectResourceExtendedAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscriptions
        if self.subscriptions:
            _dict['subscriptions'] = self.subscriptions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of predictive_analytics
        if self.predictive_analytics:
            _dict['predictive_analytics'] = self.predictive_analytics.to_dict()
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['phone_number'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        # set to None if organization (nullable) is None
        # and model_fields_set contains the field
        if self.organization is None and "organization" in self.model_fields_set:
            _dict['organization'] = None

        # set to None if locale (nullable) is None
        # and model_fields_set contains the field
        if self.locale is None and "locale" in self.model_fields_set:
            _dict['locale'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and "updated" in self.model_fields_set:
            _dict['updated'] = None

        # set to None if last_event_date (nullable) is None
        # and model_fields_set contains the field
        if self.last_event_date is None and "last_event_date" in self.model_fields_set:
            _dict['last_event_date'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileResponseObjectResourceExtendedAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "phone_number": obj.get("phone_number"),
            "external_id": obj.get("external_id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "organization": obj.get("organization"),
            "locale": obj.get("locale"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "last_event_date": obj.get("last_event_date"),
            "location": ProfileLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "properties": obj.get("properties"),
            "subscriptions": Subscriptions.from_dict(obj["subscriptions"]) if obj.get("subscriptions") is not None else None,
            "predictive_analytics": PredictiveAnalytics.from_dict(obj["predictive_analytics"]) if obj.get("predictive_analytics") is not None else None
        })
        return _obj


