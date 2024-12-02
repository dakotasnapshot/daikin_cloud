import requests
from .const import API_URL

class DaikinCloudAPI:
    def __init__(self, config):
        self.username = config["username"]
        self.password = config["password"]
        self.integrator_token = config["integrator_token"]
        self.access_token = None

    def authenticate(self):
        """Authenticate with the Daikin Cloud API."""
        response = requests.post(
            f"{API_URL}/users/auth/login",
            json={
                "email": self.username,
                "password": self.password
            },
            headers={"Integrator-Token": self.integrator_token}
        )
        response.raise_for_status()
        self.access_token = response.json().get("accessToken")

    def get_devices(self):
        """Get devices from the API."""
        response = requests.get(
            f"{API_URL}/deviceData",
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
        response.raise_for_status()
        return response.json()

    def set_device_mode(self, device_id, mode):
        """Set the mode of a device."""
        requests.post(
            f"{API_URL}/deviceData/{device_id}",
            json={"mode": mode},
            headers={"Authorization": f"Bearer {self.access_token}"}
        )

    def set_device_temperature(self, device_id, temperature):
        """Set the temperature of a device."""
        requests.post(
            f"{API_URL}/deviceData/{device_id}",
            json={"cspHome": temperature},
            headers={"Authorization": f"Bearer {self.access_token}"}
        )
