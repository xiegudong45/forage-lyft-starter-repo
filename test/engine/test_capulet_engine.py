
from datetime import datetime
from unittest import TestCase

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(TestCase):
    def test_needs_service(self):
        last_service_mileage = 500
        current_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
        
        
        last_service_mileage = 500
        current_mileage = 50000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())