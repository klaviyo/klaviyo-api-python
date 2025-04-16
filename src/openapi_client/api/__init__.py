# flake8: noqa

from typing import TYPE_CHECKING

# non-runtime imports for type hints

if TYPE_CHECKING:
    from openapi_client.api.accounts_api import AccountsApi
    from openapi_client.api.campaigns_api import CampaignsApi
    from openapi_client.api.catalogs_api import CatalogsApi
    from openapi_client.api.coupons_api import CouponsApi
    from openapi_client.api.data_privacy_api import DataPrivacyApi
    from openapi_client.api.events_api import EventsApi
    from openapi_client.api.flows_api import FlowsApi
    from openapi_client.api.forms_api import FormsApi
    from openapi_client.api.images_api import ImagesApi
    from openapi_client.api.lists_api import ListsApi
    from openapi_client.api.metrics_api import MetricsApi
    from openapi_client.api.profiles_api import ProfilesApi
    from openapi_client.api.reporting_api import ReportingApi
    from openapi_client.api.reviews_api import ReviewsApi
    from openapi_client.api.segments_api import SegmentsApi
    from openapi_client.api.tags_api import TagsApi
    from openapi_client.api.templates_api import TemplatesApi
    from openapi_client.api.tracking_settings_api import TrackingSettingsApi
    from openapi_client.api.web_feeds_api import WebFeedsApi
    from openapi_client.api.webhooks_api import WebhooksApi
    


# lazily import apis into api package (see https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access)

object_origins = {
    # import apis into sdk package
    "AccountsApi": "openapi_client.api.accounts_api",
    "CampaignsApi": "openapi_client.api.campaigns_api",
    "CatalogsApi": "openapi_client.api.catalogs_api",
    "CouponsApi": "openapi_client.api.coupons_api",
    "DataPrivacyApi": "openapi_client.api.data_privacy_api",
    "EventsApi": "openapi_client.api.events_api",
    "FlowsApi": "openapi_client.api.flows_api",
    "FormsApi": "openapi_client.api.forms_api",
    "ImagesApi": "openapi_client.api.images_api",
    "ListsApi": "openapi_client.api.lists_api",
    "MetricsApi": "openapi_client.api.metrics_api",
    "ProfilesApi": "openapi_client.api.profiles_api",
    "ReportingApi": "openapi_client.api.reporting_api",
    "ReviewsApi": "openapi_client.api.reviews_api",
    "SegmentsApi": "openapi_client.api.segments_api",
    "TagsApi": "openapi_client.api.tags_api",
    "TemplatesApi": "openapi_client.api.templates_api",
    "TrackingSettingsApi": "openapi_client.api.tracking_settings_api",
    "WebFeedsApi": "openapi_client.api.web_feeds_api",
    "WebhooksApi": "openapi_client.api.webhooks_api",
    
}

def __getattr__(name):
    if name in object_origins:
        module = __import__(object_origins[name], None, None, [name])
        return getattr(module, name)
    return __import__(f"openapi_client.api.{name}")
