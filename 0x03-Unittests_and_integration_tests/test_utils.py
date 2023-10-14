#!/usr/bin/env python3

"""First test case"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""

@parameterized.expand(
   [
      ({"a": 1}, ("a",), 1),
      ({"a": {"b": 2}}, ("a",), {"b": 2}),
      ({"a": {"b": 2}}, ("a", "b"), 2)
   ]
)
def test_access_nested_map(self, nested_map, path, expected_output):
    "test outcome"
    result = access_nested_map(nested_map, path)
    self.assertEqual(result, expected_output)