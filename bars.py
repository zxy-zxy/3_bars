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
        help="Please input a longitude of current location with format  \".15f\"",
        required=True
    )
    parser.add_argument(
        "-latitude",
        type=float,
        help="Please input a latitude of current location with format \".15f\"",
        required=True
    )

    return parser


def load_data(filepath):
    try:
        with open(filepath) as file:
            moscow_bars_raw_data = file.read()
            return moscow_bars_raw_data
    except FileNotFoundError as e:
        return None


def read_data(raw_data):
    try:
        moscow_bars_data = json.loads(raw_data)
        return moscow_bars_data
    except JSONDecodeError as e:
        return None


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


def get_found_bars_presentation(found_bars):
    return "\n".join(
        map(
            lambda x:
            "Category: {}, Name: {}".format(
                x[0],
                x[1]["properties"]["Attributes"]["Name"]
            ),
            found_bars
        )
    )


if __name__ == "__main__":
    args_parser = create_parser()
    args = args_parser.parse_args()

    filepath = args.filepath
    longitude = args.longitude
    latitude = args.latitude

    moscow_bars_raw_data = load_data(filepath)
    if moscow_bars_raw_data is None:
        sys.exit('File "{}" not found.'.format(filepath))

    moscow_bars_data = read_data(moscow_bars_raw_data)
    if moscow_bars_data is None:
        sys.exit('Error has occured while reading data.')

    if not "features" in moscow_bars_data.keys():
        sys.exit('Wrong file format.')

    moscow_bars_list = moscow_bars_data["features"]

    biggest_bar = get_biggest_bar(moscow_bars_list)
    smallest_bar = get_smallest_bar(moscow_bars_list)
    closest_bar = get_closest_bar(
        moscow_bars_list,
        longitude,
        latitude
    )

    print(
        get_found_bars_presentation(
            [
                ("Biggest bar", biggest_bar),
                ("Smallest bar", smallest_bar),
                ("Closest bar", closest_bar)
            ]
        )
    )
