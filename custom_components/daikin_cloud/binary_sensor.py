from homeassistant.components.binary_sensor import BinarySensorEntity

class DaikinCloudBinarySensor(BinarySensorEntity):
    def __init__(self, device, api_client):
        self._device = device
        self._api_client = api_client
        self._attr_name = f"{device['name']} Connectivity"
        self._attr_is_on = device.get("connected", False)

    @property
    def device_class(self):
        return "connectivity"

    async def async_update(self):
        self._attr_is_on = await self._api_client.get_device_status(self._device["id"])
