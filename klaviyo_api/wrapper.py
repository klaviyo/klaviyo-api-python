from __future__ import absolute_import

from __future__ import print_function
import tenacity
import openapi_client
import klaviyo_api.custom_retry as custom_retry
from dataclasses import dataclass
from typing import Callable, ClassVar
from openapi_client.api import catalogs_api
from openapi_client.api import client_api
from openapi_client.api import events_api
from openapi_client.api import flows_api
from openapi_client.api import lists_api
from openapi_client.api import metrics_api
from openapi_client.api import profiles_api
from openapi_client.api import segments_api
from openapi_client.api import templates_api


@dataclass
class KlaviyoAPI:

    api_key: str
    max_delay: int = 60
    max_retries: int = 3
    test_host: str = ''

    _REVISION = "2022-10-17"

    _STATUS_CODE_TOO_MANY_REQUESTS = 429
    _STATUS_CODE_SERVICE_UNAVAILABLE = 503
    _STATUS_CODE_GATEWAY_TIMEOUT = 504
    _STATUS_CODE_A_TIMEOUT_OCCURED = 524

    _RETRY_CODES = {
        _STATUS_CODE_TOO_MANY_REQUESTS,
        _STATUS_CODE_SERVICE_UNAVAILABLE,
        _STATUS_CODE_GATEWAY_TIMEOUT,
        _STATUS_CODE_A_TIMEOUT_OCCURED
        }

    _CURSOR_LENGTH = 44
    _CURSOR_SEARCH_TOKENS = ['page%5Bcursor%5D','page[cursor]']

    def __post_init__(self):

        self.configuration = openapi_client.Configuration(
            api_key={'Klaviyo-API-Key':f'Klaviyo-API-Key {self.api_key}'}
            )

        if self.test_host:
            self.configuration.host = self.test_host

        self.api_client = openapi_client.ApiClient(self.configuration)

        self.api_client.default_headers['revision'] = self._REVISION
        
        if self.max_retries <= 0:
            self.max_wait = .1
        else:
            self.max_wait = self.max_delay/self.max_retries


        self.retry_logic = tenacity.retry(
            reraise=True,
            retry=custom_retry.retry_if_qualifies(self._RETRY_CODES),
            wait=tenacity.wait.wait_random_exponential(multiplier = 1, max = self.max_wait),
            stop=tenacity.stop.stop_after_attempt(self.max_retries)
        )

        
        ## Adding Catalogs to Client
        self.Catalogs=catalogs_api.CatalogsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Catalogs
        self.Catalogs.create_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_category))
        self.Catalogs.create_catalog_category_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_category_relationships))
        self.Catalogs.create_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_item))
        self.Catalogs.create_catalog_item_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_item_relationships))
        self.Catalogs.create_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.create_catalog_variant))
        self.Catalogs.delete_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_category))
        self.Catalogs.delete_catalog_category_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_category_relationships))
        self.Catalogs.delete_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_item))
        self.Catalogs.delete_catalog_item_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_item_relationships))
        self.Catalogs.delete_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.delete_catalog_variant))
        self.Catalogs.get_catalog_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_categories))
        self.Catalogs.get_catalog_category=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category))
        self.Catalogs.get_catalog_category_items=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category_items))
        self.Catalogs.get_catalog_category_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_category_relationships))
        self.Catalogs.get_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item))
        self.Catalogs.get_catalog_item_categories=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item_categories))
        self.Catalogs.get_catalog_item_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.get_catalog_item_relationships))
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
        self.Catalogs.update_catalog_category_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_category_relationships))
        self.Catalogs.update_catalog_item=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_item))
        self.Catalogs.update_catalog_item_relationships=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_item_relationships))
        self.Catalogs.update_catalog_variant=self._page_cursor_update(self.retry_logic(self.Catalogs.update_catalog_variant))
        
        
        ## Adding Client to Client
        self.Client=client_api.ClientApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Client
        self.Client.create_client_event=self._page_cursor_update(self.retry_logic(self.Client.create_client_event))
        self.Client.create_client_profile=self._page_cursor_update(self.retry_logic(self.Client.create_client_profile))
        self.Client.create_client_subscription=self._page_cursor_update(self.retry_logic(self.Client.create_client_subscription))
        
        
        ## Adding Events to Client
        self.Events=events_api.EventsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Events
        self.Events.create_event=self._page_cursor_update(self.retry_logic(self.Events.create_event))
        self.Events.get_event=self._page_cursor_update(self.retry_logic(self.Events.get_event))
        self.Events.get_event_metrics=self._page_cursor_update(self.retry_logic(self.Events.get_event_metrics))
        self.Events.get_event_profiles=self._page_cursor_update(self.retry_logic(self.Events.get_event_profiles))
        self.Events.get_event_relationships=self._page_cursor_update(self.retry_logic(self.Events.get_event_relationships))
        self.Events.get_events=self._page_cursor_update(self.retry_logic(self.Events.get_events))
        
        
        ## Adding Flows to Client
        self.Flows=flows_api.FlowsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Flows
        self.Flows.get_flow=self._page_cursor_update(self.retry_logic(self.Flows.get_flow))
        self.Flows.get_flow_action=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action))
        self.Flows.get_flow_action_flow=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_flow))
        self.Flows.get_flow_action_messages=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_messages))
        self.Flows.get_flow_action_relationships=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_action_relationships))
        self.Flows.get_flow_flow_actions=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_flow_actions))
        self.Flows.get_flow_message=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message))
        self.Flows.get_flow_message_action=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_action))
        self.Flows.get_flow_message_relationships=self._page_cursor_update(self.retry_logic(self.Flows.get_flow_message_relationships))
        self.Flows.get_flows=self._page_cursor_update(self.retry_logic(self.Flows.get_flows))
        self.Flows.update_flow=self._page_cursor_update(self.retry_logic(self.Flows.update_flow))
        
        
        ## Adding Lists to Client
        self.Lists=lists_api.ListsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Lists
        self.Lists.create_list=self._page_cursor_update(self.retry_logic(self.Lists.create_list))
        self.Lists.create_list_relationships=self._page_cursor_update(self.retry_logic(self.Lists.create_list_relationships))
        self.Lists.delete_list=self._page_cursor_update(self.retry_logic(self.Lists.delete_list))
        self.Lists.delete_list_relationships=self._page_cursor_update(self.retry_logic(self.Lists.delete_list_relationships))
        self.Lists.get_list=self._page_cursor_update(self.retry_logic(self.Lists.get_list))
        self.Lists.get_list_profiles=self._page_cursor_update(self.retry_logic(self.Lists.get_list_profiles))
        self.Lists.get_list_relationships=self._page_cursor_update(self.retry_logic(self.Lists.get_list_relationships))
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
        self.Profiles.create_profile=self._page_cursor_update(self.retry_logic(self.Profiles.create_profile))
        self.Profiles.get_profile=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile))
        self.Profiles.get_profile_lists=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_lists))
        self.Profiles.get_profile_relationships=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_relationships))
        self.Profiles.get_profile_segments=self._page_cursor_update(self.retry_logic(self.Profiles.get_profile_segments))
        self.Profiles.get_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.get_profiles))
        self.Profiles.subscribe_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.subscribe_profiles))
        self.Profiles.suppress_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.suppress_profiles))
        self.Profiles.unsubscribe_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.unsubscribe_profiles))
        self.Profiles.unsuppress_profiles=self._page_cursor_update(self.retry_logic(self.Profiles.unsuppress_profiles))
        self.Profiles.update_profile=self._page_cursor_update(self.retry_logic(self.Profiles.update_profile))
        
        
        ## Adding Segments to Client
        self.Segments=segments_api.SegmentsApi(self.api_client)
        
        ## Applying tenacity retry decorator to each endpoint in Segments
        self.Segments.get_segment=self._page_cursor_update(self.retry_logic(self.Segments.get_segment))
        self.Segments.get_segment_profiles=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_profiles))
        self.Segments.get_segment_relationships=self._page_cursor_update(self.retry_logic(self.Segments.get_segment_relationships))
        self.Segments.get_segments=self._page_cursor_update(self.retry_logic(self.Segments.get_segments))
        self.Segments.update_segment=self._page_cursor_update(self.retry_logic(self.Segments.update_segment))
        
        
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
                                start = page_cursor.find(found_token)+len(found_token)+1
                                page_cursor = page_cursor[start:start+cls._CURSOR_LENGTH]
                                kwargs['page_cursor'] = page_cursor
            return func(*args,**kwargs)
        return _wrapped_func