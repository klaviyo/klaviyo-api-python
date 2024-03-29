# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-02-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CatalogVariantBulkCreateJobEnum(str, Enum):
    """
    CatalogVariantBulkCreateJobEnum
    """

    """
    allowed enum values
    """
    CATALOG_MINUS_VARIANT_MINUS_BULK_MINUS_CREATE_MINUS_JOB = 'catalog-variant-bulk-create-job'

    @classmethod
    def from_json(cls, json_str: str) -> CatalogVariantBulkCreateJobEnum:
        """Create an instance of CatalogVariantBulkCreateJobEnum from a JSON string"""
        return CatalogVariantBulkCreateJobEnum(json.loads(json_str))


