# Klaviyo Python SDK

- SDK version: 1.0.3
- API revision: 2022-10-17

## Helpful Resources

- [API Reference](https://developers.klaviyo.com/en/v2022-10-17/reference)
- [API Guides](https://developers.klaviyo.com/en/v2022-10-17/docs)
- [Postman Workspace](https://www.postman.com/klaviyo/workspace/klaviyo-developers)
- [Interactive Guide (Jupyter Notebook)](https://github.com/klaviyo-labs/klaviyo-api-guides)

## Design & Approach

This SDK is a thin wrapper around our API. See our API Reference for full documentation on behavior.

This SDK exactly mirrors the organization and naming convention of the above language-agnostic resources, with a few namespace changes to make it Pythonic (details in Appendix).

## Organization

This SDK is organized into the following resources:



- Catalogs



- Client



- Events



- Flows



- Lists



- Metrics



- Profiles



- Segments



- Templates



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
* `max_delay` denotes total delay (in seconds) across all attempts.

```python
from klaviyo_api import KlaviyoAPI

klaviyo = KlaviyoAPI("YOUR API KEY HERE", max_delay=60, max_retries=3, test_host=None)
```

### Example request

```python
klaviyo.Metrics.get_metrics() 
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
- Organization: Resource groups and operation_ids are listed below in alphabetical order, first by Resource name, then by **OpenAPI Summary**. Operation summaries are those listed in the right side bar of the [API Reference](https://developers.klaviyo.com/en/v2022-10-17/reference/get_events).
- For example values / data types, as well as whether parameters are required/optional, please reference the corresponding API Reference link.
- Some keyword args may potentially be required for the API call to succeed, the linked API docs are the source of truth regarding which keyword params are required.
- JSON payloads should be passed in as native python dictionaries.
- You can override the client private key by passing in an optional `api_key` keyword arg to any API call that takes a private key. As a reminder: do NOT do this client-side/onsite.

# Comprehensive list of Operations & Parameters





## Catalogs

#### [Create Catalog Category](https://developers.klaviyo.com/en/v2022-10-17/reference/create_catalog_category)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_category(body);
```




#### [Create Catalog Category Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/create_catalog_category_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.create_catalog_category_relationships(id, related_resource, body);
```




#### [Create Catalog Item](https://developers.klaviyo.com/en/v2022-10-17/reference/create_catalog_item)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_item(body);
```




#### [Create Catalog Item Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/create_catalog_item_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.create_catalog_item_relationships(id, related_resource, body);
```




#### [Create Catalog Variant](https://developers.klaviyo.com/en/v2022-10-17/reference/create_catalog_variant)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.create_catalog_variant(body);
```




#### [Delete Catalog Category](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_catalog_category)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_category(id);
```




#### [Delete Catalog Category Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_catalog_category_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.delete_catalog_category_relationships(id, related_resource, body);
```




#### [Delete Catalog Item](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_catalog_item)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_item(id);
```




#### [Delete Catalog Item Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_catalog_item_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.delete_catalog_item_relationships(id, related_resource, body);
```




#### [Delete Catalog Variant](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_catalog_variant)

```python
## Positional Arguments

# id | str

klaviyo.Catalogs.delete_catalog_variant(id);
```




#### [Get Catalog Categories](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_categories)

```python

## Keyword Arguments

# fields_catalog_category | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_categories(fields_catalog_category=fields_catalog_category, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Get Catalog Category](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_category)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_category | [str]

klaviyo.Catalogs.get_catalog_category(id, fields_catalog_category=fields_catalog_category);
```




#### [Get Catalog Category Items](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_category_items)

```python
## Positional Arguments

# category_id | str

## Keyword Arguments

# fields_catalog_item | [str]
# fields_catalog_variant | [str]
# filter | str
# include | [str]
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_category_items(category_id, fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, filter=filter, include=include, page_cursor=page_cursor, sort=sort);
```




#### [Get Catalog Category Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_category_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

## Keyword Arguments

# page_cursor | str

klaviyo.Catalogs.get_catalog_category_relationships(id, related_resource, page_cursor=page_cursor);
```




#### [Get Catalog Item](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_item)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_item | [str]
# fields_catalog_variant | [str]
# include | [str]

klaviyo.Catalogs.get_catalog_item(id, fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, include=include);
```




#### [Get Catalog Item Categories](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_item_categories)

```python
## Positional Arguments

# item_id | str

## Keyword Arguments

# fields_catalog_category | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_item_categories(item_id, fields_catalog_category=fields_catalog_category, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Get Catalog Item Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_item_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

## Keyword Arguments

# page_cursor | str

klaviyo.Catalogs.get_catalog_item_relationships(id, related_resource, page_cursor=page_cursor);
```




#### [Get Catalog Item Variants](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_item_variants)

```python
## Positional Arguments

# item_id | str

## Keyword Arguments

# fields_catalog_variant | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_item_variants(item_id, fields_catalog_variant=fields_catalog_variant, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Get Catalog Items](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_items)

```python

## Keyword Arguments

# fields_catalog_item | [str]
# fields_catalog_variant | [str]
# filter | str
# include | [str]
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_items(fields_catalog_item=fields_catalog_item, fields_catalog_variant=fields_catalog_variant, filter=filter, include=include, page_cursor=page_cursor, sort=sort);
```




#### [Get Catalog Variant](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_variant)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_catalog_variant | [str]

klaviyo.Catalogs.get_catalog_variant(id, fields_catalog_variant=fields_catalog_variant);
```




#### [Get Catalog Variants](https://developers.klaviyo.com/en/v2022-10-17/reference/get_catalog_variants)

```python

## Keyword Arguments

# fields_catalog_variant | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Catalogs.get_catalog_variants(fields_catalog_variant=fields_catalog_variant, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Get Create Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_create_job | [str]
# fields_catalog_category | [str]
# include | [str]

klaviyo.Catalogs.get_create_categories_job(job_id, fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, fields_catalog_category=fields_catalog_category, include=include);
```




#### [Get Create Categories Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_create_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_create_categories_jobs(fields_catalog_category_bulk_create_job=fields_catalog_category_bulk_create_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Create Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_create_job | [str]
# fields_catalog_item | [str]
# include | [str]

klaviyo.Catalogs.get_create_items_job(job_id, fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, fields_catalog_item=fields_catalog_item, include=include);
```




#### [Get Create Items Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_create_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_create_items_jobs(fields_catalog_item_bulk_create_job=fields_catalog_item_bulk_create_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Create Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_create_job | [str]
# fields_catalog_variant | [str]
# include | [str]

klaviyo.Catalogs.get_create_variants_job(job_id, fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, fields_catalog_variant=fields_catalog_variant, include=include);
```




#### [Get Create Variants Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_create_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_create_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_create_variants_jobs(fields_catalog_variant_bulk_create_job=fields_catalog_variant_bulk_create_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Delete Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_delete_job | [str]

klaviyo.Catalogs.get_delete_categories_job(job_id, fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job);
```




#### [Get Delete Categories Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_delete_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_delete_categories_jobs(fields_catalog_category_bulk_delete_job=fields_catalog_category_bulk_delete_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Delete Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_delete_job | [str]

klaviyo.Catalogs.get_delete_items_job(job_id, fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job);
```




#### [Get Delete Items Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_delete_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_delete_items_jobs(fields_catalog_item_bulk_delete_job=fields_catalog_item_bulk_delete_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Delete Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_delete_job | [str]

klaviyo.Catalogs.get_delete_variants_job(job_id, fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job);
```




#### [Get Delete Variants Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_delete_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_delete_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_delete_variants_jobs(fields_catalog_variant_bulk_delete_job=fields_catalog_variant_bulk_delete_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Update Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_categories_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_category_bulk_update_job | [str]
# fields_catalog_category | [str]
# include | [str]

klaviyo.Catalogs.get_update_categories_job(job_id, fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, fields_catalog_category=fields_catalog_category, include=include);
```




#### [Get Update Categories Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_categories_jobs)

```python

## Keyword Arguments

# fields_catalog_category_bulk_update_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_update_categories_jobs(fields_catalog_category_bulk_update_job=fields_catalog_category_bulk_update_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Update Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_items_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_item_bulk_update_job | [str]
# fields_catalog_item | [str]
# include | [str]

klaviyo.Catalogs.get_update_items_job(job_id, fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, fields_catalog_item=fields_catalog_item, include=include);
```




#### [Get Update Items Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_items_jobs)

```python

## Keyword Arguments

# fields_catalog_item_bulk_update_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_update_items_jobs(fields_catalog_item_bulk_update_job=fields_catalog_item_bulk_update_job, filter=filter, page_cursor=page_cursor);
```




#### [Get Update Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_variants_job)

```python
## Positional Arguments

# job_id | str

## Keyword Arguments

# fields_catalog_variant_bulk_update_job | [str]
# fields_catalog_variant | [str]
# include | [str]

klaviyo.Catalogs.get_update_variants_job(job_id, fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, fields_catalog_variant=fields_catalog_variant, include=include);
```




#### [Get Update Variants Jobs](https://developers.klaviyo.com/en/v2022-10-17/reference/get_update_variants_jobs)

```python

## Keyword Arguments

# fields_catalog_variant_bulk_update_job | [str]
# filter | str
# page_cursor | str

klaviyo.Catalogs.get_update_variants_jobs(fields_catalog_variant_bulk_update_job=fields_catalog_variant_bulk_update_job, filter=filter, page_cursor=page_cursor);
```




#### [Spawn Create Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_create_categories_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_create_categories_job(body);
```




#### [Spawn Create Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_create_items_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_create_items_job(body);
```




#### [Spawn Create Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_create_variants_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_create_variants_job(body);
```




#### [Spawn Delete Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_delete_categories_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_delete_categories_job(body);
```




#### [Spawn Delete Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_delete_items_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_delete_items_job(body);
```




#### [Spawn Delete Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_delete_variants_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_delete_variants_job(body);
```




#### [Spawn Update Categories Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_update_categories_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_update_categories_job(body);
```




#### [Spawn Update Items Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_update_items_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_update_items_job(body);
```




#### [Spawn Update Variants Job](https://developers.klaviyo.com/en/v2022-10-17/reference/spawn_update_variants_job)

```python
## Positional Arguments

# body | dict

klaviyo.Catalogs.spawn_update_variants_job(body);
```




#### [Update Catalog Category](https://developers.klaviyo.com/en/v2022-10-17/reference/update_catalog_category)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_category(id, body);
```




#### [Update Catalog Category Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/update_catalog_category_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.update_catalog_category_relationships(id, related_resource, body);
```




#### [Update Catalog Item](https://developers.klaviyo.com/en/v2022-10-17/reference/update_catalog_item)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_item(id, body);
```




#### [Update Catalog Item Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/update_catalog_item_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Catalogs.update_catalog_item_relationships(id, related_resource, body);
```




#### [Update Catalog Variant](https://developers.klaviyo.com/en/v2022-10-17/reference/update_catalog_variant)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Catalogs.update_catalog_variant(id, body);
```






## Client

#### [Create Client Event](https://developers.klaviyo.com/en/v2022-10-17/reference/create_client_event)

```python
## Positional Arguments

# company_id | str
# body | dict

klaviyo.Client.create_client_event(company_id, body);
```




#### [Create Client Profile](https://developers.klaviyo.com/en/v2022-10-17/reference/create_client_profile)

```python
## Positional Arguments

# company_id | str
# body | dict

klaviyo.Client.create_client_profile(company_id, body);
```




#### [Create Client Subscription](https://developers.klaviyo.com/en/v2022-10-17/reference/create_client_subscription)

```python
## Positional Arguments

# company_id | str
# body | dict

klaviyo.Client.create_client_subscription(company_id, body);
```






## Events

#### [Create Event](https://developers.klaviyo.com/en/v2022-10-17/reference/create_event)

```python
## Positional Arguments

# body | dict

klaviyo.Events.create_event(body);
```




#### [Get Event](https://developers.klaviyo.com/en/v2022-10-17/reference/get_event)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_event | [str]
# fields_metric | [str]
# fields_profile | [str]
# include | [str]

klaviyo.Events.get_event(id, fields_event=fields_event, fields_metric=fields_metric, fields_profile=fields_profile, include=include);
```




#### [Get Event Metrics](https://developers.klaviyo.com/en/v2022-10-17/reference/get_event_metrics)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_metric | [str]

klaviyo.Events.get_event_metrics(id, fields_metric=fields_metric);
```




#### [Get Event Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/get_event_profiles)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_profile | [str]

klaviyo.Events.get_event_profiles(id, fields_profile=fields_profile);
```




#### [Get Event Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_event_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

klaviyo.Events.get_event_relationships(id, related_resource);
```




#### [Get Events](https://developers.klaviyo.com/en/v2022-10-17/reference/get_events)

```python

## Keyword Arguments

# fields_event | [str]
# fields_metric | [str]
# fields_profile | [str]
# filter | str
# include | [str]
# page_cursor | str
# sort | str

klaviyo.Events.get_events(fields_event=fields_event, fields_metric=fields_metric, fields_profile=fields_profile, filter=filter, include=include, page_cursor=page_cursor, sort=sort);
```






## Flows

#### [Get Flow](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | [str]
# fields_flow | [str]
# fields_tag | [str]
# include | [str]

klaviyo.Flows.get_flow(id, fields_flow_action=fields_flow_action, fields_flow=fields_flow, fields_tag=fields_tag, include=include);
```




#### [Get Flow Action](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_action)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | [str]
# fields_flow_message | [str]
# fields_flow | [str]
# include | [str]

klaviyo.Flows.get_flow_action(id, fields_flow_action=fields_flow_action, fields_flow_message=fields_flow_message, fields_flow=fields_flow, include=include);
```




#### [Get Flow For Flow Action](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_action_flow)

```python
## Positional Arguments

# action_id | str

## Keyword Arguments

# fields_flow | [str]

klaviyo.Flows.get_flow_action_flow(action_id, fields_flow=fields_flow);
```




#### [Get Messages For Flow Action](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_action_messages)

```python
## Positional Arguments

# action_id | str

## Keyword Arguments

# fields_flow_message | [str]
# filter | str
# sort | str

klaviyo.Flows.get_flow_action_messages(action_id, fields_flow_message=fields_flow_message, filter=filter, sort=sort);
```




#### [Get Flow Action Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_action_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

## Keyword Arguments

# filter | str
# sort | str

klaviyo.Flows.get_flow_action_relationships(id, related_resource, filter=filter, sort=sort);
```




#### [Get Flow Actions For Flow](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_flow_actions)

```python
## Positional Arguments

# flow_id | str

## Keyword Arguments

# fields_flow_action | [str]
# filter | str
# sort | str

klaviyo.Flows.get_flow_flow_actions(flow_id, fields_flow_action=fields_flow_action, filter=filter, sort=sort);
```




#### [Get Flow Message](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_message)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_flow_action | [str]
# fields_flow_message | [str]
# include | [str]

klaviyo.Flows.get_flow_message(id, fields_flow_action=fields_flow_action, fields_flow_message=fields_flow_message, include=include);
```




#### [Get Flow Action For Message](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_message_action)

```python
## Positional Arguments

# message_id | str

## Keyword Arguments

# fields_flow_action | [str]

klaviyo.Flows.get_flow_message_action(message_id, fields_flow_action=fields_flow_action);
```




#### [Get Flow Message Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flow_message_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

klaviyo.Flows.get_flow_message_relationships(id, related_resource);
```




#### [Get Flows](https://developers.klaviyo.com/en/v2022-10-17/reference/get_flows)

```python

## Keyword Arguments

# fields_flow_action | [str]
# fields_flow | [str]
# fields_tag | [str]
# filter | str
# include | [str]
# sort | str

klaviyo.Flows.get_flows(fields_flow_action=fields_flow_action, fields_flow=fields_flow, fields_tag=fields_tag, filter=filter, include=include, sort=sort);
```




#### [Update Flow Status](https://developers.klaviyo.com/en/v2022-10-17/reference/update_flow)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Flows.update_flow(id, body);
```






## Lists

#### [Create List](https://developers.klaviyo.com/en/v2022-10-17/reference/create_list)

```python
## Positional Arguments

# body | dict

klaviyo.Lists.create_list(body);
```




#### [Add Profile to List](https://developers.klaviyo.com/en/v2022-10-17/reference/create_list_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Lists.create_list_relationships(id, related_resource, body);
```




#### [Delete List](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_list)

```python
## Positional Arguments

# id | str

klaviyo.Lists.delete_list(id);
```




#### [Remove Profile from List](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_list_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str
# body | dict

klaviyo.Lists.delete_list_relationships(id, related_resource, body);
```




#### [Get List](https://developers.klaviyo.com/en/v2022-10-17/reference/get_list)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_list | [str]
# fields_tag | [str]
# include | [str]

klaviyo.Lists.get_list(id, fields_list=fields_list, fields_tag=fields_tag, include=include);
```




#### [Get List Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/get_list_profiles)

```python
## Positional Arguments

# list_id | str

## Keyword Arguments

# fields_profile | [str]
# filter | str
# page_cursor | str

klaviyo.Lists.get_list_profiles(list_id, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor);
```




#### [Get List Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_list_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

## Keyword Arguments

# page_cursor | str

klaviyo.Lists.get_list_relationships(id, related_resource, page_cursor=page_cursor);
```




#### [Get Lists](https://developers.klaviyo.com/en/v2022-10-17/reference/get_lists)

```python

## Keyword Arguments

# fields_list | [str]
# fields_tag | [str]
# filter | str
# include | [str]
# page_cursor | str

klaviyo.Lists.get_lists(fields_list=fields_list, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor);
```




#### [Update List](https://developers.klaviyo.com/en/v2022-10-17/reference/update_list)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Lists.update_list(id, body);
```






## Metrics

#### [Get Metric](https://developers.klaviyo.com/en/v2022-10-17/reference/get_metric)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_metric | [str]

klaviyo.Metrics.get_metric(id, fields_metric=fields_metric);
```




#### [Get Metrics](https://developers.klaviyo.com/en/v2022-10-17/reference/get_metrics)

```python

## Keyword Arguments

# fields_metric | [str]
# filter | str
# page_cursor | str

klaviyo.Metrics.get_metrics(fields_metric=fields_metric, filter=filter, page_cursor=page_cursor);
```




#### [Query Metric Aggregates](https://developers.klaviyo.com/en/v2022-10-17/reference/query_metric_aggregates)

```python
## Positional Arguments

# body | dict

klaviyo.Metrics.query_metric_aggregates(body);
```






## Profiles

#### [Create Profile](https://developers.klaviyo.com/en/v2022-10-17/reference/create_profile)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.create_profile(body);
```




#### [Get Profile](https://developers.klaviyo.com/en/v2022-10-17/reference/get_profile)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_list | [str]
# fields_profile | [str]
# fields_segment | [str]
# include | [str]

klaviyo.Profiles.get_profile(id, fields_list=fields_list, fields_profile=fields_profile, fields_segment=fields_segment, include=include);
```




#### [Get Profile Lists](https://developers.klaviyo.com/en/v2022-10-17/reference/get_profile_lists)

```python
## Positional Arguments

# profile_id | str

## Keyword Arguments

# fields_list | [str]

klaviyo.Profiles.get_profile_lists(profile_id, fields_list=fields_list);
```




#### [Get Profile Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_profile_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

klaviyo.Profiles.get_profile_relationships(id, related_resource);
```




#### [Get Profile Segments](https://developers.klaviyo.com/en/v2022-10-17/reference/get_profile_segments)

```python
## Positional Arguments

# profile_id | str

## Keyword Arguments

# fields_segment | [str]

klaviyo.Profiles.get_profile_segments(profile_id, fields_segment=fields_segment);
```




#### [Get Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/get_profiles)

```python

## Keyword Arguments

# fields_profile | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Profiles.get_profiles(fields_profile=fields_profile, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Subscribe Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/subscribe_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.subscribe_profiles(body);
```




#### [Suppress Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/suppress_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.suppress_profiles(body);
```




#### [Unsubscribe Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/unsubscribe_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.unsubscribe_profiles(body);
```




#### [Unsuppress Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/unsuppress_profiles)

```python
## Positional Arguments

# body | dict

klaviyo.Profiles.unsuppress_profiles(body);
```




#### [Update Profile](https://developers.klaviyo.com/en/v2022-10-17/reference/update_profile)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Profiles.update_profile(id, body);
```






## Segments

#### [Get Segment](https://developers.klaviyo.com/en/v2022-10-17/reference/get_segment)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_segment | [str]
# fields_tag | [str]
# include | [str]

klaviyo.Segments.get_segment(id, fields_segment=fields_segment, fields_tag=fields_tag, include=include);
```




#### [Get Segment Profiles](https://developers.klaviyo.com/en/v2022-10-17/reference/get_segment_profiles)

```python
## Positional Arguments

# segment_id | str

## Keyword Arguments

# fields_profile | [str]
# filter | str
# page_cursor | str

klaviyo.Segments.get_segment_profiles(segment_id, fields_profile=fields_profile, filter=filter, page_cursor=page_cursor);
```




#### [Get Segment Relationships](https://developers.klaviyo.com/en/v2022-10-17/reference/get_segment_relationships)

```python
## Positional Arguments

# id | str
# related_resource | str

## Keyword Arguments

# page_cursor | str

klaviyo.Segments.get_segment_relationships(id, related_resource, page_cursor=page_cursor);
```




#### [Get Segments](https://developers.klaviyo.com/en/v2022-10-17/reference/get_segments)

```python

## Keyword Arguments

# fields_segment | [str]
# fields_tag | [str]
# filter | str
# include | [str]
# page_cursor | str

klaviyo.Segments.get_segments(fields_segment=fields_segment, fields_tag=fields_tag, filter=filter, include=include, page_cursor=page_cursor);
```




#### [Update Segment](https://developers.klaviyo.com/en/v2022-10-17/reference/update_segment)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Segments.update_segment(id, body);
```






## Templates

#### [Create Template](https://developers.klaviyo.com/en/v2022-10-17/reference/create_template)

```python
## Positional Arguments

# body | dict

klaviyo.Templates.create_template(body);
```




#### [Create Template Clone](https://developers.klaviyo.com/en/v2022-10-17/reference/create_template_clone)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Templates.create_template_clone(id, body);
```




#### [Create Template Render](https://developers.klaviyo.com/en/v2022-10-17/reference/create_template_render)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Templates.create_template_render(id, body);
```




#### [Delete Template](https://developers.klaviyo.com/en/v2022-10-17/reference/delete_template)

```python
## Positional Arguments

# id | str

klaviyo.Templates.delete_template(id);
```




#### [Get Template](https://developers.klaviyo.com/en/v2022-10-17/reference/get_template)

```python
## Positional Arguments

# id | str

## Keyword Arguments

# fields_template | [str]

klaviyo.Templates.get_template(id, fields_template=fields_template);
```




#### [Get Templates](https://developers.klaviyo.com/en/v2022-10-17/reference/get_templates)

```python

## Keyword Arguments

# fields_template | [str]
# filter | str
# page_cursor | str
# sort | str

klaviyo.Templates.get_templates(fields_template=fields_template, filter=filter, page_cursor=page_cursor, sort=sort);
```




#### [Update Template](https://developers.klaviyo.com/en/v2022-10-17/reference/update_template)

```python
## Positional Arguments

# id | str
# body | dict

klaviyo.Templates.update_template(id, body);
```




# Appendix

## Global Keyword Args

NOTE: These are arguments that you can apply to any endpoint call, and which are unique to the SDK

We currently support the following global keyword args:
- `api_key` : use this to override the client-level api_key which you define upon client instantiation

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
4. There is no need to pass in your private `api_key` for any operations, as it is defined upon client instantiation; public key is still required where applicable. However, you can pass in an optional `api_key` kwarg to override the client private key for a specific call (REMINDER: don't do this client-side).

## Namespace

In the interest of making the SDK Pythonic, we made the following namespace changes *relative* to the language agnostic resources up top (API Docs, Guides, etc).

- Resource names use Pascal case, (e.g. `Metrics`)
- function names and parameter names remain unchanged and use snake case (e.g. `get_metrics`, and `profile_id`)