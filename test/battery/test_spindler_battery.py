

from datetime import datetime
import unittest

from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        battery = SpindlerBattery(
            last_service_date=last_service_date,
            current_date=current_date,
        )
        self.assertFalse(battery.needs_service())
        
        last_service_date = current_date.replace(year=current_date.year - 3, month=current_date.month - 1)
        battery = SpindlerBattery(
            last_service_date=last_service_date,
            current_date=current_date,
        )
        self.assertTrue(battery.needs_service())
