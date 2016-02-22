# coding: utf-8

"""
TranslateApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TranslateApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_translation_request(self, translation_request_creation_payload, authorization, **kwargs):
        """
        Creates a new Translation Request
        Create translation request

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_translation_request(translation_request_creation_payload, authorization, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TranslationRequestCreationPayload translation_request_creation_payload: TranslationRequestCreationPayload (required)
        :param str authorization: Access token required to access the API (required)
        :return: TranslationRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['translation_request_creation_payload', 'authorization']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_translation_request" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'translation_request_creation_payload' is set
        if ('translation_request_creation_payload' not in params) or (params['translation_request_creation_payload'] is None):
            raise ValueError("Missing the required parameter `translation_request_creation_payload` when calling `create_translation_request`")
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_translation_request`")

        resource_path = '/translate/'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']

        form_params = {}
        files = {}

        body_params = None
        if 'translation_request_creation_payload' in params:
            body_params = params['translation_request_creation_payload']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='TranslationRequest',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
