from handler import next, spread

def test_next():
    event = {
        "pathParameters": {
            "from": "MAN",
            "to" : "NMC"
        }
    }
    print("-----")
    result = next(event, False)
    print(result)

def test_spread():
    print("-----")
    event = { 'body' : '{ "from": ["NMC", "NMN"], "to": ["MAN"], "limit":2}' };
    result = spread(event, False)

    print(result)

test_next()
test_spread()