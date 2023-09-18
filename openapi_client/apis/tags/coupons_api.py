# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-09-15
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_coupons_.post import CreateCoupon
from openapi_client.paths.api_coupon_codes_.post import CreateCouponCode
from openapi_client.paths.api_coupons_id_.delete import DeleteCoupon
from openapi_client.paths.api_coupon_codes_id_.delete import DeleteCouponCode
from openapi_client.paths.api_coupons_id_.get import GetCoupon
from openapi_client.paths.api_coupon_codes_id_.get import GetCouponCode
from openapi_client.paths.api_coupon_code_bulk_create_jobs_job_id_.get import GetCouponCodeBulkCreateJob
from openapi_client.paths.api_coupon_code_bulk_create_jobs_.get import GetCouponCodeBulkCreateJobs
from openapi_client.paths.api_coupons_id_relationships_coupon_codes_.get import GetCouponCodeRelationshipsCoupon
from openapi_client.paths.api_coupon_codes_.get import GetCouponCodes
from openapi_client.paths.api_coupons_id_coupon_codes_.get import GetCouponCodesForCoupon
from openapi_client.paths.api_coupon_codes_id_coupon_.get import GetCouponForCouponCode
from openapi_client.paths.api_coupon_codes_id_relationships_coupon_.get import GetCouponRelationshipsCouponCodes
from openapi_client.paths.api_coupons_.get import GetCoupons
from openapi_client.paths.api_coupon_code_bulk_create_jobs_.post import SpawnCouponCodeBulkCreateJob
from openapi_client.paths.api_coupons_id_.patch import UpdateCoupon
from openapi_client.paths.api_coupon_codes_id_.patch import UpdateCouponCode


class CouponsApi(
    CreateCoupon,
    CreateCouponCode,
    DeleteCoupon,
    DeleteCouponCode,
    GetCoupon,
    GetCouponCode,
    GetCouponCodeBulkCreateJob,
    GetCouponCodeBulkCreateJobs,
    GetCouponCodeRelationshipsCoupon,
    GetCouponCodes,
    GetCouponCodesForCoupon,
    GetCouponForCouponCode,
    GetCouponRelationshipsCouponCodes,
    GetCoupons,
    SpawnCouponCodeBulkCreateJob,
    UpdateCoupon,
    UpdateCouponCode,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass