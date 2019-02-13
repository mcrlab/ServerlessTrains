def extract_CRS(event, station_list):

    fromCRS = event['pathParameters']['from'].upper()
    if station_list.validateCRS(fromCRS) is not True:
        raise Exception("from CRS Code is invalid")

    toCRS = event['pathParameters']['to'].upper()
    if station_list.validateCRS(toCRS) is not True:
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
