from handler import iot
from handler import next

event = { 'pathParameters' : { 'from': 'MAN', 'to': "NMC"}};
result = next(event, False)
print(result)
