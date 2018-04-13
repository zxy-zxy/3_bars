import sys
import argparse
import math
import json
from json import JSONDecodeError


def process_user_input():
    args_parser = create_parser()
    args = args_parser.parse_args()

    filepath = args.filepath
    longitude = args.longitude
    latitude = args.latitude

    return filepath, longitude, latitude


def process_moscow_bars_list(moscow_bars_list):
    biggest_bar = get_biggest_bar(moscow_bars_list)
    smallest_bar = get_smallest_bar(moscow_bars_list)
    closest_bar = get_closest_bar(
        moscow_bars_list,
        longitude,
        latitude
    )
    return [
        ("Biggest bar", biggest_bar),
        ("Smallest bar", smallest_bar),
        ("Closest bar", closest_bar)
    ]


def print_moscow_bars(moscow_bars_list_to_print):
    for (category, bar) in moscow_bars_list_to_print:
        print("Category: {}, name: {}".format(
            category,
            get_found_bar_presentation(bar))
        )


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


def get_found_bar_presentation(found_bar):
    return found_bar["properties"]["Attributes"]["Name"]


if __name__ == "__main__":

    filepath, longitude, latitude = process_user_input()

    try:
        moscow_bars_data = load_moscow_bars_data(filepath)
    except FileNotFoundError:
        sys.exit("Error has occured while reading data")
    except JSONDecodeError:
        sys.exit("Error has occured while parsing data")

    moscow_bars_list = moscow_bars_data.get("features")
    if moscow_bars_list is None:
        sys.exit("Wrong file format.")

    moscow_bars_list_to_print = process_moscow_bars_list(moscow_bars_list)

    print_moscow_bars(moscow_bars_list_to_print)
