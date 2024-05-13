#!/usr/bin/env python3
""" Documentation """

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from utils import get_json
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient.
    This class contains unit tests for the GithubOrgClient class.
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


    def test_public_repos_url(self):
        """ 
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
            new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test the public_repos method of the GithubOrgClient class.

        Args:
            mock_json (MagicMock): The mock object used to assert the API call.

        Returns:
            None
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method of the GithubOrgClient class.

        Args:
            repo (dict): The repository payload.
            license_key (str): The license key to check.
            expected (bool): The expected result.

        Returns:
            None
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


    @parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            """
            Set up the test class.

            Returns:
                None
            """
            config = {'return_value.json.side_effect':
                    [
                        cls.org_payload, cls.repos_payload,
                        cls.org_payload, cls.repos_payload
                    ]
                    }
            cls.get_patcher = patch('requests.get', **config)

            cls.mock = cls.get_patcher.start()

        def test_public_repos(self):
            """
            Integration test for the public_repos method.

            Returns:
                None
            """
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.org, self.org_payload)
            self.assertEqual(test_class.repos_payload, self.repos_payload)
            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.mock.assert_called()

        def test_public_repos_with_license(self):
            """
            Integration test for the public_repos method with a specific license.

            Returns:
                None
            """
            test_class = GithubOrgClient("google")

            self.assertEqual(test_class.public_repos(), self.expected_repos)
            self.assertEqual(test_class.public_repos("XLICENSE"), [])
            self.assertEqual(test_class.public_repos(
                "apache-2.0"), self.apache2_repos)
            self.mock.assert_called()

        @classmethod
        def tearDownClass(cls):
            """
            Tear down the test class.

            Returns:
                None
            """
            cls.get_patcher.stop()
