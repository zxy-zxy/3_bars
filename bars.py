import json
import os
import math

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data


def get_biggest_bar(data):
    return max(data["features"],
               key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def get_smallest_bar(data):
    return min(data["features"],
               key=lambda x: x["properties"]["Attributes"]["SeatsCount"])


def calculate_distance(coordinates, longitude, latitude):
    return math.sqrt((coordinates[0] - longitude) ** 2 + (coordinates[1] - latitude) ** 2)


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(
        data["features"],
        key=(lambda coordinates: calculate_distance(
            coordinates["geometry"]["coordinates"],
            longitude,
            latitude)
             )
    )
    return closest_bar


def get_bar_presentation(bar_dict):
    return "name : {}".format(bar_dict["properties"]["Attributes"]["Name"])


if __name__ == "__main__":
    filename = os.path.join(ROOT_DIR, "data", "bars.json")
    moscow_bars = load_data(filename)
    longitude, latitude = map(float, input().split())
    biggest_bar = get_biggest_bar(moscow_bars)
    print("Biggest bar: {}".format(get_bar_presentation(biggest_bar)))
    smallest_bar = get_smallest_bar(moscow_bars)
    print("Smallest bar: {}".format(get_bar_presentation(smallest_bar)))
    closest_bar = get_closest_bar(moscow_bars, longitude, latitude)
    print("Closest bar: {}".format(get_bar_presentation(closest_bar)))
