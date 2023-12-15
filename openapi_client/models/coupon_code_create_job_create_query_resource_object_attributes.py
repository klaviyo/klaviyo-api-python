# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-12-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from openapi_client.models.coupon_code_create_job_create_query_resource_object_attributes_coupon_codes import CouponCodeCreateJobCreateQueryResourceObjectAttributesCouponCodes

class CouponCodeCreateJobCreateQueryResourceObjectAttributes(BaseModel):
    """
    CouponCodeCreateJobCreateQueryResourceObjectAttributes
    """
    coupon_codes: CouponCodeCreateJobCreateQueryResourceObjectAttributesCouponCodes = Field(..., alias="coupon-codes")
    __properties = ["coupon-codes"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CouponCodeCreateJobCreateQueryResourceObjectAttributes:
        """Create an instance of CouponCodeCreateJobCreateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of coupon_codes
        if self.coupon_codes:
            _dict['coupon-codes'] = self.coupon_codes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CouponCodeCreateJobCreateQueryResourceObjectAttributes:
        """Create an instance of CouponCodeCreateJobCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CouponCodeCreateJobCreateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = CouponCodeCreateJobCreateQueryResourceObjectAttributes.parse_obj({
            "coupon_codes": CouponCodeCreateJobCreateQueryResourceObjectAttributesCouponCodes.from_dict(obj.get("coupon-codes")) if obj.get("coupon-codes") is not None else None
        })
        return _obj


