# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

NOTE: For more granular API-specific changes, please see our [API Changelog](https://developers.klaviyo.com/en/docs/changelog_)

## [13.0.0] - 2024-07-15
### Fixed
- **Breaking**
	- Fixed types in several DTO classes


## [12.0.0] - 2024-07-15
### Added
- Added several method aliases based on previous operation IDs
### Fixed
- **Breaking**
	- Removed incorrect `links` property from several DTO classes. From issue https://github.com/klaviyo/klaviyo-api-python/issues/64


## [11.0.1] - 2024-07-15
### Fixed
- Typing error when using `additional_fields_profile=['subscriptions']` on `get_profiles`. From issue https://github.com/klaviyo/klaviyo-api-python/issues/61


## [11.0.0] Typed SDK - revision 2024-07-15

### Added
- Typed Responses (Breaking change)
    - By default, all API methods will return a type representing the response payload instead of dictionary, as was the case in previous versions of this SDK. Using the typed response, you can access fields of a response using dot notation, like so:
      ```python
      from klaviyo_api import KlaviyoAPI

      client = KlaviyoAPI(
        api_key,
        max_delay=0,
        max_retries=0
      )

      profiles = client.Profiles.get_profiles()
      profile_id = profiles.data[0].id
      profile = client.Profiles.get_profile(profile_id)
      profile_id = profile.data.id
      profile_email = profile.data.attributes.email

      print(type(profile).__name__) # prints GetProfileResponseCompoundDocument
      ```
      The class used in this example is found [here](src/openapi_client/models/get_profile_response_collection_compound_document.py). 

      This is a breaking change, as response objects will now require dot notation to access their fields versus the subscriptable access method used for dictionaries, i.e. `profile.data.id` vs `profile['data']['id']`. We have provided a [backwards compatibility strategy](#backwards-compatibility) to smooth the transition from dictionary responses to typed responses.

      #### Backwards Compatibility
      To maintain backwards compatibility with previous versions of this SDK, we have added an `options` argument that allows you to continue using dictionaries as response values. There are two ways to use this `options` argument:
        ```python
        from klaviyo_api import KlaviyoAPI
        from openapi_client.api_arg_options import USE_DICTIONARY_FOR_RESPONSE_DATA

        client = KlaviyoAPI(
            api_key,
            max_delay=0,
            max_retries=0
        )


        # 1: Passing options to an individual API method
        profiles = client.Profiles.get_profiles(options= {
              USE_DICTIONARY_FOR_RESPONSE_DATA: True
          })
        profile_id = profiles["data"][0]['id']
        profile_email = profiles["data"][0]['attributes']['email']

        # 2: Passing options to API Client
        dictionary_client = KlaviyoAPI(
          api_key,
          max_delay=0,
          max_retries=0,
          options={USE_DICTIONARY_FOR_RESPONSE_DATA : True}
        )
        profiles_ = dictionary_client.Profiles.get_profiles()
        profile_0_id = profiles_["data"][0]['id']

        profile_0 = dictionary_client.Profiles.get_profile(id=profile_0_id)
        profile_0_email = profile_0["data"]['attributes']['email']
        ```
        The first way will only return a dictionary for that specific `get_profiles` call. The second makes it so that all API methods called using `dictionary_client` will return dictionaries as responses.

  - Some API methods still return response data that is not fully typed. See the [Untyped Response Data for Specific APIs](README.md#untyped-response-data-for-specific-apis) in the README for more details.
- Filter Builder - A new class to help construct filter query parameters.
  ```python
  old_date = datetime.datetime(2023, 8, 15, 12, 30, 0, 0, tzinfo=datetime.timezone.utc)
  f = FilterBuilder()
  f.any("email", ["sarah.mason@klaviyo-demo.com", "sm@klaviyo-demo.com"])
  f.greater_than("created", old_date)

  # f.build() returns 'any(email,["sarah.mason@klaviyo-demo.com","sm@klaviyo-demo.com"]),greater-than(created,2023-08-15T12:30:00+00:00)'
  profile_response = client.Profiles.get_profiles(filter=f.build())

  # You can also chain FilterBuilder methods
  f = FilterBuilder()
  filters = f.any("email", ["sarah.mason@klaviyo-demo.com", "sm@klaviyo-demo.com"]).greater_than("created", date).build()
  assert filters == "any(email,['sarah.mason@klaviyo-demo.com','sm@klaviyo-demo.com']),greater-than(created,2023-08-15T12:30:00+00:00)"
  ```


## [10.0.0] - revision 2024-07-15

### Added

 - Forms API
  - New `klaviyo.Forms` class with methods to get forms, form versions and relationships
 - Webhooks API
  - new `klaviyo.Webooks` class containing CRUD operations for webhooks

### Changed
 - `klaviyo.Profiles.subscribe()`
  - added `historical_import` flag for importing historically consented profiles can now be optionally supplied in the payload for the Subscribe Profiles endpoint.
  - When using this flag, a consented_at date must be provided and must be in the past.


## [9.0.0] - revision 2024-06-15

### Added
  - Segments Api
    - New create segment endpoint `SegmentsApi.createSegment()`.
    - New delete segment endpoint `SegementsApi.deleteSegment()`.
    - Updated exisiting segments endpoints to include the segment definition
    - For more information, see our [Segments API overview](https://developers.klaviyo.com/en/reference/segments_api_overview).

  - Flows Api
    - New delete flows endpoint `FlowsApi.deleteFlow()`


## [8.0.1] - revision 2024-05-15

### Added

- Fixes issue where `filter` query params for any API call were being duplicated on request send. See issue: https://github.com/klaviyo/klaviyo-api-python/issues/51


## [8.0.0] - revision 2024-05-15

### Added

- Bulk Create Events API with 
	- We have added support for creating events in bulk via the EventsApi.bulkCreateEvents method
- Create multiple events for new and existing profiles and/or update profile properties in a single API call. For more information, see our [Events API overview](https://developers.klaviyo.com/en/reference/events_api_overview).

### Changed

  - Accounts API
	- `Accounts.get_account` and `Accounts.get_accounts` have been updated to return the account's locale, e.g.     `"en-US"`.

  - **Breaking**
    - Subscribe API Synchronous Validation Improved
        - To provide better feedback for handling SMS subscriptions, we’ve added improved validation behavior to ProfilesApi.subscribeProfiles method. In prior revisions, such requests may appear as 202s but will fail to update SMS consent. To handle this issue, 400 validation errors are returned for the following cases
            1. If a profile is subscribed to SMS marketing and [age-gating is enabled](https://help.klaviyo.com/hc/en-us/articles/4408311712667) but age_gated_date_of_birth is not provided, or the DOB does not meet the region's requirements.
            2. If the account does not have a sending number in the phone number’s region.
            3. If the phone number is in a region not supported by Klaviyo.
            4. If consented_at is set and the list or global setting is double opt-in.
    - Pydantic V2
        - This SDK now uses Pydantic V2. This may cause some compatibility issues if your source code depends on Pydantic V1.
    - Renamed Fields in SDK
        - As of the 2024-05-15 release, some models fields are named differently than they appear in API documentation. These fields are
            - `datetime`: renamed to `datetime_`
            - `date`: renamed to `date_`

            This is to manage compatibility with Pydantic v2. An example of this can be seen in [StaticScheduleOptions](src/openapi_client/models/static_schedule_options.py).

            ```python
            class StaticScheduleOptions(BaseModel):
                """
                StaticScheduleOptions
                """ # noqa: E501
                datetime_: datetime = Field(description="The time to send at", alias="datetime")

            schedule_options = StaticScheduleOptions(datetime_=datetime.datetime.strptime("2024-05-19T00:00:00+00:00", "%Y-%m-%dT%H:%M:%S%z")
            print(schedule_options.datetime_)
            ```


## [7.0.0] - revision 2024-02-15

### Added: 

- New `ReportingApi` allows you to request campaign and flow performance data that you can view in the Klaviyo UI.

- `campaign_values_query`
  - Request campaign analytics data, for example, a campaign performance report on the open rate over the past 30 days.

- `flow_values_query`
  - Request flow analytics data, for example, a flow performance report on the revenue per recipient value over the past 3 months.

- `flow_series_query`
  - Fetch flow series data for a specific interval and timeframe, for example, a flow performance report on weekly click rates  over the past 12 months.


- New `ProfilesApi` endpoint allows you to create or update a profile with a set of profile attributes.

  - `create_or_update_profile`
    - This endpoint operates synchronously and offers an upsert pattern similar to the [v1/v2 Identify API](https://developers.klaviyo.com/en/docs/apis_comparison_chart).

### Changed:
	
- Removed the $attribution field from event_properties in get_event and  get_events (breaking change).
	
  - To include this data in your request, add include=attributions to your request.


## [6.1.0] - revision 2023-12-15

### Added

#### New Endpoints: Bulk Profile Imports

We have added the following endpoints to enable bulk profile imports:
- `Profiles.spawn_bulk_profile_import_job`
- `Profiles.get_bulk_profile_import_job`
- `Profiles.get_bulk_profile_import_jobs`
- `Profiles.get_bulk_profile_import_job_lists`
- `Profiles.get_bulk_profile_import_job_profiles`
- `Profiles.get_bulk_profile_import_job_import_errors`
- `Profiles.get_bulk_profile_import_job_relationships_profiles`
- `Profiles.get_bulk_profile_import_job_relationships_lists`

### Changed

#### Relationships field of `Profiles.subscribe_profiles` payload is now optional

When using `Profiles.subscribe_profiles`, the `relationships` field of the payload is now optional (see [Profiles.subscribe_profiles reference](https://developers.klaviyo.com/en/reference/subscribe_profiles) for details).

## [6.0.1] - revision 2023-10-15

### Fixed

#### Patched a bug that was causing query_metric_aggregates to return None upon success

A bug was introduced in version 5.0.0 until this patch, that resulted in this SDK specifically returning None upon success for the following operation [Metrics.query_metrics_aggregates](https://developers.klaviyo.com/en/reference/query_metric_aggregates).

## [6.0.0] - revision 2023-10-15

### Added

#### Support for returning list suppressions via the [/profiles endpoint](https://developers.klaviyo.com/en/reference/get_profiles)

We now support filtering on list suppression with the get profiles endpoint, which brings us to parity with v2 list suppression endpoint that was the previously recommended solution.

Rules for suppression [filtering](https://developers.klaviyo.com/en/docs/filtering_):  

- You may not mix-and-match list and global filters  
- You may only specify a single date filter  
- You may or may not specify a reason  
- You must specify a list_id to filter on any list suppression properties

Examples:

- To return profiles who were suppressed after a certain date:  
  `filter="greater-than(subscriptions.email.marketing.suppression.timestamp,2023-03-01T01:00:00Z)"`
- To return profiles who were suppressed from a specific list after a certain date:  
  `filter="greater-than(subscriptions.email.marketing.list_suppressions.timestamp,2023-03-01T01:00:00Z),equals(subscriptions.email.marketing.list_suppressions.list_id,\"LIST_ID\")"`
- To return all profiles who were suppressed for a specific reason after a certain date:  
  `filter="greater-than(subscriptions.email.marketing.suppression.timestamp,2023-03-01T01:00:00Z),equals(subscriptions.email.marketing.suppression.reason,\"user_suppressed\")"`

#### Optionally retrieve subscription status on Get List Profiles, Get Segment Profiles, Get Event Profile

Now you can retrieve subscription status on any endpoint that returns profiles, including Get List Profiles, Get Segment Profiles and Get Event Profile.  Use `additional_fields_profile="subscriptions"` on these endpoints to include subscription information.

### Changed

#### Subscription object not returned by default on Get Profile / Get Profiles

The subscription object is no longer returned by default with get profile(s) requests. However, it can be included by adding the  `additional_fields_profile="subscriptions"` to the request. This change will allow us to provide a more performant experience when making requests to Get Profiles without including the subscriptions object.

#### Profile Subscription Fields Renamed

In the interest of providing more clarity and information on the subscription object, we have renamed several fields, and added several as well. This will provide more context on a contact's subscriptions and consent, as well as boolean fields to see who you can or cannot message.

For SMSMarketing:

- `timestamp` is now `consent_timestamp`
- `last_updated` is a new field that mirrors `consent_timestamp`
- `can_receive_sms_marketing` is a new field which is `True` if the profile is consented for SMS 

For EmailMarketing:

- `timestamp` is now `consent_timestamp`
- `can_receive_email_marketing` is True if the profile does not have a global suppression
- `suppressions` is now `suppression`
- `last_updated` is a new field that is the most recent of all the dates on the object

## [5.2.0] - revision 2023-09-15

### Added

- `Images` API
  - We now support the following operations to work with images:
    - `get_image`
    - `get_images`
    - `update_image`
    - `upload_image_from_file`
    - `upload_image_from_url`
- `Coupons` API
  - We now support CRUD operations for both Coupons and Coupon Codes
  - Check out [Coupons API guide](https://developers.klaviyo.com/en/docs/use_klaviyos_coupons_api) for more information.
- Additional filtering/sorting option for getting profiles from `Lists` and `Segments`: `joined_group_at`
- New profile merge endpoint: `Profiles.merge_profiles`
- Increased the maximum page size limit for `Lists.get_list_relationships_profiles` and `Segments.get_segment_relationships_profiles` to 1000

## [5.1.2] - revision 2023-08-15

### Added

- override `api_key` with OAuth access token by setting client `access_token` keyword arg


## [5.1.1] - revision 2023-08-15

### Fixed

- Fixed a bug that was impacting the `unset` functionality for `update_profile`

## [5.1.0] - revision 2023-08-15

### Added

- Flow Message Template endpoints:
  - You can now retrieve the templates associated with flow messages using `Flows.get_flow_message_template()` or `Flows.get_flow_message_relationships_template()`. You can also include the template HTML for a flow message using `Flows.get_flow_message(id, include=['template'])`.
- Create or Update Push Token endpoint:
  - We have added an endpoint to create or update push tokens, `Profiles.create_push_token()`. This endpoint can be used to migrate profiles and their push tokens from another platform to Klaviyo. If you’re looking to register push tokens from users’ devices, please use our [mobile SDKs](https://developers.klaviyo.com/en/docs/sdk_overview#mobile-sdks).

## [5.0.0] - revision 2023-07-15

### Changed

- To override the client-level `api_key` for a specific request, you will now need to use the following new keyword arg: `_request_auth`
  - previously, this keyword arg was called `api_key`

### Fixed

- Fixed errors that were occurring on requests using oneOf schemas

## [4.0.0] - revision 2023-07-15

### Added

- Back-In-stock APIs
  - We have added support for subscribing profiles to back-in-stock notifications, for both email and SMS, using the new [create_back_in_stock_subscription](./README.md#create-back-in-stock-subscription) endpoint.  
- New functionality to Campaigns API
  - CRUD support for SMS campaigns is now available
  - You can now also retrieve all messages for a campaign to determine performance data on campaigns where you’re running A/B tests
    - To support this functionality, we introduced a relationship between [campaigns and campaign messages](./README.md#get-campaign-relationships-campaign-messages), and between [campaign messages and templates](./README.md#get-campaign-message-relationships-template)


### Changed

- Relationship Standardization
  - We are making a number of changes across endpoints to standardize how we handle [relationships](https://developers.klaviyo.com/en/docs/relationships_) in our APIs and leverage consistently typed objects across endpoints. For example, you can create a profile in our APIs in the same shape, regardless of whether you’re calling the profiles endpoint or the events endpoint.
  - The changes include:
    - Updating 1:1 relationships to use singular tense and an object (instead of plural and an array) 
      - example: for [get_flow_action](./README.md#get-flow-action), if you want to use the `include` param, you would set `include=` to `"flow"` (instead of `"flows"`)
    - Moving related object IDs from the attributes payload to relationships
      - example: The format for the [body](https://developers.klaviyo.com/en/reference/create_tag) of [create_tag](./README.md#create-tag) has changed, with `tag_group_id` previously at `data.attributes.tag_group_id` being removed and replaced by a `data` object containing `type`+`id` and located at `data.relationships.tag-group.data`.
    - Specifying a relationship between two Klaviyo objects to allow for improved consistency and greater interoperability across endpoints 
      - example: for [create_event](./README.md#create-event), you can now create/update a profile for an event in the same way you would when using the profiles API directly
  - NOTE: The examples for the above relationship changes are illustrative, not comprehensive. For a complete list of ALL the endpoints that have changed and exactly how, please refer to our latest [API Changelog](https://developers.klaviyo.com/en/docs/changelog_#revision-2023-07-15)
- For [get_campaigns](./README.md#get-campaigns) endpoint, `filter` param is now required, to, at minimum, filter on `messages.channel`


### Removed

- We removed the `company_id` from the response for [get_template](./README.md#get-template) and [get_templates](./README.md#get-templates). If you need to obtain the company ID / public API key for an account, please use the [Accounts API](./README.md#accounts).

## [3.0.0] - revision 2023-06-15

### Added

- Accounts API is now available, this will allow you to access information about the Klaviyo account associated with your API key.
  - `get_accounts`
  - `get_account`
  
**Note:** You will need to generate a new API key with either the `Accounts` scope enabled or `Full Access` to use these endpoints.

### Changed

- The names of positional arguments have changed from `[resource_type]_id` to `id` (i.e. `campaign_id` to `id`) for some relationship endpoints. If keyword arguments were used instead of positional arguments for `[resource_type]_id` you might need to slightly refactor the code.

### Removed

- All `client` endpoint:
  - `create_client_event`
  - `create_client_profile`
  - `create_client_subscription`

## [2.0.0] - revision 2023-04-06

### Added

- Profiles API now returns predictive analytics when calling `get_profile` and `get_profiles` by passing in `additional_fields_profile = ["predictive_analytics"]`.

### Changed

- Relationship endpoints that were previously grouped together are now split into related-resource-specific endpoints. This means that all relationship endpoints have new function names. 

### Migration Guide

- To migrate to this latest version, all calls to relationship endpoints need to be updated, as in the following example:
  - `get_campaign_relationships(campaign_id, "tags")` will become `get_campaign_relationships_tags(campaign_id)`.

## [1.3.1] - revision 2023-03-09

### Added

- Added `page_size` support for paging through endpoints that return profiles.

## [1.2.1] - revision 2023-02-23

### Fixed
- Fixed a bug that caused paging through events to periodically fail.

## [1.2.0] - revision 2023-02-23

### Added

- Added support for Campaigns (which were previously in our Beta API/SDKs).

### Changed

- Pagination for Flows changed from page offset to cursor.

## [1.1.0] - revision 2023-01-25

### Added

- Added the following endpoints (which were previously in our Beta API/SDKs):
  - Data Privacy
  - All Tags endpoints, as well as the following related resource-specific endpoints:
    - Get Flow Tags
    - Get List Tags
    - Get Segment Tags

## [1.0.0] - revision 2022-10-19

### Added

- Initial release

### Changed

- Namespace changes:
  - Pypi package name: `klaviyo–sdk-beta` → `klaviyo-api`
  - Module name: `klaviyo_sdk_beta` → `klaviyo_api`
  - client name: `Client` → `KlaviyoAPI`
  - Client variable name in readme examples: `client` → `klaviyo`
  - Some functions have changed name
- New resources and endpoints: see [API Changelog](https://developers.klaviyo.com/en/docs/changelog_) for full details
