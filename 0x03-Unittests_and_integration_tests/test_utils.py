#!/usr/bin/env python3
""" unittest: use parameterized to make it easy"""
import unittest
import requests
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for the access_nested_map function.
    """

    @parameterized.expand([
        # ("Case1",{"a": 1}, ("a",), 1) use like this to make descriptive
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        # in test methods we can add new arg to track the cases bynames
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with different inputs.

        Args:
            name (str): The name of the test case.
            nested_map (dict): The nested map to access.
            path (tuple): The path to the desired value.
            expected: The expected value.

        Returns:
            None
        """
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test case to verify that accessing a
        nested map with an invalid path raises an exception.

        Args:
            nested_map (dict): The nested map to be accessed.
            path (list): The path to the desired value in the nested map.
            expected (Exception): The expected exception to be raised.

        Raises:
            AssertionError: If the expected exception is not raised.

        Returns:
            None
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test case class for testing the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test the get_json function.

        Args:
            url (str): The URL to make the GET request to.
            payload (dict): The expected JSON payload.

        Returns:
            None
        """
        with patch('requests.get') as mock_get:
            mock_res = Mock()
            mock_res.json.return_value = payload
            mock_get.return_value = mock_res

            res = get_json(url)

            mock_get.assert_called_once_with(url)

            self.assertEqual(res, payload)
