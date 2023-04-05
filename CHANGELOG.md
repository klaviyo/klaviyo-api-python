# Changelog

NOTE: For more granular API-specific changes, please see our [API Changelog](https://developers.klaviyo.com/en/docs/changelog_)

## 2.0.0
Breaking Changes:
  - Relationship endpoints that were previously grouped together are now split into related-resource-specific endpoints
  - To migrate to this latest version, all calls to relationship endpoints need to be updated, as in the following example:
    - `get_campaign_relationships(campaign_id, "tags")` will become `get_campaign_relationships_tags(campaign_id)`


Additive updates:
- Our Profiles API can now return predictive analytics when calling get_profile and get_profiles, by passing in the following keyword arg to those methods:
  - `additional_fields_profile = "predictive_analytics"`


## 1.3.0

### Added
- `page_size`:  you can now set page_size when paging through endpoints that return profiles

## 1.2.1

### Bug Fixes
- Fixed bug that caused paging through events to periodically fail

## 1.2.0

### Added
- Campaigns (which were previously in our Beta API/SDKs)

### Changes
- Flows
    - Pagination changed from page offset to cursor

## 1.1.0

  - Added the following endpoints (which were previously in our Beta API/SDKs):
    - Data Privacy
    - All Tags endpoints, as well as the following related resource-specific endpoints:
      - Get Flow Tags
      - Get List Tags
      - Get Segment Tags

## 1.0.0

  * Initial release

  Differences between 1.0.0 and BETA:

  - Namespace changes
    - Pypi package name: `klaviyo–sdk-beta` → `klaviyo-api`
    - Module name: `klaviyo_sdk_beta` → `klaviyo_api`
    - client name: `Client` → `KlaviyoAPI`
    - Client variable name in readme examples: `client` → `klaviyo`
    - Some functions have changed name
  - New resources and endpoints: see [API Changelog](https://developers.klaviyo.com/en/docs/changelog_) for full details

