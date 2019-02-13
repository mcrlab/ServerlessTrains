import zeep
from lib.trainapp import TrainApp
from lib.stationlist import StationList
import json
import os

WSDL = os.environ['WSDL']

def stations(event, context):

    stationList = StationList()
    data = stationList.stations()

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps(data)
    }
    return response


def next(event, context):
    response = {}
    try:
        stationList = StationList()

        fromCRS = event['pathParameters']['from'].upper()
        if stationList.validateCRS(fromCRS) is not True:
            raise Exception("CRS Code is invalid")

        toCRS = event['pathParameters']['to'].upper()
        if stationList.validateCRS(toCRS) is not True:
            raise Exception("CRS Code is invalid")

        client = zeep.Client(wsdl=WSDL)
        departures = TrainApp(client).fetchDeparturesForStation(fromCRS, toCRS)

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(departures)
        }
    except Exception as e:
        print(e)
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": str(e)
        }
    finally:
        return response


def iot(event, context):
    response = {}
    try:
        stationList = StationList()

        fromCRS = event['pathParameters']['from'].upper()
        if stationList.validateCRS(fromCRS) is not True:
            raise Exception("CRS Code is invalid")

        toCRS = event['pathParameters']['to'].upper()
        if stationList.validateCRS(toCRS) is not True:
            raise Exception("CRS Code is invalid")
        client = zeep.Client(wsdl=WSDL)
        trains = TrainApp(client).fetchDeparturesForStation(fromCRS, toCRS)
        if len(trains) > 0:
            etd = trains[0]['origin']['etd']
            hour, minute = etd.split(":")
            time = int(hour) * 60 + int(minute)
        else:
            time = ""

        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": time
        }

    except Exception as e:
        response = {
            "statusCode": 500,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": str(e)
        }
    finally:
        return response
