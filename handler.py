from lib.trainapp import TrainApp
import json

def endpoint(event, context):
    try:
        app = TrainApp(event, context)
        trains = app.fetchDeparturesForStation("NMC", "MAN");
        sorted_trains = sorted(trains, key=lambda k:k['std'])
        data = {
            "departures": sorted_trains
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
    except:
        response = {
            "statusCode": 200,
            "body": "Error"
        }
    finally:
        return response
