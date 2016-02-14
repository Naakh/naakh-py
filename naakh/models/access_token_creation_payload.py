# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AccessTokenCreationPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AccessTokenCreationPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'oauth_client_id': 'str',
            'oauth_client_secret': 'str',
            'password': 'str',
            'phone_number': 'str'
        }

        self.attribute_map = {
            'oauth_client_id': 'oauth_client_id',
            'oauth_client_secret': 'oauth_client_secret',
            'password': 'password',
            'phone_number': 'phone_number'
        }

        self._oauth_client_id = None
        self._oauth_client_secret = None
        self._password = None
        self._phone_number = None

    @property
    def oauth_client_id(self):
        """
        Gets the oauth_client_id of this AccessTokenCreationPayload.


        :return: The oauth_client_id of this AccessTokenCreationPayload.
        :rtype: str
        """
        return self._oauth_client_id

    @oauth_client_id.setter
    def oauth_client_id(self, oauth_client_id):
        """
        Sets the oauth_client_id of this AccessTokenCreationPayload.


        :param oauth_client_id: The oauth_client_id of this AccessTokenCreationPayload.
        :type: str
        """
        self._oauth_client_id = oauth_client_id

    @property
    def oauth_client_secret(self):
        """
        Gets the oauth_client_secret of this AccessTokenCreationPayload.


        :return: The oauth_client_secret of this AccessTokenCreationPayload.
        :rtype: str
        """
        return self._oauth_client_secret

    @oauth_client_secret.setter
    def oauth_client_secret(self, oauth_client_secret):
        """
        Sets the oauth_client_secret of this AccessTokenCreationPayload.


        :param oauth_client_secret: The oauth_client_secret of this AccessTokenCreationPayload.
        :type: str
        """
        self._oauth_client_secret = oauth_client_secret

    @property
    def password(self):
        """
        Gets the password of this AccessTokenCreationPayload.


        :return: The password of this AccessTokenCreationPayload.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AccessTokenCreationPayload.


        :param password: The password of this AccessTokenCreationPayload.
        :type: str
        """
        self._password = password

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccessTokenCreationPayload.


        :return: The phone_number of this AccessTokenCreationPayload.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccessTokenCreationPayload.


        :param phone_number: The phone_number of this AccessTokenCreationPayload.
        :type: str
        """
        self._phone_number = phone_number

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
