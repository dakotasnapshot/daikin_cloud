from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_OFF, SUPPORT_TARGET_TEMPERATURE
from homeassistant.const import TEMP_FAHRENHEIT, ATTR_TEMPERATURE

class DaikinCloudClimate(ClimateEntity):
    def __init__(self, device, api_client):
        self._device = device
        self._api_client = api_client
        self._attr_name = device["name"]
        self._attr_temperature_unit = TEMP_FAHRENHEIT
        self._attr_supported_features = SUPPORT_TARGET_TEMPERATURE

    @property
    def hvac_mode(self):
        return self._device.get("mode")

    @property
    def hvac_modes(self):
        return [HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_OFF]

    @property
    def current_temperature(self):
        return self._device.get("current_temp")

    @property
    def target_temperature(self):
        return self._device.get("target_temp")

    async def async_set_temperature(self, **kwargs):
        if ATTR_TEMPERATURE in kwargs:
            temperature = kwargs[ATTR_TEMPERATURE]
            await self._api_client.set_temperature(self._device["id"], temperature)

    async def async_set_hvac_mode(self, hvac_mode):
        mode_map = {
            HVAC_MODE_HEAT: "heat",
            HVAC_MODE_COOL: "cool",
            HVAC_MODE_OFF: "off",
        }
        await self._api_client.set_mode(self._device["id"], mode_map[hvac_mode])
