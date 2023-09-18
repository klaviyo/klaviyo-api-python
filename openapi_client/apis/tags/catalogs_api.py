# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-09-15
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_back_in_stock_subscriptions_.post import CreateBackInStockSubscription
from openapi_client.paths.api_catalog_categories_.post import CreateCatalogCategory
from openapi_client.paths.api_catalog_categories_id_relationships_items_.post import CreateCatalogCategoryRelationshipsItems
from openapi_client.paths.api_catalog_items_.post import CreateCatalogItem
from openapi_client.paths.api_catalog_items_id_relationships_categories_.post import CreateCatalogItemRelationshipsCategories
from openapi_client.paths.api_catalog_variants_.post import CreateCatalogVariant
from openapi_client.paths.api_catalog_categories_id_.delete import DeleteCatalogCategory
from openapi_client.paths.api_catalog_categories_id_relationships_items_.delete import DeleteCatalogCategoryRelationshipsItems
from openapi_client.paths.api_catalog_items_id_.delete import DeleteCatalogItem
from openapi_client.paths.api_catalog_items_id_relationships_categories_.delete import DeleteCatalogItemRelationshipsCategories
from openapi_client.paths.api_catalog_variants_id_.delete import DeleteCatalogVariant
from openapi_client.paths.api_catalog_categories_.get import GetCatalogCategories
from openapi_client.paths.api_catalog_categories_id_.get import GetCatalogCategory
from openapi_client.paths.api_catalog_categories_id_items_.get import GetCatalogCategoryItems
from openapi_client.paths.api_catalog_categories_id_relationships_items_.get import GetCatalogCategoryRelationshipsItems
from openapi_client.paths.api_catalog_items_id_.get import GetCatalogItem
from openapi_client.paths.api_catalog_items_id_categories_.get import GetCatalogItemCategories
from openapi_client.paths.api_catalog_items_id_relationships_categories_.get import GetCatalogItemRelationshipsCategories
from openapi_client.paths.api_catalog_items_id_variants_.get import GetCatalogItemVariants
from openapi_client.paths.api_catalog_items_.get import GetCatalogItems
from openapi_client.paths.api_catalog_variants_id_.get import GetCatalogVariant
from openapi_client.paths.api_catalog_variants_.get import GetCatalogVariants
from openapi_client.paths.api_catalog_category_bulk_create_jobs_job_id_.get import GetCreateCategoriesJob
from openapi_client.paths.api_catalog_category_bulk_create_jobs_.get import GetCreateCategoriesJobs
from openapi_client.paths.api_catalog_item_bulk_create_jobs_job_id_.get import GetCreateItemsJob
from openapi_client.paths.api_catalog_item_bulk_create_jobs_.get import GetCreateItemsJobs
from openapi_client.paths.api_catalog_variant_bulk_create_jobs_job_id_.get import GetCreateVariantsJob
from openapi_client.paths.api_catalog_variant_bulk_create_jobs_.get import GetCreateVariantsJobs
from openapi_client.paths.api_catalog_category_bulk_delete_jobs_job_id_.get import GetDeleteCategoriesJob
from openapi_client.paths.api_catalog_category_bulk_delete_jobs_.get import GetDeleteCategoriesJobs
from openapi_client.paths.api_catalog_item_bulk_delete_jobs_job_id_.get import GetDeleteItemsJob
from openapi_client.paths.api_catalog_item_bulk_delete_jobs_.get import GetDeleteItemsJobs
from openapi_client.paths.api_catalog_variant_bulk_delete_jobs_job_id_.get import GetDeleteVariantsJob
from openapi_client.paths.api_catalog_variant_bulk_delete_jobs_.get import GetDeleteVariantsJobs
from openapi_client.paths.api_catalog_category_bulk_update_jobs_job_id_.get import GetUpdateCategoriesJob
from openapi_client.paths.api_catalog_category_bulk_update_jobs_.get import GetUpdateCategoriesJobs
from openapi_client.paths.api_catalog_item_bulk_update_jobs_job_id_.get import GetUpdateItemsJob
from openapi_client.paths.api_catalog_item_bulk_update_jobs_.get import GetUpdateItemsJobs
from openapi_client.paths.api_catalog_variant_bulk_update_jobs_job_id_.get import GetUpdateVariantsJob
from openapi_client.paths.api_catalog_variant_bulk_update_jobs_.get import GetUpdateVariantsJobs
from openapi_client.paths.api_catalog_category_bulk_create_jobs_.post import SpawnCreateCategoriesJob
from openapi_client.paths.api_catalog_item_bulk_create_jobs_.post import SpawnCreateItemsJob
from openapi_client.paths.api_catalog_variant_bulk_create_jobs_.post import SpawnCreateVariantsJob
from openapi_client.paths.api_catalog_category_bulk_delete_jobs_.post import SpawnDeleteCategoriesJob
from openapi_client.paths.api_catalog_item_bulk_delete_jobs_.post import SpawnDeleteItemsJob
from openapi_client.paths.api_catalog_variant_bulk_delete_jobs_.post import SpawnDeleteVariantsJob
from openapi_client.paths.api_catalog_category_bulk_update_jobs_.post import SpawnUpdateCategoriesJob
from openapi_client.paths.api_catalog_item_bulk_update_jobs_.post import SpawnUpdateItemsJob
from openapi_client.paths.api_catalog_variant_bulk_update_jobs_.post import SpawnUpdateVariantsJob
from openapi_client.paths.api_catalog_categories_id_.patch import UpdateCatalogCategory
from openapi_client.paths.api_catalog_categories_id_relationships_items_.patch import UpdateCatalogCategoryRelationshipsItems
from openapi_client.paths.api_catalog_items_id_.patch import UpdateCatalogItem
from openapi_client.paths.api_catalog_items_id_relationships_categories_.patch import UpdateCatalogItemRelationshipsCategories
from openapi_client.paths.api_catalog_variants_id_.patch import UpdateCatalogVariant


class CatalogsApi(
    CreateBackInStockSubscription,
    CreateCatalogCategory,
    CreateCatalogCategoryRelationshipsItems,
    CreateCatalogItem,
    CreateCatalogItemRelationshipsCategories,
    CreateCatalogVariant,
    DeleteCatalogCategory,
    DeleteCatalogCategoryRelationshipsItems,
    DeleteCatalogItem,
    DeleteCatalogItemRelationshipsCategories,
    DeleteCatalogVariant,
    GetCatalogCategories,
    GetCatalogCategory,
    GetCatalogCategoryItems,
    GetCatalogCategoryRelationshipsItems,
    GetCatalogItem,
    GetCatalogItemCategories,
    GetCatalogItemRelationshipsCategories,
    GetCatalogItemVariants,
    GetCatalogItems,
    GetCatalogVariant,
    GetCatalogVariants,
    GetCreateCategoriesJob,
    GetCreateCategoriesJobs,
    GetCreateItemsJob,
    GetCreateItemsJobs,
    GetCreateVariantsJob,
    GetCreateVariantsJobs,
    GetDeleteCategoriesJob,
    GetDeleteCategoriesJobs,
    GetDeleteItemsJob,
    GetDeleteItemsJobs,
    GetDeleteVariantsJob,
    GetDeleteVariantsJobs,
    GetUpdateCategoriesJob,
    GetUpdateCategoriesJobs,
    GetUpdateItemsJob,
    GetUpdateItemsJobs,
    GetUpdateVariantsJob,
    GetUpdateVariantsJobs,
    SpawnCreateCategoriesJob,
    SpawnCreateItemsJob,
    SpawnCreateVariantsJob,
    SpawnDeleteCategoriesJob,
    SpawnDeleteItemsJob,
    SpawnDeleteVariantsJob,
    SpawnUpdateCategoriesJob,
    SpawnUpdateItemsJob,
    SpawnUpdateVariantsJob,
    UpdateCatalogCategory,
    UpdateCatalogCategoryRelationshipsItems,
    UpdateCatalogItem,
    UpdateCatalogItemRelationshipsCategories,
    UpdateCatalogVariant,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass