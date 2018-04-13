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
    try:
        with open(filepath) as file:
            raw_data = file.read()
    except FileNotFoundError:
        return None
    try:
        moscow_bars_data = json.loads(raw_data)
        return moscow_bars_data
    except JSONDecodeError:
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


def get_found_bar_presentation(found_bar):
    return found_bar["properties"]["Attributes"]["Name"]


if __name__ == "__main__":
    args_parser = create_parser()
    args = args_parser.parse_args()

    filepath = args.filepath
    longitude = args.longitude
    latitude = args.latitude

    moscow_bars_data = load_moscow_bars_data(filepath)
    if moscow_bars_data is None:
        sys.exit('Error has occured while reading data.')

    moscow_bars_list = moscow_bars_data.get("features")
    if moscow_bars_list is None:
        sys.exit('Wrong file format.')

    biggest_bar = get_biggest_bar(moscow_bars_list)
    smallest_bar = get_smallest_bar(moscow_bars_list)
    closest_bar = get_closest_bar(
        moscow_bars_list,
        longitude,
        latitude
    )

    print(
        "\n".join(
            map(
                lambda x:
                "Category: {}, name: ".format(
                    x[0],
                    get_found_bar_presentation(x[1])
                ),
                [
                    ("Biggest bar", biggest_bar),
                    ("Smallest bar", smallest_bar),
                    ("Closest bar", closest_bar)
                ]
            )
        )
    )
