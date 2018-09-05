from lib.trainapp import TrainApp
app = TrainApp(False, False)
data = app.fetchDeparturesForStation("NMC", "MAN")
sorted(data, key=lambda k:k['std'])
print(data)
