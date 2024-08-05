from __future__ import absolute_import

from __future__ import print_function
import tenacity
from urllib.parse import quote, unquote

import openapi_client
import klaviyo_api.custom_retry as custom_retry
from dataclasses import dataclass, field
from typing import Callable, ClassVar, Dict, Any
from openapi_client.api import accounts_api
from openapi_client.api import campaigns_api
from openapi_client.api import catalogs_api
from openapi_client.api import coupons_api
from openapi_client.api import data_privacy_api
from openapi_client.api import events_api
from openapi_client.api import flows_api
from openapi_client.api import forms_api
from openapi_client.api import images_api
from openapi_client.api import lists_api
from openapi_client.api import metrics_api
from openapi_client.api import profiles_api
from openapi_client.api import reporting_api
from openapi_client.api import segments_api
from openapi_client.api import tags_api
from openapi_client.api import templates_api
from openapi_client.api import tests_api
from openapi_client.api import webhooks_api


@dataclass
class KlaviyoAPI:

    api_key: str
    max_delay: int = 60
    max_retries: int = 3
    test_host: str = ''
    access_token: str = None
    options: Dict[str, Any] = field(default_factory=dict)


    _REVISION = "2024-07-15"

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

        if self.test_host:
            self.configuration.host = self.test_host

        self.api_client = openapi_client.ApiClient(self.configuration, options=self.options)

        self.api_client.default_headers['revision'] = self._REVISION
        
        if self.max_delay<= 0:
            self.max_delay = .1
        
        if self.max_retries <= 0:
            self.max_retries = 1
                
        self.retry_logic = tenacity.retry(
            reraise=True,
            retry=custom_retry.retry_if_qualifies(self._RETRY_CODES),
            wait=tenacity.wait.wait_random_exponential(multiplier = 1, max = self.max_delay),
            stop=tenacity.stop.stop_after_attempt(self.max_retries)
        )

        
        ## Adding Accounts to Client
        self.Accounts=accounts_api.AccountsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Accounts
        self.Accounts.get_account=self._page_cursor_update(self.retry_logic(self.Accounts.get_account))
        self.Accounts.get_accounts=self._page_cursor_update(self.retry_logic(self.Accounts.get_accounts))
        
        
        ## Adding Campaigns to Client
        self.Campaigns=campaigns_api.CampaignsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Campaigns
        self.Campaigns.create_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign))
        self.Campaigns.create_campaign_clone=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_clone))
        self.Campaigns.create_campaign_message_assign_template=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_message_assign_template))
        self.Campaigns.create_campaign_recipient_estimation_job=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_recipient_estimation_job))
        self.Campaigns.create_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.create_campaign_send_job))
        self.Campaigns.delete_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.delete_campaign))
        self.Campaigns.get_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign))
        self.Campaigns.get_campaign_campaign_messages=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_campaign_messages))
        self.Campaigns.get_campaign_message=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message))
        self.Campaigns.get_campaign_message_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message_campaign))
        self.Campaigns.get_campaign_message_relationships_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message_relationships_campaign))
        self.Campaigns.get_campaign_message_relationships_template=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message_relationships_template))
        self.Campaigns.get_campaign_message_template=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_message_template))
        self.Campaigns.get_campaign_recipient_estimation=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_recipient_estimation))
        self.Campaigns.get_campaign_recipient_estimation_job=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_recipient_estimation_job))
        self.Campaigns.get_campaign_relationships_campaign_messages=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_relationships_campaign_messages))
        self.Campaigns.get_campaign_relationships_tags=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_relationships_tags))
        self.Campaigns.get_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_send_job))
        self.Campaigns.get_campaign_tags=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaign_tags))
        self.Campaigns.get_campaigns=self._page_cursor_update(self.retry_logic(self.Campaigns.get_campaigns))
        self.Campaigns.update_campaign=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign))
        self.Campaigns.update_campaign_message=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign_message))
        self.Campaigns.update_campaign_send_job=self._page_cursor_update(self.retry_logic(self.Campaigns.update_campaign_send_job))
        
        
        ## Adding Catalogs to Client
        self.Catalogs=catalogs_api.CatalogsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Catalogs
        self.Catalogs.create_back_in_stock_subscription=self._page_cursor_update(self.retry_logic(self.Catalogs.create_back_in_stock_subscription))
        self.Catalogs.create_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_category))
        self.Catalogs.create_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_category_relationships_items))
        self.Catalogs.create_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_item))
        self.Catalogs.create_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_item_relationships_categories))
        self.Catalogs.create_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_variant))
        self.Catalogs.delete_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_category))
        self.Catalogs.delete_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_category_relationships_items))
        self.Catalogs.delete_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_item))
        self.Catalogs.delete_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_item_relationships_categories))
        self.Catalogs.delete_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_variant))
        self.Catalogs.get_catalog_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_categories))
        self.Catalogs.get_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category))
        self.Catalogs.get_catalog_category_items=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category_items))
        self.Catalogs.get_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category_relationships_items))
        self.Catalogs.get_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item))
        self.Catalogs.get_catalog_item_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item_categories))
        self.Catalogs.get_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item_relationships_categories))
        self.Catalogs.get_catalog_item_variants=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item_variants))
        self.Catalogs.get_catalog_items=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_items))
        self.Catalogs.get_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_variant))
        self.Catalogs.get_catalog_variants=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_variants))
        self.Catalogs.get_create_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_categories_job))
        self.Catalogs.get_create_categories_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_categories_jobs))
        self.Catalogs.get_create_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_items_job))
        self.Catalogs.get_create_items_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_items_jobs))
        self.Catalogs.get_create_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_variants_job))
        self.Catalogs.get_create_variants_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_create_variants_jobs))
        self.Catalogs.get_delete_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_categories_job))
        self.Catalogs.get_delete_categories_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_categories_jobs))
        self.Catalogs.get_delete_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_items_job))
        self.Catalogs.get_delete_items_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_items_jobs))
        self.Catalogs.get_delete_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_variants_job))
        self.Catalogs.get_delete_variants_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_delete_variants_jobs))
        self.Catalogs.get_update_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_categories_job))
        self.Catalogs.get_update_categories_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_categories_jobs))
        self.Catalogs.get_update_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_items_job))
        self.Catalogs.get_update_items_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_items_jobs))
        self.Catalogs.get_update_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_variants_job))
        self.Catalogs.get_update_variants_jobs=self._page_cursor_update(self.retry_logic(self.Catalogs.get_update_variants_jobs))
        self.Catalogs.spawn_create_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_create_categories_job))
        self.Catalogs.spawn_create_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_create_items_job))
        self.Catalogs.spawn_create_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_create_variants_job))
        self.Catalogs.spawn_delete_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_delete_categories_job))
        self.Catalogs.spawn_delete_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_delete_items_job))
        self.Catalogs.spawn_delete_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_delete_variants_job))
        self.Catalogs.spawn_update_categories_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_update_categories_job))
        self.Catalogs.spawn_update_items_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_update_items_job))
        self.Catalogs.spawn_update_variants_job=self._page_cursor_update(self.retry_logic(self.Catalogs.spawn_update_variants_job))
        self.Catalogs.update_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_category))
        self.Catalogs.update_catalog_category_relationships_items=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_category_relationships_items))
        self.Catalogs.update_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_item))
        self.Catalogs.update_catalog_item_relationships_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_item_relationships_categories))
        self.Catalogs.update_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_variant))
        
        
        ## Adding Coupons to Client
        self.Coupons=coupons_api.CouponsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Coupons
        self.Coupons.create_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.create_coupon))
        self.Coupons.create_coupon_code=self._page_cursor_update(self.retry_logic(self.Coupons.create_coupon_code))
        self.Coupons.delete_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.delete_coupon))
        self.Coupons.delete_coupon_code=self._page_cursor_update(self.retry_logic(self.Coupons.delete_coupon_code))
        self.Coupons.get_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon))
        self.Coupons.get_coupon_code=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_code))
        self.Coupons.get_coupon_code_bulk_create_job=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_code_bulk_create_job))
        self.Coupons.get_coupon_code_bulk_create_jobs=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_code_bulk_create_jobs))
        self.Coupons.get_coupon_code_relationships_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_code_relationships_coupon))
        self.Coupons.get_coupon_codes=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_codes))
        self.Coupons.get_coupon_codes_for_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_codes_for_coupon))
        self.Coupons.get_coupon_for_coupon_code=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_for_coupon_code))
        self.Coupons.get_coupon_relationships_coupon_codes=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupon_relationships_coupon_codes))
        self.Coupons.get_coupons=self._page_cursor_update(self.retry_logic(self.Coupons.get_coupons))
        self.Coupons.spawn_coupon_code_bulk_create_job=self._page_cursor_update(self.retry_logic(self.Coupons.spawn_coupon_code_bulk_create_job))
        self.Coupons.update_coupon=self._page_cursor_update(self.retry_logic(self.Coupons.update_coupon))
        self.Coupons.update_coupon_code=self._page_cursor_update(self.retry_logic(self.Coupons.update_coupon_code))
        
        
        ## Adding Data_Privacy to Client
        self.Data_Privacy=data_privacy_api.DataPrivacyApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Data_Privacy
        self.Data_Privacy.request_profile_deletion=self._page_cursor_update(self.retry_logic(self.Data_Privacy.request_profile_deletion))
        
        
        ## Adding Events to Client
        self.Events=events_api.EventsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Events
        self.Events.bulk_create_events=self._page_cursor_update(self.retry_logic(self.Events.bulk_create_events))
        self.Events.create_event=self._page_cursor_update(self.retry_logic(self.Events.create_event))
        self.Events.get_event=self._page_cursor_update(self.retry_logic(self.Events.get_event))
        self.Events.get_event_metric=self._page_cursor_update(self.retry_logic(self.Events.get_event_metric))
        self.Events.get_event_profile=self._page_cursor_update(self.retry_logic(self.Events.get_event_profile))
        self.Events.get_event_relationships_metric=self._page_cursor_update(self.retry_logic(self.Events.get_event_relationships_metric))
        self.Events.get_event_relationships_profile=self._page_cursor_update(self.retry_logic(self.Events.get_event_relationships_profile))
        self.Events.get_events=self._page_cursor_update(self.retry_logic(self.Events.get_events))
        
        
        ## Adding Flows to Client
        self.Flows=flows_api.FlowsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Flows
        self.Flows.delete_flow=self._page_cursor_update(self.retry_logic(self.Flows.delete_flow))
        self.Flows.get_flow=self._page_cursor_update(self.retry_logic(self.Flows.get_flow))
        self.Flows.get_flow_action=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action))
        self.Flows.get_flow_action_flow=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_flow))
        self.Flows.get_flow_action_messages=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_messages))
        self.Flows.get_flow_action_relationships_flow=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_relationships_flow))
        self.Flows.get_flow_action_relationships_messages=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_relationships_messages))
        self.Flows.get_flow_flow_actions=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_flow_actions))
        self.Flows.get_flow_message=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message))
        self.Flows.get_flow_message_action=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_action))
        self.Flows.get_flow_message_relationships_action=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_relationships_action))
        self.Flows.get_flow_message_relationships_template=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_relationships_template))
        self.Flows.get_flow_message_template=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_template))
        self.Flows.get_flow_relationships_flow_actions=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_relationships_flow_actions))
        self.Flows.get_flow_relationships_tags=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_relationships_tags))
        self.Flows.get_flow_tags=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_tags))
        self.Flows.get_flows=self._page_cursor_update(self.retry_logic(self.Flows.get_flows))
        self.Flows.update_flow=self._page_cursor_update(self.retry_logic(self.Flows.update_flow))
        
        
        ## Adding Forms to Client
        self.Forms=forms_api.FormsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Forms
        self.Forms.get_form=self._page_cursor_update(self.retry_logic(self.Forms.get_form))
        self.Forms.get_form_for_form_version=self._page_cursor_update(self.retry_logic(self.Forms.get_form_for_form_version))
        self.Forms.get_form_id_for_form_version=self._page_cursor_update(self.retry_logic(self.Forms.get_form_id_for_form_version))
        self.Forms.get_form_version=self._page_cursor_update(self.retry_logic(self.Forms.get_form_version))
        self.Forms.get_forms=self._page_cursor_update(self.retry_logic(self.Forms.get_forms))
        self.Forms.get_version_ids_for_form=self._page_cursor_update(self.retry_logic(self.Forms.get_version_ids_for_form))
        self.Forms.get_versions_for_form=self._page_cursor_update(self.retry_logic(self.Forms.get_versions_for_form))
        
        
        ## Adding Images to Client
        self.Images=images_api.ImagesApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Images
        self.Images.get_image=self._page_cursor_update(self.retry_logic(self.Images.get_image))
        self.Images.get_images=self._page_cursor_update(self.retry_logic(self.Images.get_images))
        self.Images.update_image=self._page_cursor_update(self.retry_logic(self.Images.update_image))
        self.Images.upload_image_from_file=self._page_cursor_update(self.retry_logic(self.Images.upload_image_from_file))
        self.Images.upload_image_from_url=self._page_cursor_update(self.retry_logic(self.Images.upload_image_from_url))
        
        
        ## Adding Lists to Client
        self.Lists=lists_api.ListsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Lists
        self.Lists.create_list=self._page_cursor_update(self.retry_logic(self.Lists.create_list))
        self.Lists.create_list_relationships=self._page_cursor_update(self.retry_logic(self.Lists.create_list_relationships))
        self.Lists.delete_list=self._page_cursor_update(self.retry_logic(self.Lists.delete_list))
        self.Lists.delete_list_relationships=self._page_cursor_update(self.retry_logic(self.Lists.delete_list_relationships))
        self.Lists.get_list=self._page_cursor_update(self.retry_logic(self.Lists.get_list))
        self.Lists.get_list_profiles=self._page_cursor_update(self.retry_logic(self.Lists.get_list_profiles))
        self.Lists.get_list_relationships_profiles=self._page_cursor_update(self.retry_logic(self.Lists.get_list_relationships_profiles))
        self.Lists.get_list_relationships_tags=self._page_cursor_update(self.retry_logic(self.Lists.get_list_relationships_tags))
        self.Lists.get_list_tags=self._page_cursor_update(self.retry_logic(self.Lists.get_list_tags))
        self.Lists.get_lists=self._page_cursor_update(self.retry_logic(self.Lists.get_lists))
        self.Lists.update_list=self._page_cursor_update(self.retry_logic(self.Lists.update_list))
        
        
        ## Adding Metrics to Client
        self.Metrics=metrics_api.MetricsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Metrics
        self.Metrics.get_metric=self._page_cursor_update(self.retry_logic(self.Metrics.get_metric))
        self.Metrics.get_metrics=self._page_cursor_update(self.retry_logic(self.Metrics.get_metrics))
        self.Metrics.query_metric_aggregates=self._page_cursor_update(self.retry_logic(self.Metrics.query_metric_aggregates))
        
        
        ## Adding Profiles to Client
        self.Profiles=profiles_api.ProfilesApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Profiles
        self.Profiles.create_or_update_profile=self._page_cursor_update(self.retry_logic(self.Profiles.create_or_update_profile))
        self.Profiles.create_profile=self._page_cursor_update(self.retry_logic(self.Profiles.create_profile))
        self.Profiles.create_push_token=self._page_cursor_update(self.retry_logic(self.Profiles.create_push_token))
        self.Profiles.get_bulk_profile_import_job=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job))
        self.Profiles.get_bulk_profile_import_job_import_errors=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job_import_errors))
        self.Profiles.get_bulk_profile_import_job_lists=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job_lists))
        self.Profiles.get_bulk_profile_import_job_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job_profiles))
        self.Profiles.get_bulk_profile_import_job_relationships_lists=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job_relationships_lists))
        self.Profiles.get_bulk_profile_import_job_relationships_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_job_relationships_profiles))
        self.Profiles.get_bulk_profile_import_jobs=self._page_cursor_update(self.retry_logic(self.Profiles.get_bulk_profile_import_jobs))
        self.Profiles.get_profile=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile))
        self.Profiles.get_profile_lists=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_lists))
        self.Profiles.get_profile_relationships_lists=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_relationships_lists))
        self.Profiles.get_profile_relationships_segments=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_relationships_segments))
        self.Profiles.get_profile_segments=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_segments))
        self.Profiles.get_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.get_profiles))
        self.Profiles.merge_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.merge_profiles))
        self.Profiles.spawn_bulk_profile_import_job=self._page_cursor_update(self.retry_logic(self.Profiles.spawn_bulk_profile_import_job))
        self.Profiles.subscribe_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.subscribe_profiles))
        self.Profiles.suppress_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.suppress_profiles))
        self.Profiles.unsubscribe_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.unsubscribe_profiles))
        self.Profiles.unsuppress_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.unsuppress_profiles))
        self.Profiles.update_profile=self._page_cursor_update(self.retry_logic(self.Profiles.update_profile))
        
        
        ## Adding Reporting to Client
        self.Reporting=reporting_api.ReportingApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Reporting
        self.Reporting.query_campaign_values=self._page_cursor_update(self.retry_logic(self.Reporting.query_campaign_values))
        self.Reporting.query_flow_series=self._page_cursor_update(self.retry_logic(self.Reporting.query_flow_series))
        self.Reporting.query_flow_values=self._page_cursor_update(self.retry_logic(self.Reporting.query_flow_values))
        
        
        ## Adding Segments to Client
        self.Segments=segments_api.SegmentsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Segments
        self.Segments.create_segment=self._page_cursor_update(self.retry_logic(self.Segments.create_segment))
        self.Segments.delete_segment=self._page_cursor_update(self.retry_logic(self.Segments.delete_segment))
        self.Segments.get_segment=self._page_cursor_update(self.retry_logic(self.Segments.get_segment))
        self.Segments.get_segment_profiles=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_profiles))
        self.Segments.get_segment_relationships_profiles=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_relationships_profiles))
        self.Segments.get_segment_relationships_tags=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_relationships_tags))
        self.Segments.get_segment_tags=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_tags))
        self.Segments.get_segments=self._page_cursor_update(self.retry_logic(self.Segments.get_segments))
        self.Segments.update_segment=self._page_cursor_update(self.retry_logic(self.Segments.update_segment))
        
        
        ## Adding Tags to Client
        self.Tags=tags_api.TagsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Tags
        self.Tags.create_tag=self._page_cursor_update(self.retry_logic(self.Tags.create_tag))
        self.Tags.create_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_group))
        self.Tags.create_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_relationships_campaigns))
        self.Tags.create_tag_relationships_flows=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_relationships_flows))
        self.Tags.create_tag_relationships_lists=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_relationships_lists))
        self.Tags.create_tag_relationships_segments=self._page_cursor_update(self.retry_logic(self.Tags.create_tag_relationships_segments))
        self.Tags.delete_tag=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag))
        self.Tags.delete_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_group))
        self.Tags.delete_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_relationships_campaigns))
        self.Tags.delete_tag_relationships_flows=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_relationships_flows))
        self.Tags.delete_tag_relationships_lists=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_relationships_lists))
        self.Tags.delete_tag_relationships_segments=self._page_cursor_update(self.retry_logic(self.Tags.delete_tag_relationships_segments))
        self.Tags.get_tag=self._page_cursor_update(self.retry_logic(self.Tags.get_tag))
        self.Tags.get_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_group))
        self.Tags.get_tag_group_relationships_tags=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_group_relationships_tags))
        self.Tags.get_tag_group_tags=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_group_tags))
        self.Tags.get_tag_groups=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_groups))
        self.Tags.get_tag_relationships_campaigns=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships_campaigns))
        self.Tags.get_tag_relationships_flows=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships_flows))
        self.Tags.get_tag_relationships_lists=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships_lists))
        self.Tags.get_tag_relationships_segments=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships_segments))
        self.Tags.get_tag_relationships_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_relationships_tag_group))
        self.Tags.get_tag_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.get_tag_tag_group))
        self.Tags.get_tags=self._page_cursor_update(self.retry_logic(self.Tags.get_tags))
        self.Tags.update_tag=self._page_cursor_update(self.retry_logic(self.Tags.update_tag))
        self.Tags.update_tag_group=self._page_cursor_update(self.retry_logic(self.Tags.update_tag_group))
        
        
        ## Adding Templates to Client
        self.Templates=templates_api.TemplatesApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Templates
        self.Templates.create_template=self._page_cursor_update(self.retry_logic(self.Templates.create_template))
        self.Templates.create_template_clone=self._page_cursor_update(self.retry_logic(self.Templates.create_template_clone))
        self.Templates.create_template_render=self._page_cursor_update(self.retry_logic(self.Templates.create_template_render))
        self.Templates.delete_template=self._page_cursor_update(self.retry_logic(self.Templates.delete_template))
        self.Templates.get_template=self._page_cursor_update(self.retry_logic(self.Templates.get_template))
        self.Templates.get_templates=self._page_cursor_update(self.retry_logic(self.Templates.get_templates))
        self.Templates.update_template=self._page_cursor_update(self.retry_logic(self.Templates.update_template))
        
        
        ## Adding Tests to Client
        self.Tests=tests_api.TestsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Tests
        self.Tests.get_test_bulk_create_photos_jobs=self._page_cursor_update(self.retry_logic(self.Tests.get_test_bulk_create_photos_jobs))
        self.Tests.get_test_cities=self._page_cursor_update(self.retry_logic(self.Tests.get_test_cities))
        self.Tests.get_test_photographers=self._page_cursor_update(self.retry_logic(self.Tests.get_test_photographers))
        self.Tests.get_test_photos=self._page_cursor_update(self.retry_logic(self.Tests.get_test_photos))
        
        
        ## Adding Webhooks to Client
        self.Webhooks=webhooks_api.WebhooksApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Webhooks
        self.Webhooks.create_webhook=self._page_cursor_update(self.retry_logic(self.Webhooks.create_webhook))
        self.Webhooks.delete_webhook=self._page_cursor_update(self.retry_logic(self.Webhooks.delete_webhook))
        self.Webhooks.get_webhook=self._page_cursor_update(self.retry_logic(self.Webhooks.get_webhook))
        self.Webhooks.get_webhook_topic=self._page_cursor_update(self.retry_logic(self.Webhooks.get_webhook_topic))
        self.Webhooks.get_webhook_topics=self._page_cursor_update(self.retry_logic(self.Webhooks.get_webhook_topics))
        self.Webhooks.get_webhooks=self._page_cursor_update(self.retry_logic(self.Webhooks.get_webhooks))
        self.Webhooks.update_webhook=self._page_cursor_update(self.retry_logic(self.Webhooks.update_webhook))
        
        

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