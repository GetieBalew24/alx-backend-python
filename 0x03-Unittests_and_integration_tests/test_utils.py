#!/usr/bin/env python3
""" Module the first unit test for utils.access_nested_map"""

import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
from parameterized import parameterized


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