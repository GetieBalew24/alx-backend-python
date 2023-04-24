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
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)

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
    
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()