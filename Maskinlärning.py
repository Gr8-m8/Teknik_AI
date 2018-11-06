import random
import string
from sklearn import tree

class EvObject:
  def __init__(self, hairClr, eyeClr, skinClr, accesory):
    self.attributes = [hairClr, eyeClr, skinClr, accesory]

class PredictManager:
  def __init__(self):
    self.features = []
    self.lables = []
	
  def AddFeature(self, evObject, lableSet):
    self.features += [evObject.attributes]
    self.lables.append(lableSet)

  def Predict(self, evObject):
    self.clf = tree.DecisionTreeClassifier().fit(self.features, self.lables)
    return self.clf.predict([evObject.attributes])


pm = PredictManager()
#pm.AddFeature(EvObject(0, 1, 23, 5), "THOMAS")
pm.AddFeature(EvObject(1, 1, 1, 11), "THOMAS")
pm.AddFeature(EvObject(1, 1, 1, 10), "MAX")
pm.AddFeature(EvObject(1, 1, 1, 8), "Sophie")

pm.AddFeature(EvObject(3, 1, 5, 10), "LUCAS")
pm.AddFeature(EvObject(7, 1, 5, 10), "Philippe")
pm.AddFeature(EvObject(3, 6, 5, 7), "JOE")

#pm.AddFeature(EvObject("Vit", "BRUN", "Blek", "" ), "Paul")
#pm.AddFeature(EvObject("Vit", "BRUN", "Blek", "" ), "Paul")
#pm.AddFeature(EvObject("Vit", "BRUN", "Blek", "" ), "Paul")

out = [];
print("Vem där!")
print("Beskriv karaktären du valt för datorn")
print("Svara med orden: \n Svart, Brun, Gul, \n Blå, Orange, Vit, \n Blek, Inget, Glasögon, \n Hatt, Mustach, SKÄGG")

map = {
  "SVART": 0.0, "BRUN": 1.0, "ORANGE": 2.0, "GUL": 3.0,  "VIT": 4.0, "BLEK":5.0, "BLÅ":6.0, "INGET": 7.0, "INGEN": 7.0, "GLASÖGON": 8.0, "HATT": 9.0, "SKÄGG": 10.0, "MUSTACH": 11.0
}

def ask(prompt, map):
  while True:
    ans = input(prompt).upper()
    if ans in map:
      return map[ans]
    print("Använd ord från listan!\n")

evObj = EvObject(ask("HårFärg: ",map), ask("Ögonfärg: ",map), ask("Hudfärg: ",map), ask("Accesoar: ",map))
print("Din karaktär:")
print(pm.Predict(evObj))