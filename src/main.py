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
def get_model_identification(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_model_identification()
    print(result)
    m.close()


@app.command()
def get_manufacturer_identification(
    address: str, baudrate=460800, timeout=5, debug=False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_manufacturer_identification()
    print(result)
    m.close()


@app.command()
def get_serial_number(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_serial_number()
    print(result)
    m.close()


@app.command()
def get_firmware_version(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_firmware_version()
    print(result)
    m.close()


@app.command()
def get_volume(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_volume()
    print(result)
    m.close()


@app.command()
def set_volume(address: str, volume, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.set_volume(volume)
    print(result)
    m.close()


@app.command()
def improve_tdd(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.improve_tdd()
    print(result)
    m.close()


@app.command()
def enable_echo_suppression(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.enable_echo_suppression()
    print(result)
    m.close()


@app.command()
def disable_echo_suppression(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.disable_echo_suppression()
    print(result)
    m.close()


@app.command()
def get_network_registration_status(
    address: str, baudrate=460800, timeout=5, debug=False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_registration_status()
    print(result)
    m.close()


@app.command()
def get_network_mode(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_mode()
    print(result)
    m.close()


@app.command()
def get_network_name(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_name()
    print(result)
    m.close()


@app.command()
def get_network_operator(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_network_operator()
    print(result)
    m.close()


@app.command()
def get_signal_quality(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality()
    print(result)
    m.close()


@app.command()
def get_signal_quality_db(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality_db()
    print(result)
    m.close()


@app.command()
def get_signal_quality_range(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_signal_quality_range()
    print(result.value)
    m.close()


@app.command()
def get_phone_number(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_phone_number()
    print(result)
    m.close()


@app.command()
def get_sim_status(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sim_status()
    print(result)
    m.close()


@app.command()
def set_network_mode(
    address: str, network_mode: str, baudrate=460800, timeout=5, debug=False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.set_network_mode(NetworkMode[network_mode])
    print(result)
    m.close()


@app.command()
def call(address: str, number: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.call(number)
    print(result)
    m.close()


@app.command()
def answer(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.answer()
    print(result)
    m.close()


@app.command()
def hangup(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.hangup()
    print(result)
    m.close()


@app.command()
def get_sms_list(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sms_list()
    print(result)
    m.close()


@app.command()
def empty_sms(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.empty_sms()
    print(result)
    m.close()


@app.command()
def send_sms(
    address: str, number: str, message: str, baudrate=460800, timeout=5, debug=False
):
    m = Modem(address, baudrate, timeout, debug)
    result = m.send_sms(number, message)
    print(result)
    m.close()


@app.command()
def get_sms(address: str, index: int, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_sms(index)
    print(result)
    m.close()


@app.command()
def delete_sms(address: str, index: int, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.delete_sms(index)
    print(result)
    m.close()


@app.command()
def get_gps_status(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_gps_status()
    print(result)
    m.close()


@app.command()
def start_gps(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.start_gps()
    print(result)
    m.close()


@app.command()
def stop_gps(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.stop_gps()
    print(result)
    m.close()


@app.command()
def get_gps_coordinates(address: str, baudrate=460800, timeout=5, debug=False):
    m = Modem(address, baudrate, timeout, debug)
    result = m.get_gps_coordinates()
    print(result)
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
