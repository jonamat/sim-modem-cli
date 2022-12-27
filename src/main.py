import json
import typer
from sim_modem import Modem, NetworkMode, SignalQuality
import pkg_resources

app = typer.Typer(
    add_completion=False,
    help="Manage your SIM modem easily",
    name="sim-modem-cli",
    no_args_is_help=True,
)

@app.command()
def get_model_identification(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_model_identification()
    print(f"Model: {result}")
    m.close()


@app.command()
def get_manufacturer_identification(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_manufacturer_identification()
    print(f"Manufacturer: {result}")
    m.close()


@app.command()
def get_serial_number(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_serial_number()
    print(f"Serial number: {result}")
    m.close()


@app.command()
def get_firmware_version(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_firmware_version()
    print(f"Firmware version: {result}")
    m.close()


@app.command()
def get_volume(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_volume()
    print(f"Volume: {result}")
    m.close()


@app.command()
def set_volume(
    address: str, volume, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.set_volume(volume)
    print("Done")
    m.close()


@app.command()
def improve_tdd(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.improve_tdd()
    print(result)
    m.close()


@app.command()
def enable_echo_suppression(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.enable_echo_suppression()
    print(result)
    m.close()


@app.command()
def disable_echo_suppression(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.disable_echo_suppression()
    print("Done")
    m.close()


@app.command()
def get_network_registration_status(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_registration_status()
    print("Done")
    m.close()


@app.command()
def get_network_mode(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_mode()
    print("Done")
    m.close()


@app.command()
def get_network_name(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_name()
    print(f"Network name: {result}")
    m.close()


@app.command()
def get_network_operator(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_operator()
    print(f"Network operator: {result}")
    m.close()


@app.command()
def get_signal_quality(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality()
    print(f"Signal quality: {result}")
    m.close()


@app.command()
def get_signal_quality_db(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality_db()
    print(f"Signal quality in decibels: {result}")
    m.close()


@app.command()
def get_signal_quality_range(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality_range()
    print(f"Signal quality: {result.name}")
    m.close()


@app.command()
def get_phone_number(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_phone_number()
    print(f"Phone number: {result}")
    m.close()


@app.command()
def get_sim_status(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sim_status()
    print(f"SIM status: {result}")
    m.close()


@app.command()
def set_network_mode(
    address: str,
    network_mode: str,
    baudrate: int = 460800,
    timeout: int = 5,
    debug: bool = False,
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.set_network_mode(NetworkMode[network_mode])
    print(f"Network mode set to: {result}")
    m.close()


@app.command()
def call(
    address: str,
    number: str,
    baudrate: int = 460800,
    timeout: int = 5,
    debug: bool = False,
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.call(number)
    print(f"Calling {number}...")
    m.close()


@app.command()
def answer(address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.answer()
    print("Done")
    m.close()


@app.command()
def hangup(address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.hangup()
    print("Done")
    m.close()


@app.command()
def get_sms_list(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sms_list()
    json_result = json.dumps(result, indent=4)
    print(f"SMS list: {json_result}")
    m.close()


@app.command()
def empty_sms(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.empty_sms()
    print("Done")
    m.close()


@app.command()
def send_sms(
    address: str,
    number: str,
    message: str,
    baudrate: int = 460800,
    timeout: int = 5,
    debug: bool = False,
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.send_sms(number, message)
    print("Done")
    m.close()


@app.command()
def get_sms(
    address: str,
    index: int,
    baudrate: int = 460800,
    timeout: int = 5,
    debug: bool = False,
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sms(index)
    json_result = json.dumps(result, indent=4)
    print(f"SMS: {json_result}")
    m.close()


@app.command()
def delete_sms(
    address: str,
    index: int,
    baudrate: int = 460800,
    timeout: int = 5,
    debug: bool = False,
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.delete_sms(index)
    print("Done")
    m.close()


@app.command()
def get_gps_status(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_gps_status()
    print(f"GPS status: {result}")
    m.close()


@app.command()
def start_gps(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.start_gps()
    print("Done")
    m.close()


@app.command()
def stop_gps(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.stop_gps()
    print("Done")
    m.close()


@app.command()
def get_gps_coordinates(
    address: str, baudrate: int = 460800, timeout: int = 5, debug: bool = False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_gps_coordinates()
    print(f"GPS coordinates: {result}")
    m.close()


def version_callback(value: bool):
    if value:
        version = pkg_resources.get_distribution("sim-modem-cli").version
        typer.echo(f"sim-modem-cli, version {version}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the sim-modem-cli version information",
    )
):
    ...


if __name__ == "__main__":
    app()
