# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.audiences_sub_object import AudiencesSubObject
from openapi_client.model.campaign_clone_query import CampaignCloneQuery
from openapi_client.model.campaign_clone_query_as_sub_resource import CampaignCloneQueryAsSubResource
from openapi_client.model.campaign_clone_query_as_sub_resource_attributes import CampaignCloneQueryAsSubResourceAttributes
from openapi_client.model.campaign_create_query import CampaignCreateQuery
from openapi_client.model.campaign_create_query_as_sub_resource import CampaignCreateQueryAsSubResource
from openapi_client.model.campaign_create_query_as_sub_resource_attributes import CampaignCreateQueryAsSubResourceAttributes
from openapi_client.model.campaign_message_partial_update_query import CampaignMessagePartialUpdateQuery
from openapi_client.model.campaign_message_partial_update_query_as_sub_resource import CampaignMessagePartialUpdateQueryAsSubResource
from openapi_client.model.campaign_message_partial_update_query_as_sub_resource_attributes import CampaignMessagePartialUpdateQueryAsSubResourceAttributes
from openapi_client.model.campaign_partial_update_query import CampaignPartialUpdateQuery
from openapi_client.model.campaign_partial_update_query_as_sub_resource import CampaignPartialUpdateQueryAsSubResource
from openapi_client.model.campaign_partial_update_query_as_sub_resource_attributes import CampaignPartialUpdateQueryAsSubResourceAttributes
from openapi_client.model.campaign_send_job_create_query import CampaignSendJobCreateQuery
from openapi_client.model.campaign_send_job_create_query_as_sub_resource import CampaignSendJobCreateQueryAsSubResource
from openapi_client.model.campaign_send_job_create_query_as_sub_resource_attributes import CampaignSendJobCreateQueryAsSubResourceAttributes
from openapi_client.model.campaign_send_job_partial_update_query import CampaignSendJobPartialUpdateQuery
from openapi_client.model.campaign_send_job_partial_update_query_as_sub_resource import CampaignSendJobPartialUpdateQueryAsSubResource
from openapi_client.model.campaign_send_job_partial_update_query_as_sub_resource_attributes import CampaignSendJobPartialUpdateQueryAsSubResourceAttributes
from openapi_client.model.catalog_category_create_job_create_query import CatalogCategoryCreateJobCreateQuery
from openapi_client.model.catalog_category_create_job_create_query_as_sub_resource import CatalogCategoryCreateJobCreateQueryAsSubResource
from openapi_client.model.catalog_category_create_job_create_query_as_sub_resource_attributes import CatalogCategoryCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_category_create_query import CatalogCategoryCreateQuery
from openapi_client.model.catalog_category_create_query_as_sub_resource import CatalogCategoryCreateQueryAsSubResource
from openapi_client.model.catalog_category_create_query_as_sub_resource_attributes import CatalogCategoryCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_category_delete_job_create_query import CatalogCategoryDeleteJobCreateQuery
from openapi_client.model.catalog_category_delete_job_create_query_as_sub_resource import CatalogCategoryDeleteJobCreateQueryAsSubResource
from openapi_client.model.catalog_category_delete_job_create_query_as_sub_resource_attributes import CatalogCategoryDeleteJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_category_delete_query_as_sub_resource import CatalogCategoryDeleteQueryAsSubResource
from openapi_client.model.catalog_category_item_op import CatalogCategoryItemOp
from openapi_client.model.catalog_category_update_job_create_query import CatalogCategoryUpdateJobCreateQuery
from openapi_client.model.catalog_category_update_job_create_query_as_sub_resource import CatalogCategoryUpdateJobCreateQueryAsSubResource
from openapi_client.model.catalog_category_update_job_create_query_as_sub_resource_attributes import CatalogCategoryUpdateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_category_update_query import CatalogCategoryUpdateQuery
from openapi_client.model.catalog_category_update_query_as_sub_resource import CatalogCategoryUpdateQueryAsSubResource
from openapi_client.model.catalog_category_update_query_as_sub_resource_attributes import CatalogCategoryUpdateQueryAsSubResourceAttributes
from openapi_client.model.catalog_item_category_op import CatalogItemCategoryOp
from openapi_client.model.catalog_item_create_job_create_query import CatalogItemCreateJobCreateQuery
from openapi_client.model.catalog_item_create_job_create_query_as_sub_resource import CatalogItemCreateJobCreateQueryAsSubResource
from openapi_client.model.catalog_item_create_job_create_query_as_sub_resource_attributes import CatalogItemCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_item_create_query import CatalogItemCreateQuery
from openapi_client.model.catalog_item_create_query_as_sub_resource import CatalogItemCreateQueryAsSubResource
from openapi_client.model.catalog_item_create_query_as_sub_resource_attributes import CatalogItemCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_item_create_query_as_sub_resource_relationships import CatalogItemCreateQueryAsSubResourceRelationships
from openapi_client.model.catalog_item_create_query_as_sub_resource_relationships_categories import CatalogItemCreateQueryAsSubResourceRelationshipsCategories
from openapi_client.model.catalog_item_create_query_as_sub_resource_relationships_categories_data_inner import CatalogItemCreateQueryAsSubResourceRelationshipsCategoriesDataInner
from openapi_client.model.catalog_item_delete_job_create_query import CatalogItemDeleteJobCreateQuery
from openapi_client.model.catalog_item_delete_job_create_query_as_sub_resource import CatalogItemDeleteJobCreateQueryAsSubResource
from openapi_client.model.catalog_item_delete_job_create_query_as_sub_resource_attributes import CatalogItemDeleteJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_item_delete_query_as_sub_resource import CatalogItemDeleteQueryAsSubResource
from openapi_client.model.catalog_item_update_job_create_query import CatalogItemUpdateJobCreateQuery
from openapi_client.model.catalog_item_update_job_create_query_as_sub_resource import CatalogItemUpdateJobCreateQueryAsSubResource
from openapi_client.model.catalog_item_update_job_create_query_as_sub_resource_attributes import CatalogItemUpdateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_item_update_query import CatalogItemUpdateQuery
from openapi_client.model.catalog_item_update_query_as_sub_resource import CatalogItemUpdateQueryAsSubResource
from openapi_client.model.catalog_item_update_query_as_sub_resource_attributes import CatalogItemUpdateQueryAsSubResourceAttributes
from openapi_client.model.catalog_job_error_payload import CatalogJobErrorPayload
from openapi_client.model.catalog_variant_create_job_create_query import CatalogVariantCreateJobCreateQuery
from openapi_client.model.catalog_variant_create_job_create_query_as_sub_resource import CatalogVariantCreateJobCreateQueryAsSubResource
from openapi_client.model.catalog_variant_create_job_create_query_as_sub_resource_attributes import CatalogVariantCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_variant_create_query import CatalogVariantCreateQuery
from openapi_client.model.catalog_variant_create_query_as_sub_resource import CatalogVariantCreateQueryAsSubResource
from openapi_client.model.catalog_variant_create_query_as_sub_resource_attributes import CatalogVariantCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_variant_create_query_as_sub_resource_relationships import CatalogVariantCreateQueryAsSubResourceRelationships
from openapi_client.model.catalog_variant_create_query_as_sub_resource_relationships_items import CatalogVariantCreateQueryAsSubResourceRelationshipsItems
from openapi_client.model.catalog_variant_create_query_as_sub_resource_relationships_items_data_inner import CatalogVariantCreateQueryAsSubResourceRelationshipsItemsDataInner
from openapi_client.model.catalog_variant_delete_job_create_query import CatalogVariantDeleteJobCreateQuery
from openapi_client.model.catalog_variant_delete_job_create_query_as_sub_resource import CatalogVariantDeleteJobCreateQueryAsSubResource
from openapi_client.model.catalog_variant_delete_job_create_query_as_sub_resource_attributes import CatalogVariantDeleteJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_variant_delete_query_as_sub_resource import CatalogVariantDeleteQueryAsSubResource
from openapi_client.model.catalog_variant_update_job_create_query import CatalogVariantUpdateJobCreateQuery
from openapi_client.model.catalog_variant_update_job_create_query_as_sub_resource import CatalogVariantUpdateJobCreateQueryAsSubResource
from openapi_client.model.catalog_variant_update_job_create_query_as_sub_resource_attributes import CatalogVariantUpdateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.catalog_variant_update_query import CatalogVariantUpdateQuery
from openapi_client.model.catalog_variant_update_query_as_sub_resource import CatalogVariantUpdateQueryAsSubResource
from openapi_client.model.catalog_variant_update_query_as_sub_resource_attributes import CatalogVariantUpdateQueryAsSubResourceAttributes
from openapi_client.model.content_sub_object import ContentSubObject
from openapi_client.model.data_privacy_create_deletion_job_query import DataPrivacyCreateDeletionJobQuery
from openapi_client.model.data_privacy_create_deletion_job_query_as_sub_resource import DataPrivacyCreateDeletionJobQueryAsSubResource
from openapi_client.model.data_privacy_create_deletion_job_query_as_sub_resource_attributes import DataPrivacyCreateDeletionJobQueryAsSubResourceAttributes
from openapi_client.model.email_message_content import EmailMessageContent
from openapi_client.model.email_tracking_options import EmailTrackingOptions
from openapi_client.model.error_source import ErrorSource
from openapi_client.model.event_create_query import EventCreateQuery
from openapi_client.model.event_create_query_as_sub_resource import EventCreateQueryAsSubResource
from openapi_client.model.event_create_query_as_sub_resource_attributes import EventCreateQueryAsSubResourceAttributes
from openapi_client.model.flow_update_query import FlowUpdateQuery
from openapi_client.model.flow_update_query_as_sub_resource import FlowUpdateQueryAsSubResource
from openapi_client.model.flow_update_query_as_sub_resource_attributes import FlowUpdateQueryAsSubResourceAttributes
from openapi_client.model.get_catalog_items4_xx_response import GetCatalogItems4XXResponse
from openapi_client.model.get_catalog_items4_xx_response_errors_inner import GetCatalogItems4XXResponseErrorsInner
from openapi_client.model.get_catalog_items4_xx_response_errors_inner_source import GetCatalogItems4XXResponseErrorsInnerSource
from openapi_client.model.included_categories import IncludedCategories
from openapi_client.model.included_categories_attributes import IncludedCategoriesAttributes
from openapi_client.model.included_flow_action import IncludedFlowAction
from openapi_client.model.included_flow_actions import IncludedFlowActions
from openapi_client.model.included_flow_actions_attributes import IncludedFlowActionsAttributes
from openapi_client.model.included_flow_actions_attributes_tracking_options import IncludedFlowActionsAttributesTrackingOptions
from openapi_client.model.included_flow_messages import IncludedFlowMessages
from openapi_client.model.included_flow_messages_attributes import IncludedFlowMessagesAttributes
from openapi_client.model.included_flow_messages_attributes_content import IncludedFlowMessagesAttributesContent
from openapi_client.model.included_flows import IncludedFlows
from openapi_client.model.included_flows_attributes import IncludedFlowsAttributes
from openapi_client.model.included_items import IncludedItems
from openapi_client.model.included_items_attributes import IncludedItemsAttributes
from openapi_client.model.included_lists import IncludedLists
from openapi_client.model.included_lists_attributes import IncludedListsAttributes
from openapi_client.model.included_metrics import IncludedMetrics
from openapi_client.model.included_metrics_attributes import IncludedMetricsAttributes
from openapi_client.model.included_profile import IncludedProfile
from openapi_client.model.included_profiles import IncludedProfiles
from openapi_client.model.included_profiles_attributes import IncludedProfilesAttributes
from openapi_client.model.included_segments import IncludedSegments
from openapi_client.model.included_tags import IncludedTags
from openapi_client.model.included_variants import IncludedVariants
from openapi_client.model.included_variants_attributes import IncludedVariantsAttributes
from openapi_client.model.included_variants_links import IncludedVariantsLinks
from openapi_client.model.list_create_query import ListCreateQuery
from openapi_client.model.list_create_query_as_sub_resource import ListCreateQueryAsSubResource
from openapi_client.model.list_create_query_as_sub_resource_attributes import ListCreateQueryAsSubResourceAttributes
from openapi_client.model.list_members_add_query import ListMembersAddQuery
from openapi_client.model.list_members_add_query_data_inner import ListMembersAddQueryDataInner
from openapi_client.model.list_members_delete_query import ListMembersDeleteQuery
from openapi_client.model.list_partial_update_query import ListPartialUpdateQuery
from openapi_client.model.list_partial_update_query_as_sub_resource import ListPartialUpdateQueryAsSubResource
from openapi_client.model.metric_aggregate_query import MetricAggregateQuery
from openapi_client.model.metric_aggregate_query_as_sub_resource import MetricAggregateQueryAsSubResource
from openapi_client.model.metric_aggregate_query_as_sub_resource_attributes import MetricAggregateQueryAsSubResourceAttributes
from openapi_client.model.metric_aggregate_row_dto import MetricAggregateRowDTO
from openapi_client.model.metric_create_query import MetricCreateQuery
from openapi_client.model.onsite_profile_create_query import OnsiteProfileCreateQuery
from openapi_client.model.onsite_profile_create_query_as_sub_resource import OnsiteProfileCreateQueryAsSubResource
from openapi_client.model.onsite_profile_meta import OnsiteProfileMeta
from openapi_client.model.onsite_profile_meta_identifiers import OnsiteProfileMetaIdentifiers
from openapi_client.model.onsite_subscription_create_query import OnsiteSubscriptionCreateQuery
from openapi_client.model.onsite_subscription_create_query_as_sub_resource import OnsiteSubscriptionCreateQueryAsSubResource
from openapi_client.model.onsite_subscription_create_query_as_sub_resource_attributes import OnsiteSubscriptionCreateQueryAsSubResourceAttributes
from openapi_client.model.profile_create_query import ProfileCreateQuery
from openapi_client.model.profile_create_query_as_sub_resource import ProfileCreateQueryAsSubResource
from openapi_client.model.profile_create_query_as_sub_resource_attributes import ProfileCreateQueryAsSubResourceAttributes
from openapi_client.model.profile_location import ProfileLocation
from openapi_client.model.profile_location_latitude import ProfileLocationLatitude
from openapi_client.model.profile_partial_update_query import ProfilePartialUpdateQuery
from openapi_client.model.profile_partial_update_query_as_sub_resource import ProfilePartialUpdateQueryAsSubResource
from openapi_client.model.sms_message_content import SMSMessageContent
from openapi_client.model.sms_render_options import SMSRenderOptions
from openapi_client.model.sms_tracking_options import SMSTrackingOptions
from openapi_client.model.segment_partial_update_query import SegmentPartialUpdateQuery
from openapi_client.model.segment_partial_update_query_as_sub_resource import SegmentPartialUpdateQueryAsSubResource
from openapi_client.model.send_options import SendOptions
from openapi_client.model.send_options_sub_object import SendOptionsSubObject
from openapi_client.model.send_strategy_sub_object import SendStrategySubObject
from openapi_client.model.send_strategy_sub_object_options import SendStrategySubObjectOptions
from openapi_client.model.send_time_sub_object import SendTimeSubObject
from openapi_client.model.static_schedule_options import StaticScheduleOptions
from openapi_client.model.subscription import Subscription
from openapi_client.model.subscription_create_job_create_query import SubscriptionCreateJobCreateQuery
from openapi_client.model.subscription_create_job_create_query_as_sub_resource import SubscriptionCreateJobCreateQueryAsSubResource
from openapi_client.model.subscription_create_job_create_query_as_sub_resource_attributes import SubscriptionCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.suppression import Suppression
from openapi_client.model.suppression_create_job_create_query import SuppressionCreateJobCreateQuery
from openapi_client.model.suppression_create_job_create_query_as_sub_resource import SuppressionCreateJobCreateQueryAsSubResource
from openapi_client.model.suppression_create_job_create_query_as_sub_resource_attributes import SuppressionCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.tag_create_query import TagCreateQuery
from openapi_client.model.tag_create_query_as_sub_resource import TagCreateQueryAsSubResource
from openapi_client.model.tag_create_query_as_sub_resource_attributes import TagCreateQueryAsSubResourceAttributes
from openapi_client.model.tag_group_create_query import TagGroupCreateQuery
from openapi_client.model.tag_group_create_query_as_sub_resource import TagGroupCreateQueryAsSubResource
from openapi_client.model.tag_group_create_query_as_sub_resource_attributes import TagGroupCreateQueryAsSubResourceAttributes
from openapi_client.model.tag_group_update_query import TagGroupUpdateQuery
from openapi_client.model.tag_group_update_query_as_sub_resource import TagGroupUpdateQueryAsSubResource
from openapi_client.model.tag_group_update_query_as_sub_resource_attributes import TagGroupUpdateQueryAsSubResourceAttributes
from openapi_client.model.tag_update_query import TagUpdateQuery
from openapi_client.model.tag_update_query_as_sub_resource import TagUpdateQueryAsSubResource
from openapi_client.model.template_clone_query import TemplateCloneQuery
from openapi_client.model.template_clone_query_as_sub_resource import TemplateCloneQueryAsSubResource
from openapi_client.model.template_clone_query_as_sub_resource_attributes import TemplateCloneQueryAsSubResourceAttributes
from openapi_client.model.template_create_query import TemplateCreateQuery
from openapi_client.model.template_create_query_as_sub_resource import TemplateCreateQueryAsSubResource
from openapi_client.model.template_create_query_as_sub_resource_attributes import TemplateCreateQueryAsSubResourceAttributes
from openapi_client.model.template_update_query import TemplateUpdateQuery
from openapi_client.model.template_update_query_as_sub_resource import TemplateUpdateQueryAsSubResource
from openapi_client.model.template_update_query_as_sub_resource_attributes import TemplateUpdateQueryAsSubResourceAttributes
from openapi_client.model.throttled_schedule_options import ThrottledScheduleOptions
from openapi_client.model.tracking_options_sub_object import TrackingOptionsSubObject
from openapi_client.model.utm_params_sub_object import UTMParamsSubObject
from openapi_client.model.unsubscription_create_job_create_query import UnsubscriptionCreateJobCreateQuery
from openapi_client.model.unsubscription_create_job_create_query_as_sub_resource import UnsubscriptionCreateJobCreateQueryAsSubResource
from openapi_client.model.unsubscription_create_job_create_query_as_sub_resource_attributes import UnsubscriptionCreateJobCreateQueryAsSubResourceAttributes
from openapi_client.model.unsuppression_create_job_create_query import UnsuppressionCreateJobCreateQuery
from openapi_client.model.unsuppression_create_job_create_query_as_sub_resource import UnsuppressionCreateJobCreateQueryAsSubResource
from openapi_client.model.utm_param_info import UtmParamInfo
from openapi_client.model.v2_template_render_query import V2TemplateRenderQuery
from openapi_client.model.v2_template_render_query_as_sub_resource import V2TemplateRenderQueryAsSubResource
from openapi_client.model.v2_template_render_query_as_sub_resource_attributes import V2TemplateRenderQueryAsSubResourceAttributes
