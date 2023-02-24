# Changelog

NOTE: For more granular API-specific changes, please see our [API Changelog](https://developers.klaviyo.com/en/docs/changelog_)

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

