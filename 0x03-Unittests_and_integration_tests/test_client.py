#!/usr/bin/env python3
""" Documentation """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient.
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """
        Test the org method of the GithubOrgClient class.

        Args:
            data (str): The name of the organization.
            mock (MagicMock): The mock object used to assert the API call.

        Returns:
            None
        """
        tstcls = GithubOrgClient(data)
        tstcls.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{data}')
