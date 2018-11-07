import random
import string
from sklearn import tree
from PIL import Image

class EvObject:
  def __init__(self, hairClr, eyeClr, skinClr, accesory):
    self.attributes = [hairClr, eyeClr, skinClr, accesory]

class PredictManager:
  def __init__(self):
    self.features = []
    self.lables = []
    
    self.dictionary = {
    "SVART": 0.0, "BRUN": 1.0, "ORANGE": 2.0, "GUL": 3.0,  "VIT": 4.0, "BLEK":5.0, "BLÅ":6.0, "INGET": 7.0, "INGEN": 7.0, "GLASÖGON": 8.0, "HATT": 9.0, "SKÄGG": 10.0, "MUSTACH": 11.0
    }
	
  def AddFeature(self, evObject, lableSet):
    self.features += [evObject.attributes]
    self.lables.append(lableSet)

  def Predict(self, evObject):
    self.clf = tree.DecisionTreeClassifier().fit(self.features, self.lables)
    return self.clf.predict([evObject.attributes])

  def ask(self, prompt):
    while True:
      ans = input(prompt).upper()
      if ans in self.dictionary:
        return self.dictionary[ans]
      print("-Använd ord från listan!-")

  

pm = PredictManager()
#RAD1==========================================
pm.AddFeature(EvObject(1, 1, 1, 11), "THOMAS")
pm.AddFeature(EvObject(1, 1, 1, 10), "MAX")
pm.AddFeature(EvObject(1, 1, 1, 8), "Sophie")
pm.AddFeature(EvObject(3, 1, 5, 10), "LUCAS")
pm.AddFeature(EvObject(7, 1, 5, 10), "Philippe")
pm.AddFeature(EvObject(3, 6, 5, 7), "JOE")
#RAD2==========================================
pm.AddFeature(EvObject(4, 1, 5, 10), "Paul")
pm.AddFeature(EvObject(4, 1, 5, 11), "Peter")
#
pm.AddFeature(EvObject(2, 1, 5, 7), "Herman") 
pm.AddFeature(EvObject(7, 1, 5, 7), "Herman")
#
pm.AddFeature(EvObject(4, 4, 5, 10), "Charles") 
pm.AddFeature(EvObject(7, 4, 5, 10), "Charles")
#
pm.AddFeature(EvObject(4, 6, 5, 8), "Anne")
pm.AddFeature(EvObject(1, 1, 1, 9), "Bernard")
#RAD3==========================================
pm.AddFeature(EvObject(1, 1, 5, 11), "Michael")
#
pm.AddFeature(EvObject(7, 1, 1, 10), "Roger")
pm.AddFeature(EvObject(1, 1, 1, 10), "Roger")
#
pm.AddFeature(EvObject(2, 1, 5, 9), "Maria")
pm.AddFeature(EvObject(3, 6, 5, 7), "Sarah")
pm.AddFeature(EvObject(0, 1, 5, 7), "Theo")
pm.AddFeature(EvObject(3, 1, 5, 9), "Eric")
#RAD4==========================================
pm.AddFeature(EvObject(4, 1, 5, 7), "Victor")
pm.AddFeature(EvObject(2, 6, 5, 8), "Stephen")
pm.AddFeature(EvObject(3, 1, 5, 11), "Hans")
pm.AddFeature(EvObject(4, 4, 5, 10), "Daniel")
pm.AddFeature(EvObject(1, 1, 5, 9), "Katrin")
pm.AddFeature(EvObject(0, 1, 5, 9), "Frank")
out = [];
print("Vem där!")
img = Image.open("karaktarer.jpg")
img.show()
print("Beskriv karaktären du valt för datorn \n")
print("  Svara med orden: ")
for i in pm.dictionary:
  print("    " + i)
print("\n")

evObj = EvObject(pm.ask("HårFärg: "), pm.ask("Ögonfärg: "), pm.ask("Hudfärg: "), pm.ask("Accesoar/Annat hår: "))
print("Din karaktär:")
print(pm.Predict(evObj))