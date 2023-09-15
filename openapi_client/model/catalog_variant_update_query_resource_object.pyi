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


class CatalogVariantUpdateQueryResourceObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "attributes",
            "id",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['CatalogVariantEnum']:
                return CatalogVariantEnum
            id = schemas.StrSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
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
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "sku", "inventory_policy", "inventory_quantity", "price", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> typing.Union[MetaOapg.properties.sku, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inventory_policy"]) -> typing.Union[MetaOapg.properties.inventory_policy, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inventory_quantity"]) -> typing.Union[MetaOapg.properties.inventory_quantity, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
                
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
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "sku", "inventory_policy", "inventory_quantity", "price", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    title: typing.Union[MetaOapg.properties.title, None, str, schemas.Unset] = schemas.unset,
                    description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
                    sku: typing.Union[MetaOapg.properties.sku, None, str, schemas.Unset] = schemas.unset,
                    inventory_policy: typing.Union[MetaOapg.properties.inventory_policy, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    inventory_quantity: typing.Union[MetaOapg.properties.inventory_quantity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    url: typing.Union[MetaOapg.properties.url, None, str, schemas.Unset] = schemas.unset,
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
                        title=title,
                        description=description,
                        sku=sku,
                        inventory_policy=inventory_policy,
                        inventory_quantity=inventory_quantity,
                        price=price,
                        url=url,
                        image_full_url=image_full_url,
                        image_thumbnail_url=image_thumbnail_url,
                        images=images,
                        custom_metadata=custom_metadata,
                        published=published,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
    
    attributes: MetaOapg.properties.attributes
    id: MetaOapg.properties.id
    type: 'CatalogVariantEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: 'CatalogVariantEnum',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CatalogVariantUpdateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            id=id,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.catalog_variant_enum import CatalogVariantEnum
