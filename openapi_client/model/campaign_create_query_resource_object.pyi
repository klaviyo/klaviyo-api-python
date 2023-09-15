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


class CampaignCreateQueryResourceObject(
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
            def type() -> typing.Type['CampaignEnum']:
                return CampaignEnum
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "send_strategy",
                        "campaign-messages",
                        "name",
                        "audiences",
                    }
                    
                    class properties:
                        
                        
                        class name(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'name':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                    
                        @staticmethod
                        def audiences() -> typing.Type['AudiencesSubObject']:
                            return AudiencesSubObject
                    
                        @staticmethod
                        def send_strategy() -> typing.Type['SendStrategySubObject']:
                            return SendStrategySubObject
                        
                        
                        class send_options(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                additional_properties = schemas.AnyTypeSchema
                            
                            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                return super().get_item_oapg(name)
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            ) -> 'send_options':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class tracking_options(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                additional_properties = schemas.AnyTypeSchema
                            
                            def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                                return super().get_item_oapg(name)
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            ) -> 'tracking_options':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        
                        
                        class campaign_messages(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                    
                                    
                                    class data(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            @staticmethod
                                            def items() -> typing.Type['CampaignMessageCreateQueryResourceObject']:
                                                return CampaignMessageCreateQueryResourceObject
                                    
                                        def __new__(
                                            cls,
                                            _arg: typing.Union[typing.Tuple['CampaignMessageCreateQueryResourceObject'], typing.List['CampaignMessageCreateQueryResourceObject']],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'data':
                                            return super().__new__(
                                                cls,
                                                _arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> 'CampaignMessageCreateQueryResourceObject':
                                            return super().__getitem__(i)
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
                                data: typing.Union[MetaOapg.properties.data, list, tuple, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'campaign_messages':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "name": name,
                            "audiences": audiences,
                            "send_strategy": send_strategy,
                            "send_options": send_options,
                            "tracking_options": tracking_options,
                            "campaign-messages": campaign_messages,
                        }
                
                send_strategy: 'SendStrategySubObject'
                name: MetaOapg.properties.name
                audiences: 'AudiencesSubObject'
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["audiences"]) -> 'AudiencesSubObject': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["send_strategy"]) -> 'SendStrategySubObject': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["send_options"]) -> MetaOapg.properties.send_options: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["tracking_options"]) -> MetaOapg.properties.tracking_options: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["campaign-messages"]) -> MetaOapg.properties.campaign_messages: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "audiences", "send_strategy", "send_options", "tracking_options", "campaign-messages", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["audiences"]) -> 'AudiencesSubObject': ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["send_strategy"]) -> 'SendStrategySubObject': ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["send_options"]) -> typing.Union[MetaOapg.properties.send_options, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["tracking_options"]) -> typing.Union[MetaOapg.properties.tracking_options, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["campaign-messages"]) -> MetaOapg.properties.campaign_messages: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "audiences", "send_strategy", "send_options", "tracking_options", "campaign-messages", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    send_strategy: 'SendStrategySubObject',
                    name: typing.Union[MetaOapg.properties.name, None, str, ],
                    audiences: 'AudiencesSubObject',
                    send_options: typing.Union[MetaOapg.properties.send_options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    tracking_options: typing.Union[MetaOapg.properties.tracking_options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        send_strategy=send_strategy,
                        name=name,
                        audiences=audiences,
                        send_options=send_options,
                        tracking_options=tracking_options,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "attributes": attributes,
            }
    
    attributes: MetaOapg.properties.attributes
    type: 'CampaignEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CampaignEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'CampaignEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        type: 'CampaignEnum',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CampaignCreateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.audiences_sub_object import AudiencesSubObject
from openapi_client.model.campaign_enum import CampaignEnum
from openapi_client.model.campaign_message_create_query_resource_object import CampaignMessageCreateQueryResourceObject
from openapi_client.model.send_strategy_sub_object import SendStrategySubObject
