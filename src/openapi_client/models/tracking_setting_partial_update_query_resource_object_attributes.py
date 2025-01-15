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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.custom_tracking_param_dto import CustomTrackingParamDTO
from openapi_client.models.tracking_param_dto import TrackingParamDTO
from typing import Optional, Set
from typing_extensions import Self

class TrackingSettingPartialUpdateQueryResourceObjectAttributes(BaseModel):
    """
    TrackingSettingPartialUpdateQueryResourceObjectAttributes
    """ # noqa: E501
    auto_add_parameters: Optional[StrictBool] = Field(default=None, description="Whether tracking parameters are automatically added to campaigns and flows.")
    utm_source: Optional[TrackingParamDTO] = None
    utm_medium: Optional[TrackingParamDTO] = None
    utm_campaign: Optional[TrackingParamDTO] = None
    utm_id: Optional[TrackingParamDTO] = None
    utm_term: Optional[TrackingParamDTO] = None
    custom_parameters: Optional[List[CustomTrackingParamDTO]] = Field(default=None, description="List of custom tracking parameters.")
    __properties: ClassVar[List[str]] = ["auto_add_parameters", "utm_source", "utm_medium", "utm_campaign", "utm_id", "utm_term", "custom_parameters"]

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
        """Create an instance of TrackingSettingPartialUpdateQueryResourceObjectAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of utm_source
        if self.utm_source:
            _dict['utm_source'] = self.utm_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_medium
        if self.utm_medium:
            _dict['utm_medium'] = self.utm_medium.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_campaign
        if self.utm_campaign:
            _dict['utm_campaign'] = self.utm_campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_id
        if self.utm_id:
            _dict['utm_id'] = self.utm_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of utm_term
        if self.utm_term:
            _dict['utm_term'] = self.utm_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_parameters (list)
        _items = []
        if self.custom_parameters:
            for _item in self.custom_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_parameters'] = _items
        # set to None if auto_add_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.auto_add_parameters is None and "auto_add_parameters" in self.model_fields_set:
            _dict['auto_add_parameters'] = None

        # set to None if custom_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.custom_parameters is None and "custom_parameters" in self.model_fields_set:
            _dict['custom_parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingSettingPartialUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto_add_parameters": obj.get("auto_add_parameters"),
            "utm_source": TrackingParamDTO.from_dict(obj["utm_source"]) if obj.get("utm_source") is not None else None,
            "utm_medium": TrackingParamDTO.from_dict(obj["utm_medium"]) if obj.get("utm_medium") is not None else None,
            "utm_campaign": TrackingParamDTO.from_dict(obj["utm_campaign"]) if obj.get("utm_campaign") is not None else None,
            "utm_id": TrackingParamDTO.from_dict(obj["utm_id"]) if obj.get("utm_id") is not None else None,
            "utm_term": TrackingParamDTO.from_dict(obj["utm_term"]) if obj.get("utm_term") is not None else None,
            "custom_parameters": [CustomTrackingParamDTO.from_dict(_item) for _item in obj["custom_parameters"]] if obj.get("custom_parameters") is not None else None
        })
        return _obj


