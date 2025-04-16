# Klaviyo Python SDK

- SDK version: 19.0.0
- API revision: 2025-04-15

## Table of Contents
<!-- TOC -->
  * [Helpful Resources](#helpful-resources)
  * [Design & Approach](#design--approach)
  * [Organization](#organization)
  * [Installation](#installation)
  * [Usage Example](#usage-example)
    * [To instantiate the client](#to-instantiate-the-client)
    * [Example request](#example-request)
    * [Use Case Examples](#use-case-examples)
      * [How to use filtering, sorting, and spare fieldset JSON API features](#how-to-use-filtering-sorting-and-spare-fieldset-json-api-features)
      * [How to filter based on datetime](#how-to-filter-based-on-datetime)
      * [How to use pagination and the page[size] param](#how-to-use-pagination-and-the-pagesize-param)
      * [How to add additional information to your API response via additional-fields and the `includes` parameter](#how-to-add-additional-information-to-your-api-response-via-additional-fields-and-the-includes-parameter)
      * [How to use our relationship endpoints to see related resources](#how-to-use-our-relationship-endpoints-to-see-related-resources)
      * [How to see what Klaviyo objects are associated with a specific tag](#how-to-see-what-klaviyo-objects-are-associated-with-a-specific-tag)
      * [Uploading Image From File](#uploading-image-from-file)
  * [Error Handling](#error-handling)
  * [Important Notes](#important-notes)
* [Comprehensive List of Operations & Parameters](#comprehensive-list-of-operations--parameters)
  * [Accounts](#accounts)
  * [Campaigns](#campaigns)
  * [Catalogs](#catalogs)
  * [Coupons](#coupons)
  * [Data_Privacy](#dataprivacy)
  * [Events](#events)
  * [Flows](#flows)
  * [Images](#images)
  * [Lists](#lists)
  * [Metrics](#metrics)
  * [Profiles](#profiles)
  * [Reporting](#reporting)
  * [Segments](#segments)
  * [Tags](#tags)
  * [Templates](#templates)
* [Appendix](#appendix)
  * [Global Keyword Args](#global-keyword-args)
  * [Refresher on catching exceptions:](#refresher-on-catching-exceptions)
  * [Parameters & Arguments](#parameters--arguments)
  * [Namespace](#namespace)
  * [Renamed Fields](#renamed-fields)
  * [Filter Builder](#filter-builder)
  * [Typed Responses](#typed-responses)
    * [Backwards Compatibility](#backwards-compatibility)
  * [Untyped Response Data for Specific APIs](#untyped-response-data-for-specific-apis)
  * [Lazy Imports](#lazy-imports)
<!-- TOC -->

## Helpful Resources

- [API Reference](https://developers.klaviyo.com/en/v2025-04-15/reference)
- [API Guides](https://developers.klaviyo.com/en/v2025-04-15/docs)
- [Postman Workspace](https://www.postman.com/klaviyo/workspace/klaviyo-developers)
- [Interactive Guide (Jupyter Notebook)](https://github.com/klaviyo-labs/klaviyo-api-guides)

## Design & Approach

This SDK is a thin wrapper around our API. See our API Reference for full documentation on behavior.

This SDK exactly mirrors the organization and naming convention of the above language-agnostic resources, with a few namespace changes to make it Pythonic (details in Appendix).

## Organization

This SDK is organized into the following resources:



- Accounts



- Campaigns



- Catalogs



- Coupons



- Data_Privacy



- Events



- Flows



- Forms



- Images



- Lists



- Metrics



- Profiles



- Reporting



- Reviews



- Segments



- Tags



- Templates



- Tracking_Settings



- Web_Feeds



- Webhooks



## Installation

You can install this library using [our pip package here](https://pypi.org/project/klaviyo-api/).

Depending on your system configuration, you will need to run *one* of the following shell commands:

```bash
pip install klaviyo-api
```

OR 

```bash
pip3 install klaviyo-api
```

## Usage Example

### To instantiate the client

NOTE: 
* The SDK retries on resolvable errors, namely: rate limits (common) and server errors (rare).
* The keyword arguments define some advanced settings; the example is populated with the default values.
* `max_delay` denotes delay (in seconds) for a single retry attempt.

```python
from klaviyo_api import KlaviyoAPI

klaviyo = KlaviyoAPI("YOUR_API_KEY_HERE", max_delay=60, max_retries=3, test_host=None)
```

### Example request

```python
klaviyo.Metrics.get_metrics() 
```

### Use Case Examples

#### How to use filtering, sorting, and spare fieldset JSON API features

**Use Case**: Get events associated with a specific metric, then return just the event properties sorted by oldest to newest datetime.

```python
klaviyo.Events.get_events(
    fields_event=['event_properties'], 
    filter="equals(metric_id,\"aBc123\")", 
    sort='-datetime'
    )
```

#### How to filter based on datetime

**Use Case**: Get profiles that have been updated between two datetimes.

```python
klaviyo.Profiles.get_profiles(
    filter='less-than(updated,2023-04-26T00:00:00Z),greater-than(updated,2023-04-19T00:00:00Z)'
    )
```

#### How to use pagination and the page[size] param

**Use Case**: Use cursor-based pagination to get the next 20 profile records.

```python
klaviyo.Profiles.get_profiles(
    page_cursor="https://a.klaviyo.com/api/profiles/?page%5Bcursor%5D=bmV4dDo6aWQ6OjAxRjNaWk5ITlRYMUtFVEhQMzJTUzRBN0ZY",
    page_size=20
)
```

NOTE: This page cursor value is exactly what is returned in the `self`/`next`/`prev` response values

#### How to add additional information to your API response via additional-fields and the `includes` parameter

**Use Case**: Get a specific profile, return an additional predictive analytics field, and also return the list objects associated with the profile.

```python
klaviyo.Profiles.get_profile(
    '01GDDKASAP8TKDDA2GRZDSVP4H', 
    additional_fields_profile=['predictive_analytics'], 
    include=['lists']
)
```

#### How to use our relationship endpoints to see related resources

**Use Case**: Get all list memberships for a profile with the given `profile_id`.

```python
klaviyo.Profiles.get_profile_relationships_lists('01GDDKASAP8TKDDA2GRZDSVP4H')
```

#### How to see what Klaviyo objects are associated with a specific tag

**Use Case**: Get all campaigns associated with the given `tag_id`.

```python
klaviyo.Tags.get_tag_relationships_campaigns('9c8db7a0-5ab5-4e3c-9a37-a3224fd14382')
```

#### Uploading Image From File

When using `Images.upload_image_from_file(file, name=name)`, `file`` can be either a file path string OR a bytearray.

NOTE: when file is a bytearray, you will need to use the optional `name` parameter to specify the file name, else name will default to `unnamed_image_from_python_sdk`

*as a file path*
```python
filepath = '/path/to/image.png'
klaviyo.Images.upload_image_from_file(file, name=name)
```

*as a bytearray*
```python
filepath = '/path/to/image.png'
with open(filepath, 'rb') as f:
    file = f.read()
klaviyo.Images.upload_image_from_file(file, name=name)
```

## Error Handling

This SDK throws an `ApiException` error when the server returns a non-`2XX` response. 

An `ApiException` consists of the following attributes:

* `status` : `int`
* `reason` : `str`
* `body` : `bytes`
    * this can be decoded into a native python dictionary as follows:
        ```python
        # to decode to a dictionary
        import json
        BODY_DICT = json.loads(YOUR_EXCEPTION.body)

        # to decode to a string
        BODY_STRING = YOUR_EXCEPTION.body.decode('utf-8')
        ```
* `headers` : [class 'urllib3._collections.HTTPHeaderDict'](https://urllib3.readthedocs.io/en/stable/user-guide.html?highlight=httpheaderdict#response-content)
    * This can be interacted with as a normal dictionary:
        * ex:
            ```
            date = YOUR_EXCEPTION.headers['Date']
            keys = YOUR_EXCEPTION.headers.keys()
            values = YOUR_EXCEPTION.headers.values()
            ```

## Important Notes

- The main difference between this SDK and the language-agnostic API Docs that the below endpoints link to is that this SDK automatically adds the `revision` header corresponding to the SDK version.
- Organization: Resource groups and operation_ids are listed below in alphabetical order, first by Resource name, then by **OpenAPI Summary**. Operation summaries are those listed in the right side bar of the [API Reference](https://developers.klaviyo.com/en/v2025-04-15/reference/get_events).
- For example values / data types, as well as whether parameters are required/optional, please reference the corresponding API Reference link.
- Some keyword args may potentially be required for the API call to succeed, the linked API docs are the source of truth regarding which keyword params are required.
- JSON payloads should be passed in as native python dictionaries.
- You can override the client private key by passing in an optional `_request_auth` keyword arg to any API call that takes a private key. As a reminder: do NOT do this client-side/onsite.

# Comprehensive List of Operations & Parameters





## Accounts

#### [Get Account](https://developers.klaviyo.com/en/v2025-04-15/reference/get_account)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_account | List[str]

klaviyo.Accounts.get_account(id, fields_account=fields_account)
```




#### [Get Accounts](https://developers.klaviyo.com/en/v2025-04-15/reference/get_accounts)

```python

## Keyword Arguments

# fields_account | List[str]

klaviyo.Accounts.get_accounts(fields_account=fields_account)
```






## Campaigns

#### [Assign Template to Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/assign_template_to_campaign_message)

```python
## Positional Arguments

# body | dict

klaviyo.Campaigns.assign_template_to_campaign_message(body)
```
##### Method alias:
```python
klaviyo.Campaigns.create_campaign_message_assign_template(body)
```




#### [Cancel Campaign Send](https://developers.klaviyo.com/en/v2025-04-15/reference/cancel_campaign_send)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Campaigns.cancel_campaign_send(id, body)
```
##### Method alias:
```python
klaviyo.Campaigns.update_campaign_send_job(id, body)
```




#### [Create Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/create_campaign)

```python
## Positional Arguments

# body | dict

klaviyo.Campaigns.create_campaign(body)
```




#### [Create Campaign Clone](https://developers.klaviyo.com/en/v2025-04-15/reference/create_campaign_clone)

```python
## Positional Arguments

# body | dict

klaviyo.Campaigns.create_campaign_clone(body)
```
##### Method alias:
```python
klaviyo.Campaigns.clone_campaign(body)
```




#### [Delete Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_campaign)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.delete_campaign(id)
```




#### [Get Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_message | List[str]
# fields_campaign | List[str]
# fields_tag | List[str]
# include | List[str]

klaviyo.Campaigns.get_campaign(id, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_tag=fields_tag, include=include)
```




#### [Get Campaign for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_for_campaign_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign | List[str]

klaviyo.Campaigns.get_campaign_for_campaign_message(id, fields_campaign=fields_campaign)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_campaign(id, fields_campaign=fields_campaign)
```




#### [Get Campaign ID for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_id_for_campaign_message)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.get_campaign_id_for_campaign_message(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_relationships_campaign(id)
```




#### [Get Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_message | List[str]
# fields_campaign | List[str]
# fields_image | List[str]
# fields_template | List[str]
# include | List[str]

klaviyo.Campaigns.get_campaign_message(id, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_image=fields_image, fields_template=fields_template, include=include)
```




#### [Get Campaign Recipient Estimation](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_recipient_estimation)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_recipient_estimation | List[str]

klaviyo.Campaigns.get_campaign_recipient_estimation(id, fields_campaign_recipient_estimation=fields_campaign_recipient_estimation)
```




#### [Get Campaign Recipient Estimation Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_recipient_estimation_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_recipient_estimation_job | List[str]

klaviyo.Campaigns.get_campaign_recipient_estimation_job(id, fields_campaign_recipient_estimation_job=fields_campaign_recipient_estimation_job)
```




#### [Get Campaign Send Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_send_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_send_job | List[str]

klaviyo.Campaigns.get_campaign_send_job(id, fields_campaign_send_job=fields_campaign_send_job)
```




#### [Get Campaigns](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaigns)

```python
## Positional Arguments

# filter | str

## Keyword Arguments

# fields_campaign_message | List[str]
# fields_campaign | List[str]
# fields_tag | List[str]
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Campaigns.get_campaigns(filter, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_tag=fields_tag, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Image for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_image_for_campaign_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_image | List[str]

klaviyo.Campaigns.get_image_for_campaign_message(id, fields_image=fields_image)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_image(id, fields_image=fields_image)
```




#### [Get Image ID for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_image_id_for_campaign_message)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.get_image_id_for_campaign_message(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_relationships_image(id)
```




#### [Get Message IDs for Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/get_message_ids_for_campaign)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.get_message_ids_for_campaign(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_relationships_campaign_messages(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_relationships_messages(id)
```




#### [Get Messages for Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/get_messages_for_campaign)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_campaign_message | List[str]
# fields_campaign | List[str]
# fields_image | List[str]
# fields_template | List[str]
# include | List[str]

klaviyo.Campaigns.get_messages_for_campaign(id, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_image=fields_image, fields_template=fields_template, include=include)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_campaign_messages(id, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_image=fields_image, fields_template=fields_template, include=include)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_messages(id, fields_campaign_message=fields_campaign_message, fields_campaign=fields_campaign, fields_image=fields_image, fields_template=fields_template, include=include)
```




#### [Get Tag IDs for Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_ids_for_campaign)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.get_tag_ids_for_campaign(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_relationships_tags(id)
```




#### [Get Tags for Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags_for_campaign)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | List[str]

klaviyo.Campaigns.get_tags_for_campaign(id, fields_tag=fields_tag)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_tags(id, fields_tag=fields_tag)
```




#### [Get Template for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_template_for_campaign_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_template | List[str]

klaviyo.Campaigns.get_template_for_campaign_message(id, fields_template=fields_template)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_template(id, fields_template=fields_template)
```




#### [Get Template ID for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_template_id_for_campaign_message)

```python
## Positional Arguments

# id | str

klaviyo.Campaigns.get_template_id_for_campaign_message(id)
```
##### Method alias:
```python
klaviyo.Campaigns.get_campaign_message_relationships_template(id)
```




#### [Refresh Campaign Recipient Estimation](https://developers.klaviyo.com/en/v2025-04-15/reference/refresh_campaign_recipient_estimation)

```python
## Positional Arguments

# body | dict

klaviyo.Campaigns.refresh_campaign_recipient_estimation(body)
```
##### Method alias:
```python
klaviyo.Campaigns.create_campaign_recipient_estimation_job(body)
```




#### [Send Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/send_campaign)

```python
## Positional Arguments

# body | dict

klaviyo.Campaigns.send_campaign(body)
```
##### Method alias:
```python
klaviyo.Campaigns.create_campaign_send_job(body)
```




#### [Update Campaign](https://developers.klaviyo.com/en/v2025-04-15/reference/update_campaign)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Campaigns.update_campaign(id, body)
```




#### [Update Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/update_campaign_message)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Campaigns.update_campaign_message(id, body)
```




#### [Update Image for Campaign Message](https://developers.klaviyo.com/en/v2025-04-15/reference/update_image_for_campaign_message)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Campaigns.update_image_for_campaign_message(id, body)
```
##### Method alias:
```python
klaviyo.Campaigns.update_campaign_message_relationships_image(id, body)
```






## Catalogs

#### [Add Categories to Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/add_categories_to_catalog_item)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.add_categories_to_catalog_item(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.add_category_to_catalog_item(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_item_relationships_category(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_item_relationships_categories(id, body)
```




#### [Add Items to Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/add_items_to_catalog_category)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.add_items_to_catalog_category(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_category_relationships_item(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_category_relationships_items(id, body)
```




#### [Bulk Create Catalog Categories](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_create_catalog_categories)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_create_catalog_categories(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_create_categories_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_category_bulk_create_job(body)
```




#### [Bulk Create Catalog Items](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_create_catalog_items)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_create_catalog_items(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_create_items_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_item_bulk_create_job(body)
```




#### [Bulk Create Catalog Variants](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_create_catalog_variants)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_create_catalog_variants(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_create_variants_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_variant_bulk_create_job(body)
```




#### [Bulk Delete Catalog Categories](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_delete_catalog_categories)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_delete_catalog_categories(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_delete_categories_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_category_bulk_delete_job(body)
```




#### [Bulk Delete Catalog Items](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_delete_catalog_items)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_delete_catalog_items(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_delete_items_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_item_bulk_delete_job(body)
```




#### [Bulk Delete Catalog Variants](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_delete_catalog_variants)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_delete_catalog_variants(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_delete_variants_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_variant_bulk_delete_job(body)
```




#### [Bulk Update Catalog Categories](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_update_catalog_categories)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_update_catalog_categories(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_update_categories_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_category_bulk_update_job(body)
```




#### [Bulk Update Catalog Items](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_update_catalog_items)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_update_catalog_items(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_update_items_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_item_bulk_update_job(body)
```




#### [Bulk Update Catalog Variants](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_update_catalog_variants)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.bulk_update_catalog_variants(body)
```
##### Method alias:
```python
klaviyo.Catalogs.spawn_update_variants_job(body)
```
##### Method alias:
```python
klaviyo.Catalogs.create_catalog_variant_bulk_update_job(body)
```




#### [Create Back In Stock Subscription](https://developers.klaviyo.com/en/v2025-04-15/reference/create_back_in_stock_subscription)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_back_in_stock_subscription(body)
```




#### [Create Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/create_catalog_category)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_category(body)
```




#### [Create Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/create_catalog_item)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_item(body)
```




#### [Create Catalog Variant](https://developers.klaviyo.com/en/v2025-04-15/reference/create_catalog_variant)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_variant(body)
```




#### [Delete Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_catalog_category)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_category(id)
```




#### [Delete Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_catalog_item)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_item(id)
```




#### [Delete Catalog Variant](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_catalog_variant)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_variant(id)
```




#### [Get Bulk Create Catalog Items Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_catalog_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_create_job | List[str]
# fields_catalog_item | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_create_catalog_items_job(job_id, fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, fields_catalog_item=fields_catalog_item, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_items_job(job_id, fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, fields_catalog_item=fields_catalog_item, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_create_job(job_id, fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, fields_catalog_item=fields_catalog_item, include=include)
```




#### [Get Bulk Create Catalog Items Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_catalog_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_create_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_create_catalog_items_jobs(fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_items_jobs(fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_create_jobs(fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Create Categories Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_create_job | List[str]
# fields_catalog_category | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_create_categories_job(job_id, fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, fields_catalog_category=fields_catalog_category, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_categories_job(job_id, fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, fields_catalog_category=fields_catalog_category, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_create_job(job_id, fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, fields_catalog_category=fields_catalog_category, include=include)
```




#### [Get Bulk Create Categories Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_create_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_create_categories_jobs(fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_categories_jobs(fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_create_jobs(fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Create Variants Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_create_job | List[str]
# fields_catalog_variant | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_create_variants_job(job_id, fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, fields_catalog_variant=fields_catalog_variant, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_variants_job(job_id, fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, fields_catalog_variant=fields_catalog_variant, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_create_job(job_id, fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, fields_catalog_variant=fields_catalog_variant, include=include)
```




#### [Get Bulk Create Variants Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_create_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_create_variants_jobs(fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_create_variants_jobs(fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_create_jobs(fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Delete Catalog Items Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_catalog_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_delete_job | List[str]

klaviyo.Catalogs.get_bulk_delete_catalog_items_job(job_id, fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_items_job(job_id, fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_delete_job(job_id, fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job)
```




#### [Get Bulk Delete Catalog Items Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_catalog_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_delete_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_delete_catalog_items_jobs(fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_items_jobs(fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_delete_jobs(fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Delete Categories Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_delete_job | List[str]

klaviyo.Catalogs.get_bulk_delete_categories_job(job_id, fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_categories_job(job_id, fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_delete_job(job_id, fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job)
```




#### [Get Bulk Delete Categories Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_delete_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_delete_categories_jobs(fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_categories_jobs(fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_delete_jobs(fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Delete Variants Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_delete_job | List[str]

klaviyo.Catalogs.get_bulk_delete_variants_job(job_id, fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_variants_job(job_id, fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_delete_job(job_id, fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job)
```




#### [Get Bulk Delete Variants Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_delete_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_delete_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_delete_variants_jobs(fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_delete_variants_jobs(fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_delete_jobs(fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Update Catalog Items Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_catalog_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_update_job | List[str]
# fields_catalog_item | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_update_catalog_items_job(job_id, fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, fields_catalog_item=fields_catalog_item, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_items_job(job_id, fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, fields_catalog_item=fields_catalog_item, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_update_job(job_id, fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, fields_catalog_item=fields_catalog_item, include=include)
```




#### [Get Bulk Update Catalog Items Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_catalog_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_update_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_update_catalog_items_jobs(fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_items_jobs(fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_bulk_update_jobs(fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Update Categories Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_update_job | List[str]
# fields_catalog_category | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_update_categories_job(job_id, fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, fields_catalog_category=fields_catalog_category, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_categories_job(job_id, fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, fields_catalog_category=fields_catalog_category, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_update_job(job_id, fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, fields_catalog_category=fields_catalog_category, include=include)
```




#### [Get Bulk Update Categories Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_update_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_update_categories_jobs(fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_categories_jobs(fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_bulk_update_jobs(fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Update Variants Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_update_job | List[str]
# fields_catalog_variant | List[str]
# include | List[str]

klaviyo.Catalogs.get_bulk_update_variants_job(job_id, fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, fields_catalog_variant=fields_catalog_variant, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_variants_job(job_id, fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, fields_catalog_variant=fields_catalog_variant, include=include)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_update_job(job_id, fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, fields_catalog_variant=fields_catalog_variant, include=include)
```




#### [Get Bulk Update Variants Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_update_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_update_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_bulk_update_variants_jobs(fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_update_variants_jobs(fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_variant_bulk_update_jobs(fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Catalog Categories](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_categories)

```python

## Keyword Arguments

# fields_catalog_category | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_categories(fields_catalog_category=fields_catalog_category, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_category)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_category | List[str]

klaviyo.Catalogs.get_catalog_category(id, fields_catalog_category=fields_catalog_category)
```




#### [Get Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_item | List[str]
# fields_catalog_variant | List[str]
# include | List[str]

klaviyo.Catalogs.get_catalog_item(id, fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, include=include)
```




#### [Get Catalog Items](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_items)

```python

## Keyword Arguments

# fields_catalog_item | List[str]
# fields_catalog_variant | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_items(fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Catalog Variant](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_variant)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_variant | List[str]

klaviyo.Catalogs.get_catalog_variant(id, fields_catalog_variant=fields_catalog_variant)
```




#### [Get Catalog Variants](https://developers.klaviyo.com/en/v2025-04-15/reference/get_catalog_variants)

```python

## Keyword Arguments

# fields_catalog_variant | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_variants(fields_catalog_variant=fields_catalog_variant, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Categories for Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/get_categories_for_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_category | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_categories_for_catalog_item(id, fields_catalog_category=fields_catalog_category, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_categories(id, fields_catalog_category=fields_catalog_category, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Category IDs for Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/get_category_ids_for_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_category_ids_for_catalog_item(id, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_relationships_categories(id, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Item IDs for Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/get_item_ids_for_catalog_category)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_item_ids_for_catalog_category(id, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_relationships_items(id, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Items for Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/get_items_for_catalog_category)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_item | List[str]
# fields_catalog_variant | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_items_for_catalog_category(id, fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_category_items(id, fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Variant IDs for Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/get_variant_ids_for_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_variant_ids_for_catalog_item(id, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_relationships_variants(id, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Variants for Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/get_variants_for_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_variant | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_variants_for_catalog_item(id, fields_catalog_variant=fields_catalog_variant, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Catalogs.get_catalog_item_variants(id, fields_catalog_variant=fields_catalog_variant, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Remove Categories from Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_categories_from_catalog_item)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.remove_categories_from_catalog_item(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.delete_catalog_item_relationships_categories(id, body)
```




#### [Remove Items from Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_items_from_catalog_category)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.remove_items_from_catalog_category(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.delete_catalog_category_relationships_items(id, body)
```




#### [Update Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/update_catalog_category)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_category(id, body)
```




#### [Update Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/update_catalog_item)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_item(id, body)
```




#### [Update Catalog Variant](https://developers.klaviyo.com/en/v2025-04-15/reference/update_catalog_variant)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_variant(id, body)
```




#### [Update Categories for Catalog Item](https://developers.klaviyo.com/en/v2025-04-15/reference/update_categories_for_catalog_item)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_categories_for_catalog_item(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.update_catalog_item_relationships_categories(id, body)
```




#### [Update Items for Catalog Category](https://developers.klaviyo.com/en/v2025-04-15/reference/update_items_for_catalog_category)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_items_for_catalog_category(id, body)
```
##### Method alias:
```python
klaviyo.Catalogs.update_catalog_category_relationships_items(id, body)
```






## Coupons

#### [Bulk Create Coupon Codes](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_create_coupon_codes)

```python
## Positional Arguments

# body | dict

klaviyo.Coupons.bulk_create_coupon_codes(body)
```
##### Method alias:
```python
klaviyo.Coupons.spawn_coupon_code_bulk_create_job(body)
```
##### Method alias:
```python
klaviyo.Coupons.create_coupon_code_bulk_create_job(body)
```




#### [Create Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/create_coupon)

```python
## Positional Arguments

# body | dict

klaviyo.Coupons.create_coupon(body)
```




#### [Create Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/create_coupon_code)

```python
## Positional Arguments

# body | dict

klaviyo.Coupons.create_coupon_code(body)
```




#### [Delete Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_coupon)

```python
## Positional Arguments

# id | str

klaviyo.Coupons.delete_coupon(id)
```




#### [Delete Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_coupon_code)

```python
## Positional Arguments

# id | str

klaviyo.Coupons.delete_coupon_code(id)
```




#### [Get Bulk Create Coupon Code Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_coupon_code_jobs)

```python

## Keyword Arguments

# fields_coupon_code_bulk_create_job | List[str]
# filter | str
# page_cursor | str

klaviyo.Coupons.get_bulk_create_coupon_code_jobs(fields_coupon_code_bulk_create_job=fields_coupon_code_bulk_create_job, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_code_bulk_create_jobs(fields_coupon_code_bulk_create_job=fields_coupon_code_bulk_create_job, filter=filter, page_cursor=page_cursor)
```




#### [Get Bulk Create Coupon Codes Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_create_coupon_codes_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_coupon_code_bulk_create_job | List[str]
# fields_coupon_code | List[str]
# include | List[str]

klaviyo.Coupons.get_bulk_create_coupon_codes_job(job_id, fields_coupon_code_bulk_create_job=fields_coupon_code_bulk_create_job, fields_coupon_code=fields_coupon_code, include=include)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_code_bulk_create_job(job_id, fields_coupon_code_bulk_create_job=fields_coupon_code_bulk_create_job, fields_coupon_code=fields_coupon_code, include=include)
```




#### [Get Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_coupon | List[str]

klaviyo.Coupons.get_coupon(id, fields_coupon=fields_coupon)
```




#### [Get Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_code)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_coupon_code | List[str]
# fields_coupon | List[str]
# include | List[str]

klaviyo.Coupons.get_coupon_code(id, fields_coupon_code=fields_coupon_code, fields_coupon=fields_coupon, include=include)
```




#### [Get Coupon Code IDs for Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_code_ids_for_coupon)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str

klaviyo.Coupons.get_coupon_code_ids_for_coupon(id, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_code_relationships_coupon(id, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_code_ids_for_coupon(id, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_relationships_codes(id, filter=filter, page_cursor=page_cursor)
```




#### [Get Coupon Codes](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_codes)

```python
## Positional Arguments

# filter | str

## Keyword Arguments

# fields_coupon_code | List[str]
# fields_coupon | List[str]
# include | List[str]
# page_cursor | str

klaviyo.Coupons.get_coupon_codes(filter, fields_coupon_code=fields_coupon_code, fields_coupon=fields_coupon, include=include, page_cursor=page_cursor)
```




#### [Get Coupon Codes for Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_codes_for_coupon)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_coupon_code | List[str]
# filter | str
# page_cursor | str

klaviyo.Coupons.get_coupon_codes_for_coupon(id, fields_coupon_code=fields_coupon_code, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_coupon_codes(id, fields_coupon_code=fields_coupon_code, filter=filter, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Coupons.get_codes_for_coupon(id, fields_coupon_code=fields_coupon_code, filter=filter, page_cursor=page_cursor)
```




#### [Get Coupon For Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_for_coupon_code)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_coupon | List[str]

klaviyo.Coupons.get_coupon_for_coupon_code(id, fields_coupon=fields_coupon)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_code_coupon(id, fields_coupon=fields_coupon)
```




#### [Get Coupon ID for Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupon_id_for_coupon_code)

```python
## Positional Arguments

# id | str

klaviyo.Coupons.get_coupon_id_for_coupon_code(id)
```
##### Method alias:
```python
klaviyo.Coupons.get_coupon_relationships_coupon_codes(id)
```




#### [Get Coupons](https://developers.klaviyo.com/en/v2025-04-15/reference/get_coupons)

```python

## Keyword Arguments

# fields_coupon | List[str]
# page_cursor | str

klaviyo.Coupons.get_coupons(fields_coupon=fields_coupon, page_cursor=page_cursor)
```




#### [Update Coupon](https://developers.klaviyo.com/en/v2025-04-15/reference/update_coupon)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Coupons.update_coupon(id, body)
```




#### [Update Coupon Code](https://developers.klaviyo.com/en/v2025-04-15/reference/update_coupon_code)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Coupons.update_coupon_code(id, body)
```






## Data_Privacy

#### [Request Profile Deletion](https://developers.klaviyo.com/en/v2025-04-15/reference/request_profile_deletion)

```python
## Positional Arguments

# body | dict

klaviyo.Data_Privacy.request_profile_deletion(body)
```
##### Method alias:
```python
klaviyo.Data_Privacy.create_data_privacy_deletion_job(body)
```






## Events

#### [Bulk Create Events](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_create_events)

```python
## Positional Arguments

# body | dict

klaviyo.Events.bulk_create_events(body)
```
##### Method alias:
```python
klaviyo.Events.create_event_bulk_create_job(body)
```




#### [Create Event](https://developers.klaviyo.com/en/v2025-04-15/reference/create_event)

```python
## Positional Arguments

# body | dict

klaviyo.Events.create_event(body)
```




#### [Get Event](https://developers.klaviyo.com/en/v2025-04-15/reference/get_event)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_event | List[str]
# fields_metric | List[str]
# fields_profile | List[str]
# include | List[str]

klaviyo.Events.get_event(id, fields_event=fields_event, fields_metric=fields_metric, fields_profile=fields_profile, include=include)
```




#### [Get Events](https://developers.klaviyo.com/en/v2025-04-15/reference/get_events)

```python

## Keyword Arguments

# fields_event | List[str]
# fields_metric | List[str]
# fields_profile | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Events.get_events(fields_event=fields_event, fields_metric=fields_metric, fields_profile=fields_profile, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Metric for Event](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_for_event)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_metric | List[str]

klaviyo.Events.get_metric_for_event(id, fields_metric=fields_metric)
```
##### Method alias:
```python
klaviyo.Events.get_event_metric(id, fields_metric=fields_metric)
```




#### [Get Metric ID for Event](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_id_for_event)

```python
## Positional Arguments

# id | str

klaviyo.Events.get_metric_id_for_event(id)
```
##### Method alias:
```python
klaviyo.Events.get_event_relationships_metric(id)
```




#### [Get Profile for Event](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_for_event)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]

klaviyo.Events.get_profile_for_event(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile)
```
##### Method alias:
```python
klaviyo.Events.get_event_profile(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile)
```




#### [Get Profile ID for Event](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_id_for_event)

```python
## Positional Arguments

# id | str

klaviyo.Events.get_profile_id_for_event(id)
```
##### Method alias:
```python
klaviyo.Events.get_event_relationships_profile(id)
```






## Flows

#### [Create Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/create_flow)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# additional_fields_flow | List[str]

klaviyo.Flows.create_flow(body, additional_fields_flow=additional_fields_flow)
```




#### [Delete Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_flow)

```python
## Positional Arguments

# id | str

klaviyo.Flows.delete_flow(id)
```




#### [Get Action for Flow Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_action_for_flow_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | List[str]

klaviyo.Flows.get_action_for_flow_message(id, fields_flow_action=fields_flow_action)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_message_action(id, fields_flow_action=fields_flow_action)
```




#### [Get Action ID for Flow Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_action_id_for_flow_message)

```python
## Positional Arguments

# id | str

klaviyo.Flows.get_action_id_for_flow_message(id)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_message_relationships_action(id)
```




#### [Get Action IDs for Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/get_action_ids_for_flow)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Flows.get_action_ids_for_flow(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_relationships_flow_actions(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_relationships_actions(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Actions for Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/get_actions_for_flow)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Flows.get_actions_for_flow(id, fields_flow_action=fields_flow_action, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_flow_actions(id, fields_flow_action=fields_flow_action, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_actions(id, fields_flow_action=fields_flow_action, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_flow | List[str]
# fields_flow_action | List[str]
# fields_flow | List[str]
# fields_tag | List[str]
# include | List[str]

klaviyo.Flows.get_flow(id, additional_fields_flow=additional_fields_flow, fields_flow_action=fields_flow_action, fields_flow=fields_flow, fields_tag=fields_tag, include=include)
```




#### [Get Flow Action](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_action)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | List[str]
# fields_flow_message | List[str]
# fields_flow | List[str]
# include | List[str]

klaviyo.Flows.get_flow_action(id, fields_flow_action=fields_flow_action, fields_flow_message=fields_flow_message, fields_flow=fields_flow, include=include)
```




#### [Get Messages For Flow Action](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_action_messages)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_message | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Flows.get_flow_action_messages(id, fields_flow_message=fields_flow_message, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_messages_for_flow_action(id, fields_flow_message=fields_flow_message, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Flow for Flow Action](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_for_flow_action)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow | List[str]

klaviyo.Flows.get_flow_for_flow_action(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_action_flow(id, fields_flow=fields_flow)
```




#### [Get Flow ID for Flow Action](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_id_for_flow_action)

```python
## Positional Arguments

# id | str

klaviyo.Flows.get_flow_id_for_flow_action(id)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_action_relationships_flow(id)
```




#### [Get Flow Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | List[str]
# fields_flow_message | List[str]
# fields_template | List[str]
# include | List[str]

klaviyo.Flows.get_flow_message(id, fields_flow_action=fields_flow_action, fields_flow_message=fields_flow_message, fields_template=fields_template, include=include)
```




#### [Get Flows](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flows)

```python

## Keyword Arguments

# fields_flow_action | List[str]
# fields_flow | List[str]
# fields_tag | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Flows.get_flows(fields_flow_action=fields_flow_action, fields_flow=fields_flow, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Message IDs for Flow Action](https://developers.klaviyo.com/en/v2025-04-15/reference/get_message_ids_for_flow_action)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Flows.get_message_ids_for_flow_action(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_action_relationships_messages(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Tag IDs for Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_ids_for_flow)

```python
## Positional Arguments

# id | str

klaviyo.Flows.get_tag_ids_for_flow(id)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_relationships_tags(id)
```




#### [Get Tags for Flow](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags_for_flow)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | List[str]

klaviyo.Flows.get_tags_for_flow(id, fields_tag=fields_tag)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_tags(id, fields_tag=fields_tag)
```




#### [Get Template for Flow Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_template_for_flow_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_template | List[str]

klaviyo.Flows.get_template_for_flow_message(id, fields_template=fields_template)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_message_template(id, fields_template=fields_template)
```




#### [Get Template ID for Flow Message](https://developers.klaviyo.com/en/v2025-04-15/reference/get_template_id_for_flow_message)

```python
## Positional Arguments

# id | str

klaviyo.Flows.get_template_id_for_flow_message(id)
```
##### Method alias:
```python
klaviyo.Flows.get_flow_message_relationships_template(id)
```




#### [Update Flow Status](https://developers.klaviyo.com/en/v2025-04-15/reference/update_flow)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Flows.update_flow(id, body)
```






## Forms

#### [Delete Form](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_form)

```python
## Positional Arguments

# id | str

klaviyo.Forms.delete_form(id)
```




#### [Get Form](https://developers.klaviyo.com/en/v2025-04-15/reference/get_form)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_form_version | List[str]
# fields_form | List[str]
# include | List[str]

klaviyo.Forms.get_form(id, fields_form_version=fields_form_version, fields_form=fields_form, include=include)
```




#### [Get Form for Form Version](https://developers.klaviyo.com/en/v2025-04-15/reference/get_form_for_form_version)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_form | List[str]

klaviyo.Forms.get_form_for_form_version(id, fields_form=fields_form)
```
##### Method alias:
```python
klaviyo.Forms.get_form_version_form(id, fields_form=fields_form)
```




#### [Get Form ID for Form Version](https://developers.klaviyo.com/en/v2025-04-15/reference/get_form_id_for_form_version)

```python
## Positional Arguments

# id | str

klaviyo.Forms.get_form_id_for_form_version(id)
```
##### Method alias:
```python
klaviyo.Forms.get_form_version_relationships_form(id)
```




#### [Get Form Version](https://developers.klaviyo.com/en/v2025-04-15/reference/get_form_version)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_form_version | List[str]

klaviyo.Forms.get_form_version(id, fields_form_version=fields_form_version)
```




#### [Get Forms](https://developers.klaviyo.com/en/v2025-04-15/reference/get_forms)

```python

## Keyword Arguments

# fields_form | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Forms.get_forms(fields_form=fields_form, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Version IDs for Form](https://developers.klaviyo.com/en/v2025-04-15/reference/get_version_ids_for_form)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Forms.get_version_ids_for_form(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Forms.get_form_relationships_form_versions(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Forms.get_form_relationships_versions(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Versions for Form](https://developers.klaviyo.com/en/v2025-04-15/reference/get_versions_for_form)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_form_version | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Forms.get_versions_for_form(id, fields_form_version=fields_form_version, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Forms.get_form_form_versions(id, fields_form_version=fields_form_version, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Forms.get_form_versions(id, fields_form_version=fields_form_version, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```






## Images

#### [Get Image](https://developers.klaviyo.com/en/v2025-04-15/reference/get_image)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_image | List[str]

klaviyo.Images.get_image(id, fields_image=fields_image)
```




#### [Get Images](https://developers.klaviyo.com/en/v2025-04-15/reference/get_images)

```python

## Keyword Arguments

# fields_image | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Images.get_images(fields_image=fields_image, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Update Image](https://developers.klaviyo.com/en/v2025-04-15/reference/update_image)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Images.update_image(id, body)
```




#### [Upload Image From File](https://developers.klaviyo.com/en/v2025-04-15/reference/upload_image_from_file)

```python
## Positional Arguments

# file | bytearray

## Keyword Arguments

# name | str
# hidden | bool

klaviyo.Images.upload_image_from_file(file, name=name, hidden=hidden)
```
##### Method alias:
```python
klaviyo.Images.create_image_upload(file, name=name, hidden=hidden)
```




#### [Upload Image From URL](https://developers.klaviyo.com/en/v2025-04-15/reference/upload_image_from_url)

```python
## Positional Arguments

# body | dict

klaviyo.Images.upload_image_from_url(body)
```
##### Method alias:
```python
klaviyo.Images.create_image(body)
```






## Lists

#### [Add Profiles to List](https://developers.klaviyo.com/en/v2025-04-15/reference/add_profiles_to_list)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Lists.add_profiles_to_list(id, body)
```
##### Method alias:
```python
klaviyo.Lists.create_list_relationships(id, body)
```
##### Method alias:
```python
klaviyo.Lists.create_list_relationships_profile(id, body)
```
##### Method alias:
```python
klaviyo.Lists.create_list_relationships_profiles(id, body)
```




#### [Create List](https://developers.klaviyo.com/en/v2025-04-15/reference/create_list)

```python
## Positional Arguments

# body | dict

klaviyo.Lists.create_list(body)
```




#### [Delete List](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_list)

```python
## Positional Arguments

# id | str

klaviyo.Lists.delete_list(id)
```




#### [Get Flows Triggered by List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flows_triggered_by_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow | List[str]

klaviyo.Lists.get_flows_triggered_by_list(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Lists.get_flow_triggers_for_list(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Lists.get_list_flow_triggers(id, fields_flow=fields_flow)
```




#### [Get IDs for Flows Triggered by List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_ids_for_flows_triggered_by_list)

```python
## Positional Arguments

# id | str

klaviyo.Lists.get_ids_for_flows_triggered_by_list(id)
```
##### Method alias:
```python
klaviyo.Lists.get_flow_trigger_ids_for_list(id)
```
##### Method alias:
```python
klaviyo.Lists.get_list_relationships_flow_triggers(id)
```




#### [Get List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_list | List[str]
# fields_flow | List[str]
# fields_list | List[str]
# fields_tag | List[str]
# include | List[str]

klaviyo.Lists.get_list(id, additional_fields_list=additional_fields_list, fields_flow=fields_flow, fields_list=fields_list, fields_tag=fields_tag, include=include)
```




#### [Get Lists](https://developers.klaviyo.com/en/v2025-04-15/reference/get_lists)

```python

## Keyword Arguments

# fields_flow | List[str]
# fields_list | List[str]
# fields_tag | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Lists.get_lists(fields_flow=fields_flow, fields_list=fields_list, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Profile IDs for List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_ids_for_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Lists.get_profile_ids_for_list(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Lists.get_list_relationships_profiles(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Profiles for List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profiles_for_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Lists.get_profiles_for_list(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Lists.get_list_profiles(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Tag IDs for List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_ids_for_list)

```python
## Positional Arguments

# id | str

klaviyo.Lists.get_tag_ids_for_list(id)
```
##### Method alias:
```python
klaviyo.Lists.get_list_relationships_tags(id)
```




#### [Get Tags for List](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags_for_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | List[str]

klaviyo.Lists.get_tags_for_list(id, fields_tag=fields_tag)
```
##### Method alias:
```python
klaviyo.Lists.get_list_tags(id, fields_tag=fields_tag)
```




#### [Remove Profiles from List](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_profiles_from_list)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Lists.remove_profiles_from_list(id, body)
```
##### Method alias:
```python
klaviyo.Lists.delete_list_relationships(id, body)
```
##### Method alias:
```python
klaviyo.Lists.delete_list_relationships_profiles(id, body)
```




#### [Update List](https://developers.klaviyo.com/en/v2025-04-15/reference/update_list)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Lists.update_list(id, body)
```






## Metrics

#### [Create Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/create_custom_metric)

```python
## Positional Arguments

# body | dict

klaviyo.Metrics.create_custom_metric(body)
```




#### [Delete Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_custom_metric)

```python
## Positional Arguments

# id | str

klaviyo.Metrics.delete_custom_metric(id)
```




#### [Get Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_custom_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_custom_metric | List[str]
# fields_metric | List[str]
# include | List[str]

klaviyo.Metrics.get_custom_metric(id, fields_custom_metric=fields_custom_metric, fields_metric=fields_metric, include=include)
```




#### [Get Custom Metrics](https://developers.klaviyo.com/en/v2025-04-15/reference/get_custom_metrics)

```python

## Keyword Arguments

# fields_custom_metric | List[str]
# fields_metric | List[str]
# include | List[str]

klaviyo.Metrics.get_custom_metrics(fields_custom_metric=fields_custom_metric, fields_metric=fields_metric, include=include)
```




#### [Get Flows Triggered by Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flows_triggered_by_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow | List[str]

klaviyo.Metrics.get_flows_triggered_by_metric(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Metrics.get_flow_triggers_for_metric(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_flow_triggers(id, fields_flow=fields_flow)
```




#### [Get IDs for Flows Triggered by Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_ids_for_flows_triggered_by_metric)

```python
## Positional Arguments

# id | str

klaviyo.Metrics.get_ids_for_flows_triggered_by_metric(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_flow_trigger_ids_for_metric(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_relationships_flow_triggers(id)
```




#### [Get Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow | List[str]
# fields_metric | List[str]
# include | List[str]

klaviyo.Metrics.get_metric(id, fields_flow=fields_flow, fields_metric=fields_metric, include=include)
```




#### [Get Metric for Metric Property](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_for_metric_property)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_metric | List[str]

klaviyo.Metrics.get_metric_for_metric_property(id, fields_metric=fields_metric)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_property_metric(id, fields_metric=fields_metric)
```




#### [Get Metric ID for Metric Property](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_id_for_metric_property)

```python
## Positional Arguments

# id | str

klaviyo.Metrics.get_metric_id_for_metric_property(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_property_relationships_metric(id)
```




#### [Get Metric IDs for Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_ids_for_custom_metric)

```python
## Positional Arguments

# id | str

klaviyo.Metrics.get_metric_ids_for_custom_metric(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_custom_metric_relationships_metrics(id)
```




#### [Get Metric Property](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metric_property)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_metric_property | List[str]
# fields_metric_property | List[str]
# fields_metric | List[str]
# include | List[str]

klaviyo.Metrics.get_metric_property(id, additional_fields_metric_property=additional_fields_metric_property, fields_metric_property=fields_metric_property, fields_metric=fields_metric, include=include)
```




#### [Get Metrics](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metrics)

```python

## Keyword Arguments

# fields_flow | List[str]
# fields_metric | List[str]
# filter | str
# include | List[str]
# page_cursor | str

klaviyo.Metrics.get_metrics(fields_flow=fields_flow, fields_metric=fields_metric, filter=filter, include=include, page_cursor=page_cursor)
```




#### [Get Metrics for Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_metrics_for_custom_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_metric | List[str]

klaviyo.Metrics.get_metrics_for_custom_metric(id, fields_metric=fields_metric)
```
##### Method alias:
```python
klaviyo.Metrics.get_custom_metric_metrics(id, fields_metric=fields_metric)
```




#### [Get Properties for Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_properties_for_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_metric_property | List[str]
# fields_metric_property | List[str]

klaviyo.Metrics.get_properties_for_metric(id, additional_fields_metric_property=additional_fields_metric_property, fields_metric_property=fields_metric_property)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_metric_properties(id, additional_fields_metric_property=additional_fields_metric_property, fields_metric_property=fields_metric_property)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_properties(id, additional_fields_metric_property=additional_fields_metric_property, fields_metric_property=fields_metric_property)
```




#### [Get Property IDs for Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/get_property_ids_for_metric)

```python
## Positional Arguments

# id | str

klaviyo.Metrics.get_property_ids_for_metric(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_relationships_metric_properties(id)
```
##### Method alias:
```python
klaviyo.Metrics.get_metric_relationships_properties(id)
```




#### [Query Metric Aggregates](https://developers.klaviyo.com/en/v2025-04-15/reference/query_metric_aggregates)

```python
## Positional Arguments

# body | dict

klaviyo.Metrics.query_metric_aggregates(body)
```
##### Method alias:
```python
klaviyo.Metrics.create_metric_aggregate(body)
```




#### [Update Custom Metric](https://developers.klaviyo.com/en/v2025-04-15/reference/update_custom_metric)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Metrics.update_custom_metric(id, body)
```






## Profiles

#### [Bulk Import Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_import_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.bulk_import_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.spawn_bulk_profile_import_job(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_bulk_import_job(body)
```




#### [Bulk Subscribe Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_subscribe_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.bulk_subscribe_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.subscribe_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_subscription_bulk_create_job(body)
```




#### [Bulk Suppress Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_suppress_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.bulk_suppress_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.suppress_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_suppression_bulk_create_job(body)
```




#### [Bulk Unsubscribe Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_unsubscribe_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.bulk_unsubscribe_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.unsubscribe_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_subscription_bulk_delete_job(body)
```




#### [Bulk Unsuppress Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/bulk_unsuppress_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.bulk_unsuppress_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.unsuppress_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_suppression_bulk_delete_job(body)
```




#### [Create or Update Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/create_or_update_profile)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# additional_fields_profile | List[str]

klaviyo.Profiles.create_or_update_profile(body, additional_fields_profile=additional_fields_profile)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_import(body, additional_fields_profile=additional_fields_profile)
```




#### [Create Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/create_profile)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# additional_fields_profile | List[str]

klaviyo.Profiles.create_profile(body, additional_fields_profile=additional_fields_profile)
```




#### [Create or Update Push Token](https://developers.klaviyo.com/en/v2025-04-15/reference/create_push_token)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.create_push_token(body)
```




#### [Delete Push Token](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_push_token)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.delete_push_token(id)
```




#### [Get Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_import_profiles_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_list | List[str]
# fields_profile_bulk_import_job | List[str]
# include | List[str]

klaviyo.Profiles.get_bulk_import_profiles_job(job_id, fields_list=fields_list, fields_profile_bulk_import_job=fields_profile_bulk_import_job, include=include)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job(job_id, fields_list=fields_list, fields_profile_bulk_import_job=fields_profile_bulk_import_job, include=include)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job(job_id, fields_list=fields_list, fields_profile_bulk_import_job=fields_profile_bulk_import_job, include=include)
```




#### [Get Bulk Import Profiles Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_import_profiles_jobs)

```python

## Keyword Arguments

# fields_profile_bulk_import_job | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Profiles.get_bulk_import_profiles_jobs(fields_profile_bulk_import_job=fields_profile_bulk_import_job, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_jobs(fields_profile_bulk_import_job=fields_profile_bulk_import_job, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_jobs(fields_profile_bulk_import_job=fields_profile_bulk_import_job, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Bulk Suppress Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_suppress_profiles_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_profile_suppression_bulk_create_job | List[str]

klaviyo.Profiles.get_bulk_suppress_profiles_job(job_id, fields_profile_suppression_bulk_create_job=fields_profile_suppression_bulk_create_job)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_suppression_bulk_create_job(job_id, fields_profile_suppression_bulk_create_job=fields_profile_suppression_bulk_create_job)
```




#### [Get Bulk Suppress Profiles Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_suppress_profiles_jobs)

```python

## Keyword Arguments

# fields_profile_suppression_bulk_create_job | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Profiles.get_bulk_suppress_profiles_jobs(fields_profile_suppression_bulk_create_job=fields_profile_suppression_bulk_create_job, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_suppression_bulk_create_jobs(fields_profile_suppression_bulk_create_job=fields_profile_suppression_bulk_create_job, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Bulk Unsuppress Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_unsuppress_profiles_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_profile_suppression_bulk_delete_job | List[str]

klaviyo.Profiles.get_bulk_unsuppress_profiles_job(job_id, fields_profile_suppression_bulk_delete_job=fields_profile_suppression_bulk_delete_job)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_suppression_bulk_delete_job(job_id, fields_profile_suppression_bulk_delete_job=fields_profile_suppression_bulk_delete_job)
```




#### [Get Bulk Unsuppress Profiles Jobs](https://developers.klaviyo.com/en/v2025-04-15/reference/get_bulk_unsuppress_profiles_jobs)

```python

## Keyword Arguments

# fields_profile_suppression_bulk_delete_job | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Profiles.get_bulk_unsuppress_profiles_jobs(fields_profile_suppression_bulk_delete_job=fields_profile_suppression_bulk_delete_job, filter=filter, page_cursor=page_cursor, sort=sort)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_suppression_bulk_delete_jobs(fields_profile_suppression_bulk_delete_job=fields_profile_suppression_bulk_delete_job, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Errors for Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_errors_for_bulk_import_profiles_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_import_error | List[str]
# page_cursor | str
# page_size | int

klaviyo.Profiles.get_errors_for_bulk_import_profiles_job(id, fields_import_error=fields_import_error, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job_import_errors(id, fields_import_error=fields_import_error, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_import_errors_for_profile_bulk_import_job(id, fields_import_error=fields_import_error, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job_import_errors(id, fields_import_error=fields_import_error, page_cursor=page_cursor, page_size=page_size)
```




#### [Get List for Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_list_for_bulk_import_profiles_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_list | List[str]

klaviyo.Profiles.get_list_for_bulk_import_profiles_job(id, fields_list=fields_list)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job_lists(id, fields_list=fields_list)
```
##### Method alias:
```python
klaviyo.Profiles.get_lists_for_profile_bulk_import_job(id, fields_list=fields_list)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job_lists(id, fields_list=fields_list)
```




#### [Get List IDs for Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_list_ids_for_bulk_import_profiles_job)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.get_list_ids_for_bulk_import_profiles_job(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job_relationships_lists(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_list_ids_for_profile_bulk_import_job(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job_relationships_lists(id)
```




#### [Get List IDs for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_list_ids_for_profile)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.get_list_ids_for_profile(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_relationships_lists(id)
```




#### [Get Lists for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_lists_for_profile)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_list | List[str]

klaviyo.Profiles.get_lists_for_profile(id, fields_list=fields_list)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_lists(id, fields_list=fields_list)
```




#### [Get Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_list | List[str]
# fields_profile | List[str]
# fields_push_token | List[str]
# fields_segment | List[str]
# include | List[str]

klaviyo.Profiles.get_profile(id, additional_fields_profile=additional_fields_profile, fields_list=fields_list, fields_profile=fields_profile, fields_push_token=fields_push_token, fields_segment=fields_segment, include=include)
```




#### [Get Profile for Push Token](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_for_push_token)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]

klaviyo.Profiles.get_profile_for_push_token(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile)
```
##### Method alias:
```python
klaviyo.Profiles.get_push_token_profile(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile)
```




#### [Get Profile ID for Push Token](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_id_for_push_token)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.get_profile_id_for_push_token(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_push_token_relationships_profile(id)
```




#### [Get Profile IDs for Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_ids_for_bulk_import_profiles_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# page_cursor | str
# page_size | int

klaviyo.Profiles.get_profile_ids_for_bulk_import_profiles_job(id, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job_relationships_profiles(id, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job_relationships_profiles(id, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_ids_for_profile_bulk_import_job(id, page_cursor=page_cursor, page_size=page_size)
```




#### [Get Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profiles)

```python

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Profiles.get_profiles(additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, filter=filter, include=include, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Profiles for Bulk Import Profiles Job](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profiles_for_bulk_import_profiles_job)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]
# page_cursor | str
# page_size | int

klaviyo.Profiles.get_profiles_for_bulk_import_profiles_job(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_bulk_profile_import_job_profiles(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_bulk_import_job_profiles(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, page_cursor=page_cursor, page_size=page_size)
```
##### Method alias:
```python
klaviyo.Profiles.get_profiles_for_profile_bulk_import_job(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, page_cursor=page_cursor, page_size=page_size)
```




#### [Get Push Token](https://developers.klaviyo.com/en/v2025-04-15/reference/get_push_token)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_profile | List[str]
# fields_push_token | List[str]
# include | List[str]

klaviyo.Profiles.get_push_token(id, fields_profile=fields_profile, fields_push_token=fields_push_token, include=include)
```




#### [Get Push Token IDs for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_push_token_ids_for_profile)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.get_push_token_ids_for_profile(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_relationships_push_tokens(id)
```




#### [Get Push Tokens](https://developers.klaviyo.com/en/v2025-04-15/reference/get_push_tokens)

```python

## Keyword Arguments

# fields_profile | List[str]
# fields_push_token | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# page_size | int

klaviyo.Profiles.get_push_tokens(fields_profile=fields_profile, fields_push_token=fields_push_token, filter=filter, include=include, page_cursor=page_cursor, page_size=page_size)
```




#### [Get Push Tokens for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_push_tokens_for_profile)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_push_token | List[str]

klaviyo.Profiles.get_push_tokens_for_profile(id, fields_push_token=fields_push_token)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_push_tokens(id, fields_push_token=fields_push_token)
```




#### [Get Segment IDs for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_segment_ids_for_profile)

```python
## Positional Arguments

# id | str

klaviyo.Profiles.get_segment_ids_for_profile(id)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_relationships_segments(id)
```




#### [Get Segments for Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/get_segments_for_profile)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_segment | List[str]

klaviyo.Profiles.get_segments_for_profile(id, fields_segment=fields_segment)
```
##### Method alias:
```python
klaviyo.Profiles.get_profile_segments(id, fields_segment=fields_segment)
```




#### [Merge Profiles](https://developers.klaviyo.com/en/v2025-04-15/reference/merge_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.merge_profiles(body)
```
##### Method alias:
```python
klaviyo.Profiles.create_profile_merge(body)
```




#### [Update Profile](https://developers.klaviyo.com/en/v2025-04-15/reference/update_profile)

```python
## Positional Arguments

# id | str
# body | dict

## Keyword Arguments

# additional_fields_profile | List[str]

klaviyo.Profiles.update_profile(id, body, additional_fields_profile=additional_fields_profile)
```






## Reporting

#### [Query Campaign Values](https://developers.klaviyo.com/en/v2025-04-15/reference/query_campaign_values)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# page_cursor | str

klaviyo.Reporting.query_campaign_values(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_campaign_value_report(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_campaign_values_report(body, page_cursor=page_cursor)
```




#### [Query Flow Series](https://developers.klaviyo.com/en/v2025-04-15/reference/query_flow_series)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# page_cursor | str

klaviyo.Reporting.query_flow_series(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_flow_sery_report(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_flow_series_report(body, page_cursor=page_cursor)
```




#### [Query Flow Values](https://developers.klaviyo.com/en/v2025-04-15/reference/query_flow_values)

```python
## Positional Arguments

# body | dict

## Keyword Arguments

# page_cursor | str

klaviyo.Reporting.query_flow_values(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_flow_value_report(body, page_cursor=page_cursor)
```
##### Method alias:
```python
klaviyo.Reporting.create_flow_values_report(body, page_cursor=page_cursor)
```




#### [Query Form Series](https://developers.klaviyo.com/en/v2025-04-15/reference/query_form_series)

```python
## Positional Arguments

# body | dict

klaviyo.Reporting.query_form_series(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_form_sery_report(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_form_series_report(body)
```




#### [Query Form Values](https://developers.klaviyo.com/en/v2025-04-15/reference/query_form_values)

```python
## Positional Arguments

# body | dict

klaviyo.Reporting.query_form_values(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_form_value_report(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_form_values_report(body)
```




#### [Query Segment Series](https://developers.klaviyo.com/en/v2025-04-15/reference/query_segment_series)

```python
## Positional Arguments

# body | dict

klaviyo.Reporting.query_segment_series(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_segment_sery_report(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_segment_series_report(body)
```




#### [Query Segment Values](https://developers.klaviyo.com/en/v2025-04-15/reference/query_segment_values)

```python
## Positional Arguments

# body | dict

klaviyo.Reporting.query_segment_values(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_segment_value_report(body)
```
##### Method alias:
```python
klaviyo.Reporting.create_segment_values_report(body)
```






## Reviews

#### [Get Review](https://developers.klaviyo.com/en/v2025-04-15/reference/get_review)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_event | List[str]
# fields_review | List[str]
# include | List[str]

klaviyo.Reviews.get_review(id, fields_event=fields_event, fields_review=fields_review, include=include)
```




#### [Get Reviews](https://developers.klaviyo.com/en/v2025-04-15/reference/get_reviews)

```python

## Keyword Arguments

# fields_event | List[str]
# fields_review | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Reviews.get_reviews(fields_event=fields_event, fields_review=fields_review, filter=filter, include=include, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Update Review](https://developers.klaviyo.com/en/v2025-04-15/reference/update_review)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Reviews.update_review(id, body)
```






## Segments

#### [Create Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/create_segment)

```python
## Positional Arguments

# body | dict

klaviyo.Segments.create_segment(body)
```




#### [Delete Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_segment)

```python
## Positional Arguments

# id | str

klaviyo.Segments.delete_segment(id)
```




#### [Get Flows Triggered by Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flows_triggered_by_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow | List[str]

klaviyo.Segments.get_flows_triggered_by_segment(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Segments.get_flow_triggers_for_segment(id, fields_flow=fields_flow)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_flow_triggers(id, fields_flow=fields_flow)
```




#### [Get IDs for Flows Triggered by Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_ids_for_flows_triggered_by_segment)

```python
## Positional Arguments

# id | str

klaviyo.Segments.get_ids_for_flows_triggered_by_segment(id)
```
##### Method alias:
```python
klaviyo.Segments.get_flow_trigger_ids_for_segment(id)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_relationships_flow_triggers(id)
```




#### [Get Profile IDs for Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profile_ids_for_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Segments.get_profile_ids_for_segment(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_relationships_profiles(id, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Profiles for Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_profiles_for_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_profile | List[str]
# fields_profile | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Segments.get_profiles_for_segment(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_profiles(id, additional_fields_profile=additional_fields_profile, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# additional_fields_segment | List[str]
# fields_flow | List[str]
# fields_segment | List[str]
# fields_tag | List[str]
# include | List[str]

klaviyo.Segments.get_segment(id, additional_fields_segment=additional_fields_segment, fields_flow=fields_flow, fields_segment=fields_segment, fields_tag=fields_tag, include=include)
```




#### [Get Segments](https://developers.klaviyo.com/en/v2025-04-15/reference/get_segments)

```python

## Keyword Arguments

# fields_flow | List[str]
# fields_segment | List[str]
# fields_tag | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Segments.get_segments(fields_flow=fields_flow, fields_segment=fields_segment, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Tag IDs for Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_ids_for_segment)

```python
## Positional Arguments

# id | str

klaviyo.Segments.get_tag_ids_for_segment(id)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_relationships_tags(id)
```




#### [Get Tags for Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags_for_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | List[str]

klaviyo.Segments.get_tags_for_segment(id, fields_tag=fields_tag)
```
##### Method alias:
```python
klaviyo.Segments.get_segment_tags(id, fields_tag=fields_tag)
```




#### [Update Segment](https://developers.klaviyo.com/en/v2025-04-15/reference/update_segment)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Segments.update_segment(id, body)
```






## Tags

#### [Create Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/create_tag)

```python
## Positional Arguments

# body | dict

klaviyo.Tags.create_tag(body)
```




#### [Create Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/create_tag_group)

```python
## Positional Arguments

# body | dict

klaviyo.Tags.create_tag_group(body)
```




#### [Delete Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.delete_tag(id)
```




#### [Delete Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_tag_group)

```python
## Positional Arguments

# id | str

klaviyo.Tags.delete_tag_group(id)
```




#### [Get Campaign IDs for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_campaign_ids_for_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_campaign_ids_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_campaigns(id)
```




#### [Get Flow IDs for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_flow_ids_for_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_flow_ids_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_flows(id)
```




#### [Get List IDs for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_list_ids_for_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_list_ids_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_lists(id)
```




#### [Get Segment IDs for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_segment_ids_for_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_segment_ids_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_segments(id)
```




#### [Get Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag_group | List[str]
# fields_tag | List[str]
# include | List[str]

klaviyo.Tags.get_tag(id, fields_tag_group=fields_tag_group, fields_tag=fields_tag, include=include)
```




#### [Get Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_group)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag_group | List[str]

klaviyo.Tags.get_tag_group(id, fields_tag_group=fields_tag_group)
```




#### [Get Tag Group for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_group_for_tag)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag_group | List[str]

klaviyo.Tags.get_tag_group_for_tag(id, fields_tag_group=fields_tag_group)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_tag_group(id, fields_tag_group=fields_tag_group)
```
##### Method alias:
```python
klaviyo.Tags.get_group_for_tag(id, fields_tag_group=fields_tag_group)
```




#### [Get Tag Group ID for Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_group_id_for_tag)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_tag_group_id_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_tag_group(id)
```
##### Method alias:
```python
klaviyo.Tags.get_group_id_for_tag(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_relationships_group(id)
```




#### [Get Tag Groups](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_groups)

```python

## Keyword Arguments

# fields_tag_group | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Tags.get_tag_groups(fields_tag_group=fields_tag_group, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Tag IDs for Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tag_ids_for_tag_group)

```python
## Positional Arguments

# id | str

klaviyo.Tags.get_tag_ids_for_tag_group(id)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_group_relationships_tags(id)
```




#### [Get Tags](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags)

```python

## Keyword Arguments

# fields_tag_group | List[str]
# fields_tag | List[str]
# filter | str
# include | List[str]
# page_cursor | str
# sort | str

klaviyo.Tags.get_tags(fields_tag_group=fields_tag_group, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor, sort=sort)
```




#### [Get Tags for Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tags_for_tag_group)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tag | List[str]

klaviyo.Tags.get_tags_for_tag_group(id, fields_tag=fields_tag)
```
##### Method alias:
```python
klaviyo.Tags.get_tag_group_tags(id, fields_tag=fields_tag)
```




#### [Remove Tag from Campaigns](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_tag_from_campaigns)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.remove_tag_from_campaigns(id, body)
```
##### Method alias:
```python
klaviyo.Tags.delete_tag_relationships_campaigns(id, body)
```
##### Method alias:
```python
klaviyo.Tags.remove_campaigns_from_tag(id, body)
```




#### [Remove Tag from Flows](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_tag_from_flows)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.remove_tag_from_flows(id, body)
```
##### Method alias:
```python
klaviyo.Tags.delete_tag_relationships_flows(id, body)
```
##### Method alias:
```python
klaviyo.Tags.remove_flows_from_tag(id, body)
```




#### [Remove Tag from Lists](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_tag_from_lists)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.remove_tag_from_lists(id, body)
```
##### Method alias:
```python
klaviyo.Tags.delete_tag_relationships_lists(id, body)
```
##### Method alias:
```python
klaviyo.Tags.remove_lists_from_tag(id, body)
```




#### [Remove Tag from Segments](https://developers.klaviyo.com/en/v2025-04-15/reference/remove_tag_from_segments)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.remove_tag_from_segments(id, body)
```
##### Method alias:
```python
klaviyo.Tags.delete_tag_relationships_segments(id, body)
```
##### Method alias:
```python
klaviyo.Tags.remove_segments_from_tag(id, body)
```




#### [Tag Campaigns](https://developers.klaviyo.com/en/v2025-04-15/reference/tag_campaigns)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.tag_campaigns(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_campaign(id, body)
```
##### Method alias:
```python
klaviyo.Tags.add_campaigns_to_tag(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_campaigns(id, body)
```




#### [Tag Flows](https://developers.klaviyo.com/en/v2025-04-15/reference/tag_flows)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.tag_flows(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_flow(id, body)
```
##### Method alias:
```python
klaviyo.Tags.add_flows_to_tag(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_flows(id, body)
```




#### [Tag Lists](https://developers.klaviyo.com/en/v2025-04-15/reference/tag_lists)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.tag_lists(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_list(id, body)
```
##### Method alias:
```python
klaviyo.Tags.add_lists_to_tag(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_lists(id, body)
```




#### [Tag Segments](https://developers.klaviyo.com/en/v2025-04-15/reference/tag_segments)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.tag_segments(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_segment(id, body)
```
##### Method alias:
```python
klaviyo.Tags.add_segments_to_tag(id, body)
```
##### Method alias:
```python
klaviyo.Tags.create_tag_relationships_segments(id, body)
```




#### [Update Tag](https://developers.klaviyo.com/en/v2025-04-15/reference/update_tag)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.update_tag(id, body)
```




#### [Update Tag Group](https://developers.klaviyo.com/en/v2025-04-15/reference/update_tag_group)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tags.update_tag_group(id, body)
```






## Templates

#### [Clone Template](https://developers.klaviyo.com/en/v2025-04-15/reference/clone_template)

```python
## Positional Arguments

# body | dict

klaviyo.Templates.clone_template(body)
```
##### Method alias:
```python
klaviyo.Templates.create_template_clone(body)
```




#### [Create Template](https://developers.klaviyo.com/en/v2025-04-15/reference/create_template)

```python
## Positional Arguments

# body | dict

klaviyo.Templates.create_template(body)
```




#### [Create Universal Content](https://developers.klaviyo.com/en/v2025-04-15/reference/create_universal_content)

```python
## Positional Arguments

# body | dict

klaviyo.Templates.create_universal_content(body)
```
##### Method alias:
```python
klaviyo.Templates.create_template_universal_content(body)
```




#### [Delete Template](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_template)

```python
## Positional Arguments

# id | str

klaviyo.Templates.delete_template(id)
```




#### [Delete Universal Content](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_universal_content)

```python
## Positional Arguments

# id | str

klaviyo.Templates.delete_universal_content(id)
```
##### Method alias:
```python
klaviyo.Templates.delete_template_universal_content(id)
```




#### [Get All Universal Content](https://developers.klaviyo.com/en/v2025-04-15/reference/get_all_universal_content)

```python

## Keyword Arguments

# fields_template_universal_content | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Templates.get_all_universal_content(fields_template_universal_content=fields_template_universal_content, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```
##### Method alias:
```python
klaviyo.Templates.get_template_universal_content(fields_template_universal_content=fields_template_universal_content, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Get Template](https://developers.klaviyo.com/en/v2025-04-15/reference/get_template)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_template | List[str]

klaviyo.Templates.get_template(id, fields_template=fields_template)
```




#### [Get Templates](https://developers.klaviyo.com/en/v2025-04-15/reference/get_templates)

```python

## Keyword Arguments

# fields_template | List[str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Templates.get_templates(fields_template=fields_template, filter=filter, page_cursor=page_cursor, sort=sort)
```




#### [Get Universal Content](https://developers.klaviyo.com/en/v2025-04-15/reference/get_universal_content)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_template_universal_content | List[str]

klaviyo.Templates.get_universal_content(id, fields_template_universal_content=fields_template_universal_content)
```




#### [Render Template](https://developers.klaviyo.com/en/v2025-04-15/reference/render_template)

```python
## Positional Arguments

# body | dict

klaviyo.Templates.render_template(body)
```
##### Method alias:
```python
klaviyo.Templates.create_template_render(body)
```




#### [Update Template](https://developers.klaviyo.com/en/v2025-04-15/reference/update_template)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Templates.update_template(id, body)
```




#### [Update Universal Content](https://developers.klaviyo.com/en/v2025-04-15/reference/update_universal_content)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Templates.update_universal_content(id, body)
```
##### Method alias:
```python
klaviyo.Templates.update_template_universal_content(id, body)
```






## Tracking_Settings

#### [Get Tracking Setting](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tracking_setting)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_tracking_setting | List[str]

klaviyo.Tracking_Settings.get_tracking_setting(id, fields_tracking_setting=fields_tracking_setting)
```




#### [Get Tracking Settings](https://developers.klaviyo.com/en/v2025-04-15/reference/get_tracking_settings)

```python

## Keyword Arguments

# fields_tracking_setting | List[str]
# page_cursor | str
# page_size | int

klaviyo.Tracking_Settings.get_tracking_settings(fields_tracking_setting=fields_tracking_setting, page_cursor=page_cursor, page_size=page_size)
```




#### [Update Tracking Setting](https://developers.klaviyo.com/en/v2025-04-15/reference/update_tracking_setting)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Tracking_Settings.update_tracking_setting(id, body)
```






## Web_Feeds

#### [Create Web Feed](https://developers.klaviyo.com/en/v2025-04-15/reference/create_web_feed)

```python
## Positional Arguments

# body | dict

klaviyo.Web_Feeds.create_web_feed(body)
```




#### [Delete Web Feed](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_web_feed)

```python
## Positional Arguments

# id | str

klaviyo.Web_Feeds.delete_web_feed(id)
```




#### [Get Web Feed](https://developers.klaviyo.com/en/v2025-04-15/reference/get_web_feed)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_web_feed | List[str]

klaviyo.Web_Feeds.get_web_feed(id, fields_web_feed=fields_web_feed)
```




#### [Get Web Feeds](https://developers.klaviyo.com/en/v2025-04-15/reference/get_web_feeds)

```python

## Keyword Arguments

# fields_web_feed | List[str]
# filter | str
# page_cursor | str
# page_size | int
# sort | str

klaviyo.Web_Feeds.get_web_feeds(fields_web_feed=fields_web_feed, filter=filter, page_cursor=page_cursor, page_size=page_size, sort=sort)
```




#### [Update Web Feed](https://developers.klaviyo.com/en/v2025-04-15/reference/update_web_feed)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Web_Feeds.update_web_feed(id, body)
```






## Webhooks

#### [Create Webhook](https://developers.klaviyo.com/en/v2025-04-15/reference/create_webhook)

```python
## Positional Arguments

# body | dict

klaviyo.Webhooks.create_webhook(body)
```




#### [Delete Webhook](https://developers.klaviyo.com/en/v2025-04-15/reference/delete_webhook)

```python
## Positional Arguments

# id | str

klaviyo.Webhooks.delete_webhook(id)
```




#### [Get Webhook](https://developers.klaviyo.com/en/v2025-04-15/reference/get_webhook)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_webhook | List[str]
# include | List[str]

klaviyo.Webhooks.get_webhook(id, fields_webhook=fields_webhook, include=include)
```




#### [Get Webhook Topic](https://developers.klaviyo.com/en/v2025-04-15/reference/get_webhook_topic)

```python
## Positional Arguments

# id | str

klaviyo.Webhooks.get_webhook_topic(id)
```




#### [Get Webhook Topics](https://developers.klaviyo.com/en/v2025-04-15/reference/get_webhook_topics)

```python

klaviyo.Webhooks.get_webhook_topics()
```




#### [Get Webhooks](https://developers.klaviyo.com/en/v2025-04-15/reference/get_webhooks)

```python

## Keyword Arguments

# fields_webhook | List[str]
# include | List[str]

klaviyo.Webhooks.get_webhooks(fields_webhook=fields_webhook, include=include)
```




#### [Update Webhook](https://developers.klaviyo.com/en/v2025-04-15/reference/update_webhook)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Webhooks.update_webhook(id, body)
```




# Appendix

## Global Keyword Args

NOTE: These are arguments that you can apply to any endpoint call, and which are unique to the SDK

We currently support the following global keyword args:
- `_request_auth` : use this to override the client-level api_key which you define upon client instantiation

## Refresher on catching exceptions:

```python
try:
    YOUR_CALL
except Exception as e:
    print(e.status)
    print(e.reason)
    print(e.body)
    print(e.headers)
```

## Parameters & Arguments

The parameters follow the same naming conventions as the resource groups and operations.

We stick to the following convention for parameters/arguments

1. All parameters are passed as function args.
2. All query and path params that are tagged as `required` in the docs are passed as positional args.
3. All optional query params are passed as keyword args.
4. Where applicable, the `body` param is passed in as a positional arg, and is expected to be a native python dictionary. Within that dictionary, refer to the API docs to see which fields are required/optional, along with valid values.
4. There is no need to pass in your private `api_key` for any operations, as it is defined upon client instantiation; public key is still required where applicable. However, you can pass in an optional `_request_auth` kwarg to override the client private key for a specific call (REMINDER: don't do this client-side).

## Namespace

In the interest of making the SDK Pythonic, we made the following namespace changes *relative* to the language agnostic resources up top (API Docs, Guides, etc).

- Resource names use Title + Snake Casing, (e.g. `Data_Privacy`)
- function names and parameter names use snake case (e.g. `get_metrics`, and `profile_id`)

## Renamed Fields
As of the 2024-05-15 release, some models fields are named differently than they appear in API documentation. These fields are

- `datetime`: renamed to `datetime_`
- `date`: renamed to `date_`

This is to manage compatibility with Pydantic v2. An example of this can be seen in [StaticScheduleOptions](src/openapi_client/models/static_schedule_options.py).

```python
class StaticScheduleOptions(BaseModel):
    """
    StaticScheduleOptions
    """ # noqa: E501
    datetime_: datetime = Field(description="The time to send at", alias="datetime")
```

### Usage
```python
schedule_options = StaticScheduleOptions(datetime_=datetime.datetime.strptime("2024-05-19T00:00:00+00:00", "%Y-%m-%dT%H:%M:%S%z")
print(schedule_options.datetime_)
```

## Filter Builder
Use this class to help construct filter query parameters.
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

## Typed Responses
By default, all API methods will return a type representing the response payload instead of dictionary, as was the case in previous versions of this SDK. Using the typed response, you can access fields of a response using dot notation, like so:
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

### Backwards Compatibility
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

## Untyped Response Data for Specific APIs
Select APIs do not yet have fully typed responses. Please use our API docs to inspect the schema of the response data for the following APIs.
- **Segments** - The subproperty `conditions` is not yet typed in responses for the following APIs:
    - [Create Segment](https://developers.klaviyo.com/en/reference/create_segment)
    - [Update Segment](https://developers.klaviyo.com/en/reference/update_segment)
    - [Get Segment](https://developers.klaviyo.com/en/reference/get_segment)
    - [Get Segments](https://developers.klaviyo.com/en/reference/get_segments)
- The `included` property is not typed in responses for the following APIs:
    - [Get Event](https://developers.klaviyo.com/en/reference/get_event)
    - [Get Events](https://developers.klaviyo.com/en/reference/get_events)
    - [Get Profile](https://developers.klaviyo.com/en/reference/get_profile)
    - [Get Profiles](https://developers.klaviyo.com/en/reference/get_profiles)
    - [Get Flow](https://developers.klaviyo.com/en/reference/get_flow)
    - [Get Flows](https://developers.klaviyo.com/en/reference/get_flows)
    - [Get Flow Message](https://developers.klaviyo.com/en/reference/get_flow_message)
    - [Get Campaign](https://developers.klaviyo.com/en/reference/get_campaign)
    - [Get Campaigns](https://developers.klaviyo.com/en/reference/get_campaigns)
- The `tracking_options` subproperty is not typed in responses for the following APIs:
    - [Get Flow Action](https://developers.klaviyo.com/en/reference/get_flow_action)
    - [Get Actions for Flow](https://developers.klaviyo.com/en/reference/get_actions_for_flow)
    - [Create Campaign](https://developers.klaviyo.com/en/reference/create_campaign)
    - [Update Campaign](https://developers.klaviyo.com/en/reference/update_campaign)
    - [Get Campaign](https://developers.klaviyo.com/en/reference/get_campaign)
    - [Get Campaigns](https://developers.klaviyo.com/en/reference/get_campaigns)
- The `send_options` subproperty is not typed in responses for the following APIs:
    - [Create Campaign](https://developers.klaviyo.com/en/reference/create_campaign)
    - [Update Campaign](https://developers.klaviyo.com/en/reference/update_campaign)
    - [Get Campaign](https://developers.klaviyo.com/en/reference/get_campaign)
    - [Get Campaigns](https://developers.klaviyo.com/en/reference/get_campaigns)
    - [Get Campaign for Campaign Message](https://developers.klaviyo.com/en/reference/get_campaign_for_campaign_message)
    - [Get Messages for Campaign](https://developers.klaviyo.com/en/reference/get_messages_for_campaign)
- The `content` subproperty is not typed in responses for the following APIs:
    - [Get Flow Message](https://developers.klaviyo.com/en/reference/get_flow_message)
    - [Get Messages for Flow Action](https://developers.klaviyo.com/en/reference/get_messages_for_flow_action)
    - [Get Campaign for Campaign Message](https://developers.klaviyo.com/en/reference/get_campaign_for_campaign_message)
    - [Get Messages for Campaign](https://developers.klaviyo.com/en/reference/get_messages_for_campaign)