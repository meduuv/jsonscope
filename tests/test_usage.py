import unittest
from jsonscope.core import pretty, validate, walk

class UsageTests(unittest.TestCase):
    def test_pretty(self): self.assertIn('"a": 1', pretty({'a':1}))
    def test_validate(self): self.assertTrue(validate('{"a":1}')[0]); self.assertFalse(validate('{')[0])
    def test_walk(self): self.assertEqual([p for p,_ in walk({'a':[1]})], ['$', '$.a', '$.a[0]'])

if __name__=='__main__': unittest.main()
