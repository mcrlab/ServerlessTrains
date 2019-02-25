from handler import iot
from handler import next
from handler import spread
import os

WSDL = os.environ['WSDL']
token = os.environ['DARWIN_TOKEN']

event = { 'body' : '{ "from": ["NMC","NMN"], "to": ["MAN"], "limit":2}' };
result = spread(event, False)
print(result)
