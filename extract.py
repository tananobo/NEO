
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_list = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            neo_list.append(NearEarthObject(**elem))
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, "r") as f:
        read = json.load(f)
        approach_list = []
        data_attribute_name = read["fields"]
        data = read['data']
        for d in data:
            tmp = {}
            tmp[data_attribute_name[0]] = d[0]
            tmp[data_attribute_name[3]] = d[3]
            tmp[data_attribute_name[4]] = float(
                d[4]) if data_attribute_name[4] != "" else float('nan')
            tmp[data_attribute_name[7]] = float(
                d[7]) if data_attribute_name[7] != "" else float('nan') 
            approach_list.append(CloseApproach(**tmp))
    return approach_list



