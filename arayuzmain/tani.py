import pickle
import os
import joblib


from tf.keras.models import load_model
model=load_model('home/nil/Masaüstü/DJANGO/sepsis_arayuz/arayuzmain/models')

print(model.predict([[1,1,220235,60.0]]))

results = []
import math

def most_common(lst):
    return max(set(lst), key=lst.count)


def belirle(a,b,c,d,e):

  """ 

   Alacağımız değerler :

    temperature : 676 derece fahrenheit biz hesaplicaz. derece cinsinden alınacak.

    heart rate : 211,220045

    resp rate: 618,615,651,614 bpm

    wbc count: 1542,51301,51384,51300,51439,51363,51458,21128,51516

    paco2 : 778,220235

  1 - SIRS mi? 4 değer ile bakılabilir. Modele gerek yok if'le hallederiz.
  2 - Enfeksiyon şüphesi veya bulgusu var mı? Kullanıcıdan yes/no ile alınır.
  3 - Severe Sepsis için Sepsis + Sofa Score + Hypertansion + Lactate
  4 - Septik Shock için Severe Sepsis + Sofa Score + Lactate + Hypertansion

  """ 

  # dereceyi fahrenheita dönüştürüyorum.
  f = (a * 1.8) + 32  

  #itemid = [676,211,618,1542,778]
  #veriler = [a,  b,  c,  d,   e]

  itemid = [676,678,211,220045,618,615,651,614,1542,51301,51384,51300,51439,51363,51458,21128,51516,778,220235]
  veriler = [a, f,  b,   b,    c,    c, c,  c,   d,   d,    d,    d,    d,    d,    d,    d,    d,   e,    e]

  zip_iterator = zip(itemid, veriler)
  item_veri = dict(zip_iterator) 

  # itemid ile verilerin sırası eşleşsin! 

  for key in item_veri:

    print(key)

    prediction = model.predict([[155,154,key,item_veri[key]]])
    #print(prediction)
    prediction = prediction.tolist()[0]

    # handle etme işlemi.
    # listenin max'ını bul ve ceil fonksiyonuyla değiştir.
    max_value = max(prediction)
    max2 = math.ceil(max_value)

    prediction[prediction.index(max_value)]=max2

    print(prediction)
    results.append(prediction)

    print("\n")

  tanılar = []

  for result in results:
    #print(result)
    tanılar.append(result.index(1))

  last = most_common(tanılar)

  if last == 0:
      return ("Sepsis dışı - Bilinmiyor")

  if last == 1:
      return ("Sepsis")

  if last == 2:
      return ("Şiddetli Sepsis")

  if last == 3:
      return ("Septik Shock")


print(tanı(37.5,90,19,6.9,45))

""" 
loaded_model = joblib.load("finalized_model.sav")
result = loaded_model.predict([[1,1,220235,60.0]])
print(result)

#os.chdir("drive/MyDrive")

with open('fitted_model_comp1.pickle','rb') as modelFile:
     model = pickle.load(modelFile)

prediction = model.predict([[1,1,220235,60.0]])
print(prediction)

"""