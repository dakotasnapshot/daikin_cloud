from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN, CONF_USERNAME, CONF_PASSWORD, CONF_INTEGRATOR_TOKEN

class DaikinCloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Daikin Cloud API."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                # Perform authentication here
                await self.hass.async_add_executor_job(
                    authenticate_daikin_cloud,
                    user_input[CONF_USERNAME],
                    user_input[CONF_PASSWORD],
                    user_input[CONF_INTEGRATOR_TOKEN]
                )
                return self.async_create_entry(
                    title="Daikin Cloud", data=user_input
                )
            except Exception:
                errors["base"] = "auth"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_USERNAME): str,
                vol.Required(CONF_PASSWORD): str,
                vol.Required(CONF_INTEGRATOR_TOKEN): str
            }),
            errors=errors
        )
