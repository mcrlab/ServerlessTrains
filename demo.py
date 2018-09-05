from lib.trainapp import TrainApp
app = TrainApp(False, False)
nmc = app.fetchDeparturesForStation("NMC")
nmn = app.fetchDeparturesForStation("NMN")
data = nmc + nmn
sorted(data, key=lambda k:k['std'])
print(data)
