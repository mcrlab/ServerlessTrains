import zeep
import boto3
import datetime
import json
import pickle
import os

dynamodb = boto3.resource('dynamodb')

class DarwinService():
    def __init__(self, wsdl, token):
        self.wsdl = wsdl
        self.token = token
        return

    def load_departures(self, from_crs, to_crs, number_of_departures):
        try:
            table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

            time = datetime.datetime.now().strftime('%H%M%d%m%Y')
            key = from_crs + to_crs + time

            result = table.get_item(
                Key={
                    'id': key
                }
            )

            print(result['Item'])

            client = zeep.Client(self.wsdl)
            response = client.service.GetDepBoardWithDetails(numRows=number_of_departures,
                                                            crs=from_crs,
                                                            filterCrs=to_crs,
                                                            timeOffset=0,
                                                            timeWindow=120,
                                                            _soapheaders={"AccessToken":self.token})
            pickled = pickle.dumps(response)
            
            item = {
                'id': key,
                'text': pickled
            }

            table.put_item(Item=item)

            return response

        except(zeep.exceptions.Fault):
            raise Exception("Failed to make request to Darwin API")
