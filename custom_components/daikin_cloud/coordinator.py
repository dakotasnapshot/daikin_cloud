from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.core import HomeAssistant
import aiohttp
import asyncio
import logging

_LOGGER = logging.getLogger(__name__)

class DaikinCloudCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, api_client, update_interval):
        super().__init__(
            hass,
            _LOGGER,
            name="Daikin Cloud Coordinator",
            update_interval=update_interval,
        )
        self.api_client = api_client

    async def _async_update_data(self):
        return await self.api_client.get_device_data()
