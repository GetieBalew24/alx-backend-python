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
            """Tests public_repos_url` property."""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock, ) as mock_org:
            mock_org.return_value = {'repos_url': "https://api.github.com/users/google/repos", }
            self.assertEqual(GithubOrgClient("google")._public_repos_url, "https://api.github.com/users/google/repos", )