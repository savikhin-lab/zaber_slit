import os
import sys
import click
import numpy as np
from math import floor
from pathlib import Path
from scipy.interpolate import interp1d
from .stepper import Stepper


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
        cal_file_path = os.environ["ZABERCAL"]
        if cal_file_path is None:
            print("ZABERCAL environment variable not found.")
            sys.exit(-1)
        cal_file_path = Path(cal_file_path)
        cal_data = np.loadtxt(cal_file_path, delimiter=",")
        interp_steps = interp1d(cal_data[:, 0], cal_data[:, 1], kind="cubic")
        steps = floor(interp_steps(new_pos))
        stepper.move(steps)
    else:
        stepper.move(new_pos)
    return


def port_not_found():
    print("Port name not found. Please set the ZABERPORT environment variable.")


cli.add_command(pos)
cli.add_command(move)
