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


class Metadata(object):
    """
    NOTE: This class is NOT autogenerated.
    It is essentially a dict that you can attach any properties
    """
    def __init__(self):
        self._dct = {}

    def to_dict(self):
        """
        Already a dict so can just return it
        """
        return self._dct

    @property
    def dct(self):
        return self._dct

    @dct.setter
    def dct(self, dct):
        """
        Will set the dct as long as the value associated with the key
        are all strings
        """
        for key, value in dct.iteritems():
            if not isinstance(value, str):
                raise Exception("All the values of the dict need to be string")

        self._dct = dct

    def to_dict(self):
        """
        Will return the dict object because it is a dict
        """
        return self._dict

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
