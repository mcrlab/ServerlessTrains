from lib.trainapp import TrainApp

fromCRS = "MAN"
toCRS = "NMC"

trains = TrainApp().fetchDeparturesForStation(fromCRS, toCRS)
print(trains[0])
etd = trains[0]['origin']['etd']
hour, minute = etd.split(":")
print(hour)
print(minute)
time = int(hour) * 60 + int(minute)
print(time)
