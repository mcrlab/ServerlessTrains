from handler import next
from handler import spread
import os

event = {
    "pathParameters": {
        "from": "MAN",
        "to" : "NMC"
    }
}
print("-----")
result = next(event, False)
print(result)
print("-----")
event = { 'body' : '{ "from": ["DON"], "to": ["HUL"], "limit":2}' };
result = spread(event, False)

print(result)
