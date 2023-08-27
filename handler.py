from lib.trainapp import TrainApp
from lib.stationlist import StationList
from lib.darwinservice import DarwinService
from mocks.mock_darwin_service import MockDarwinService

from lib.utilities import extract_crs, time_to_integer
from lib.utilities import build_response_object
from lib.encoders import ServiceListEncoder, SimpleEncoder

from datetime import datetime
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
            response = build_response_object(200, time_to_integer(departures[0].estimated_departure_time()))
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
        routes = data['routes']

        now = datetime.now()

        current_time = now.strftime("%H:%M")
        number_of_departures = int(data['limit'])

        if not isinstance(routes, list):
            raise Exception("Routes not provided")

        if number_of_departures == 0:
            raise Exception("No limit specified")

        departures = TrainApp(service).multiple_departures(routes)

        data = ServiceListEncoder().to_json(departures)

        response = build_response_object(200, json.dumps({
            "current_time": current_time,
            "departures" : data[0:number_of_departures]
        }))
    
    except Exception as e:
        body = str(e)
        response = build_response_object(500, body)

    finally:
        return response
