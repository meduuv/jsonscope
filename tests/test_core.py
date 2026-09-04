import unittest

from jsonscope.core import compact, format_json, get_path, inspect, validate


class JsonScopeTests(unittest.TestCase):
    def test_validate(self):
        self.assertTrue(validate('{"a": 1}'))
        self.assertFalse(validate('{bad'))

    def test_format_and_compact(self):
        value = {"a": [1, 2]}
        self.assertIn("\n", format_json(value))
        self.assertEqual(compact(value), '{"a":[1,2]}')

    def test_path(self):
        value = {"user": {"name": "medu"}, "items": ["a", "b"]}
        self.assertEqual(get_path(value, "user.name"), "medu")
        self.assertEqual(get_path(value, "items.1"), "b")

    def test_inspect(self):
        self.assertEqual(inspect({"a": 1})["type"], "object")
        self.assertEqual(inspect([1])["items"], 1)


if __name__ == "__main__":
    unittest.main()
