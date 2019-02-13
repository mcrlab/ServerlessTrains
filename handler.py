import zeep
from lib.trainapp import TrainApp
from lib.stationlist import StationList
import json
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']


def extract_CRS(event):
    stationList = StationList()

    fromCRS = event['pathParameters']['from'].upper()
    if stationList.validateCRS(fromCRS) is not True:
        raise Exception("from CRS Code is invalid")

    toCRS = event['pathParameters']['to'].upper()
    if stationList.validateCRS(toCRS) is not True:
        raise Exception("to CRS Code is invalid")

    return fromCRS, toCRS


def build_response_object(status_code, body):
    response = {
        "statusCode": status_code,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": body
    }
    return response


def stations(event, context):

    stationList = StationList()
    data = stationList.stations()
    body = json.dumps(data)
    response = build_response_object(200, body);
    return response


def next(event, context):
    response = {}
    try:

        fromCRS, toCRS = extract_CRS(event)

        client = zeep.Client(wsdl=WSDL)
        departures = TrainApp(client, token).fetch_departures(fromCRS, toCRS)
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
        fromCRS, toCRS = extract_CRS(event)
        client = zeep.Client(wsdl=WSDL)
        trains = TrainApp(client, token).fetch_departures(fromCRS, toCRS)
        if len(trains) > 0:
            etd = trains[0]['origin']['etd']
            hour, minute = etd.split(":")
            time = int(hour) * 60 + int(minute)
        else:
            time = ""

        response = build_response_object(200, time)

    except Exception as e:
        body = str(e)
        response = build_response_object(500, body);

    finally:
        return response
