
from unittest import TestCase
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(TestCase):
    def test_needs_service(self):
        warn_light_is_on = False
        engine = SternmanEngine(warn_light_is_on)
        self.assertFalse(engine.needs_service())
        
        
        warn_light_is_on = True
        engine = SternmanEngine(warn_light_is_on)
        self.assertTrue(engine.needs_service())