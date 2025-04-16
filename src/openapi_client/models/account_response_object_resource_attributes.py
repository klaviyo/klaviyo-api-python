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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.contact_information import ContactInformation
from typing import Optional, Set
from typing_extensions import Self

class AccountResponseObjectResourceAttributes(BaseModel):
    """
    AccountResponseObjectResourceAttributes
    """ # noqa: E501
    test_account: StrictBool = Field(description="Indicates if the account is a test account. Test accounts are not a separate testing engineering environment. Test accounts use the same production environment as normal Klaviyo accounts. This feature is primarily UI based to reduce human errors")
    contact_information: ContactInformation
    industry: Optional[StrictStr] = Field(default=None, description="The kind of business and/or types of goods that the business sells. This is leveraged in Klaviyo analytics and guidance.")
    timezone: Optional[StrictStr] = Field(description="The account's timezone is used when displaying dates and times. This is an IANA timezone. See [the full list here ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).")
    preferred_currency: Optional[StrictStr] = Field(description="The preferred currency for the account. This is the currency used for currency-based metrics in dashboards, analytics, coupons, and templates.")
    public_api_key: Optional[StrictStr] = Field(description="The Public API Key can be used for client-side API calls. [More info here](https://developers.klaviyo.com/en/docs/retrieve_api_credentials).")
    locale: Optional[StrictStr] = Field(description="The account's locale is used to determine the region and language for the account.")
    __properties: ClassVar[List[str]] = ["test_account", "contact_information", "industry", "timezone", "preferred_currency", "public_api_key", "locale"]

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
        """Create an instance of AccountResponseObjectResourceAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact_information
        if self.contact_information:
            _dict['contact_information'] = self.contact_information.to_dict()
        # set to None if industry (nullable) is None
        # and model_fields_set contains the field
        if self.industry is None and "industry" in self.model_fields_set:
            _dict['industry'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if preferred_currency (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_currency is None and "preferred_currency" in self.model_fields_set:
            _dict['preferred_currency'] = None

        # set to None if public_api_key (nullable) is None
        # and model_fields_set contains the field
        if self.public_api_key is None and "public_api_key" in self.model_fields_set:
            _dict['public_api_key'] = None

        # set to None if locale (nullable) is None
        # and model_fields_set contains the field
        if self.locale is None and "locale" in self.model_fields_set:
            _dict['locale'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountResponseObjectResourceAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "test_account": obj.get("test_account"),
            "contact_information": ContactInformation.from_dict(obj["contact_information"]) if obj.get("contact_information") is not None else None,
            "industry": obj.get("industry"),
            "timezone": obj.get("timezone"),
            "preferred_currency": obj.get("preferred_currency"),
            "public_api_key": obj.get("public_api_key"),
            "locale": obj.get("locale")
        })
        return _obj


