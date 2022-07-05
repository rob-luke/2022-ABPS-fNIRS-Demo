# This script implements a single condition and control
# block design fNIRS experiment.
#
# The participant is asked to perform an action at random
# times. Between actions the participant should rest, and
# during this time they will see a cross. There is also a
# control condition, that the participant will not be aware of.
#
# The experiment also provides some niceties such as saving
# the configuration so the experiment can be reproduced.
# And it provides introductory instructions to the participant.
#
# Example execution:
#    python experiment.py --subject=RL --session=01 --run=1
# You will then be prompted to press enter to start the
# experiment. Start all the other aspects of your experiment
# first (recording device, LSL streamer, etc), and then press enter
# to run the experiment.

import datetime
import random
import time
from os import system

import click
import yaml

import pyxid2


VERSION = 1
TASK = "fingertapping"


def _update_text_and_marker(text, marker, outlet):
    system('clear')
    for n in range(20):
        print("")
    print(text.center(180))
    for n in range(20):
        print("")
    mask = 2 ** marker
    outlet.activate_line(bitmask=mask)


def _save_run_parameters(params):
    """Save the experimental parameters to enable reproducibility."""
    fname = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    fname = f"{fname}-{params['subject']}-{params['session']}-{params['run']}-{params['task']}.yaml"
    with open(fname, "w") as outfile:
        yaml.dump(params, outfile, default_flow_style=False)


@click.command()
@click.option(
    "--subject",
    type=str,
    required=True,
    help="Subject ID.",
)
@click.option(
    "--session",
    type=str,
    required=True,
    help="Session ID.",
)
@click.option(
    "--run",
    type=int,
    required=True,
    help="Run index.",
)
@click.option(
    "--isi-minimum",
    type=float,
    default=8.0,
    help="Inter-stimulus interval minimum time in seconds.",
)
@click.option(
    "--isi-maximum",
    type=float,
    default=15.0,
    help="Inter-stimulus interval maximum time in seconds.",
)
@click.option(
    "--condition-duration-minimum",
    type=float,
    default=4.0,
    help="Minimum duration that the condition is presented in seconds.",
)
@click.option(
    "--condition-duration-maximum",
    type=float,
    default=4.0,
    help="Maximum duration that the condition is presented in seconds.",
)
@click.option(
    "--condition-repeats",
    type=int,
    default=10,
    help="The number of times each condition is repeated.",
)
@click.option(
    "--random-seed",
    type=str,
    default="",
    help="Random seed to allow replication of the experiment",
)
def main(
    isi_minimum: float,
    isi_maximum: float,
    condition_duration_minimum: float,
    condition_duration_maximum: float,
    condition_repeats: int,
    subject: str,
    session: str,
    run: int,
    random_seed: str,
):
    params = click.get_current_context().params
    if not random_seed:
        params["random_seed"] = subject + session + str(run)
    print(params["random_seed"])
    params["experiment_version"] = VERSION
    params["task"] = TASK
    params["datetime"] = datetime.datetime.now().isoformat()
    _save_run_parameters(params)
    random.seed(params["random_seed"])

    conditions = {3: "+", 4: "Right"}

    # Set up c-pod connection
    devices = pyxid2.get_xid_devices()
    dev = devices[0]  # get the first device to use
    print(f"Connected to device: {dev}")
    dev.reset_base_timer()
    dev.reset_rt_timer()
    dev.set_pulse_duration(300)

    input("Press Enter when you are ready to start the experiment...")
    trials = list(conditions.keys()) * condition_repeats
    random.shuffle(trials)

    intro_text = (
        "Watch the screen and tap your thumb to fingers in turn on the same hand when "
        "instructed to. The screen will tell you which hand to tap with."
        "\nPerform the action for the duration that it is shown on the screen, "
        "and relax when the cross reappears."
    )

    _update_text_and_marker(intro_text, 1, dev)
    time.sleep(3.0)
    _update_text_and_marker("+", 2, dev)
    time.sleep(3.0)

    for trial in trials:

        _update_text_and_marker("+", 2, dev)
        time.sleep(random.uniform(isi_minimum, isi_maximum))

        _update_text_and_marker(conditions[trial], trial, dev)
        time.sleep(
            random.uniform(condition_duration_minimum,
                           condition_duration_maximum)
        )

    # End the experiment
    _update_text_and_marker("+", 2, dev)
    time.sleep(5)


if __name__ == "__main__":
    main()
