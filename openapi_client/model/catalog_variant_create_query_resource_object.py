# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-09-15
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class CatalogVariantCreateQueryResourceObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "attributes",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['CatalogVariantEnum']:
                return CatalogVariantEnum
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "inventory_quantity",
                        "price",
                        "description",
                        "external_id",
                        "sku",
                        "title",
                        "url",
                    }
                    
                    class properties:
                        
                        
                        class external_id(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'external_id':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class catalog_type(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'catalog_type':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class integration_type(
                            schemas.EnumBase,
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "$custom": "CUSTOM",
                                }
                            
                            @schemas.classproperty
                            def CUSTOM(cls):
                                return cls("$custom")
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'integration_type':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class title(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'title':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class description(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'description':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class sku(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'sku':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class inventory_policy(
                            schemas.EnumBase,
                            schemas.IntSchema
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    0: "POSITIVE_0",
                                    1: "POSITIVE_1",
                                    2: "POSITIVE_2",
                                }
                            
                            @schemas.classproperty
                            def POSITIVE_0(cls):
                                return cls(0)
                            
                            @schemas.classproperty
                            def POSITIVE_1(cls):
                                return cls(1)
                            
                            @schemas.classproperty
                            def POSITIVE_2(cls):
                                return cls(2)
                        inventory_quantity = schemas.NumberSchema
                        price = schemas.NumberSchema
                        
                        
                        class url(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'url':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class image_full_url(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'image_full_url':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class image_thumbnail_url(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'image_thumbnail_url':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class images(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'images':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        custom_metadata = schemas.DictSchema
                        published = schemas.BoolSchema
                        __annotations__ = {
                            "external_id": external_id,
                            "catalog_type": catalog_type,
                            "integration_type": integration_type,
                            "title": title,
                            "description": description,
                            "sku": sku,
                            "inventory_policy": inventory_policy,
                            "inventory_quantity": inventory_quantity,
                            "price": price,
                            "url": url,
                            "image_full_url": image_full_url,
                            "image_thumbnail_url": image_thumbnail_url,
                            "images": images,
                            "custom_metadata": custom_metadata,
                            "published": published,
                        }
                
                inventory_quantity: MetaOapg.properties.inventory_quantity
                price: MetaOapg.properties.price
                description: MetaOapg.properties.description
                external_id: MetaOapg.properties.external_id
                sku: MetaOapg.properties.sku
                title: MetaOapg.properties.title
                url: MetaOapg.properties.url
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["catalog_type"]) -> MetaOapg.properties.catalog_type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["integration_type"]) -> MetaOapg.properties.integration_type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inventory_policy"]) -> MetaOapg.properties.inventory_policy: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inventory_quantity"]) -> MetaOapg.properties.inventory_quantity: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["image_full_url"]) -> MetaOapg.properties.image_full_url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["image_thumbnail_url"]) -> MetaOapg.properties.image_thumbnail_url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["images"]) -> MetaOapg.properties.images: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["custom_metadata"]) -> MetaOapg.properties.custom_metadata: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["external_id", "catalog_type", "integration_type", "title", "description", "sku", "inventory_policy", "inventory_quantity", "price", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["catalog_type"]) -> typing.Union[MetaOapg.properties.catalog_type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["integration_type"]) -> typing.Union[MetaOapg.properties.integration_type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inventory_policy"]) -> typing.Union[MetaOapg.properties.inventory_policy, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inventory_quantity"]) -> MetaOapg.properties.inventory_quantity: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["image_full_url"]) -> typing.Union[MetaOapg.properties.image_full_url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["image_thumbnail_url"]) -> typing.Union[MetaOapg.properties.image_thumbnail_url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["images"]) -> typing.Union[MetaOapg.properties.images, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["custom_metadata"]) -> typing.Union[MetaOapg.properties.custom_metadata, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["published"]) -> typing.Union[MetaOapg.properties.published, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["external_id", "catalog_type", "integration_type", "title", "description", "sku", "inventory_policy", "inventory_quantity", "price", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    inventory_quantity: typing.Union[MetaOapg.properties.inventory_quantity, decimal.Decimal, int, float, ],
                    price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
                    description: typing.Union[MetaOapg.properties.description, None, str, ],
                    external_id: typing.Union[MetaOapg.properties.external_id, None, str, ],
                    sku: typing.Union[MetaOapg.properties.sku, None, str, ],
                    title: typing.Union[MetaOapg.properties.title, None, str, ],
                    url: typing.Union[MetaOapg.properties.url, None, str, ],
                    catalog_type: typing.Union[MetaOapg.properties.catalog_type, None, str, schemas.Unset] = schemas.unset,
                    integration_type: typing.Union[MetaOapg.properties.integration_type, None, str, schemas.Unset] = schemas.unset,
                    inventory_policy: typing.Union[MetaOapg.properties.inventory_policy, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    image_full_url: typing.Union[MetaOapg.properties.image_full_url, None, str, schemas.Unset] = schemas.unset,
                    image_thumbnail_url: typing.Union[MetaOapg.properties.image_thumbnail_url, None, str, schemas.Unset] = schemas.unset,
                    images: typing.Union[MetaOapg.properties.images, list, tuple, schemas.Unset] = schemas.unset,
                    custom_metadata: typing.Union[MetaOapg.properties.custom_metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    published: typing.Union[MetaOapg.properties.published, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        inventory_quantity=inventory_quantity,
                        price=price,
                        description=description,
                        external_id=external_id,
                        sku=sku,
                        title=title,
                        url=url,
                        catalog_type=catalog_type,
                        integration_type=integration_type,
                        inventory_policy=inventory_policy,
                        image_full_url=image_full_url,
                        image_thumbnail_url=image_thumbnail_url,
                        images=images,
                        custom_metadata=custom_metadata,
                        published=published,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class item(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                    
                                    
                                    class data(
                                        schemas.DictSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            required = {
                                                "id",
                                                "type",
                                            }
                                            
                                            class properties:
                                            
                                                @staticmethod
                                                def type() -> typing.Type['CatalogItemEnum']:
                                                    return CatalogItemEnum
                                                id = schemas.StrSchema
                                                __annotations__ = {
                                                    "type": type,
                                                    "id": id,
                                                }
                                        
                                        id: MetaOapg.properties.id
                                        type: 'CatalogItemEnum'
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CatalogItemEnum': ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                        
                                        @typing.overload
                                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                        
                                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", ], str]):
                                            # dict_instance[name] accessor
                                            return super().__getitem__(name)
                                        
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'CatalogItemEnum': ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                                        
                                        @typing.overload
                                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                        
                                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", ], str]):
                                            return super().get_item_oapg(name)
                                        
                                    
                                        def __new__(
                                            cls,
                                            *_args: typing.Union[dict, frozendict.frozendict, ],
                                            id: typing.Union[MetaOapg.properties.id, str, ],
                                            type: 'CatalogItemEnum',
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                        ) -> 'data':
                                            return super().__new__(
                                                cls,
                                                *_args,
                                                id=id,
                                                type=type,
                                                _configuration=_configuration,
                                                **kwargs,
                                            )
                                    __annotations__ = {
                                        "data": data,
                                    }
                            
                            data: MetaOapg.properties.data
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'item':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "item": item,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["item"]) -> MetaOapg.properties.item: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["item", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["item"]) -> typing.Union[MetaOapg.properties.item, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    item: typing.Union[MetaOapg.properties.item, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *_args,
                        item=item,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "attributes": attributes,
                "relationships": relationships,
            }
    
    attributes: MetaOapg.properties.attributes
    type: 'CatalogVariantEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "attributes", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "attributes", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        type: 'CatalogVariantEnum',
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CatalogVariantCreateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            type=type,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.catalog_item_enum import CatalogItemEnum
from openapi_client.model.catalog_variant_enum import CatalogVariantEnum