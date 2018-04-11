import sys
import math
import json
from json import JSONDecodeError


def load_data(filepath):
    try:
        with open(filepath) as file:
            moscow_bars_raw = file.read()
    except IOError as e:
        print("Error has occured while opening the file: {}".format(e))
        sys.exit(1)
    try:
        moscow_bars = json.loads(moscow_bars_raw)
    except JSONDecodeError as e:
        print("Error has occured while reading the data: {}".format(e))
        sys.exit(1)

    return moscow_bars


def get_information_about_capacity(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_biggest_bar(moscow_bars):
    return max(
        moscow_bars["features"],
        key=lambda x: get_information_about_capacity(x)
    )


def get_smallest_bar(moscow_bars):
    return min(
        moscow_bars["features"],
        key=lambda x: get_information_about_capacity(x)
    )


def calculate_distance(coordinates, longitude, latitude):
    return math.sqrt((coordinates[0] - longitude) ** 2 + (coordinates[1] - latitude) ** 2)


def get_closest_bar(moscow_bars, longitude, latitude):
    closest_bar = min(
        moscow_bars["features"],
        key=lambda coordinates: calculate_distance(
            coordinates["geometry"]["coordinates"],
            longitude,
            latitude
        )
    )
    return closest_bar


def get_bar_presentation(bar_dict):
    return "{}".format(bar_dict["properties"]["Attributes"]["Name"])


if __name__ == "__main__":
    filename = input("Please input filename: ")
    moscow_bars_list = load_data(filename)
    try:
        longitude, latitude = map(float, input("Please input longitude and lattitude divided by space: ").split())
    except ValueError as e:
        print("Error has occured while parsing the data: {}".format(e))
        sys.exit(1)
    biggest_bar = get_biggest_bar(moscow_bars_list)
    print("Biggest bar: {}".format(get_bar_presentation(biggest_bar)))
    smallest_bar = get_smallest_bar(moscow_bars_list)
    print("Smallest bar: {}".format(get_bar_presentation(smallest_bar)))
    closest_bar = get_closest_bar(moscow_bars_list, longitude, latitude)
    print("Closest bar: {}".format(get_bar_presentation(closest_bar)))
