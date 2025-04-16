from __future__ import absolute_import

from __future__ import print_function
from urllib.parse import quote, unquote

import openapi_client
from klaviyo_api.custom_retry import RetryWithExponentialBackoff
from dataclasses import dataclass, field
from typing import Callable, ClassVar, Dict, Any

@dataclass
class KlaviyoAPI:

    api_key: str
    max_delay: int = 60
    max_retries: int = 3
    test_host: str = ''
    access_token: str = None
    options: Dict[str, Any] = field(default_factory=dict)


    _REVISION = "2025-04-15"

    _STATUS_CODE_CONNECTION_RESET_BY_PEER = 104
    _STATUS_CODE_TOO_MANY_REQUESTS = 429
    _STATUS_CODE_SERVICE_UNAVAILABLE = 503
    _STATUS_CODE_GATEWAY_TIMEOUT = 504
    _STATUS_CODE_A_TIMEOUT_OCCURED = 524

    _RETRY_CODES = {
        _STATUS_CODE_CONNECTION_RESET_BY_PEER,
        _STATUS_CODE_TOO_MANY_REQUESTS,
        _STATUS_CODE_SERVICE_UNAVAILABLE,
        _STATUS_CODE_GATEWAY_TIMEOUT,
        _STATUS_CODE_A_TIMEOUT_OCCURED,
        }

    _CURSOR_SEARCH_TOKENS = ['page%5Bcursor%5D','page[cursor]']


    def __post_init__(self):

        if self.access_token is not None:
            
            self.configuration = openapi_client.Configuration(
                access_token=self.access_token
            )

        elif self.api_key is not None:

            self.configuration = openapi_client.Configuration(
                api_key={'Klaviyo-API-Key':f'Klaviyo-API-Key {self.api_key}'}
                )

        else:
            raise ValueError('One of api_key or access_token must be provided to initialize KlaviyoAPI')

        if self.test_host:
            self.configuration.host = self.test_host

        self.api_client = openapi_client.ApiClient(self.configuration, options=self.options)

        self.api_client.default_headers['revision'] = self._REVISION
        
        if self.max_delay<= 0:
            self.max_delay = .1

        self.retry_wrapper = RetryWithExponentialBackoff(self._RETRY_CODES, self.max_retries, self.max_delay)

    
    @property
    def Accounts(self):
        from openapi_client.api import accounts_api

        ## Adding Accounts to Client
        Accounts=accounts_api.AccountsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Accounts
        Accounts.get_account=self._page_cursor_update(self.retry_logic(Accounts.get_account))
        Accounts.get_accounts=self._page_cursor_update(self.retry_logic(Accounts.get_accounts))
        
        return Accounts
    
    @property
    def Campaigns(self):
        from openapi_client.api import campaigns_api

        ## Adding Campaigns to Client
        Campaigns=campaigns_api.CampaignsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Campaigns
        Campaigns.assign_template_to_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.assign_template_to_campaign_message))
        Campaigns.create_campaign_message_assign_template=self._page_cursor_update(self.retry_logic(Campaigns.create_campaign_message_assign_template))
        Campaigns.cancel_campaign_send=self._page_cursor_update(self.retry_logic(Campaigns.cancel_campaign_send))
        Campaigns.update_campaign_send_job=self._page_cursor_update(self.retry_logic(Campaigns.update_campaign_send_job))
        Campaigns.create_campaign=self._page_cursor_update(self.retry_logic(Campaigns.create_campaign))
        Campaigns.create_campaign_clone=self._page_cursor_update(self.retry_logic(Campaigns.create_campaign_clone))
        Campaigns.clone_campaign=self._page_cursor_update(self.retry_logic(Campaigns.clone_campaign))
        Campaigns.delete_campaign=self._page_cursor_update(self.retry_logic(Campaigns.delete_campaign))
        Campaigns.get_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign))
        Campaigns.get_campaign_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_for_campaign_message))
        Campaigns.get_campaign_message_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_campaign))
        Campaigns.get_campaign_id_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_id_for_campaign_message))
        Campaigns.get_campaign_message_relationships_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_relationships_campaign))
        Campaigns.get_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message))
        Campaigns.get_campaign_recipient_estimation=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_recipient_estimation))
        Campaigns.get_campaign_recipient_estimation_job=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_recipient_estimation_job))
        Campaigns.get_campaign_send_job=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_send_job))
        Campaigns.get_campaigns=self._page_cursor_update(self.retry_logic(Campaigns.get_campaigns))
        Campaigns.get_image_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_image_for_campaign_message))
        Campaigns.get_campaign_message_image=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_image))
        Campaigns.get_image_id_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_image_id_for_campaign_message))
        Campaigns.get_campaign_message_relationships_image=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_relationships_image))
        Campaigns.get_message_ids_for_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_message_ids_for_campaign))
        Campaigns.get_campaign_relationships_campaign_messages=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_relationships_campaign_messages))
        Campaigns.get_campaign_relationships_messages=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_relationships_messages))
        Campaigns.get_messages_for_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_messages_for_campaign))
        Campaigns.get_campaign_campaign_messages=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_campaign_messages))
        Campaigns.get_campaign_messages=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_messages))
        Campaigns.get_tag_ids_for_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_tag_ids_for_campaign))
        Campaigns.get_campaign_relationships_tags=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_relationships_tags))
        Campaigns.get_tags_for_campaign=self._page_cursor_update(self.retry_logic(Campaigns.get_tags_for_campaign))
        Campaigns.get_campaign_tags=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_tags))
        Campaigns.get_template_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_template_for_campaign_message))
        Campaigns.get_campaign_message_template=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_template))
        Campaigns.get_template_id_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.get_template_id_for_campaign_message))
        Campaigns.get_campaign_message_relationships_template=self._page_cursor_update(self.retry_logic(Campaigns.get_campaign_message_relationships_template))
        Campaigns.refresh_campaign_recipient_estimation=self._page_cursor_update(self.retry_logic(Campaigns.refresh_campaign_recipient_estimation))
        Campaigns.create_campaign_recipient_estimation_job=self._page_cursor_update(self.retry_logic(Campaigns.create_campaign_recipient_estimation_job))
        Campaigns.send_campaign=self._page_cursor_update(self.retry_logic(Campaigns.send_campaign))
        Campaigns.create_campaign_send_job=self._page_cursor_update(self.retry_logic(Campaigns.create_campaign_send_job))
        Campaigns.update_campaign=self._page_cursor_update(self.retry_logic(Campaigns.update_campaign))
        Campaigns.update_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.update_campaign_message))
        Campaigns.update_image_for_campaign_message=self._page_cursor_update(self.retry_logic(Campaigns.update_image_for_campaign_message))
        Campaigns.update_campaign_message_relationships_image=self._page_cursor_update(self.retry_logic(Campaigns.update_campaign_message_relationships_image))
        
        return Campaigns
    
    @property
    def Catalogs(self):
        from openapi_client.api import catalogs_api

        ## Adding Catalogs to Client
        Catalogs=catalogs_api.CatalogsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Catalogs
        Catalogs.add_categories_to_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.add_categories_to_catalog_item))
        Catalogs.add_category_to_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.add_category_to_catalog_item))
        Catalogs.create_catalog_item_relationships_category=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item_relationships_category))
        Catalogs.create_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item_relationships_categories))
        Catalogs.add_items_to_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.add_items_to_catalog_category))
        Catalogs.create_catalog_category_relationships_item=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category_relationships_item))
        Catalogs.create_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category_relationships_items))
        Catalogs.bulk_create_catalog_categories=self._page_cursor_update(self.retry_logic(Catalogs.bulk_create_catalog_categories))
        Catalogs.spawn_create_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_create_categories_job))
        Catalogs.create_catalog_category_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category_bulk_create_job))
        Catalogs.bulk_create_catalog_items=self._page_cursor_update(self.retry_logic(Catalogs.bulk_create_catalog_items))
        Catalogs.spawn_create_items_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_create_items_job))
        Catalogs.create_catalog_item_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item_bulk_create_job))
        Catalogs.bulk_create_catalog_variants=self._page_cursor_update(self.retry_logic(Catalogs.bulk_create_catalog_variants))
        Catalogs.spawn_create_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_create_variants_job))
        Catalogs.create_catalog_variant_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_variant_bulk_create_job))
        Catalogs.bulk_delete_catalog_categories=self._page_cursor_update(self.retry_logic(Catalogs.bulk_delete_catalog_categories))
        Catalogs.spawn_delete_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_delete_categories_job))
        Catalogs.create_catalog_category_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category_bulk_delete_job))
        Catalogs.bulk_delete_catalog_items=self._page_cursor_update(self.retry_logic(Catalogs.bulk_delete_catalog_items))
        Catalogs.spawn_delete_items_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_delete_items_job))
        Catalogs.create_catalog_item_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item_bulk_delete_job))
        Catalogs.bulk_delete_catalog_variants=self._page_cursor_update(self.retry_logic(Catalogs.bulk_delete_catalog_variants))
        Catalogs.spawn_delete_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_delete_variants_job))
        Catalogs.create_catalog_variant_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_variant_bulk_delete_job))
        Catalogs.bulk_update_catalog_categories=self._page_cursor_update(self.retry_logic(Catalogs.bulk_update_catalog_categories))
        Catalogs.spawn_update_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_update_categories_job))
        Catalogs.create_catalog_category_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category_bulk_update_job))
        Catalogs.bulk_update_catalog_items=self._page_cursor_update(self.retry_logic(Catalogs.bulk_update_catalog_items))
        Catalogs.spawn_update_items_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_update_items_job))
        Catalogs.create_catalog_item_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item_bulk_update_job))
        Catalogs.bulk_update_catalog_variants=self._page_cursor_update(self.retry_logic(Catalogs.bulk_update_catalog_variants))
        Catalogs.spawn_update_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.spawn_update_variants_job))
        Catalogs.create_catalog_variant_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_variant_bulk_update_job))
        Catalogs.create_back_in_stock_subscription=self._page_cursor_update(self.retry_logic(Catalogs.create_back_in_stock_subscription))
        Catalogs.create_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_category))
        Catalogs.create_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_item))
        Catalogs.create_catalog_variant=self._page_cursor_update(self.retry_logic(Catalogs.create_catalog_variant))
        Catalogs.delete_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.delete_catalog_category))
        Catalogs.delete_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.delete_catalog_item))
        Catalogs.delete_catalog_variant=self._page_cursor_update(self.retry_logic(Catalogs.delete_catalog_variant))
        Catalogs.get_bulk_create_catalog_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_catalog_items_job))
        Catalogs.get_create_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_create_items_job))
        Catalogs.get_catalog_item_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_create_job))
        Catalogs.get_bulk_create_catalog_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_catalog_items_jobs))
        Catalogs.get_create_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_create_items_jobs))
        Catalogs.get_catalog_item_bulk_create_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_create_jobs))
        Catalogs.get_bulk_create_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_categories_job))
        Catalogs.get_create_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_create_categories_job))
        Catalogs.get_catalog_category_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_create_job))
        Catalogs.get_bulk_create_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_categories_jobs))
        Catalogs.get_create_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_create_categories_jobs))
        Catalogs.get_catalog_category_bulk_create_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_create_jobs))
        Catalogs.get_bulk_create_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_variants_job))
        Catalogs.get_create_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_create_variants_job))
        Catalogs.get_catalog_variant_bulk_create_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_create_job))
        Catalogs.get_bulk_create_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_create_variants_jobs))
        Catalogs.get_create_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_create_variants_jobs))
        Catalogs.get_catalog_variant_bulk_create_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_create_jobs))
        Catalogs.get_bulk_delete_catalog_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_catalog_items_job))
        Catalogs.get_delete_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_items_job))
        Catalogs.get_catalog_item_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_delete_job))
        Catalogs.get_bulk_delete_catalog_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_catalog_items_jobs))
        Catalogs.get_delete_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_items_jobs))
        Catalogs.get_catalog_item_bulk_delete_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_delete_jobs))
        Catalogs.get_bulk_delete_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_categories_job))
        Catalogs.get_delete_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_categories_job))
        Catalogs.get_catalog_category_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_delete_job))
        Catalogs.get_bulk_delete_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_categories_jobs))
        Catalogs.get_delete_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_categories_jobs))
        Catalogs.get_catalog_category_bulk_delete_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_delete_jobs))
        Catalogs.get_bulk_delete_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_variants_job))
        Catalogs.get_delete_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_variants_job))
        Catalogs.get_catalog_variant_bulk_delete_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_delete_job))
        Catalogs.get_bulk_delete_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_delete_variants_jobs))
        Catalogs.get_delete_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_delete_variants_jobs))
        Catalogs.get_catalog_variant_bulk_delete_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_delete_jobs))
        Catalogs.get_bulk_update_catalog_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_catalog_items_job))
        Catalogs.get_update_items_job=self._page_cursor_update(self.retry_logic(Catalogs.get_update_items_job))
        Catalogs.get_catalog_item_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_update_job))
        Catalogs.get_bulk_update_catalog_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_catalog_items_jobs))
        Catalogs.get_update_items_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_update_items_jobs))
        Catalogs.get_catalog_item_bulk_update_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_bulk_update_jobs))
        Catalogs.get_bulk_update_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_categories_job))
        Catalogs.get_update_categories_job=self._page_cursor_update(self.retry_logic(Catalogs.get_update_categories_job))
        Catalogs.get_catalog_category_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_update_job))
        Catalogs.get_bulk_update_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_categories_jobs))
        Catalogs.get_update_categories_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_update_categories_jobs))
        Catalogs.get_catalog_category_bulk_update_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_bulk_update_jobs))
        Catalogs.get_bulk_update_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_variants_job))
        Catalogs.get_update_variants_job=self._page_cursor_update(self.retry_logic(Catalogs.get_update_variants_job))
        Catalogs.get_catalog_variant_bulk_update_job=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_update_job))
        Catalogs.get_bulk_update_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_bulk_update_variants_jobs))
        Catalogs.get_update_variants_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_update_variants_jobs))
        Catalogs.get_catalog_variant_bulk_update_jobs=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant_bulk_update_jobs))
        Catalogs.get_catalog_categories=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_categories))
        Catalogs.get_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category))
        Catalogs.get_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item))
        Catalogs.get_catalog_items=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_items))
        Catalogs.get_catalog_variant=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variant))
        Catalogs.get_catalog_variants=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_variants))
        Catalogs.get_categories_for_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.get_categories_for_catalog_item))
        Catalogs.get_catalog_item_categories=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_categories))
        Catalogs.get_category_ids_for_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.get_category_ids_for_catalog_item))
        Catalogs.get_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_relationships_categories))
        Catalogs.get_item_ids_for_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.get_item_ids_for_catalog_category))
        Catalogs.get_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_relationships_items))
        Catalogs.get_items_for_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.get_items_for_catalog_category))
        Catalogs.get_catalog_category_items=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_category_items))
        Catalogs.get_variant_ids_for_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.get_variant_ids_for_catalog_item))
        Catalogs.get_catalog_item_relationships_variants=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_relationships_variants))
        Catalogs.get_variants_for_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.get_variants_for_catalog_item))
        Catalogs.get_catalog_item_variants=self._page_cursor_update(self.retry_logic(Catalogs.get_catalog_item_variants))
        Catalogs.remove_categories_from_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.remove_categories_from_catalog_item))
        Catalogs.delete_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(Catalogs.delete_catalog_item_relationships_categories))
        Catalogs.remove_items_from_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.remove_items_from_catalog_category))
        Catalogs.delete_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(Catalogs.delete_catalog_category_relationships_items))
        Catalogs.update_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.update_catalog_category))
        Catalogs.update_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.update_catalog_item))
        Catalogs.update_catalog_variant=self._page_cursor_update(self.retry_logic(Catalogs.update_catalog_variant))
        Catalogs.update_categories_for_catalog_item=self._page_cursor_update(self.retry_logic(Catalogs.update_categories_for_catalog_item))
        Catalogs.update_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(Catalogs.update_catalog_item_relationships_categories))
        Catalogs.update_items_for_catalog_category=self._page_cursor_update(self.retry_logic(Catalogs.update_items_for_catalog_category))
        Catalogs.update_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(Catalogs.update_catalog_category_relationships_items))
        
        return Catalogs
    
    @property
    def Coupons(self):
        from openapi_client.api import coupons_api

        ## Adding Coupons to Client
        Coupons=coupons_api.CouponsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Coupons
        Coupons.bulk_create_coupon_codes=self._page_cursor_update(self.retry_logic(Coupons.bulk_create_coupon_codes))
        Coupons.spawn_coupon_code_bulk_create_job=self._page_cursor_update(self.retry_logic(Coupons.spawn_coupon_code_bulk_create_job))
        Coupons.create_coupon_code_bulk_create_job=self._page_cursor_update(self.retry_logic(Coupons.create_coupon_code_bulk_create_job))
        Coupons.create_coupon=self._page_cursor_update(self.retry_logic(Coupons.create_coupon))
        Coupons.create_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.create_coupon_code))
        Coupons.delete_coupon=self._page_cursor_update(self.retry_logic(Coupons.delete_coupon))
        Coupons.delete_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.delete_coupon_code))
        Coupons.get_bulk_create_coupon_code_jobs=self._page_cursor_update(self.retry_logic(Coupons.get_bulk_create_coupon_code_jobs))
        Coupons.get_coupon_code_bulk_create_jobs=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code_bulk_create_jobs))
        Coupons.get_bulk_create_coupon_codes_job=self._page_cursor_update(self.retry_logic(Coupons.get_bulk_create_coupon_codes_job))
        Coupons.get_coupon_code_bulk_create_job=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code_bulk_create_job))
        Coupons.get_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_coupon))
        Coupons.get_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code))
        Coupons.get_coupon_code_ids_for_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code_ids_for_coupon))
        Coupons.get_coupon_code_relationships_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code_relationships_coupon))
        Coupons.get_code_ids_for_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_code_ids_for_coupon))
        Coupons.get_coupon_relationships_codes=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_relationships_codes))
        Coupons.get_coupon_codes=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_codes))
        Coupons.get_coupon_codes_for_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_codes_for_coupon))
        Coupons.get_coupon_coupon_codes=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_coupon_codes))
        Coupons.get_codes_for_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_codes_for_coupon))
        Coupons.get_coupon_for_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_for_coupon_code))
        Coupons.get_coupon_code_coupon=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_code_coupon))
        Coupons.get_coupon_id_for_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_id_for_coupon_code))
        Coupons.get_coupon_relationships_coupon_codes=self._page_cursor_update(self.retry_logic(Coupons.get_coupon_relationships_coupon_codes))
        Coupons.get_coupons=self._page_cursor_update(self.retry_logic(Coupons.get_coupons))
        Coupons.update_coupon=self._page_cursor_update(self.retry_logic(Coupons.update_coupon))
        Coupons.update_coupon_code=self._page_cursor_update(self.retry_logic(Coupons.update_coupon_code))
        
        return Coupons
    
    @property
    def Data_Privacy(self):
        from openapi_client.api import data_privacy_api

        ## Adding Data_Privacy to Client
        Data_Privacy=data_privacy_api.DataPrivacyApi(self.api_client)

        ## Applying retry decorator to each endpoint in Data_Privacy
        Data_Privacy.request_profile_deletion=self._page_cursor_update(self.retry_logic(Data_Privacy.request_profile_deletion))
        Data_Privacy.create_data_privacy_deletion_job=self._page_cursor_update(self.retry_logic(Data_Privacy.create_data_privacy_deletion_job))
        
        return Data_Privacy
    
    @property
    def Events(self):
        from openapi_client.api import events_api

        ## Adding Events to Client
        Events=events_api.EventsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Events
        Events.bulk_create_events=self._page_cursor_update(self.retry_logic(Events.bulk_create_events))
        Events.create_event_bulk_create_job=self._page_cursor_update(self.retry_logic(Events.create_event_bulk_create_job))
        Events.create_event=self._page_cursor_update(self.retry_logic(Events.create_event))
        Events.get_event=self._page_cursor_update(self.retry_logic(Events.get_event))
        Events.get_events=self._page_cursor_update(self.retry_logic(Events.get_events))
        Events.get_metric_for_event=self._page_cursor_update(self.retry_logic(Events.get_metric_for_event))
        Events.get_event_metric=self._page_cursor_update(self.retry_logic(Events.get_event_metric))
        Events.get_metric_id_for_event=self._page_cursor_update(self.retry_logic(Events.get_metric_id_for_event))
        Events.get_event_relationships_metric=self._page_cursor_update(self.retry_logic(Events.get_event_relationships_metric))
        Events.get_profile_for_event=self._page_cursor_update(self.retry_logic(Events.get_profile_for_event))
        Events.get_event_profile=self._page_cursor_update(self.retry_logic(Events.get_event_profile))
        Events.get_profile_id_for_event=self._page_cursor_update(self.retry_logic(Events.get_profile_id_for_event))
        Events.get_event_relationships_profile=self._page_cursor_update(self.retry_logic(Events.get_event_relationships_profile))
        
        return Events
    
    @property
    def Flows(self):
        from openapi_client.api import flows_api

        ## Adding Flows to Client
        Flows=flows_api.FlowsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Flows
        Flows.create_flow=self._page_cursor_update(self.retry_logic(Flows.create_flow))
        Flows.delete_flow=self._page_cursor_update(self.retry_logic(Flows.delete_flow))
        Flows.get_action_for_flow_message=self._page_cursor_update(self.retry_logic(Flows.get_action_for_flow_message))
        Flows.get_flow_message_action=self._page_cursor_update(self.retry_logic(Flows.get_flow_message_action))
        Flows.get_action_id_for_flow_message=self._page_cursor_update(self.retry_logic(Flows.get_action_id_for_flow_message))
        Flows.get_flow_message_relationships_action=self._page_cursor_update(self.retry_logic(Flows.get_flow_message_relationships_action))
        Flows.get_action_ids_for_flow=self._page_cursor_update(self.retry_logic(Flows.get_action_ids_for_flow))
        Flows.get_flow_relationships_flow_actions=self._page_cursor_update(self.retry_logic(Flows.get_flow_relationships_flow_actions))
        Flows.get_flow_relationships_actions=self._page_cursor_update(self.retry_logic(Flows.get_flow_relationships_actions))
        Flows.get_actions_for_flow=self._page_cursor_update(self.retry_logic(Flows.get_actions_for_flow))
        Flows.get_flow_flow_actions=self._page_cursor_update(self.retry_logic(Flows.get_flow_flow_actions))
        Flows.get_flow_actions=self._page_cursor_update(self.retry_logic(Flows.get_flow_actions))
        Flows.get_flow=self._page_cursor_update(self.retry_logic(Flows.get_flow))
        Flows.get_flow_action=self._page_cursor_update(self.retry_logic(Flows.get_flow_action))
        Flows.get_flow_action_messages=self._page_cursor_update(self.retry_logic(Flows.get_flow_action_messages))
        Flows.get_messages_for_flow_action=self._page_cursor_update(self.retry_logic(Flows.get_messages_for_flow_action))
        Flows.get_flow_for_flow_action=self._page_cursor_update(self.retry_logic(Flows.get_flow_for_flow_action))
        Flows.get_flow_action_flow=self._page_cursor_update(self.retry_logic(Flows.get_flow_action_flow))
        Flows.get_flow_id_for_flow_action=self._page_cursor_update(self.retry_logic(Flows.get_flow_id_for_flow_action))
        Flows.get_flow_action_relationships_flow=self._page_cursor_update(self.retry_logic(Flows.get_flow_action_relationships_flow))
        Flows.get_flow_message=self._page_cursor_update(self.retry_logic(Flows.get_flow_message))
        Flows.get_flows=self._page_cursor_update(self.retry_logic(Flows.get_flows))
        Flows.get_message_ids_for_flow_action=self._page_cursor_update(self.retry_logic(Flows.get_message_ids_for_flow_action))
        Flows.get_flow_action_relationships_messages=self._page_cursor_update(self.retry_logic(Flows.get_flow_action_relationships_messages))
        Flows.get_tag_ids_for_flow=self._page_cursor_update(self.retry_logic(Flows.get_tag_ids_for_flow))
        Flows.get_flow_relationships_tags=self._page_cursor_update(self.retry_logic(Flows.get_flow_relationships_tags))
        Flows.get_tags_for_flow=self._page_cursor_update(self.retry_logic(Flows.get_tags_for_flow))
        Flows.get_flow_tags=self._page_cursor_update(self.retry_logic(Flows.get_flow_tags))
        Flows.get_template_for_flow_message=self._page_cursor_update(self.retry_logic(Flows.get_template_for_flow_message))
        Flows.get_flow_message_template=self._page_cursor_update(self.retry_logic(Flows.get_flow_message_template))
        Flows.get_template_id_for_flow_message=self._page_cursor_update(self.retry_logic(Flows.get_template_id_for_flow_message))
        Flows.get_flow_message_relationships_template=self._page_cursor_update(self.retry_logic(Flows.get_flow_message_relationships_template))
        Flows.update_flow=self._page_cursor_update(self.retry_logic(Flows.update_flow))
        
        return Flows
    
    @property
    def Forms(self):
        from openapi_client.api import forms_api

        ## Adding Forms to Client
        Forms=forms_api.FormsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Forms
        Forms.delete_form=self._page_cursor_update(self.retry_logic(Forms.delete_form))
        Forms.get_form=self._page_cursor_update(self.retry_logic(Forms.get_form))
        Forms.get_form_for_form_version=self._page_cursor_update(self.retry_logic(Forms.get_form_for_form_version))
        Forms.get_form_version_form=self._page_cursor_update(self.retry_logic(Forms.get_form_version_form))
        Forms.get_form_id_for_form_version=self._page_cursor_update(self.retry_logic(Forms.get_form_id_for_form_version))
        Forms.get_form_version_relationships_form=self._page_cursor_update(self.retry_logic(Forms.get_form_version_relationships_form))
        Forms.get_form_version=self._page_cursor_update(self.retry_logic(Forms.get_form_version))
        Forms.get_forms=self._page_cursor_update(self.retry_logic(Forms.get_forms))
        Forms.get_version_ids_for_form=self._page_cursor_update(self.retry_logic(Forms.get_version_ids_for_form))
        Forms.get_form_relationships_form_versions=self._page_cursor_update(self.retry_logic(Forms.get_form_relationships_form_versions))
        Forms.get_form_relationships_versions=self._page_cursor_update(self.retry_logic(Forms.get_form_relationships_versions))
        Forms.get_versions_for_form=self._page_cursor_update(self.retry_logic(Forms.get_versions_for_form))
        Forms.get_form_form_versions=self._page_cursor_update(self.retry_logic(Forms.get_form_form_versions))
        Forms.get_form_versions=self._page_cursor_update(self.retry_logic(Forms.get_form_versions))
        
        return Forms
    
    @property
    def Images(self):
        from openapi_client.api import images_api

        ## Adding Images to Client
        Images=images_api.ImagesApi(self.api_client)

        ## Applying retry decorator to each endpoint in Images
        Images.get_image=self._page_cursor_update(self.retry_logic(Images.get_image))
        Images.get_images=self._page_cursor_update(self.retry_logic(Images.get_images))
        Images.update_image=self._page_cursor_update(self.retry_logic(Images.update_image))
        Images.upload_image_from_file=self._page_cursor_update(self.retry_logic(Images.upload_image_from_file))
        Images.create_image_upload=self._page_cursor_update(self.retry_logic(Images.create_image_upload))
        Images.upload_image_from_url=self._page_cursor_update(self.retry_logic(Images.upload_image_from_url))
        Images.create_image=self._page_cursor_update(self.retry_logic(Images.create_image))
        
        return Images
    
    @property
    def Lists(self):
        from openapi_client.api import lists_api

        ## Adding Lists to Client
        Lists=lists_api.ListsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Lists
        Lists.add_profiles_to_list=self._page_cursor_update(self.retry_logic(Lists.add_profiles_to_list))
        Lists.create_list_relationships=self._page_cursor_update(self.retry_logic(Lists.create_list_relationships))
        Lists.create_list_relationships_profile=self._page_cursor_update(self.retry_logic(Lists.create_list_relationships_profile))
        Lists.create_list_relationships_profiles=self._page_cursor_update(self.retry_logic(Lists.create_list_relationships_profiles))
        Lists.create_list=self._page_cursor_update(self.retry_logic(Lists.create_list))
        Lists.delete_list=self._page_cursor_update(self.retry_logic(Lists.delete_list))
        Lists.get_flows_triggered_by_list=self._page_cursor_update(self.retry_logic(Lists.get_flows_triggered_by_list))
        Lists.get_flow_triggers_for_list=self._page_cursor_update(self.retry_logic(Lists.get_flow_triggers_for_list))
        Lists.get_list_flow_triggers=self._page_cursor_update(self.retry_logic(Lists.get_list_flow_triggers))
        Lists.get_ids_for_flows_triggered_by_list=self._page_cursor_update(self.retry_logic(Lists.get_ids_for_flows_triggered_by_list))
        Lists.get_flow_trigger_ids_for_list=self._page_cursor_update(self.retry_logic(Lists.get_flow_trigger_ids_for_list))
        Lists.get_list_relationships_flow_triggers=self._page_cursor_update(self.retry_logic(Lists.get_list_relationships_flow_triggers))
        Lists.get_list=self._page_cursor_update(self.retry_logic(Lists.get_list))
        Lists.get_lists=self._page_cursor_update(self.retry_logic(Lists.get_lists))
        Lists.get_profile_ids_for_list=self._page_cursor_update(self.retry_logic(Lists.get_profile_ids_for_list))
        Lists.get_list_relationships_profiles=self._page_cursor_update(self.retry_logic(Lists.get_list_relationships_profiles))
        Lists.get_profiles_for_list=self._page_cursor_update(self.retry_logic(Lists.get_profiles_for_list))
        Lists.get_list_profiles=self._page_cursor_update(self.retry_logic(Lists.get_list_profiles))
        Lists.get_tag_ids_for_list=self._page_cursor_update(self.retry_logic(Lists.get_tag_ids_for_list))
        Lists.get_list_relationships_tags=self._page_cursor_update(self.retry_logic(Lists.get_list_relationships_tags))
        Lists.get_tags_for_list=self._page_cursor_update(self.retry_logic(Lists.get_tags_for_list))
        Lists.get_list_tags=self._page_cursor_update(self.retry_logic(Lists.get_list_tags))
        Lists.remove_profiles_from_list=self._page_cursor_update(self.retry_logic(Lists.remove_profiles_from_list))
        Lists.delete_list_relationships=self._page_cursor_update(self.retry_logic(Lists.delete_list_relationships))
        Lists.delete_list_relationships_profiles=self._page_cursor_update(self.retry_logic(Lists.delete_list_relationships_profiles))
        Lists.update_list=self._page_cursor_update(self.retry_logic(Lists.update_list))
        
        return Lists
    
    @property
    def Metrics(self):
        from openapi_client.api import metrics_api

        ## Adding Metrics to Client
        Metrics=metrics_api.MetricsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Metrics
        Metrics.create_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.create_custom_metric))
        Metrics.delete_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.delete_custom_metric))
        Metrics.get_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.get_custom_metric))
        Metrics.get_custom_metrics=self._page_cursor_update(self.retry_logic(Metrics.get_custom_metrics))
        Metrics.get_flows_triggered_by_metric=self._page_cursor_update(self.retry_logic(Metrics.get_flows_triggered_by_metric))
        Metrics.get_flow_triggers_for_metric=self._page_cursor_update(self.retry_logic(Metrics.get_flow_triggers_for_metric))
        Metrics.get_metric_flow_triggers=self._page_cursor_update(self.retry_logic(Metrics.get_metric_flow_triggers))
        Metrics.get_ids_for_flows_triggered_by_metric=self._page_cursor_update(self.retry_logic(Metrics.get_ids_for_flows_triggered_by_metric))
        Metrics.get_flow_trigger_ids_for_metric=self._page_cursor_update(self.retry_logic(Metrics.get_flow_trigger_ids_for_metric))
        Metrics.get_metric_relationships_flow_triggers=self._page_cursor_update(self.retry_logic(Metrics.get_metric_relationships_flow_triggers))
        Metrics.get_metric=self._page_cursor_update(self.retry_logic(Metrics.get_metric))
        Metrics.get_metric_for_metric_property=self._page_cursor_update(self.retry_logic(Metrics.get_metric_for_metric_property))
        Metrics.get_metric_property_metric=self._page_cursor_update(self.retry_logic(Metrics.get_metric_property_metric))
        Metrics.get_metric_id_for_metric_property=self._page_cursor_update(self.retry_logic(Metrics.get_metric_id_for_metric_property))
        Metrics.get_metric_property_relationships_metric=self._page_cursor_update(self.retry_logic(Metrics.get_metric_property_relationships_metric))
        Metrics.get_metric_ids_for_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.get_metric_ids_for_custom_metric))
        Metrics.get_custom_metric_relationships_metrics=self._page_cursor_update(self.retry_logic(Metrics.get_custom_metric_relationships_metrics))
        Metrics.get_metric_property=self._page_cursor_update(self.retry_logic(Metrics.get_metric_property))
        Metrics.get_metrics=self._page_cursor_update(self.retry_logic(Metrics.get_metrics))
        Metrics.get_metrics_for_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.get_metrics_for_custom_metric))
        Metrics.get_custom_metric_metrics=self._page_cursor_update(self.retry_logic(Metrics.get_custom_metric_metrics))
        Metrics.get_properties_for_metric=self._page_cursor_update(self.retry_logic(Metrics.get_properties_for_metric))
        Metrics.get_metric_metric_properties=self._page_cursor_update(self.retry_logic(Metrics.get_metric_metric_properties))
        Metrics.get_metric_properties=self._page_cursor_update(self.retry_logic(Metrics.get_metric_properties))
        Metrics.get_property_ids_for_metric=self._page_cursor_update(self.retry_logic(Metrics.get_property_ids_for_metric))
        Metrics.get_metric_relationships_metric_properties=self._page_cursor_update(self.retry_logic(Metrics.get_metric_relationships_metric_properties))
        Metrics.get_metric_relationships_properties=self._page_cursor_update(self.retry_logic(Metrics.get_metric_relationships_properties))
        Metrics.query_metric_aggregates=self._page_cursor_update(self.retry_logic(Metrics.query_metric_aggregates))
        Metrics.create_metric_aggregate=self._page_cursor_update(self.retry_logic(Metrics.create_metric_aggregate))
        Metrics.update_custom_metric=self._page_cursor_update(self.retry_logic(Metrics.update_custom_metric))
        
        return Metrics
    
    @property
    def Profiles(self):
        from openapi_client.api import profiles_api

        ## Adding Profiles to Client
        Profiles=profiles_api.ProfilesApi(self.api_client)

        ## Applying retry decorator to each endpoint in Profiles
        Profiles.bulk_import_profiles=self._page_cursor_update(self.retry_logic(Profiles.bulk_import_profiles))
        Profiles.spawn_bulk_profile_import_job=self._page_cursor_update(self.retry_logic(Profiles.spawn_bulk_profile_import_job))
        Profiles.create_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.create_profile_bulk_import_job))
        Profiles.bulk_subscribe_profiles=self._page_cursor_update(self.retry_logic(Profiles.bulk_subscribe_profiles))
        Profiles.subscribe_profiles=self._page_cursor_update(self.retry_logic(Profiles.subscribe_profiles))
        Profiles.create_profile_subscription_bulk_create_job=self._page_cursor_update(self.retry_logic(Profiles.create_profile_subscription_bulk_create_job))
        Profiles.bulk_suppress_profiles=self._page_cursor_update(self.retry_logic(Profiles.bulk_suppress_profiles))
        Profiles.suppress_profiles=self._page_cursor_update(self.retry_logic(Profiles.suppress_profiles))
        Profiles.create_profile_suppression_bulk_create_job=self._page_cursor_update(self.retry_logic(Profiles.create_profile_suppression_bulk_create_job))
        Profiles.bulk_unsubscribe_profiles=self._page_cursor_update(self.retry_logic(Profiles.bulk_unsubscribe_profiles))
        Profiles.unsubscribe_profiles=self._page_cursor_update(self.retry_logic(Profiles.unsubscribe_profiles))
        Profiles.create_profile_subscription_bulk_delete_job=self._page_cursor_update(self.retry_logic(Profiles.create_profile_subscription_bulk_delete_job))
        Profiles.bulk_unsuppress_profiles=self._page_cursor_update(self.retry_logic(Profiles.bulk_unsuppress_profiles))
        Profiles.unsuppress_profiles=self._page_cursor_update(self.retry_logic(Profiles.unsuppress_profiles))
        Profiles.create_profile_suppression_bulk_delete_job=self._page_cursor_update(self.retry_logic(Profiles.create_profile_suppression_bulk_delete_job))
        Profiles.create_or_update_profile=self._page_cursor_update(self.retry_logic(Profiles.create_or_update_profile))
        Profiles.create_profile_import=self._page_cursor_update(self.retry_logic(Profiles.create_profile_import))
        Profiles.create_profile=self._page_cursor_update(self.retry_logic(Profiles.create_profile))
        Profiles.create_push_token=self._page_cursor_update(self.retry_logic(Profiles.create_push_token))
        Profiles.delete_push_token=self._page_cursor_update(self.retry_logic(Profiles.delete_push_token))
        Profiles.get_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job))
        Profiles.get_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job))
        Profiles.get_bulk_import_profiles_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_import_profiles_jobs))
        Profiles.get_bulk_profile_import_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_jobs))
        Profiles.get_profile_bulk_import_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_jobs))
        Profiles.get_bulk_suppress_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_suppress_profiles_job))
        Profiles.get_profile_suppression_bulk_create_job=self._page_cursor_update(self.retry_logic(Profiles.get_profile_suppression_bulk_create_job))
        Profiles.get_bulk_suppress_profiles_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_suppress_profiles_jobs))
        Profiles.get_profile_suppression_bulk_create_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_profile_suppression_bulk_create_jobs))
        Profiles.get_bulk_unsuppress_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_unsuppress_profiles_job))
        Profiles.get_profile_suppression_bulk_delete_job=self._page_cursor_update(self.retry_logic(Profiles.get_profile_suppression_bulk_delete_job))
        Profiles.get_bulk_unsuppress_profiles_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_unsuppress_profiles_jobs))
        Profiles.get_profile_suppression_bulk_delete_jobs=self._page_cursor_update(self.retry_logic(Profiles.get_profile_suppression_bulk_delete_jobs))
        Profiles.get_errors_for_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_errors_for_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job_import_errors=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job_import_errors))
        Profiles.get_import_errors_for_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_import_errors_for_profile_bulk_import_job))
        Profiles.get_profile_bulk_import_job_import_errors=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job_import_errors))
        Profiles.get_list_for_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_list_for_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job_lists=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job_lists))
        Profiles.get_lists_for_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_lists_for_profile_bulk_import_job))
        Profiles.get_profile_bulk_import_job_lists=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job_lists))
        Profiles.get_list_ids_for_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_list_ids_for_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job_relationships_lists=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job_relationships_lists))
        Profiles.get_list_ids_for_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_list_ids_for_profile_bulk_import_job))
        Profiles.get_profile_bulk_import_job_relationships_lists=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job_relationships_lists))
        Profiles.get_list_ids_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_list_ids_for_profile))
        Profiles.get_profile_relationships_lists=self._page_cursor_update(self.retry_logic(Profiles.get_profile_relationships_lists))
        Profiles.get_lists_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_lists_for_profile))
        Profiles.get_profile_lists=self._page_cursor_update(self.retry_logic(Profiles.get_profile_lists))
        Profiles.get_profile=self._page_cursor_update(self.retry_logic(Profiles.get_profile))
        Profiles.get_profile_for_push_token=self._page_cursor_update(self.retry_logic(Profiles.get_profile_for_push_token))
        Profiles.get_push_token_profile=self._page_cursor_update(self.retry_logic(Profiles.get_push_token_profile))
        Profiles.get_profile_id_for_push_token=self._page_cursor_update(self.retry_logic(Profiles.get_profile_id_for_push_token))
        Profiles.get_push_token_relationships_profile=self._page_cursor_update(self.retry_logic(Profiles.get_push_token_relationships_profile))
        Profiles.get_profile_ids_for_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_profile_ids_for_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job_relationships_profiles=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job_relationships_profiles))
        Profiles.get_profile_bulk_import_job_relationships_profiles=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job_relationships_profiles))
        Profiles.get_profile_ids_for_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_profile_ids_for_profile_bulk_import_job))
        Profiles.get_profiles=self._page_cursor_update(self.retry_logic(Profiles.get_profiles))
        Profiles.get_profiles_for_bulk_import_profiles_job=self._page_cursor_update(self.retry_logic(Profiles.get_profiles_for_bulk_import_profiles_job))
        Profiles.get_bulk_profile_import_job_profiles=self._page_cursor_update(self.retry_logic(Profiles.get_bulk_profile_import_job_profiles))
        Profiles.get_profile_bulk_import_job_profiles=self._page_cursor_update(self.retry_logic(Profiles.get_profile_bulk_import_job_profiles))
        Profiles.get_profiles_for_profile_bulk_import_job=self._page_cursor_update(self.retry_logic(Profiles.get_profiles_for_profile_bulk_import_job))
        Profiles.get_push_token=self._page_cursor_update(self.retry_logic(Profiles.get_push_token))
        Profiles.get_push_token_ids_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_push_token_ids_for_profile))
        Profiles.get_profile_relationships_push_tokens=self._page_cursor_update(self.retry_logic(Profiles.get_profile_relationships_push_tokens))
        Profiles.get_push_tokens=self._page_cursor_update(self.retry_logic(Profiles.get_push_tokens))
        Profiles.get_push_tokens_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_push_tokens_for_profile))
        Profiles.get_profile_push_tokens=self._page_cursor_update(self.retry_logic(Profiles.get_profile_push_tokens))
        Profiles.get_segment_ids_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_segment_ids_for_profile))
        Profiles.get_profile_relationships_segments=self._page_cursor_update(self.retry_logic(Profiles.get_profile_relationships_segments))
        Profiles.get_segments_for_profile=self._page_cursor_update(self.retry_logic(Profiles.get_segments_for_profile))
        Profiles.get_profile_segments=self._page_cursor_update(self.retry_logic(Profiles.get_profile_segments))
        Profiles.merge_profiles=self._page_cursor_update(self.retry_logic(Profiles.merge_profiles))
        Profiles.create_profile_merge=self._page_cursor_update(self.retry_logic(Profiles.create_profile_merge))
        Profiles.update_profile=self._page_cursor_update(self.retry_logic(Profiles.update_profile))
        
        return Profiles
    
    @property
    def Reporting(self):
        from openapi_client.api import reporting_api

        ## Adding Reporting to Client
        Reporting=reporting_api.ReportingApi(self.api_client)

        ## Applying retry decorator to each endpoint in Reporting
        Reporting.query_campaign_values=self._page_cursor_update(self.retry_logic(Reporting.query_campaign_values))
        Reporting.create_campaign_value_report=self._page_cursor_update(self.retry_logic(Reporting.create_campaign_value_report))
        Reporting.create_campaign_values_report=self._page_cursor_update(self.retry_logic(Reporting.create_campaign_values_report))
        Reporting.query_flow_series=self._page_cursor_update(self.retry_logic(Reporting.query_flow_series))
        Reporting.create_flow_sery_report=self._page_cursor_update(self.retry_logic(Reporting.create_flow_sery_report))
        Reporting.create_flow_series_report=self._page_cursor_update(self.retry_logic(Reporting.create_flow_series_report))
        Reporting.query_flow_values=self._page_cursor_update(self.retry_logic(Reporting.query_flow_values))
        Reporting.create_flow_value_report=self._page_cursor_update(self.retry_logic(Reporting.create_flow_value_report))
        Reporting.create_flow_values_report=self._page_cursor_update(self.retry_logic(Reporting.create_flow_values_report))
        Reporting.query_form_series=self._page_cursor_update(self.retry_logic(Reporting.query_form_series))
        Reporting.create_form_sery_report=self._page_cursor_update(self.retry_logic(Reporting.create_form_sery_report))
        Reporting.create_form_series_report=self._page_cursor_update(self.retry_logic(Reporting.create_form_series_report))
        Reporting.query_form_values=self._page_cursor_update(self.retry_logic(Reporting.query_form_values))
        Reporting.create_form_value_report=self._page_cursor_update(self.retry_logic(Reporting.create_form_value_report))
        Reporting.create_form_values_report=self._page_cursor_update(self.retry_logic(Reporting.create_form_values_report))
        Reporting.query_segment_series=self._page_cursor_update(self.retry_logic(Reporting.query_segment_series))
        Reporting.create_segment_sery_report=self._page_cursor_update(self.retry_logic(Reporting.create_segment_sery_report))
        Reporting.create_segment_series_report=self._page_cursor_update(self.retry_logic(Reporting.create_segment_series_report))
        Reporting.query_segment_values=self._page_cursor_update(self.retry_logic(Reporting.query_segment_values))
        Reporting.create_segment_value_report=self._page_cursor_update(self.retry_logic(Reporting.create_segment_value_report))
        Reporting.create_segment_values_report=self._page_cursor_update(self.retry_logic(Reporting.create_segment_values_report))
        
        return Reporting
    
    @property
    def Reviews(self):
        from openapi_client.api import reviews_api

        ## Adding Reviews to Client
        Reviews=reviews_api.ReviewsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Reviews
        Reviews.get_review=self._page_cursor_update(self.retry_logic(Reviews.get_review))
        Reviews.get_reviews=self._page_cursor_update(self.retry_logic(Reviews.get_reviews))
        Reviews.update_review=self._page_cursor_update(self.retry_logic(Reviews.update_review))
        
        return Reviews
    
    @property
    def Segments(self):
        from openapi_client.api import segments_api

        ## Adding Segments to Client
        Segments=segments_api.SegmentsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Segments
        Segments.create_segment=self._page_cursor_update(self.retry_logic(Segments.create_segment))
        Segments.delete_segment=self._page_cursor_update(self.retry_logic(Segments.delete_segment))
        Segments.get_flows_triggered_by_segment=self._page_cursor_update(self.retry_logic(Segments.get_flows_triggered_by_segment))
        Segments.get_flow_triggers_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_flow_triggers_for_segment))
        Segments.get_segment_flow_triggers=self._page_cursor_update(self.retry_logic(Segments.get_segment_flow_triggers))
        Segments.get_ids_for_flows_triggered_by_segment=self._page_cursor_update(self.retry_logic(Segments.get_ids_for_flows_triggered_by_segment))
        Segments.get_flow_trigger_ids_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_flow_trigger_ids_for_segment))
        Segments.get_segment_relationships_flow_triggers=self._page_cursor_update(self.retry_logic(Segments.get_segment_relationships_flow_triggers))
        Segments.get_profile_ids_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_profile_ids_for_segment))
        Segments.get_segment_relationships_profiles=self._page_cursor_update(self.retry_logic(Segments.get_segment_relationships_profiles))
        Segments.get_profiles_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_profiles_for_segment))
        Segments.get_segment_profiles=self._page_cursor_update(self.retry_logic(Segments.get_segment_profiles))
        Segments.get_segment=self._page_cursor_update(self.retry_logic(Segments.get_segment))
        Segments.get_segments=self._page_cursor_update(self.retry_logic(Segments.get_segments))
        Segments.get_tag_ids_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_tag_ids_for_segment))
        Segments.get_segment_relationships_tags=self._page_cursor_update(self.retry_logic(Segments.get_segment_relationships_tags))
        Segments.get_tags_for_segment=self._page_cursor_update(self.retry_logic(Segments.get_tags_for_segment))
        Segments.get_segment_tags=self._page_cursor_update(self.retry_logic(Segments.get_segment_tags))
        Segments.update_segment=self._page_cursor_update(self.retry_logic(Segments.update_segment))
        
        return Segments
    
    @property
    def Tags(self):
        from openapi_client.api import tags_api

        ## Adding Tags to Client
        Tags=tags_api.TagsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Tags
        Tags.create_tag=self._page_cursor_update(self.retry_logic(Tags.create_tag))
        Tags.create_tag_group=self._page_cursor_update(self.retry_logic(Tags.create_tag_group))
        Tags.delete_tag=self._page_cursor_update(self.retry_logic(Tags.delete_tag))
        Tags.delete_tag_group=self._page_cursor_update(self.retry_logic(Tags.delete_tag_group))
        Tags.get_campaign_ids_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_campaign_ids_for_tag))
        Tags.get_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_campaigns))
        Tags.get_flow_ids_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_flow_ids_for_tag))
        Tags.get_tag_relationships_flows=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_flows))
        Tags.get_list_ids_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_list_ids_for_tag))
        Tags.get_tag_relationships_lists=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_lists))
        Tags.get_segment_ids_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_segment_ids_for_tag))
        Tags.get_tag_relationships_segments=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_segments))
        Tags.get_tag=self._page_cursor_update(self.retry_logic(Tags.get_tag))
        Tags.get_tag_group=self._page_cursor_update(self.retry_logic(Tags.get_tag_group))
        Tags.get_tag_group_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_tag_group_for_tag))
        Tags.get_tag_tag_group=self._page_cursor_update(self.retry_logic(Tags.get_tag_tag_group))
        Tags.get_group_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_group_for_tag))
        Tags.get_tag_group_id_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_tag_group_id_for_tag))
        Tags.get_tag_relationships_tag_group=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_tag_group))
        Tags.get_group_id_for_tag=self._page_cursor_update(self.retry_logic(Tags.get_group_id_for_tag))
        Tags.get_tag_relationships_group=self._page_cursor_update(self.retry_logic(Tags.get_tag_relationships_group))
        Tags.get_tag_groups=self._page_cursor_update(self.retry_logic(Tags.get_tag_groups))
        Tags.get_tag_ids_for_tag_group=self._page_cursor_update(self.retry_logic(Tags.get_tag_ids_for_tag_group))
        Tags.get_tag_group_relationships_tags=self._page_cursor_update(self.retry_logic(Tags.get_tag_group_relationships_tags))
        Tags.get_tags=self._page_cursor_update(self.retry_logic(Tags.get_tags))
        Tags.get_tags_for_tag_group=self._page_cursor_update(self.retry_logic(Tags.get_tags_for_tag_group))
        Tags.get_tag_group_tags=self._page_cursor_update(self.retry_logic(Tags.get_tag_group_tags))
        Tags.remove_tag_from_campaigns=self._page_cursor_update(self.retry_logic(Tags.remove_tag_from_campaigns))
        Tags.delete_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(Tags.delete_tag_relationships_campaigns))
        Tags.remove_campaigns_from_tag=self._page_cursor_update(self.retry_logic(Tags.remove_campaigns_from_tag))
        Tags.remove_tag_from_flows=self._page_cursor_update(self.retry_logic(Tags.remove_tag_from_flows))
        Tags.delete_tag_relationships_flows=self._page_cursor_update(self.retry_logic(Tags.delete_tag_relationships_flows))
        Tags.remove_flows_from_tag=self._page_cursor_update(self.retry_logic(Tags.remove_flows_from_tag))
        Tags.remove_tag_from_lists=self._page_cursor_update(self.retry_logic(Tags.remove_tag_from_lists))
        Tags.delete_tag_relationships_lists=self._page_cursor_update(self.retry_logic(Tags.delete_tag_relationships_lists))
        Tags.remove_lists_from_tag=self._page_cursor_update(self.retry_logic(Tags.remove_lists_from_tag))
        Tags.remove_tag_from_segments=self._page_cursor_update(self.retry_logic(Tags.remove_tag_from_segments))
        Tags.delete_tag_relationships_segments=self._page_cursor_update(self.retry_logic(Tags.delete_tag_relationships_segments))
        Tags.remove_segments_from_tag=self._page_cursor_update(self.retry_logic(Tags.remove_segments_from_tag))
        Tags.tag_campaigns=self._page_cursor_update(self.retry_logic(Tags.tag_campaigns))
        Tags.create_tag_relationships_campaign=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_campaign))
        Tags.add_campaigns_to_tag=self._page_cursor_update(self.retry_logic(Tags.add_campaigns_to_tag))
        Tags.create_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_campaigns))
        Tags.tag_flows=self._page_cursor_update(self.retry_logic(Tags.tag_flows))
        Tags.create_tag_relationships_flow=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_flow))
        Tags.add_flows_to_tag=self._page_cursor_update(self.retry_logic(Tags.add_flows_to_tag))
        Tags.create_tag_relationships_flows=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_flows))
        Tags.tag_lists=self._page_cursor_update(self.retry_logic(Tags.tag_lists))
        Tags.create_tag_relationships_list=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_list))
        Tags.add_lists_to_tag=self._page_cursor_update(self.retry_logic(Tags.add_lists_to_tag))
        Tags.create_tag_relationships_lists=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_lists))
        Tags.tag_segments=self._page_cursor_update(self.retry_logic(Tags.tag_segments))
        Tags.create_tag_relationships_segment=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_segment))
        Tags.add_segments_to_tag=self._page_cursor_update(self.retry_logic(Tags.add_segments_to_tag))
        Tags.create_tag_relationships_segments=self._page_cursor_update(self.retry_logic(Tags.create_tag_relationships_segments))
        Tags.update_tag=self._page_cursor_update(self.retry_logic(Tags.update_tag))
        Tags.update_tag_group=self._page_cursor_update(self.retry_logic(Tags.update_tag_group))
        
        return Tags
    
    @property
    def Templates(self):
        from openapi_client.api import templates_api

        ## Adding Templates to Client
        Templates=templates_api.TemplatesApi(self.api_client)

        ## Applying retry decorator to each endpoint in Templates
        Templates.clone_template=self._page_cursor_update(self.retry_logic(Templates.clone_template))
        Templates.create_template_clone=self._page_cursor_update(self.retry_logic(Templates.create_template_clone))
        Templates.create_template=self._page_cursor_update(self.retry_logic(Templates.create_template))
        Templates.create_universal_content=self._page_cursor_update(self.retry_logic(Templates.create_universal_content))
        Templates.create_template_universal_content=self._page_cursor_update(self.retry_logic(Templates.create_template_universal_content))
        Templates.delete_template=self._page_cursor_update(self.retry_logic(Templates.delete_template))
        Templates.delete_universal_content=self._page_cursor_update(self.retry_logic(Templates.delete_universal_content))
        Templates.delete_template_universal_content=self._page_cursor_update(self.retry_logic(Templates.delete_template_universal_content))
        Templates.get_all_universal_content=self._page_cursor_update(self.retry_logic(Templates.get_all_universal_content))
        Templates.get_template_universal_content=self._page_cursor_update(self.retry_logic(Templates.get_template_universal_content))
        Templates.get_template=self._page_cursor_update(self.retry_logic(Templates.get_template))
        Templates.get_templates=self._page_cursor_update(self.retry_logic(Templates.get_templates))
        Templates.get_universal_content=self._page_cursor_update(self.retry_logic(Templates.get_universal_content))
        Templates.render_template=self._page_cursor_update(self.retry_logic(Templates.render_template))
        Templates.create_template_render=self._page_cursor_update(self.retry_logic(Templates.create_template_render))
        Templates.update_template=self._page_cursor_update(self.retry_logic(Templates.update_template))
        Templates.update_universal_content=self._page_cursor_update(self.retry_logic(Templates.update_universal_content))
        Templates.update_template_universal_content=self._page_cursor_update(self.retry_logic(Templates.update_template_universal_content))
        
        return Templates
    
    @property
    def Tracking_Settings(self):
        from openapi_client.api import tracking_settings_api

        ## Adding Tracking_Settings to Client
        Tracking_Settings=tracking_settings_api.TrackingSettingsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Tracking_Settings
        Tracking_Settings.get_tracking_setting=self._page_cursor_update(self.retry_logic(Tracking_Settings.get_tracking_setting))
        Tracking_Settings.get_tracking_settings=self._page_cursor_update(self.retry_logic(Tracking_Settings.get_tracking_settings))
        Tracking_Settings.update_tracking_setting=self._page_cursor_update(self.retry_logic(Tracking_Settings.update_tracking_setting))
        
        return Tracking_Settings
    
    @property
    def Web_Feeds(self):
        from openapi_client.api import web_feeds_api

        ## Adding Web_Feeds to Client
        Web_Feeds=web_feeds_api.WebFeedsApi(self.api_client)

        ## Applying retry decorator to each endpoint in Web_Feeds
        Web_Feeds.create_web_feed=self._page_cursor_update(self.retry_logic(Web_Feeds.create_web_feed))
        Web_Feeds.delete_web_feed=self._page_cursor_update(self.retry_logic(Web_Feeds.delete_web_feed))
        Web_Feeds.get_web_feed=self._page_cursor_update(self.retry_logic(Web_Feeds.get_web_feed))
        Web_Feeds.get_web_feeds=self._page_cursor_update(self.retry_logic(Web_Feeds.get_web_feeds))
        Web_Feeds.update_web_feed=self._page_cursor_update(self.retry_logic(Web_Feeds.update_web_feed))
        
        return Web_Feeds
    
    @property
    def Webhooks(self):
        from openapi_client.api import webhooks_api

        ## Adding Webhooks to Client
        Webhooks=webhooks_api.WebhooksApi(self.api_client)

        ## Applying retry decorator to each endpoint in Webhooks
        Webhooks.create_webhook=self._page_cursor_update(self.retry_logic(Webhooks.create_webhook))
        Webhooks.delete_webhook=self._page_cursor_update(self.retry_logic(Webhooks.delete_webhook))
        Webhooks.get_webhook=self._page_cursor_update(self.retry_logic(Webhooks.get_webhook))
        Webhooks.get_webhook_topic=self._page_cursor_update(self.retry_logic(Webhooks.get_webhook_topic))
        Webhooks.get_webhook_topics=self._page_cursor_update(self.retry_logic(Webhooks.get_webhook_topics))
        Webhooks.get_webhooks=self._page_cursor_update(self.retry_logic(Webhooks.get_webhooks))
        Webhooks.update_webhook=self._page_cursor_update(self.retry_logic(Webhooks.update_webhook))
        
        return Webhooks
    

    @classmethod
    def _page_cursor_update(cls, func: Callable, *args, **kwargs) -> Callable: 
        def _wrapped_func(*args, **kwargs):
            if 'page_cursor' in kwargs:
                page_cursor = kwargs['page_cursor']
                if page_cursor:
                    if isinstance(page_cursor,str):
                        if 'https://' in page_cursor:
                            search_tokens = cls._CURSOR_SEARCH_TOKENS
                            found_token = None
                            for token in search_tokens:
                                if token in page_cursor:
                                    found_token = token
                                    break
                            if found_token:
                                page_cursor=page_cursor.split(found_token)[-1]
                                page_cursor = page_cursor.split('&')[0]                                
                        page_cursor = unquote(page_cursor)
                        kwargs['page_cursor'] = page_cursor   
            return func(*args,**kwargs)
        return _wrapped_func

    def retry_logic(self, func: Callable, *args, **kwargs) -> Callable:
        def _wrapped_func(*args, **kwargs):
            return self.retry_wrapper.with_retry(func, *args, **kwargs)
        return _wrapped_func