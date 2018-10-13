from lib.trainapp import TrainApp
from lib.stationlist import StationList
import json

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

def endpoint(event, context):
    statusCode = 200
    body = ""

    try:
        stationList = StationList()

        fromCRS = event['pathParameters']['from'].upper()
        if stationList.validateCRS(fromCRS) is not True:
            raise Exception("CRS Code is invalid")

        toCRS = event['pathParameters']['to'].upper()
        if stationList.validateCRS(toCRS) is not True:
            raise Exception("CRS Code is invalid")

        trains = TrainApp().fetchDeparturesForStation(fromCRS, toCRS)

        data = {
            "departures": trains
        }
        body = json.dumps(data)

    except Exception as e:
       statusCode = 500
       body = str(e)

    finally:
       response = {
           "statusCode": statusCode,
           "headers": {
             'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Credentials': True,
           },
           "body": body
       }
       return response
