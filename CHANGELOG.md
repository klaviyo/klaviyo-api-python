# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

NOTE: For more granular API-specific changes, please see our [API Changelog](https://developers.klaviyo.com/en/docs/changelog_)

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
## [2.0.0] - 2023-04-06
### Added
- Profiles API now returns predictive analytics when calling `get_profile` and `get_profiles` by passing in `additional_fields_profile = ["predictive_analytics"]`.

### Changed
- Relationship endpoints that were previously grouped together are now split into related-resource-specific endpoints. This means that all relationship endpoints have new function names. 

### Migration Guide
- To migrate to this latest version, all calls to relationship endpoints need to be updated, as in the following example:
  - `get_campaign_relationships(campaign_id, "tags")` will become `get_campaign_relationships_tags(campaign_id)`.

## [1.3.1] - 2023-03-09
### Added
- Added `page_size` support for paging through endpoints that return profiles.

## [1.2.1] - 2023-02-23
### Fixed
- Fixed a bug that caused paging through events to periodically fail.

## [1.2.0] - 2023-02-23
### Added
- Added support for Campaigns (which were previously in our Beta API/SDKs).

### Changed
- Pagination for Flows changed from page offset to cursor.

## [1.1.0] - 2023-01-25
### Added
- Added the following endpoints (which were previously in our Beta API/SDKs):
  - Data Privacy
  - All Tags endpoints, as well as the following related resource-specific endpoints:
    - Get Flow Tags
    - Get List Tags
    - Get Segment Tags

## [1.0.0] - 2022-10-19
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
