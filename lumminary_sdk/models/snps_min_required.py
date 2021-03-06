# coding: utf-8

"""
    Lumminary API

    A general-purpose API for accessing genomic data  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnpsMinRequired(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'snps': 'list[str]',
        'min_pct': 'int'
    }

    attribute_map = {
        'snps': 'snps',
        'min_pct': 'min_pct'
    }

    def __init__(self, snps=None, min_pct=None):  # noqa: E501
        """SnpsMinRequired - a model defined in Swagger"""  # noqa: E501

        self._snps = None
        self._min_pct = None
        self.discriminator = None

        self.snps = snps
        self.min_pct = min_pct

    @property
    def snps(self):
        """Gets the snps of this SnpsMinRequired.  # noqa: E501

        List of snps that are (possibly partially) required for the Product to be compatible with a Dataset  # noqa: E501

        :return: The snps of this SnpsMinRequired.  # noqa: E501
        :rtype: list[str]
        """
        return self._snps

    @snps.setter
    def snps(self, snps):
        """Sets the snps of this SnpsMinRequired.

        List of snps that are (possibly partially) required for the Product to be compatible with a Dataset  # noqa: E501

        :param snps: The snps of this SnpsMinRequired.  # noqa: E501
        :type: list[str]
        """
        if snps is None:
            raise ValueError("Invalid value for `snps`, must not be `None`")  # noqa: E501

        self._snps = snps

    @property
    def min_pct(self):
        """Gets the min_pct of this SnpsMinRequired.  # noqa: E501

        Minimum required percentage of snps that should be present in the Dataset for compatibility  # noqa: E501

        :return: The min_pct of this SnpsMinRequired.  # noqa: E501
        :rtype: int
        """
        return self._min_pct

    @min_pct.setter
    def min_pct(self, min_pct):
        """Sets the min_pct of this SnpsMinRequired.

        Minimum required percentage of snps that should be present in the Dataset for compatibility  # noqa: E501

        :param min_pct: The min_pct of this SnpsMinRequired.  # noqa: E501
        :type: int
        """
        if min_pct is None:
            raise ValueError("Invalid value for `min_pct`, must not be `None`")  # noqa: E501
        if min_pct is not None and min_pct < 0:  # noqa: E501
            raise ValueError("Invalid value for `min_pct`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_pct = min_pct

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnpsMinRequired):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
