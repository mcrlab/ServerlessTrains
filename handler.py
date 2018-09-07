from lib.trainapp import TrainApp
import json

def endpoint(event, context):
    response = {}
    try:
        fromCRS = event['pathParameters']['from']
        toCRS = event['pathParameters']['to']

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
        response = {
            "statusCode": 200,
            "headers": {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Credentials': True,
            },
            "body": e
        }
    finally:
        return response
