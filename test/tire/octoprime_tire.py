from unittest import TestCase

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(TestCase):
    def test_need_service(self):
        tires = [0, 1, 1, 1]
        tire = OctoprimeTire(tires)
        self.assertTrue(tire.needs_service())

        tires = [0, 0, 1, 1]
        tire = OctoprimeTire(tires)
        self.assertFalse(tire.needs_service())
