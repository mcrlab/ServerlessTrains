import zeep
from lib.trainapp import TrainApp
from lib.stationlist import StationList
from lib.utilities import extract_CRS
from lib.utilities import build_response_object
from lib.darwinservice import DarwinService

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
        fromCRS, toCRS = extract_CRS(event, station_list)

        service = DarwinService(WSDL, token)
        departures = TrainApp(service).fetch_departures(fromCRS, toCRS)
        body = json.dumps(departures)
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
        fromCRS, toCRS = extract_CRS(event, station_list)
        service = DarwinService(WSDL, token)
        data = TrainApp(service).fetch_departures(fromCRS, toCRS)
        trains = data['departures'];
        if len(trains) > 0:
            etd = trains[0]['origin']['etd']
            hour, minute = etd.split(":")
            time = int(hour) * 60 + int(minute)
        else:
            time = ""

        response = build_response_object(200, time)

    except Exception as e:
        print(e)
        body = str(e)
        response = build_response_object(500, body);

    finally:
        return response
