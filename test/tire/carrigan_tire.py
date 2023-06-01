from unittest import TestCase

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(TestCase):
    def test_need_service(self):
        tire = [0.9, 0.4, 0, 0]
        tire = CarriganTire(tire)
        self.assertTrue(tire.needs_service())
        tires = [0, 0, 0.8, 0.8999]
        tire = CarriganTire(tires)
        self.assertFalse(tire.needs_service())