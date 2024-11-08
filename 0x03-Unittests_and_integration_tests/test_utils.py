#!/usr/bin/env python3
"""
test_utils
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple, expected) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson Class"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: Dict, mock_get) -> None:
        mock_get.return_value.json.return_value = test_payload
        r = get_json(test_url)
        self.assertEqual(r, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize Class"""

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          "a_method", return_value=49) as mocked_method:
            obj = TestClass()
            r = obj.a_property
            self.assertEqual(r, 49)
            mocked_method.assert_called_once()

            cached_result = obj.a_property
            self.assertEqual(cached_result, 49)
            mocked_method.assert_called_once()
