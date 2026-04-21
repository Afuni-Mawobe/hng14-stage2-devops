import unittest
from unittest.mock import MagicMock

class TestRedis(unittest.TestCase):
    def test_redis_mocked(self):
        r = MagicMock()
        r.set('key', 'value')
        r.set.assert_called_with('key', 'value')