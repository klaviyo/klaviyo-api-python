# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-05-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProfileLocation(BaseModel):
    """
    ProfileLocation
    """ # noqa: E501
    address1: Optional[StrictStr] = Field(default=None, description="First line of street address")
    address2: Optional[StrictStr] = Field(default=None, description="Second line of street address")
    city: Optional[StrictStr] = Field(default=None, description="City name")
    country: Optional[StrictStr] = Field(default=None, description="Country name")
    latitude: Optional[Any] = Field(default=None, description="Latitude coordinate. We recommend providing a precision of four decimal places.")
    longitude: Optional[Any] = Field(default=None, description="Longitude coordinate. We recommend providing a precision of four decimal places.")
    region: Optional[StrictStr] = Field(default=None, description="Region within a country, such as state or province")
    zip: Optional[StrictStr] = Field(default=None, description="Zip code")
    timezone: Optional[StrictStr] = Field(default=None, description="Time zone name. We recommend using time zones from the IANA Time Zone Database.")
    ip: Optional[StrictStr] = Field(default=None, description="IP Address")
    __properties: ClassVar[List[str]] = ["address1", "address2", "city", "country", "latitude", "longitude", "region", "zip", "timezone", "ip"]

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
        """Create an instance of ProfileLocation from a JSON string"""
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
        # set to None if address1 (nullable) is None
        # and model_fields_set contains the field
        if self.address1 is None and "address1" in self.model_fields_set:
            _dict['address1'] = None

        # set to None if address2 (nullable) is None
        # and model_fields_set contains the field
        if self.address2 is None and "address2" in self.model_fields_set:
            _dict['address2'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if zip (nullable) is None
        # and model_fields_set contains the field
        if self.zip is None and "zip" in self.model_fields_set:
            _dict['zip'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProfileLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "region": obj.get("region"),
            "zip": obj.get("zip"),
            "timezone": obj.get("timezone"),
            "ip": obj.get("ip")
        })
        return _obj

