from lib.trainapp import TrainApp
import json

def endpoint(event, context):

    try:
        fromCRS = event['pathParameters']['from']
        toCRS = event['pathParameters']['to']

        app = TrainApp(event, context)
        trains = app.fetchDeparturesForStation(fromCRS, toCRS)
        sorted_trains = sorted(trains, key=lambda k:k['std'])
        data = {
            "departures": sorted_trains
        }
        response = {
            "statusCode": 200,
            "headers": {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Credentials': true,
            },
            "body": json.dumps(data)
        }
    except:

        response = {
            "statusCode": 200,
            "headers": {
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Credentials': true,
            },
            "body": "Error"
        }
    finally:
        return response
