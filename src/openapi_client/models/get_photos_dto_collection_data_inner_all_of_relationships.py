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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_photos_dto_collection_data_inner_all_of_relationships_test_photographers import GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers
from typing import Optional, Set
from typing_extensions import Self

class GetPhotosDTOCollectionDataInnerAllOfRelationships(BaseModel):
    """
    GetPhotosDTOCollectionDataInnerAllOfRelationships
    """ # noqa: E501
    test_photographers: Optional[GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers] = Field(default=None, alias="test-photographers")
    test_cameras: Optional[GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers] = Field(default=None, alias="test-cameras")
    test_city: Optional[GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers] = Field(default=None, alias="test-city")
    additional_camera: Optional[GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers] = Field(default=None, alias="additional-camera")
    __properties: ClassVar[List[str]] = ["test-photographers", "test-cameras", "test-city", "additional-camera"]

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
        """Create an instance of GetPhotosDTOCollectionDataInnerAllOfRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of test_photographers
        if self.test_photographers:
            _dict['test-photographers'] = self.test_photographers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_cameras
        if self.test_cameras:
            _dict['test-cameras'] = self.test_cameras.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_city
        if self.test_city:
            _dict['test-city'] = self.test_city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_camera
        if self.additional_camera:
            _dict['additional-camera'] = self.additional_camera.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPhotosDTOCollectionDataInnerAllOfRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "test-photographers": GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers.from_dict(obj["test-photographers"]) if obj.get("test-photographers") is not None else None,
            "test-cameras": GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers.from_dict(obj["test-cameras"]) if obj.get("test-cameras") is not None else None,
            "test-city": GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers.from_dict(obj["test-city"]) if obj.get("test-city") is not None else None,
            "additional-camera": GetPhotosDTOCollectionDataInnerAllOfRelationshipsTestPhotographers.from_dict(obj["additional-camera"]) if obj.get("additional-camera") is not None else None
        })
        return _obj


