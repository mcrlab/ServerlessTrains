from lib.trainapp import TrainApp
from lib.stationlist import StationList
from lib.darwinservice import DarwinService
from mocks.mock_darwin_service import MockDarwinService

from lib.utilities import extract_crs
from lib.utilities import build_response_object
from lib.encoders import ServiceListEncoder, SimpleEncoder

import json
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']


def stations(event, context):
    try:
        stationList = StationList()
        data = stationList.stations()
        body = json.dumps(data)
        response = build_response_object(200, body);
    
    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)

    finally:
        return response

def iot(event, context):
    try:
        number_of_departures = 1
        service = DarwinService(WSDL, token)

        from_crs, to_crs = extract_crs(event)
        departures = TrainApp(service).next_departures(from_crs, to_crs, number_of_departures)
        if(len(departures) > 0):
            response = build_response_object(200, departures[0].estimated_departure_time())
        else:
            response = build_response_object(200, -1)
    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)
    finally:
        return response

def next(event, context):
    try:
        number_of_departures = 4
        service = DarwinService(WSDL, token)
        from_crs, to_crs = extract_crs(event)

        departures = TrainApp(service).next_departures(from_crs, to_crs, number_of_departures)

        data = {
            "departures" : ServiceListEncoder().to_json(departures)
        }

        response = build_response_object(200, json.dumps(data))

    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)

    finally:
        return response


def spread(event, context):
    try:
        service = DarwinService(WSDL, token)
        body = event['body']
        data = json.loads(body)

        from_crs_list        = data['from']
        to_crs_list          = data['to']
        number_of_departures = int(data['limit'])

        if not isinstance(from_crs_list, list):
            raise Exception("From CRS is not a list")

        if not isinstance(to_crs_list, list):
            raise Exception("To CRS is not a list")

        if number_of_departures == 0:
            raise Exception("No limit specified")

        departures = TrainApp(service).multiple_departures(from_crs_list, to_crs_list)

        data = SimpleEncoder().to_json(departures)

        response = build_response_object(200, json.dumps(data[0:number_of_departures]))
    
    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)

    finally:
        return response
