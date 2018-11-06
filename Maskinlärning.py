import random
import string
from sklearn import tree

class EvObj:
  def __init__(self, widthSet, heightSet, tongueSet, teethSet):
    self.w = widthSet
    self.h = heightSet
    self.to = tongueSet
    self.th = teethSet

class PredictManager:
  def __init__(self):
    self.features = []
    self.lables = []
	
  def AddFeature(self, evObject, lableSet):
    self.features += [[evObject.w, evObject.h, evObject.to, evObject.th]]
    self.lables.append(lableSet)

  def Predict(self, evObject):
    self.clf = tree.DecisionTreeClassifier().fit(self.features, self.lables)
    return self.clf.predict([[evObject.w, evObject.h, evObject.to, evObject.th]])

pm = PredictManager()
pm.AddFeature(EvObj(3, 3, 2, 0), "Ä")
pm.AddFeature(EvObj(3, 2, 2, 0), "E")
pm.AddFeature(EvObj(3, 1, 2, 0), "I")

pm.AddFeature(EvObj(2, 3, 2, 0), "Ö")
pm.AddFeature(EvObj(2, 2, 2, 0), "A")
pm.AddFeature(EvObj(2, 1, 2, 0), "Y")

pm.AddFeature(EvObj(1, 3, 2, 0), "Å")
pm.AddFeature(EvObj(1, 2, 2, 0), "E")
pm.AddFeature(EvObj(1, 1, 2, 0), "O")

pm.AddFeature(EvObj(3, 0, 0, 0), "B")
pm.AddFeature(EvObj(2, 1, 3, 0), "D")

pm.AddFeature(EvObj(2, 1, 1, 1), "F")
pm.AddFeature(EvObj(2, 2, 1, 0), "G")
pm.AddFeature(EvObj(2, 2, 0, 0), "H")

pm.AddFeature(EvObj(2, 1, 1, 2), "J")
pm.AddFeature(EvObj(2, 2, 1, 0), "K")
pm.AddFeature(EvObj(2, 2, 3, 0), "L")
pm.AddFeature(EvObj(2, 0, 0, 0), "M")
pm.AddFeature(EvObj(2, 1, 3, 0), "N")

pm.AddFeature(EvObj(2, 0, 0, 0), "P")
pm.AddFeature(EvObj(2, 2, 3, 0), "R")
pm.AddFeature(EvObj(2, 1, 2, 2), "S")
pm.AddFeature(EvObj(2, 1, 3, 0), "T")

pm.AddFeature(EvObj(3, 0, 0, 1), "V")


out = [];
print("Ord Förutsägare!")
lng = int(input("Längd på ord: "))
for i in range(lng):
  #evObj = EvObj(random.randint(0,3), random.randint(0,3), random.randint(1,3), random.randint(0,2))
  print("Bokstav: " + str(i + 1))
  evObj = EvObj(input("Munnens Bred [1 - 3]: "), input("Läppar mellanrum [0 - 3]: "), input("Tungans Position [0 - 3]: "), input("Tändrader mot läppar/tänder [0 - 2]: "))
  out.append(pm.Predict(evObj))

print("Du sa:")
for i in out:
  print(i)