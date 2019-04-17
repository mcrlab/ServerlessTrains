def calculate_estimated_time(estimated, scheduled):
    if(estimated == "On time"):
        return scheduled
    else:
        return estimated


def extract_crs(event):
    try:
        from_crs = event['pathParameters']['from']
        to_crs = event['pathParameters']['to']
    except KeyError:
        raise Exception("CRS not provided")

    from_crs = from_crs.upper()
    to_crs = to_crs.upper()
    
    return from_crs, to_crs


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

def time_to_integer(time_string):
    hour, minute = time_string.split(":")
    time_int = int(hour) * 60 + int(minute)
    return time_int
