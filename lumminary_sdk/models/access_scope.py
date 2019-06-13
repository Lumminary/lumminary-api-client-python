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

from lumminary_sdk.models.customer_address import CustomerAddress  # noqa: F401,E501
from lumminary_sdk.models.customer_name import CustomerName  # noqa: F401,E501


class AccessScope(object):
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
        'name': 'CustomerName',
        'sex': 'str',
        'address': 'CustomerAddress',
        'login': 'str',
        'dataset': 'str',
        'email': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sex': 'sex',
        'address': 'address',
        'login': 'login',
        'dataset': 'dataset',
        'email': 'email'
    }

    def __init__(self, name=None, sex=None, address=None, login=None, dataset=None, email=None):  # noqa: E501
        """AccessScope - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._sex = None
        self._address = None
        self._login = None
        self._dataset = None
        self._email = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sex is not None:
            self.sex = sex
        if address is not None:
            self.address = address
        if login is not None:
            self.login = login
        if dataset is not None:
            self.dataset = dataset
        if email is not None:
            self.email = email

    @property
    def name(self):
        """Gets the name of this AccessScope.  # noqa: E501

        Access to customer name  # noqa: E501

        :return: The name of this AccessScope.  # noqa: E501
        :rtype: CustomerName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessScope.

        Access to customer name  # noqa: E501

        :param name: The name of this AccessScope.  # noqa: E501
        :type: CustomerName
        """

        self._name = name

    @property
    def sex(self):
        """Gets the sex of this AccessScope.  # noqa: E501

        The sex of the customer. One of : ['M', 'F', 'N']  # noqa: E501

        :return: The sex of this AccessScope.  # noqa: E501
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this AccessScope.

        The sex of the customer. One of : ['M', 'F', 'N']  # noqa: E501

        :param sex: The sex of this AccessScope.  # noqa: E501
        :type: str
        """

        self._sex = sex

    @property
    def address(self):
        """Gets the address of this AccessScope.  # noqa: E501

        Access to customer address  # noqa: E501

        :return: The address of this AccessScope.  # noqa: E501
        :rtype: CustomerAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AccessScope.

        Access to customer address  # noqa: E501

        :param address: The address of this AccessScope.  # noqa: E501
        :type: CustomerAddress
        """

        self._address = address

    @property
    def login(self):
        """Gets the login of this AccessScope.  # noqa: E501

        Access to no customer information, just the customer UUID  # noqa: E501

        :return: The login of this AccessScope.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this AccessScope.

        Access to no customer information, just the customer UUID  # noqa: E501

        :param login: The login of this AccessScope.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def dataset(self):
        """Gets the dataset of this AccessScope.  # noqa: E501

        Access to one of the customer's datasets  # noqa: E501

        :return: The dataset of this AccessScope.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this AccessScope.

        Access to one of the customer's datasets  # noqa: E501

        :param dataset: The dataset of this AccessScope.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def email(self):
        """Gets the email of this AccessScope.  # noqa: E501

        Access to customer email  # noqa: E501

        :return: The email of this AccessScope.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccessScope.

        Access to customer email  # noqa: E501

        :param email: The email of this AccessScope.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, AccessScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
