from unittest import TestCase

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(TestCase):
    def test_needs_service(self):
        last_service_mileage = 500
        current_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

        last_service_mileage = 500
        current_mileage = 80000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
