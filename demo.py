from handler import next
from handler import spread
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']

#event = { 'body' : '{ "from": ["DON"], "to": ["HUL"], "limit":2}' };
#result = spread(event, False)

event = {
    "pathParameters": {
        "from": "MAN",
        "to" : "NMC"
    }
}
result = next(event, False)

print(result)
