# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Set, Tuple, Union
from typing_extensions import Annotated

import inspect

from enum import EnumMeta

from openapi_client.models.data_privacy_create_deletion_job_query import DataPrivacyCreateDeletionJobQuery

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType
from openapi_client.api_arg_options import USE_DICTIONARY_FOR_RESPONSE_DATA


class DataPrivacyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def request_profile_deletion(        
        self,
        data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: StrictStr = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
        options: Dict[str, Any] = {},
) -> None:
        """Request Profile Deletion

        Request a deletion for the profiles corresponding to one of the following identifiers: `email`, `phone_number`, or `id`. If multiple identifiers are provided, we will return an error.  All profiles that match the provided identifier will be deleted.  The deletion occurs asynchronously; however, once it has completed, the deleted profile will appear on the [Deleted Profiles page](https://www.klaviyo.com/account/deleted).  For more information on the deletion process, please refer to our [Help Center docs on how to handle GDPR and CCPA deletion requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests#record-gdpr-and-ccpa%20%20-deletion-requests2).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `data-privacy:write`

        :param data_privacy_create_deletion_job_query: (required)
        :type data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._request_profile_deletion_serialize(
            data_privacy_create_deletion_job_query=data_privacy_create_deletion_job_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': None,
            '4XX': "GetAccounts4XXResponse",
            '5XX': "GetAccounts4XXResponse",
        }
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        uses_sparse_fields = self._uses_sparse_fields(args, values)

        if _request_auth is not None:
            _request_auth = {'in': 'header', 'key': 'Authorization', 'type': 'api_key', 'value': f'Klaviyo-API-Key {_request_auth}'}

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()

        if uses_sparse_fields or options.get(USE_DICTIONARY_FOR_RESPONSE_DATA, False) or self.api_client.options.get(USE_DICTIONARY_FOR_RESPONSE_DATA, False):
            _response_types_map = self._replace_type_with_dict_in_response_types_map(_response_types_map)

        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            exclude_none=uses_sparse_fields
        ).data


    # alias of request_profile_deletion
    create_data_privacy_deletion_job = request_profile_deletion

    @validate_call
    def request_profile_deletion_with_http_info(        
        self,
        data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: StrictStr = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
        options: Dict[str, Any] = {},
) -> ApiResponse[None]:
        """Request Profile Deletion

        Request a deletion for the profiles corresponding to one of the following identifiers: `email`, `phone_number`, or `id`. If multiple identifiers are provided, we will return an error.  All profiles that match the provided identifier will be deleted.  The deletion occurs asynchronously; however, once it has completed, the deleted profile will appear on the [Deleted Profiles page](https://www.klaviyo.com/account/deleted).  For more information on the deletion process, please refer to our [Help Center docs on how to handle GDPR and CCPA deletion requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests#record-gdpr-and-ccpa%20%20-deletion-requests2).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `data-privacy:write`

        :param data_privacy_create_deletion_job_query: (required)
        :type data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._request_profile_deletion_serialize(
            data_privacy_create_deletion_job_query=data_privacy_create_deletion_job_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': None,
            '4XX': "GetAccounts4XXResponse",
            '5XX': "GetAccounts4XXResponse",
        }
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        uses_sparse_fields = self._uses_sparse_fields(args, values)

        if _request_auth is not None:
            _request_auth = {'in': 'header', 'key': 'Authorization', 'type': 'api_key', 'value': f'Klaviyo-API-Key {_request_auth}'}

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        if uses_sparse_fields or options.get(USE_DICTIONARY_FOR_RESPONSE_DATA, False) or self.api_client.options.get(USE_DICTIONARY_FOR_RESPONSE_DATA, False):
            _response_types_map = self._replace_type_with_dict_in_response_types_map(_response_types_map)

        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    # alias of `request_profile_deletion_with_http_info`
    create_data_privacy_deletion_job_with_http_info = request_profile_deletion_with_http_info

    @validate_call
    def request_profile_deletion_without_preload_content(
        self,
        data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: StrictStr = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,) -> RESTResponseType:
        """Request Profile Deletion

        Request a deletion for the profiles corresponding to one of the following identifiers: `email`, `phone_number`, or `id`. If multiple identifiers are provided, we will return an error.  All profiles that match the provided identifier will be deleted.  The deletion occurs asynchronously; however, once it has completed, the deleted profile will appear on the [Deleted Profiles page](https://www.klaviyo.com/account/deleted).  For more information on the deletion process, please refer to our [Help Center docs on how to handle GDPR and CCPA deletion requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests#record-gdpr-and-ccpa%20%20-deletion-requests2).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `data-privacy:write`

        :param data_privacy_create_deletion_job_query: (required)
        :type data_privacy_create_deletion_job_query: DataPrivacyCreateDeletionJobQuery
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._request_profile_deletion_serialize(
            data_privacy_create_deletion_job_query=data_privacy_create_deletion_job_query,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': None,
            '4XX': "GetAccounts4XXResponse",
            '5XX': "GetAccounts4XXResponse",
        }
        if _request_auth is not None:
            _request_auth = {'in': 'header', 'key': 'Authorization', 'type': 'api_key', 'value': f'Klaviyo-API-Key {_request_auth}'}
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    # alias of `request_profile_deletion_without_preload_content`
    create_data_privacy_deletion_job_without_preload_content = request_profile_deletion_without_preload_content

    def _uses_sparse_fields(self, args, values) -> Set[str]:
        for arg in args:
             if arg.startswith('fields'):
                 if values[arg] is not None:
                      return True
        return False


    def _replace_type_with_dict_in_response_types_map(self, response_types_map: Dict[str, Optional[str]]) -> Dict[str, Optional[str]]:
        for key, value in response_types_map.items():
            if key.startswith('2'):
                if value is not None:
                    # Replace the Type for this key with a Dict type
                    response_types_map[key] = 'Dict[str, object]'

        return response_types_map

    def _request_profile_deletion_serialize(
        self,
        data_privacy_create_deletion_job_query,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if data_privacy_create_deletion_job_query is not None:
            _body_params = data_privacy_create_deletion_job_query


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.api+json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/vnd.api+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'Klaviyo-API-Key', 
            'OAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/data-privacy-deletion-jobs',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


    # alias of `_request_profile_deletion_serialize`
    _create_data_privacy_deletion_job_serialize = _request_profile_deletion_serialize

