# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCOUNTS = "Accounts"
    CAMPAIGNS = "Campaigns"
    CATALOGS = "Catalogs"
    COUPONS = "Coupons"
    DATA_PRIVACY = "Data Privacy"
    EVENTS = "Events"
    FLOWS = "Flows"
    IMAGES = "Images"
    LISTS = "Lists"
    METRICS = "Metrics"
    PROFILES = "Profiles"
    SEGMENTS = "Segments"
    TAGS = "Tags"
    TEMPLATES = "Templates"
