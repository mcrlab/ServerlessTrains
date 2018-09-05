from lib.trainapp import TrainApp
import json

def endpoint(event, context):
    try:
        app = TrainApp(event, context)
        nmc = app.fetchDeparturesForStation("NMC")
        nmn = app.fetchDeparturesForStation("NMN")
        trains = nmc + nmn
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
