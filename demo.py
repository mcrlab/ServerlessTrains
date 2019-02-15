from handler import iot
from handler import next
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']

event = { 'pathParameters' : { 'from': 'MAN', 'to': "NMC"}};
result = next(event, False)
print(result)
