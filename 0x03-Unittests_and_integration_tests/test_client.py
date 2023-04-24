#!/usr/bin/env python3
""" Module for testing client
Use @patch as a decorator to make sure get_json is called once with
the expected argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize 
the test with a couple of org examples to pass to GithubOrgClient"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Testing Github org Client """
    #
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """implement the test_org method
        that tests GithubOrgClient.org returns the correct value"""
        GithubOrgClient(input).org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
       
    def test_public_repos_url(self):
        """ Test the result of _public_repos_url
        is the expected one based on the mocked payload
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test = GithubOrgClient('test')
            res = test._public_repos_url
            self.assertEqual(res, payload["repos_url"])
    
    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
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
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)