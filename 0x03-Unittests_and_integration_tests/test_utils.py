#!/usr/bin/env python3
""" Module the first unit test for utils.access_nested_map"""

import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """ Class for Testing Access Nested Map to test that the method  """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    
    def test_access_nested_map(self, nested_map, path, expected):
        """ TestAccessNestedMap.test_access_nested_map method to
        test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)
        
    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ the  assertRaises context manager to test that a KeyError 
        is raised for the inputs (use @parameterized.expand)"""
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(exc.exception))
class TestGetJson(unittest.TestCase):
    """ This code creates a TestGetJson class and defines a single test method, 
    test_get_json, that uses the @patch decorator to patch the requests.
    get function with a mock object."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ method to test that utils.get_json
        returns the expected result.
        """
        #Test that utils.get_json returns the expected result."
        config = {'json.return_value': test_payload}
        # Test that utils.get_json returns the expected result."
        with patch("requests.get", return_value=Mock(**config)) as get_request:
            self.assertEqual(get_json(test_url), test_payload)
            get_request.assert_called_once_with(test_url)
            
            
class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize mplement the TestMemoize(unittest.TestCase)
    class with a test_memoize method."""

    def test_memoize(self):
        """ The correct result is returned but a_method is only called once using
        assert_called_once
        """
        class TestClass:
            """ Test Class with memoize """
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()