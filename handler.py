from lib.trainapp import TrainApp
from lib.stationlist import StationList

import json

def endpoint(event, context):
    response = {}
    try:
        stationList = StationList()

        fromCRS = event['pathParameters']['from'].upper()
        if stationList.validateCRS(fromCRS) is not True:
            raise Exception("CRS Code is invalid")

        toCRS = event['pathParameters']['to'].upper()
        if stationList.validateCRS(toCRS) is not True:
            raise Exception("CRS Code is invalid")


        trains = TrainApp().fetchDeparturesForStation(fromCRS, toCRS)
        sorted_trains = sorted(trains, key=lambda k:k['std'])
        data = {
            "departures": sorted_trains
        }

        response = {
            "statusCode": 200,
            "headers": {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(data)
        }
    except Exception as e:
        print(e)
        response = {
            "statusCode": 200,
            "headers": {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Credentials': True,
            },
            "body": str(e)
        }
    finally:
        return response
