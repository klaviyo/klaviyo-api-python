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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.flow_series_report_enum import FlowSeriesReportEnum
from openapi_client.models.post_flow_series_response_dto_data_attributes import PostFlowSeriesResponseDTODataAttributes
from openapi_client.models.post_flow_values_response_dto_data_relationships import PostFlowValuesResponseDTODataRelationships
from typing import Optional, Set
from typing_extensions import Self

class PostFlowSeriesResponseDTOData(BaseModel):
    """
    PostFlowSeriesResponseDTOData
    """ # noqa: E501
    type: FlowSeriesReportEnum
    attributes: PostFlowSeriesResponseDTODataAttributes
    relationships: Optional[PostFlowValuesResponseDTODataRelationships] = None
    __properties: ClassVar[List[str]] = ["type", "attributes", "relationships"]

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
        """Create an instance of PostFlowSeriesResponseDTOData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationships
        if self.relationships:
            _dict['relationships'] = self.relationships.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostFlowSeriesResponseDTOData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "attributes": PostFlowSeriesResponseDTODataAttributes.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "relationships": PostFlowValuesResponseDTODataRelationships.from_dict(obj["relationships"]) if obj.get("relationships") is not None else None
        })
        return _obj


