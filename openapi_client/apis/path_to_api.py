import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_accounts_ import ApiAccounts
from openapi_client.apis.paths.api_accounts_id_ import ApiAccountsId
from openapi_client.apis.paths.api_campaigns_ import ApiCampaigns
from openapi_client.apis.paths.api_campaigns_id_ import ApiCampaignsId
from openapi_client.apis.paths.api_campaign_messages_id_ import ApiCampaignMessagesId
from openapi_client.apis.paths.api_campaign_send_jobs_id_ import ApiCampaignSendJobsId
from openapi_client.apis.paths.api_campaign_recipient_estimation_jobs_id_ import ApiCampaignRecipientEstimationJobsId
from openapi_client.apis.paths.api_campaign_recipient_estimations_id_ import ApiCampaignRecipientEstimationsId
from openapi_client.apis.paths.api_campaign_clone_ import ApiCampaignClone
from openapi_client.apis.paths.api_campaign_message_assign_template_ import ApiCampaignMessageAssignTemplate
from openapi_client.apis.paths.api_campaign_send_jobs_ import ApiCampaignSendJobs
from openapi_client.apis.paths.api_campaign_recipient_estimation_jobs_ import ApiCampaignRecipientEstimationJobs
from openapi_client.apis.paths.api_campaign_messages_id_relationships_campaign_ import ApiCampaignMessagesIdRelationshipsCampaign
from openapi_client.apis.paths.api_campaign_messages_id_campaign_ import ApiCampaignMessagesIdCampaign
from openapi_client.apis.paths.api_campaign_messages_id_relationships_template_ import ApiCampaignMessagesIdRelationshipsTemplate
from openapi_client.apis.paths.api_campaign_messages_id_template_ import ApiCampaignMessagesIdTemplate
from openapi_client.apis.paths.api_campaigns_id_relationships_tags_ import ApiCampaignsIdRelationshipsTags
from openapi_client.apis.paths.api_campaigns_id_tags_ import ApiCampaignsIdTags
from openapi_client.apis.paths.api_campaigns_id_relationships_campaign_messages_ import ApiCampaignsIdRelationshipsCampaignMessages
from openapi_client.apis.paths.api_campaigns_id_campaign_messages_ import ApiCampaignsIdCampaignMessages
from openapi_client.apis.paths.api_catalog_items_ import ApiCatalogItems
from openapi_client.apis.paths.api_catalog_items_id_ import ApiCatalogItemsId
from openapi_client.apis.paths.api_catalog_variants_ import ApiCatalogVariants
from openapi_client.apis.paths.api_catalog_variants_id_ import ApiCatalogVariantsId
from openapi_client.apis.paths.api_catalog_categories_ import ApiCatalogCategories
from openapi_client.apis.paths.api_catalog_categories_id_ import ApiCatalogCategoriesId
from openapi_client.apis.paths.api_catalog_item_bulk_create_jobs_ import ApiCatalogItemBulkCreateJobs
from openapi_client.apis.paths.api_catalog_item_bulk_create_jobs_job_id_ import ApiCatalogItemBulkCreateJobsJobId
from openapi_client.apis.paths.api_catalog_item_bulk_update_jobs_ import ApiCatalogItemBulkUpdateJobs
from openapi_client.apis.paths.api_catalog_item_bulk_update_jobs_job_id_ import ApiCatalogItemBulkUpdateJobsJobId
from openapi_client.apis.paths.api_catalog_item_bulk_delete_jobs_ import ApiCatalogItemBulkDeleteJobs
from openapi_client.apis.paths.api_catalog_item_bulk_delete_jobs_job_id_ import ApiCatalogItemBulkDeleteJobsJobId
from openapi_client.apis.paths.api_catalog_variant_bulk_create_jobs_ import ApiCatalogVariantBulkCreateJobs
from openapi_client.apis.paths.api_catalog_variant_bulk_create_jobs_job_id_ import ApiCatalogVariantBulkCreateJobsJobId
from openapi_client.apis.paths.api_catalog_variant_bulk_update_jobs_ import ApiCatalogVariantBulkUpdateJobs
from openapi_client.apis.paths.api_catalog_variant_bulk_update_jobs_job_id_ import ApiCatalogVariantBulkUpdateJobsJobId
from openapi_client.apis.paths.api_catalog_variant_bulk_delete_jobs_ import ApiCatalogVariantBulkDeleteJobs
from openapi_client.apis.paths.api_catalog_variant_bulk_delete_jobs_job_id_ import ApiCatalogVariantBulkDeleteJobsJobId
from openapi_client.apis.paths.api_catalog_category_bulk_create_jobs_ import ApiCatalogCategoryBulkCreateJobs
from openapi_client.apis.paths.api_catalog_category_bulk_create_jobs_job_id_ import ApiCatalogCategoryBulkCreateJobsJobId
from openapi_client.apis.paths.api_catalog_category_bulk_update_jobs_ import ApiCatalogCategoryBulkUpdateJobs
from openapi_client.apis.paths.api_catalog_category_bulk_update_jobs_job_id_ import ApiCatalogCategoryBulkUpdateJobsJobId
from openapi_client.apis.paths.api_catalog_category_bulk_delete_jobs_ import ApiCatalogCategoryBulkDeleteJobs
from openapi_client.apis.paths.api_catalog_category_bulk_delete_jobs_job_id_ import ApiCatalogCategoryBulkDeleteJobsJobId
from openapi_client.apis.paths.api_back_in_stock_subscriptions_ import ApiBackInStockSubscriptions
from openapi_client.apis.paths.api_catalog_categories_id_items_ import ApiCatalogCategoriesIdItems
from openapi_client.apis.paths.api_catalog_items_id_variants_ import ApiCatalogItemsIdVariants
from openapi_client.apis.paths.api_catalog_items_id_categories_ import ApiCatalogItemsIdCategories
from openapi_client.apis.paths.api_catalog_categories_id_relationships_items_ import ApiCatalogCategoriesIdRelationshipsItems
from openapi_client.apis.paths.api_catalog_items_id_relationships_categories_ import ApiCatalogItemsIdRelationshipsCategories
from openapi_client.apis.paths.api_coupons_ import ApiCoupons
from openapi_client.apis.paths.api_coupons_id_ import ApiCouponsId
from openapi_client.apis.paths.api_coupon_codes_ import ApiCouponCodes
from openapi_client.apis.paths.api_coupon_codes_id_ import ApiCouponCodesId
from openapi_client.apis.paths.api_coupon_code_bulk_create_jobs_ import ApiCouponCodeBulkCreateJobs
from openapi_client.apis.paths.api_coupon_code_bulk_create_jobs_job_id_ import ApiCouponCodeBulkCreateJobsJobId
from openapi_client.apis.paths.api_coupon_codes_id_coupon_ import ApiCouponCodesIdCoupon
from openapi_client.apis.paths.api_coupon_codes_id_relationships_coupon_ import ApiCouponCodesIdRelationshipsCoupon
from openapi_client.apis.paths.api_coupons_id_coupon_codes_ import ApiCouponsIdCouponCodes
from openapi_client.apis.paths.api_coupons_id_relationships_coupon_codes_ import ApiCouponsIdRelationshipsCouponCodes
from openapi_client.apis.paths.api_data_privacy_deletion_jobs_ import ApiDataPrivacyDeletionJobs
from openapi_client.apis.paths.api_events_ import ApiEvents
from openapi_client.apis.paths.api_events_id_ import ApiEventsId
from openapi_client.apis.paths.api_events_id_metric_ import ApiEventsIdMetric
from openapi_client.apis.paths.api_events_id_profile_ import ApiEventsIdProfile
from openapi_client.apis.paths.api_events_id_relationships_metric_ import ApiEventsIdRelationshipsMetric
from openapi_client.apis.paths.api_events_id_relationships_profile_ import ApiEventsIdRelationshipsProfile
from openapi_client.apis.paths.api_flows_ import ApiFlows
from openapi_client.apis.paths.api_flows_id_ import ApiFlowsId
from openapi_client.apis.paths.api_flow_actions_id_ import ApiFlowActionsId
from openapi_client.apis.paths.api_flow_messages_id_ import ApiFlowMessagesId
from openapi_client.apis.paths.api_flows_id_flow_actions_ import ApiFlowsIdFlowActions
from openapi_client.apis.paths.api_flows_id_relationships_flow_actions_ import ApiFlowsIdRelationshipsFlowActions
from openapi_client.apis.paths.api_flows_id_relationships_tags_ import ApiFlowsIdRelationshipsTags
from openapi_client.apis.paths.api_flows_id_tags_ import ApiFlowsIdTags
from openapi_client.apis.paths.api_flow_actions_id_flow_ import ApiFlowActionsIdFlow
from openapi_client.apis.paths.api_flow_actions_id_relationships_flow_ import ApiFlowActionsIdRelationshipsFlow
from openapi_client.apis.paths.api_flow_actions_id_flow_messages_ import ApiFlowActionsIdFlowMessages
from openapi_client.apis.paths.api_flow_actions_id_relationships_flow_messages_ import ApiFlowActionsIdRelationshipsFlowMessages
from openapi_client.apis.paths.api_flow_messages_id_flow_action_ import ApiFlowMessagesIdFlowAction
from openapi_client.apis.paths.api_flow_messages_id_relationships_flow_action_ import ApiFlowMessagesIdRelationshipsFlowAction
from openapi_client.apis.paths.api_flow_messages_id_relationships_template_ import ApiFlowMessagesIdRelationshipsTemplate
from openapi_client.apis.paths.api_flow_messages_id_template_ import ApiFlowMessagesIdTemplate
from openapi_client.apis.paths.api_images_ import ApiImages
from openapi_client.apis.paths.api_images_id_ import ApiImagesId
from openapi_client.apis.paths.api_image_upload_ import ApiImageUpload
from openapi_client.apis.paths.api_lists_ import ApiLists
from openapi_client.apis.paths.api_lists_id_ import ApiListsId
from openapi_client.apis.paths.api_lists_id_relationships_tags_ import ApiListsIdRelationshipsTags
from openapi_client.apis.paths.api_lists_id_tags_ import ApiListsIdTags
from openapi_client.apis.paths.api_lists_id_relationships_profiles_ import ApiListsIdRelationshipsProfiles
from openapi_client.apis.paths.api_lists_id_profiles_ import ApiListsIdProfiles
from openapi_client.apis.paths.api_metrics_ import ApiMetrics
from openapi_client.apis.paths.api_metrics_id_ import ApiMetricsId
from openapi_client.apis.paths.api_metric_aggregates_ import ApiMetricAggregates
from openapi_client.apis.paths.api_profiles_ import ApiProfiles
from openapi_client.apis.paths.api_profiles_id_ import ApiProfilesId
from openapi_client.apis.paths.api_profile_merge_ import ApiProfileMerge
from openapi_client.apis.paths.api_profile_suppression_bulk_create_jobs_ import ApiProfileSuppressionBulkCreateJobs
from openapi_client.apis.paths.api_profile_suppression_bulk_delete_jobs_ import ApiProfileSuppressionBulkDeleteJobs
from openapi_client.apis.paths.api_profile_subscription_bulk_create_jobs_ import ApiProfileSubscriptionBulkCreateJobs
from openapi_client.apis.paths.api_profile_subscription_bulk_delete_jobs_ import ApiProfileSubscriptionBulkDeleteJobs
from openapi_client.apis.paths.api_push_tokens_ import ApiPushTokens
from openapi_client.apis.paths.api_profiles_id_lists_ import ApiProfilesIdLists
from openapi_client.apis.paths.api_profiles_id_relationships_lists_ import ApiProfilesIdRelationshipsLists
from openapi_client.apis.paths.api_profiles_id_segments_ import ApiProfilesIdSegments
from openapi_client.apis.paths.api_profiles_id_relationships_segments_ import ApiProfilesIdRelationshipsSegments
from openapi_client.apis.paths.api_segments_ import ApiSegments
from openapi_client.apis.paths.api_segments_id_ import ApiSegmentsId
from openapi_client.apis.paths.api_segments_id_relationships_tags_ import ApiSegmentsIdRelationshipsTags
from openapi_client.apis.paths.api_segments_id_tags_ import ApiSegmentsIdTags
from openapi_client.apis.paths.api_segments_id_relationships_profiles_ import ApiSegmentsIdRelationshipsProfiles
from openapi_client.apis.paths.api_segments_id_profiles_ import ApiSegmentsIdProfiles
from openapi_client.apis.paths.api_tags_ import ApiTags
from openapi_client.apis.paths.api_tags_id_ import ApiTagsId
from openapi_client.apis.paths.api_tag_groups_ import ApiTagGroups
from openapi_client.apis.paths.api_tag_groups_id_ import ApiTagGroupsId
from openapi_client.apis.paths.api_tags_id_relationships_flows_ import ApiTagsIdRelationshipsFlows
from openapi_client.apis.paths.api_tags_id_relationships_campaigns_ import ApiTagsIdRelationshipsCampaigns
from openapi_client.apis.paths.api_tags_id_relationships_lists_ import ApiTagsIdRelationshipsLists
from openapi_client.apis.paths.api_tags_id_relationships_segments_ import ApiTagsIdRelationshipsSegments
from openapi_client.apis.paths.api_tags_id_relationships_tag_group_ import ApiTagsIdRelationshipsTagGroup
from openapi_client.apis.paths.api_tag_groups_id_relationships_tags_ import ApiTagGroupsIdRelationshipsTags
from openapi_client.apis.paths.api_tags_id_tag_group_ import ApiTagsIdTagGroup
from openapi_client.apis.paths.api_tag_groups_id_tags_ import ApiTagGroupsIdTags
from openapi_client.apis.paths.api_templates_ import ApiTemplates
from openapi_client.apis.paths.api_templates_id_ import ApiTemplatesId
from openapi_client.apis.paths.api_template_render_ import ApiTemplateRender
from openapi_client.apis.paths.api_template_clone_ import ApiTemplateClone

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ACCOUNTS_: ApiAccounts,
        PathValues.API_ACCOUNTS_ID_: ApiAccountsId,
        PathValues.API_CAMPAIGNS_: ApiCampaigns,
        PathValues.API_CAMPAIGNS_ID_: ApiCampaignsId,
        PathValues.API_CAMPAIGNMESSAGES_ID_: ApiCampaignMessagesId,
        PathValues.API_CAMPAIGNSENDJOBS_ID_: ApiCampaignSendJobsId,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONJOBS_ID_: ApiCampaignRecipientEstimationJobsId,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONS_ID_: ApiCampaignRecipientEstimationsId,
        PathValues.API_CAMPAIGNCLONE_: ApiCampaignClone,
        PathValues.API_CAMPAIGNMESSAGEASSIGNTEMPLATE_: ApiCampaignMessageAssignTemplate,
        PathValues.API_CAMPAIGNSENDJOBS_: ApiCampaignSendJobs,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONJOBS_: ApiCampaignRecipientEstimationJobs,
        PathValues.API_CAMPAIGNMESSAGES_ID_RELATIONSHIPS_CAMPAIGN_: ApiCampaignMessagesIdRelationshipsCampaign,
        PathValues.API_CAMPAIGNMESSAGES_ID_CAMPAIGN_: ApiCampaignMessagesIdCampaign,
        PathValues.API_CAMPAIGNMESSAGES_ID_RELATIONSHIPS_TEMPLATE_: ApiCampaignMessagesIdRelationshipsTemplate,
        PathValues.API_CAMPAIGNMESSAGES_ID_TEMPLATE_: ApiCampaignMessagesIdTemplate,
        PathValues.API_CAMPAIGNS_ID_RELATIONSHIPS_TAGS_: ApiCampaignsIdRelationshipsTags,
        PathValues.API_CAMPAIGNS_ID_TAGS_: ApiCampaignsIdTags,
        PathValues.API_CAMPAIGNS_ID_RELATIONSHIPS_CAMPAIGNMESSAGES_: ApiCampaignsIdRelationshipsCampaignMessages,
        PathValues.API_CAMPAIGNS_ID_CAMPAIGNMESSAGES_: ApiCampaignsIdCampaignMessages,
        PathValues.API_CATALOGITEMS_: ApiCatalogItems,
        PathValues.API_CATALOGITEMS_ID_: ApiCatalogItemsId,
        PathValues.API_CATALOGVARIANTS_: ApiCatalogVariants,
        PathValues.API_CATALOGVARIANTS_ID_: ApiCatalogVariantsId,
        PathValues.API_CATALOGCATEGORIES_: ApiCatalogCategories,
        PathValues.API_CATALOGCATEGORIES_ID_: ApiCatalogCategoriesId,
        PathValues.API_CATALOGITEMBULKCREATEJOBS_: ApiCatalogItemBulkCreateJobs,
        PathValues.API_CATALOGITEMBULKCREATEJOBS_JOB_ID_: ApiCatalogItemBulkCreateJobsJobId,
        PathValues.API_CATALOGITEMBULKUPDATEJOBS_: ApiCatalogItemBulkUpdateJobs,
        PathValues.API_CATALOGITEMBULKUPDATEJOBS_JOB_ID_: ApiCatalogItemBulkUpdateJobsJobId,
        PathValues.API_CATALOGITEMBULKDELETEJOBS_: ApiCatalogItemBulkDeleteJobs,
        PathValues.API_CATALOGITEMBULKDELETEJOBS_JOB_ID_: ApiCatalogItemBulkDeleteJobsJobId,
        PathValues.API_CATALOGVARIANTBULKCREATEJOBS_: ApiCatalogVariantBulkCreateJobs,
        PathValues.API_CATALOGVARIANTBULKCREATEJOBS_JOB_ID_: ApiCatalogVariantBulkCreateJobsJobId,
        PathValues.API_CATALOGVARIANTBULKUPDATEJOBS_: ApiCatalogVariantBulkUpdateJobs,
        PathValues.API_CATALOGVARIANTBULKUPDATEJOBS_JOB_ID_: ApiCatalogVariantBulkUpdateJobsJobId,
        PathValues.API_CATALOGVARIANTBULKDELETEJOBS_: ApiCatalogVariantBulkDeleteJobs,
        PathValues.API_CATALOGVARIANTBULKDELETEJOBS_JOB_ID_: ApiCatalogVariantBulkDeleteJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKCREATEJOBS_: ApiCatalogCategoryBulkCreateJobs,
        PathValues.API_CATALOGCATEGORYBULKCREATEJOBS_JOB_ID_: ApiCatalogCategoryBulkCreateJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKUPDATEJOBS_: ApiCatalogCategoryBulkUpdateJobs,
        PathValues.API_CATALOGCATEGORYBULKUPDATEJOBS_JOB_ID_: ApiCatalogCategoryBulkUpdateJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKDELETEJOBS_: ApiCatalogCategoryBulkDeleteJobs,
        PathValues.API_CATALOGCATEGORYBULKDELETEJOBS_JOB_ID_: ApiCatalogCategoryBulkDeleteJobsJobId,
        PathValues.API_BACKINSTOCKSUBSCRIPTIONS_: ApiBackInStockSubscriptions,
        PathValues.API_CATALOGCATEGORIES_ID_ITEMS_: ApiCatalogCategoriesIdItems,
        PathValues.API_CATALOGITEMS_ID_VARIANTS_: ApiCatalogItemsIdVariants,
        PathValues.API_CATALOGITEMS_ID_CATEGORIES_: ApiCatalogItemsIdCategories,
        PathValues.API_CATALOGCATEGORIES_ID_RELATIONSHIPS_ITEMS_: ApiCatalogCategoriesIdRelationshipsItems,
        PathValues.API_CATALOGITEMS_ID_RELATIONSHIPS_CATEGORIES_: ApiCatalogItemsIdRelationshipsCategories,
        PathValues.API_COUPONS_: ApiCoupons,
        PathValues.API_COUPONS_ID_: ApiCouponsId,
        PathValues.API_COUPONCODES_: ApiCouponCodes,
        PathValues.API_COUPONCODES_ID_: ApiCouponCodesId,
        PathValues.API_COUPONCODEBULKCREATEJOBS_: ApiCouponCodeBulkCreateJobs,
        PathValues.API_COUPONCODEBULKCREATEJOBS_JOB_ID_: ApiCouponCodeBulkCreateJobsJobId,
        PathValues.API_COUPONCODES_ID_COUPON_: ApiCouponCodesIdCoupon,
        PathValues.API_COUPONCODES_ID_RELATIONSHIPS_COUPON_: ApiCouponCodesIdRelationshipsCoupon,
        PathValues.API_COUPONS_ID_COUPONCODES_: ApiCouponsIdCouponCodes,
        PathValues.API_COUPONS_ID_RELATIONSHIPS_COUPONCODES_: ApiCouponsIdRelationshipsCouponCodes,
        PathValues.API_DATAPRIVACYDELETIONJOBS_: ApiDataPrivacyDeletionJobs,
        PathValues.API_EVENTS_: ApiEvents,
        PathValues.API_EVENTS_ID_: ApiEventsId,
        PathValues.API_EVENTS_ID_METRIC_: ApiEventsIdMetric,
        PathValues.API_EVENTS_ID_PROFILE_: ApiEventsIdProfile,
        PathValues.API_EVENTS_ID_RELATIONSHIPS_METRIC_: ApiEventsIdRelationshipsMetric,
        PathValues.API_EVENTS_ID_RELATIONSHIPS_PROFILE_: ApiEventsIdRelationshipsProfile,
        PathValues.API_FLOWS_: ApiFlows,
        PathValues.API_FLOWS_ID_: ApiFlowsId,
        PathValues.API_FLOWACTIONS_ID_: ApiFlowActionsId,
        PathValues.API_FLOWMESSAGES_ID_: ApiFlowMessagesId,
        PathValues.API_FLOWS_ID_FLOWACTIONS_: ApiFlowsIdFlowActions,
        PathValues.API_FLOWS_ID_RELATIONSHIPS_FLOWACTIONS_: ApiFlowsIdRelationshipsFlowActions,
        PathValues.API_FLOWS_ID_RELATIONSHIPS_TAGS_: ApiFlowsIdRelationshipsTags,
        PathValues.API_FLOWS_ID_TAGS_: ApiFlowsIdTags,
        PathValues.API_FLOWACTIONS_ID_FLOW_: ApiFlowActionsIdFlow,
        PathValues.API_FLOWACTIONS_ID_RELATIONSHIPS_FLOW_: ApiFlowActionsIdRelationshipsFlow,
        PathValues.API_FLOWACTIONS_ID_FLOWMESSAGES_: ApiFlowActionsIdFlowMessages,
        PathValues.API_FLOWACTIONS_ID_RELATIONSHIPS_FLOWMESSAGES_: ApiFlowActionsIdRelationshipsFlowMessages,
        PathValues.API_FLOWMESSAGES_ID_FLOWACTION_: ApiFlowMessagesIdFlowAction,
        PathValues.API_FLOWMESSAGES_ID_RELATIONSHIPS_FLOWACTION_: ApiFlowMessagesIdRelationshipsFlowAction,
        PathValues.API_FLOWMESSAGES_ID_RELATIONSHIPS_TEMPLATE_: ApiFlowMessagesIdRelationshipsTemplate,
        PathValues.API_FLOWMESSAGES_ID_TEMPLATE_: ApiFlowMessagesIdTemplate,
        PathValues.API_IMAGES_: ApiImages,
        PathValues.API_IMAGES_ID_: ApiImagesId,
        PathValues.API_IMAGEUPLOAD_: ApiImageUpload,
        PathValues.API_LISTS_: ApiLists,
        PathValues.API_LISTS_ID_: ApiListsId,
        PathValues.API_LISTS_ID_RELATIONSHIPS_TAGS_: ApiListsIdRelationshipsTags,
        PathValues.API_LISTS_ID_TAGS_: ApiListsIdTags,
        PathValues.API_LISTS_ID_RELATIONSHIPS_PROFILES_: ApiListsIdRelationshipsProfiles,
        PathValues.API_LISTS_ID_PROFILES_: ApiListsIdProfiles,
        PathValues.API_METRICS_: ApiMetrics,
        PathValues.API_METRICS_ID_: ApiMetricsId,
        PathValues.API_METRICAGGREGATES_: ApiMetricAggregates,
        PathValues.API_PROFILES_: ApiProfiles,
        PathValues.API_PROFILES_ID_: ApiProfilesId,
        PathValues.API_PROFILEMERGE_: ApiProfileMerge,
        PathValues.API_PROFILESUPPRESSIONBULKCREATEJOBS_: ApiProfileSuppressionBulkCreateJobs,
        PathValues.API_PROFILESUPPRESSIONBULKDELETEJOBS_: ApiProfileSuppressionBulkDeleteJobs,
        PathValues.API_PROFILESUBSCRIPTIONBULKCREATEJOBS_: ApiProfileSubscriptionBulkCreateJobs,
        PathValues.API_PROFILESUBSCRIPTIONBULKDELETEJOBS_: ApiProfileSubscriptionBulkDeleteJobs,
        PathValues.API_PUSHTOKENS_: ApiPushTokens,
        PathValues.API_PROFILES_ID_LISTS_: ApiProfilesIdLists,
        PathValues.API_PROFILES_ID_RELATIONSHIPS_LISTS_: ApiProfilesIdRelationshipsLists,
        PathValues.API_PROFILES_ID_SEGMENTS_: ApiProfilesIdSegments,
        PathValues.API_PROFILES_ID_RELATIONSHIPS_SEGMENTS_: ApiProfilesIdRelationshipsSegments,
        PathValues.API_SEGMENTS_: ApiSegments,
        PathValues.API_SEGMENTS_ID_: ApiSegmentsId,
        PathValues.API_SEGMENTS_ID_RELATIONSHIPS_TAGS_: ApiSegmentsIdRelationshipsTags,
        PathValues.API_SEGMENTS_ID_TAGS_: ApiSegmentsIdTags,
        PathValues.API_SEGMENTS_ID_RELATIONSHIPS_PROFILES_: ApiSegmentsIdRelationshipsProfiles,
        PathValues.API_SEGMENTS_ID_PROFILES_: ApiSegmentsIdProfiles,
        PathValues.API_TAGS_: ApiTags,
        PathValues.API_TAGS_ID_: ApiTagsId,
        PathValues.API_TAGGROUPS_: ApiTagGroups,
        PathValues.API_TAGGROUPS_ID_: ApiTagGroupsId,
        PathValues.API_TAGS_ID_RELATIONSHIPS_FLOWS_: ApiTagsIdRelationshipsFlows,
        PathValues.API_TAGS_ID_RELATIONSHIPS_CAMPAIGNS_: ApiTagsIdRelationshipsCampaigns,
        PathValues.API_TAGS_ID_RELATIONSHIPS_LISTS_: ApiTagsIdRelationshipsLists,
        PathValues.API_TAGS_ID_RELATIONSHIPS_SEGMENTS_: ApiTagsIdRelationshipsSegments,
        PathValues.API_TAGS_ID_RELATIONSHIPS_TAGGROUP_: ApiTagsIdRelationshipsTagGroup,
        PathValues.API_TAGGROUPS_ID_RELATIONSHIPS_TAGS_: ApiTagGroupsIdRelationshipsTags,
        PathValues.API_TAGS_ID_TAGGROUP_: ApiTagsIdTagGroup,
        PathValues.API_TAGGROUPS_ID_TAGS_: ApiTagGroupsIdTags,
        PathValues.API_TEMPLATES_: ApiTemplates,
        PathValues.API_TEMPLATES_ID_: ApiTemplatesId,
        PathValues.API_TEMPLATERENDER_: ApiTemplateRender,
        PathValues.API_TEMPLATECLONE_: ApiTemplateClone,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ACCOUNTS_: ApiAccounts,
        PathValues.API_ACCOUNTS_ID_: ApiAccountsId,
        PathValues.API_CAMPAIGNS_: ApiCampaigns,
        PathValues.API_CAMPAIGNS_ID_: ApiCampaignsId,
        PathValues.API_CAMPAIGNMESSAGES_ID_: ApiCampaignMessagesId,
        PathValues.API_CAMPAIGNSENDJOBS_ID_: ApiCampaignSendJobsId,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONJOBS_ID_: ApiCampaignRecipientEstimationJobsId,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONS_ID_: ApiCampaignRecipientEstimationsId,
        PathValues.API_CAMPAIGNCLONE_: ApiCampaignClone,
        PathValues.API_CAMPAIGNMESSAGEASSIGNTEMPLATE_: ApiCampaignMessageAssignTemplate,
        PathValues.API_CAMPAIGNSENDJOBS_: ApiCampaignSendJobs,
        PathValues.API_CAMPAIGNRECIPIENTESTIMATIONJOBS_: ApiCampaignRecipientEstimationJobs,
        PathValues.API_CAMPAIGNMESSAGES_ID_RELATIONSHIPS_CAMPAIGN_: ApiCampaignMessagesIdRelationshipsCampaign,
        PathValues.API_CAMPAIGNMESSAGES_ID_CAMPAIGN_: ApiCampaignMessagesIdCampaign,
        PathValues.API_CAMPAIGNMESSAGES_ID_RELATIONSHIPS_TEMPLATE_: ApiCampaignMessagesIdRelationshipsTemplate,
        PathValues.API_CAMPAIGNMESSAGES_ID_TEMPLATE_: ApiCampaignMessagesIdTemplate,
        PathValues.API_CAMPAIGNS_ID_RELATIONSHIPS_TAGS_: ApiCampaignsIdRelationshipsTags,
        PathValues.API_CAMPAIGNS_ID_TAGS_: ApiCampaignsIdTags,
        PathValues.API_CAMPAIGNS_ID_RELATIONSHIPS_CAMPAIGNMESSAGES_: ApiCampaignsIdRelationshipsCampaignMessages,
        PathValues.API_CAMPAIGNS_ID_CAMPAIGNMESSAGES_: ApiCampaignsIdCampaignMessages,
        PathValues.API_CATALOGITEMS_: ApiCatalogItems,
        PathValues.API_CATALOGITEMS_ID_: ApiCatalogItemsId,
        PathValues.API_CATALOGVARIANTS_: ApiCatalogVariants,
        PathValues.API_CATALOGVARIANTS_ID_: ApiCatalogVariantsId,
        PathValues.API_CATALOGCATEGORIES_: ApiCatalogCategories,
        PathValues.API_CATALOGCATEGORIES_ID_: ApiCatalogCategoriesId,
        PathValues.API_CATALOGITEMBULKCREATEJOBS_: ApiCatalogItemBulkCreateJobs,
        PathValues.API_CATALOGITEMBULKCREATEJOBS_JOB_ID_: ApiCatalogItemBulkCreateJobsJobId,
        PathValues.API_CATALOGITEMBULKUPDATEJOBS_: ApiCatalogItemBulkUpdateJobs,
        PathValues.API_CATALOGITEMBULKUPDATEJOBS_JOB_ID_: ApiCatalogItemBulkUpdateJobsJobId,
        PathValues.API_CATALOGITEMBULKDELETEJOBS_: ApiCatalogItemBulkDeleteJobs,
        PathValues.API_CATALOGITEMBULKDELETEJOBS_JOB_ID_: ApiCatalogItemBulkDeleteJobsJobId,
        PathValues.API_CATALOGVARIANTBULKCREATEJOBS_: ApiCatalogVariantBulkCreateJobs,
        PathValues.API_CATALOGVARIANTBULKCREATEJOBS_JOB_ID_: ApiCatalogVariantBulkCreateJobsJobId,
        PathValues.API_CATALOGVARIANTBULKUPDATEJOBS_: ApiCatalogVariantBulkUpdateJobs,
        PathValues.API_CATALOGVARIANTBULKUPDATEJOBS_JOB_ID_: ApiCatalogVariantBulkUpdateJobsJobId,
        PathValues.API_CATALOGVARIANTBULKDELETEJOBS_: ApiCatalogVariantBulkDeleteJobs,
        PathValues.API_CATALOGVARIANTBULKDELETEJOBS_JOB_ID_: ApiCatalogVariantBulkDeleteJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKCREATEJOBS_: ApiCatalogCategoryBulkCreateJobs,
        PathValues.API_CATALOGCATEGORYBULKCREATEJOBS_JOB_ID_: ApiCatalogCategoryBulkCreateJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKUPDATEJOBS_: ApiCatalogCategoryBulkUpdateJobs,
        PathValues.API_CATALOGCATEGORYBULKUPDATEJOBS_JOB_ID_: ApiCatalogCategoryBulkUpdateJobsJobId,
        PathValues.API_CATALOGCATEGORYBULKDELETEJOBS_: ApiCatalogCategoryBulkDeleteJobs,
        PathValues.API_CATALOGCATEGORYBULKDELETEJOBS_JOB_ID_: ApiCatalogCategoryBulkDeleteJobsJobId,
        PathValues.API_BACKINSTOCKSUBSCRIPTIONS_: ApiBackInStockSubscriptions,
        PathValues.API_CATALOGCATEGORIES_ID_ITEMS_: ApiCatalogCategoriesIdItems,
        PathValues.API_CATALOGITEMS_ID_VARIANTS_: ApiCatalogItemsIdVariants,
        PathValues.API_CATALOGITEMS_ID_CATEGORIES_: ApiCatalogItemsIdCategories,
        PathValues.API_CATALOGCATEGORIES_ID_RELATIONSHIPS_ITEMS_: ApiCatalogCategoriesIdRelationshipsItems,
        PathValues.API_CATALOGITEMS_ID_RELATIONSHIPS_CATEGORIES_: ApiCatalogItemsIdRelationshipsCategories,
        PathValues.API_COUPONS_: ApiCoupons,
        PathValues.API_COUPONS_ID_: ApiCouponsId,
        PathValues.API_COUPONCODES_: ApiCouponCodes,
        PathValues.API_COUPONCODES_ID_: ApiCouponCodesId,
        PathValues.API_COUPONCODEBULKCREATEJOBS_: ApiCouponCodeBulkCreateJobs,
        PathValues.API_COUPONCODEBULKCREATEJOBS_JOB_ID_: ApiCouponCodeBulkCreateJobsJobId,
        PathValues.API_COUPONCODES_ID_COUPON_: ApiCouponCodesIdCoupon,
        PathValues.API_COUPONCODES_ID_RELATIONSHIPS_COUPON_: ApiCouponCodesIdRelationshipsCoupon,
        PathValues.API_COUPONS_ID_COUPONCODES_: ApiCouponsIdCouponCodes,
        PathValues.API_COUPONS_ID_RELATIONSHIPS_COUPONCODES_: ApiCouponsIdRelationshipsCouponCodes,
        PathValues.API_DATAPRIVACYDELETIONJOBS_: ApiDataPrivacyDeletionJobs,
        PathValues.API_EVENTS_: ApiEvents,
        PathValues.API_EVENTS_ID_: ApiEventsId,
        PathValues.API_EVENTS_ID_METRIC_: ApiEventsIdMetric,
        PathValues.API_EVENTS_ID_PROFILE_: ApiEventsIdProfile,
        PathValues.API_EVENTS_ID_RELATIONSHIPS_METRIC_: ApiEventsIdRelationshipsMetric,
        PathValues.API_EVENTS_ID_RELATIONSHIPS_PROFILE_: ApiEventsIdRelationshipsProfile,
        PathValues.API_FLOWS_: ApiFlows,
        PathValues.API_FLOWS_ID_: ApiFlowsId,
        PathValues.API_FLOWACTIONS_ID_: ApiFlowActionsId,
        PathValues.API_FLOWMESSAGES_ID_: ApiFlowMessagesId,
        PathValues.API_FLOWS_ID_FLOWACTIONS_: ApiFlowsIdFlowActions,
        PathValues.API_FLOWS_ID_RELATIONSHIPS_FLOWACTIONS_: ApiFlowsIdRelationshipsFlowActions,
        PathValues.API_FLOWS_ID_RELATIONSHIPS_TAGS_: ApiFlowsIdRelationshipsTags,
        PathValues.API_FLOWS_ID_TAGS_: ApiFlowsIdTags,
        PathValues.API_FLOWACTIONS_ID_FLOW_: ApiFlowActionsIdFlow,
        PathValues.API_FLOWACTIONS_ID_RELATIONSHIPS_FLOW_: ApiFlowActionsIdRelationshipsFlow,
        PathValues.API_FLOWACTIONS_ID_FLOWMESSAGES_: ApiFlowActionsIdFlowMessages,
        PathValues.API_FLOWACTIONS_ID_RELATIONSHIPS_FLOWMESSAGES_: ApiFlowActionsIdRelationshipsFlowMessages,
        PathValues.API_FLOWMESSAGES_ID_FLOWACTION_: ApiFlowMessagesIdFlowAction,
        PathValues.API_FLOWMESSAGES_ID_RELATIONSHIPS_FLOWACTION_: ApiFlowMessagesIdRelationshipsFlowAction,
        PathValues.API_FLOWMESSAGES_ID_RELATIONSHIPS_TEMPLATE_: ApiFlowMessagesIdRelationshipsTemplate,
        PathValues.API_FLOWMESSAGES_ID_TEMPLATE_: ApiFlowMessagesIdTemplate,
        PathValues.API_IMAGES_: ApiImages,
        PathValues.API_IMAGES_ID_: ApiImagesId,
        PathValues.API_IMAGEUPLOAD_: ApiImageUpload,
        PathValues.API_LISTS_: ApiLists,
        PathValues.API_LISTS_ID_: ApiListsId,
        PathValues.API_LISTS_ID_RELATIONSHIPS_TAGS_: ApiListsIdRelationshipsTags,
        PathValues.API_LISTS_ID_TAGS_: ApiListsIdTags,
        PathValues.API_LISTS_ID_RELATIONSHIPS_PROFILES_: ApiListsIdRelationshipsProfiles,
        PathValues.API_LISTS_ID_PROFILES_: ApiListsIdProfiles,
        PathValues.API_METRICS_: ApiMetrics,
        PathValues.API_METRICS_ID_: ApiMetricsId,
        PathValues.API_METRICAGGREGATES_: ApiMetricAggregates,
        PathValues.API_PROFILES_: ApiProfiles,
        PathValues.API_PROFILES_ID_: ApiProfilesId,
        PathValues.API_PROFILEMERGE_: ApiProfileMerge,
        PathValues.API_PROFILESUPPRESSIONBULKCREATEJOBS_: ApiProfileSuppressionBulkCreateJobs,
        PathValues.API_PROFILESUPPRESSIONBULKDELETEJOBS_: ApiProfileSuppressionBulkDeleteJobs,
        PathValues.API_PROFILESUBSCRIPTIONBULKCREATEJOBS_: ApiProfileSubscriptionBulkCreateJobs,
        PathValues.API_PROFILESUBSCRIPTIONBULKDELETEJOBS_: ApiProfileSubscriptionBulkDeleteJobs,
        PathValues.API_PUSHTOKENS_: ApiPushTokens,
        PathValues.API_PROFILES_ID_LISTS_: ApiProfilesIdLists,
        PathValues.API_PROFILES_ID_RELATIONSHIPS_LISTS_: ApiProfilesIdRelationshipsLists,
        PathValues.API_PROFILES_ID_SEGMENTS_: ApiProfilesIdSegments,
        PathValues.API_PROFILES_ID_RELATIONSHIPS_SEGMENTS_: ApiProfilesIdRelationshipsSegments,
        PathValues.API_SEGMENTS_: ApiSegments,
        PathValues.API_SEGMENTS_ID_: ApiSegmentsId,
        PathValues.API_SEGMENTS_ID_RELATIONSHIPS_TAGS_: ApiSegmentsIdRelationshipsTags,
        PathValues.API_SEGMENTS_ID_TAGS_: ApiSegmentsIdTags,
        PathValues.API_SEGMENTS_ID_RELATIONSHIPS_PROFILES_: ApiSegmentsIdRelationshipsProfiles,
        PathValues.API_SEGMENTS_ID_PROFILES_: ApiSegmentsIdProfiles,
        PathValues.API_TAGS_: ApiTags,
        PathValues.API_TAGS_ID_: ApiTagsId,
        PathValues.API_TAGGROUPS_: ApiTagGroups,
        PathValues.API_TAGGROUPS_ID_: ApiTagGroupsId,
        PathValues.API_TAGS_ID_RELATIONSHIPS_FLOWS_: ApiTagsIdRelationshipsFlows,
        PathValues.API_TAGS_ID_RELATIONSHIPS_CAMPAIGNS_: ApiTagsIdRelationshipsCampaigns,
        PathValues.API_TAGS_ID_RELATIONSHIPS_LISTS_: ApiTagsIdRelationshipsLists,
        PathValues.API_TAGS_ID_RELATIONSHIPS_SEGMENTS_: ApiTagsIdRelationshipsSegments,
        PathValues.API_TAGS_ID_RELATIONSHIPS_TAGGROUP_: ApiTagsIdRelationshipsTagGroup,
        PathValues.API_TAGGROUPS_ID_RELATIONSHIPS_TAGS_: ApiTagGroupsIdRelationshipsTags,
        PathValues.API_TAGS_ID_TAGGROUP_: ApiTagsIdTagGroup,
        PathValues.API_TAGGROUPS_ID_TAGS_: ApiTagGroupsIdTags,
        PathValues.API_TEMPLATES_: ApiTemplates,
        PathValues.API_TEMPLATES_ID_: ApiTemplatesId,
        PathValues.API_TEMPLATERENDER_: ApiTemplateRender,
        PathValues.API_TEMPLATECLONE_: ApiTemplateClone,
    }
)
