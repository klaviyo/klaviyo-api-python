import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.accounts_api import AccountsApi
from openapi_client.apis.tags.campaigns_api import CampaignsApi
from openapi_client.apis.tags.catalogs_api import CatalogsApi
from openapi_client.apis.tags.coupons_api import CouponsApi
from openapi_client.apis.tags.data_privacy_api import DataPrivacyApi
from openapi_client.apis.tags.events_api import EventsApi
from openapi_client.apis.tags.flows_api import FlowsApi
from openapi_client.apis.tags.images_api import ImagesApi
from openapi_client.apis.tags.lists_api import ListsApi
from openapi_client.apis.tags.metrics_api import MetricsApi
from openapi_client.apis.tags.profiles_api import ProfilesApi
from openapi_client.apis.tags.segments_api import SegmentsApi
from openapi_client.apis.tags.tags_api import TagsApi
from openapi_client.apis.tags.templates_api import TemplatesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CATALOGS: CatalogsApi,
        TagValues.COUPONS: CouponsApi,
        TagValues.DATA_PRIVACY: DataPrivacyApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.LISTS: ListsApi,
        TagValues.METRICS: MetricsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TEMPLATES: TemplatesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CATALOGS: CatalogsApi,
        TagValues.COUPONS: CouponsApi,
        TagValues.DATA_PRIVACY: DataPrivacyApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.LISTS: ListsApi,
        TagValues.METRICS: MetricsApi,
        TagValues.PROFILES: ProfilesApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.TAGS: TagsApi,
        TagValues.TEMPLATES: TemplatesApi,
    }
)
