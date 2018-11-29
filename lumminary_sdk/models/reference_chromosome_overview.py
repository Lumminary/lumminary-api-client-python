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


class ReferenceChromosomeOverview(object):
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
        'reference_accession': 'str'
    }

    attribute_map = {
        'reference_accession': 'reference_accession'
    }

    def __init__(self, reference_accession=None):  # noqa: E501
        """ReferenceChromosomeOverview - a model defined in Swagger"""  # noqa: E501

        self._reference_accession = None
        self.discriminator = None

        self.reference_accession = reference_accession

    @property
    def reference_accession(self):
        """Gets the reference_accession of this ReferenceChromosomeOverview.  # noqa: E501

        The versioned reference chromosome accession  # noqa: E501

        :return: The reference_accession of this ReferenceChromosomeOverview.  # noqa: E501
        :rtype: str
        """
        return self._reference_accession

    @reference_accession.setter
    def reference_accession(self, reference_accession):
        """Sets the reference_accession of this ReferenceChromosomeOverview.

        The versioned reference chromosome accession  # noqa: E501

        :param reference_accession: The reference_accession of this ReferenceChromosomeOverview.  # noqa: E501
        :type: str
        """
        if reference_accession is None:
            raise ValueError("Invalid value for `reference_accession`, must not be `None`")  # noqa: E501
        if reference_accession is not None and len(reference_accession) < 1:
            raise ValueError("Invalid value for `reference_accession`, length must be greater than or equal to `1`")  # noqa: E501

        self._reference_accession = reference_accession

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
        if not isinstance(other, ReferenceChromosomeOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
