from homeassistant.helpers.entity import Entity

class DaikinSensor(Entity):
    def __init__(self, api, device, sensor_type):
        self.api = api
        self.device = device
        self.sensor_type = sensor_type
        self._state = None

    @property
    def name(self):
        return f"{self.device['name']} {self.sensor_type}"

    @property
    def state(self):
        return self._state

    def update(self):
        data = self.api.get_devices()
        for device in data:
            if device["id"] == self.device["id"]:
                self._state = device.get(self.sensor_type)
