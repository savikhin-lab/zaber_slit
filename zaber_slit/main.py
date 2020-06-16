import os
import sys
import click
from .stepper import Stepper


WMAP = {
    780: 226996,
    785: 227897,
    790: 228712,
    795: 230259,
    800: 231322,
    805: 232303,
    810: 233216,
    815: 234255,
    820: 235493,
    825: 236728,
    830: 237581,
    835: 238474,
    840: 239750,
    845: 240587,
    850: 241487,
}


@click.group()
def cli():
    pass


@click.command()
@click.option("-l", "loop", is_flag=True, help="Print the position in an indefinite loop.")
def pos(loop):
    """Report the current position of the stepper motor.
    """
    try:
        port = os.environ["ZABERPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    stepper = Stepper(port)
    if loop:
        while True:
            print(f"{stepper.pos()}")
    else:
        print(f"{stepper.pos()}")
    return


@click.command()
@click.argument("new_pos", type=click.INT)
@click.option("-w", "--wavelength", is_flag=True, help="Move to a specific wavelength.")
def move(new_pos, wavelength):
    """Send the stepper to a new position.

    The default units for position are steps of the stepper motor.
    """
    try:
        port = os.environ["ZABERPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    stepper = Stepper(port)
    if wavelength:
        try:
            steps = WMAP[new_pos]
        except KeyError:
            print("Wavelengths are only available in 5nm steps on the interval [780, 850]nm.")
            sys.exit(-1)
        stepper.move(220000)
        stepper.move(steps)
    else:
        stepper.move(new_pos)
    return


def port_not_found():
    print("Port name not found. Please set the ZABERPORT environment variable.")


cli.add_command(pos)
cli.add_command(move)
