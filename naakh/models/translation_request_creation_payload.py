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


class TranslationRequestCreationPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TranslationRequestCreationPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cancel': 'bool',
            'instructions': 'str',
            'metadata': 'Metadata',
            'source_language': 'str',
            'target_audience': 'str',
            'target_languages': 'list[str]',
            'text': 'str',
            'tone': 'str',
            'topics': 'list[str]',
            'web_url': 'str'
        }

        self.attribute_map = {
            'cancel': 'cancel',
            'instructions': 'instructions',
            'metadata': 'metadata',
            'source_language': 'source_language',
            'target_audience': 'target_audience',
            'target_languages': 'target_languages',
            'text': 'text',
            'tone': 'tone',
            'topics': 'topics',
            'web_url': 'web_url'
        }

        self._cancel = None
        self._instructions = None
        self._metadata = None
        self._source_language = None
        self._target_audience = None
        self._target_languages = None
        self._text = None
        self._tone = None
        self._topics = None
        self._web_url = None

    @property
    def cancel(self):
        """
        Gets the cancel of this TranslationRequestCreationPayload.


        :return: The cancel of this TranslationRequestCreationPayload.
        :rtype: bool
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """
        Sets the cancel of this TranslationRequestCreationPayload.


        :param cancel: The cancel of this TranslationRequestCreationPayload.
        :type: bool
        """
        self._cancel = cancel

    @property
    def instructions(self):
        """
        Gets the instructions of this TranslationRequestCreationPayload.


        :return: The instructions of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """
        Sets the instructions of this TranslationRequestCreationPayload.


        :param instructions: The instructions of this TranslationRequestCreationPayload.
        :type: str
        """
        self._instructions = instructions

    @property
    def metadata(self):
        """
        Gets the metadata of this TranslationRequestCreationPayload.


        :return: The metadata of this TranslationRequestCreationPayload.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TranslationRequestCreationPayload.


        :param metadata: The metadata of this TranslationRequestCreationPayload.
        :type: Metadata
        """
        self._metadata = metadata

    @property
    def source_language(self):
        """
        Gets the source_language of this TranslationRequestCreationPayload.


        :return: The source_language of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._source_language

    @source_language.setter
    def source_language(self, source_language):
        """
        Sets the source_language of this TranslationRequestCreationPayload.


        :param source_language: The source_language of this TranslationRequestCreationPayload.
        :type: str
        """
        self._source_language = source_language

    @property
    def target_audience(self):
        """
        Gets the target_audience of this TranslationRequestCreationPayload.


        :return: The target_audience of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """
        Sets the target_audience of this TranslationRequestCreationPayload.


        :param target_audience: The target_audience of this TranslationRequestCreationPayload.
        :type: str
        """
        self._target_audience = target_audience

    @property
    def target_languages(self):
        """
        Gets the target_languages of this TranslationRequestCreationPayload.


        :return: The target_languages of this TranslationRequestCreationPayload.
        :rtype: list[str]
        """
        return self._target_languages

    @target_languages.setter
    def target_languages(self, target_languages):
        """
        Sets the target_languages of this TranslationRequestCreationPayload.


        :param target_languages: The target_languages of this TranslationRequestCreationPayload.
        :type: list[str]
        """
        self._target_languages = target_languages

    @property
    def text(self):
        """
        Gets the text of this TranslationRequestCreationPayload.


        :return: The text of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this TranslationRequestCreationPayload.


        :param text: The text of this TranslationRequestCreationPayload.
        :type: str
        """
        self._text = text

    @property
    def tone(self):
        """
        Gets the tone of this TranslationRequestCreationPayload.


        :return: The tone of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._tone

    @tone.setter
    def tone(self, tone):
        """
        Sets the tone of this TranslationRequestCreationPayload.


        :param tone: The tone of this TranslationRequestCreationPayload.
        :type: str
        """
        self._tone = tone

    @property
    def topics(self):
        """
        Gets the topics of this TranslationRequestCreationPayload.


        :return: The topics of this TranslationRequestCreationPayload.
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """
        Sets the topics of this TranslationRequestCreationPayload.


        :param topics: The topics of this TranslationRequestCreationPayload.
        :type: list[str]
        """
        self._topics = topics

    @property
    def web_url(self):
        """
        Gets the web_url of this TranslationRequestCreationPayload.


        :return: The web_url of this TranslationRequestCreationPayload.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """
        Sets the web_url of this TranslationRequestCreationPayload.


        :param web_url: The web_url of this TranslationRequestCreationPayload.
        :type: str
        """
        self._web_url = web_url

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
