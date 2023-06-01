from abc import ABC, abstractmethod
from servicable import Servicable


class Car(Servicable):
    def __init__(self, battery, engine, tire):
        self.engine = engine
        self.battery = battery
        self.tires = tire

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
