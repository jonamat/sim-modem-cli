# sim-modem-cli

A command line interface for SIM modems. It uses the [sim-modem](https://github.com/jonamat/sim-modem) library to communicate with the modem through AT commands. Tested with Simcom SIM7600G-H on Raspberry PI Zero W. The commands could be different for other modems.

## Installation

### From pip

```bash
pip install sim-modem-cli
```

### From releases page

Download the latest release from [here](https://github.com/jonamat/sim-modem-cli/releases).

### From script

```bash
bash <(curl -s https://raw.githubusercontent.com/jonamat/sim-modem-cli/master/install.sh)
```

## Usage

```bash
sim-modem-cli <command> address [<args>...] [--options] 
```

### Options

| Option     | Description          |
| ---------- | -------------------- |
| --help     | Show help message    |
| --version  | Show the version     |
| --baudrate | The baudrate to use. |
| --timeout  | The timeout to use.  |
| --debug    | Enable debug mode.   |

### Commands

| Command                         | Arguments                                  | Description                                         |
| ------------------------------- | ------------------------------------------ | --------------------------------------------------- |
| ***Hardware related commands*** |                                            |                                                     |
| get_model_identification        |                                            | Get the model identification                        |
| get_manufacturer_identification |                                            | Get the manufacturer identification                 |
| get_serial_number               |                                            | Get the serial number                               |
| get_firmware_version            |                                            | Get the firmware version                            |
| get_volume                      |                                            | Get the volume. The volume range is between 0 and 5 |
| set_volume                      | int volume (1-5)                           | Set the volume. The volume must be between 0 and 5  |
| improve_tdd                     |                                            | Decrease TDD Noise effect                           |
| enable_echo_suppression         |                                            | Enable echo suppression                             |
| disable_echo_suppression        |                                            | Disable echo suppression                            |
| ***Network related commands***  |                                            |                                                     |
| get_network_registration_status |                                            | Get the network registration status                 |
| get_network_mode                |                                            | Get the network mode                                |
| get_network_name                |                                            | Get the network name                                |
| get_network_operator            |                                            | Get the network operator                            |
| get_signal_quality              |                                            | Get the signal quality                              |
| get_signal_quality_db           |                                            | Get the signal quality in dB                        |
| get_signal_quality_range        |                                            | Get the signal quality as a range                   |
| get_phone_number                |                                            | Get the phone number                                |
| get_sim_status                  |                                            | Get the SIM status                                  |
| set_network_mode                | auto \| gsm_only \| lte_only \| no_lte     | Set the network                                     |
| ***Calls related commands***    |                                            |                                                     |
| call                            | Number to call (with international prefix) | Call a number                                       |
| answer                          |                                            | Answer a call                                       |
| hangup                          |                                            | Hangup a call                                       |
| ***SMS related commands***      |                                            |                                                     |
| get_sms_list                    |                                            | Get the list of SMS                                 |
| empty_sms                       |                                            | Empty the SMS storage                               |
| send_sms str, message: str      | Number, message                            | Send an SMS                                         |
| get_sms                         | SMS index                                  | Get an SMS by ID                                    |
| delete_sms                      | SMS index                                  | Delete an SMS by ID                                 |
| ***GPS related commands***      |                                            |                                                     |
| get_gps_status                  |                                            | Get the GPS status                                  |
| start_gps                       |                                            | Start the GPS                                       |
| stop_gps                        |                                            | Stop the GPS                                        |
| get_gps_coordinates             |                                            | Get the GPS coordinates                             |



## License

[MIT](LICENSE)