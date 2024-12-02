# daikin_cloud
Daikin Cloud API Integration for Home Assistant

Description
This is a custom integration for Home Assistant, enabling seamless communication with Daikin Cloud-connected thermostats and devices. The integration supports full synchronization of your Daikin devices, allowing control of modes and temperatures directly from Home Assistant. It also keeps your device states up-to-date, even if changes are made physically on the thermostat.

Features
Authentication: Securely connects to the Daikin Cloud API using your username, password, and integrator token.
Token Management: Automatically refreshes API tokens every 3600 seconds to maintain a persistent connection.
Device Discovery: Automatically discovers and integrates all Daikin devices linked to your account.
Device Control: Set modes (Heat, Cool, Off) and temperatures directly from Home Assistant.
Real-Time Synchronization: Automatically polls sensors to sync device states such as current temperature, setpoint, and mode.
Imperial Units: Supports Fahrenheit and imperial units for all sensor readings and controls.
HACS Support: Fully compatible with the Home Assistant Community Store (HACS) for easy installation and updates.
Requirements
A Daikin Cloud account
Integrator token provided by Daikin
Installation
Add this repository to HACS and install the integration.
Restart Home Assistant.
Navigate to Settings > Devices & Services > Integrations, click Add Integration, and select Daikin Cloud API.
Enter your Daikin Cloud credentials and integrator token to complete the setup.
Supported Entities
Sensors:
Current temperature
Setpoint temperature
Operating mode
Controls:
Set mode (Heat, Cool, Off)
Adjust temperature
Contributions
Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License.
