from handler import next, spread, iot, stations

def test_next():

    event = {
        "pathParameters": {
            "from": "NMC",
            "to" : "MAN"
        }
    }
    print("-----")
    print("testing next")
    print("-----")
    result = next(event, False)
    print(result)

def test_spread():
    print("-----")
    print("testing spread")
    print("-----")
    event = { 'body' : '{ "routes": [{"from": "DON", "to" : "CLE"}], "limit":2}' };

    result = spread(event, False)

    print(result)

def test_iot():
    event = {
        "pathParameters": {
            "from": "NMC",
            "to" : "MAN"
        }
    }
    print("-----")
    print("testing iot")
    print("-----")
    result = iot(event, False)
    print(result)

def test_stations():
    result = stations({}, False)
    print(result)

#test_stations()
#test_iot()
#test_next()
test_spread()
#test_multiple()