from lib.trainapp import TrainApp
from lib.stationlist import StationList
from lib.darwinservice import DarwinService
from lib.utilities import extract_crs
from lib.utilities import build_response_object
from lib.utilities import time_to_integer

import json
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']


def stations(event, context):

    stationList = StationList()
    data = stationList.stations()
    body = json.dumps(data)
    response = build_response_object(200, body);
    return response


def next(event, context):
    response = {}
    try:
        station_list = StationList()
        number_of_departures = 4
        service = DarwinService(WSDL, token)

        from_crs, to_crs = extract_crs(event)
        
        departures = TrainApp(service).next_departures(from_crs, to_crs, number_of_departures)
        data = {
            "departures": departures
        }

        body = json.dumps(data)
        response = build_response_object(200, body);

    except Exception as e:
        body = str(e)
        response = build_response_object(500, body);

    finally:
        return response


def iot(event, context):
    response = {}
    try:
        station_list = StationList()
        service = DarwinService(WSDL, token)
        number_of_departures = 1

        from_crs, to_crs = extract_crs(event)

        trains = TrainApp(service).next_departures(from_crs, to_crs, number_of_departures)

        if len(trains) > 0:
            etd = trains[0]['origin']['etd']
            time = time_to_integer(etd)
        else:
            time = ""

        response = build_response_object(200, time)

    except Exception as e:
        print(e)
        body = str(e)
        response = build_response_object(500, body)

    finally:
        return response

def spread(event, context):
    try:
        service = DarwinService(WSDL, token)
        body = event['body']
        data = json.loads(body)
        trains = []

        for origin in data['from']:
            for destination in data['to']:
                data = TrainApp(service).next_departures(origin, destination, 4)
                trains = trains + data
        
        departures = {
            "departures": trains
        }

        response = build_response_object(200, json.dumps(departures))
    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)
    finally:
        return response
