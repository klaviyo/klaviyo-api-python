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


class ProfileSubscriptionCreateQueryResourceObject(
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
            def type() -> typing.Type['ProfileEnum']:
                return ProfileEnum
            
            
            class attributes(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class email(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'email':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class phone_number(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'phone_number':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                    
                        @staticmethod
                        def subscriptions() -> typing.Type['SubscriptionChannels']:
                            return SubscriptionChannels
                        __annotations__ = {
                            "email": email,
                            "phone_number": phone_number,
                            "subscriptions": subscriptions,
                        }
            
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["subscriptions"]) -> 'SubscriptionChannels': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "phone_number", "subscriptions", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["subscriptions"]) -> typing.Union['SubscriptionChannels', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "phone_number", "subscriptions", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                    phone_number: typing.Union[MetaOapg.properties.phone_number, None, str, schemas.Unset] = schemas.unset,
                    subscriptions: typing.Union['SubscriptionChannels', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        email=email,
                        phone_number=phone_number,
                        subscriptions=subscriptions,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "attributes": attributes,
                "id": id,
            }
    
    attributes: MetaOapg.properties.attributes
    type: 'ProfileEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ProfileEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "attributes", "id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ProfileEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "attributes", "id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        type: 'ProfileEnum',
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileSubscriptionCreateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            type=type,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.profile_enum import ProfileEnum
from openapi_client.model.subscription_channels import SubscriptionChannels
