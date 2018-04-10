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


if __name__ == "__main__":
    filename = os.path.join(ROOT_DIR, "data", "bars.json")
    data = load_data(filename)
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    closest_bar = get_closest_bar(data, 50, 51)
    print(closest_bar)
