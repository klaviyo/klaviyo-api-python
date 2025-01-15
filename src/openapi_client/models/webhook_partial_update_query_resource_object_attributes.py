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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebhookPartialUpdateQueryResourceObjectAttributes(BaseModel):
    """
    WebhookPartialUpdateQueryResourceObjectAttributes
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="A name for the webhook.")
    description: Optional[StrictStr] = Field(default=None, description="A description for the webhook.")
    endpoint_url: Optional[StrictStr] = Field(default=None, description="A url to send webhook calls to. Must be https.")
    secret_key: Optional[StrictStr] = Field(default=None, description="A secret key, that will be used for webhook request signing.")
    enabled: Optional[StrictBool] = Field(default=None, description="Is the webhook enabled.")
    __properties: ClassVar[List[str]] = ["name", "description", "endpoint_url", "secret_key", "enabled"]

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
        """Create an instance of WebhookPartialUpdateQueryResourceObjectAttributes from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpoint_url'] = None

        # set to None if secret_key (nullable) is None
        # and model_fields_set contains the field
        if self.secret_key is None and "secret_key" in self.model_fields_set:
            _dict['secret_key'] = None

        # set to None if enabled (nullable) is None
        # and model_fields_set contains the field
        if self.enabled is None and "enabled" in self.model_fields_set:
            _dict['enabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookPartialUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "endpoint_url": obj.get("endpoint_url"),
            "secret_key": obj.get("secret_key"),
            "enabled": obj.get("enabled")
        })
        return _obj


