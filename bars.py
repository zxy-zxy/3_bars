import sys
import argparse
import math
import json
from json import JSONDecodeError


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath",
        type=str,
        help="Please provide a filepath.",
        required=True
    )
    parser.add_argument(
        "-longitude",
        type=float,
        help="Please input a longitude of current location with format  '.15f'",
        required=True
    )
    parser.add_argument(
        "-latitude",
        type=float,
        help="Please input a latitude of current location with format '.15f'",
        required=True
    )

    return parser


def load_moscow_bars_data(filepath):
    with open(filepath) as file:
        raw_data = file.read()
    moscow_bars_data = json.loads(raw_data)
    return moscow_bars_data


def get_bar_seats_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_biggest_bar(moscow_bars_list):
    return max(
        moscow_bars_list,
        key=lambda x: get_bar_seats_count(x)
    )


def get_smallest_bar(moscow_bars_list):
    return min(
        moscow_bars_list,
        key=lambda x: get_bar_seats_count(x)
    )


def calculate_distance(coordinates, longitude, latitude):
    return math.sqrt(
        (coordinates[0] - longitude) ** 2 + (coordinates[1] - latitude) ** 2
    )


def get_closest_bar(moscow_bars_list, longitude, latitude):
    closest_bar = min(
        moscow_bars_list,
        key=lambda coordinates: calculate_distance(
            coordinates["geometry"]["coordinates"],
            longitude,
            latitude
        )
    )
    return closest_bar


def print_bar(category, bar):
    print("{}: {}".format(category, bar["properties"]["Attributes"]["Name"]))


if __name__ == "__main__":

    args_parser = create_parser()
    args = args_parser.parse_args()

    try:
        moscow_bars_data = load_moscow_bars_data(args.filepath)
    except FileNotFoundError:
        sys.exit("Error has occured while reading data")
    except JSONDecodeError:
        sys.exit("Error has occured while parsing data")

    moscow_bars_list = moscow_bars_data.get("features")
    if moscow_bars_list is None:
        sys.exit("Wrong file format.")

    biggest_bar = get_biggest_bar(moscow_bars_list)
    print_bar("Biggest bar", biggest_bar)
    smallest_bar = get_smallest_bar(moscow_bars_list)
    print_bar("Smallest bar", smallest_bar)
    closest_bar = get_closest_bar(
        moscow_bars_list,
        args.longitude,
        args.latitude
    )
    print_bar("Closest bar", closest_bar)
