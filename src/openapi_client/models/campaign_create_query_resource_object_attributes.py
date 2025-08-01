# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

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
from openapi_client.models.audiences import Audiences
from openapi_client.models.campaign_create_query_resource_object_attributes_campaign_messages import CampaignCreateQueryResourceObjectAttributesCampaignMessages
from typing import Optional, Set
from typing_extensions import Self

class CampaignCreateQueryResourceObjectAttributes(BaseModel):
    """
    CampaignCreateQueryResourceObjectAttributes
    """ # noqa: E501
    name: StrictStr = Field(description="The campaign name")
    audiences: Audiences
    send_strategy: Optional[Dict[str, Any]] = Field(default=None, description="The send strategy the campaign will send with. Defaults to 'Immediate' send strategy.")
    send_options: Optional[Dict[str, Any]] = Field(default=None, description="Options to use when sending a campaign")
    tracking_options: Optional[Dict[str, Any]] = Field(default=None, description="The tracking options associated with the campaign")
    campaign_messages: CampaignCreateQueryResourceObjectAttributesCampaignMessages = Field(alias="campaign-messages")
    __properties: ClassVar[List[str]] = ["name", "audiences", "send_strategy", "send_options", "tracking_options", "campaign-messages"]

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
        """Create an instance of CampaignCreateQueryResourceObjectAttributes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of audiences
        if self.audiences:
            _dict['audiences'] = self.audiences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_messages
        if self.campaign_messages:
            _dict['campaign-messages'] = self.campaign_messages.to_dict()
        # set to None if send_strategy (nullable) is None
        # and model_fields_set contains the field
        if self.send_strategy is None and "send_strategy" in self.model_fields_set:
            _dict['send_strategy'] = None

        # set to None if send_options (nullable) is None
        # and model_fields_set contains the field
        if self.send_options is None and "send_options" in self.model_fields_set:
            _dict['send_options'] = None

        # set to None if tracking_options (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_options is None and "tracking_options" in self.model_fields_set:
            _dict['tracking_options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "audiences": Audiences.from_dict(obj["audiences"]) if obj.get("audiences") is not None else None,
            "send_strategy": obj.get("send_strategy"),
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "campaign-messages": CampaignCreateQueryResourceObjectAttributesCampaignMessages.from_dict(obj["campaign-messages"]) if obj.get("campaign-messages") is not None else None
        })
        return _obj


