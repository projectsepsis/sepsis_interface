from re import U
from django.shortcuts import render,redirect

from keras.models import load_model
model=load_model('/home/nil/Masaüstü/DJANGO/sepsis_arayuz/arayuzmain/models')

### TANI BÖLÜMÜ ######

def new_cont(temprature, heartrate, respiratoryrate, paco2, sbp, bilirubin, creatinine, platelets, lactate):
  if (temprature >38.3 or temprature<36) and heartrate>90 or (respiratoryrate>20 and paco2<32):
    print("")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")
  elif (temprature >38.3 or temprature<36) and respiratoryrate>20 or paco2<32 and heartrate>90:
    print("")
    if(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 or lactate<2):
      return ("Şiddetli Sepsis")
    elif(sbp<90 or bilirubin >2 or creatinine>4 or platelets< 100000 and lactate>=4):
      return ("Septik Şok")
    elif():
      return ("Sepsis")

    else:
        return ("Sepsis Dışı")

######################

### TEDAVİ BÖLÜMÜ ### 

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['disease', 'immunity', 'age', 'infection', 'risk', 'allergy', 'treatment'] 
treatment = pd.read_csv("outscen.csv", header=None, names=col_names)

feature_cols = ['disease', 'immunity', 'age', 'infection', 'risk', 'allergy']
X = treatment[feature_cols]
y = treatment.treatment 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train.values,y_train)
y_pred = clf.predict(X_test.values)

col_names_of_dict = ['label', 'dictionary']
treatment_dictionary = pd.read_csv("d_treatments.csv", header=None, names=col_names_of_dict)

def call_destree(disease, immunity, age, infection, risk, allergy):
  new_prediction = clf.predict([[disease,immunity,age,infection,risk,allergy]])
  return (treatment_dictionary.dictionary[new_prediction])

#####################

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
  3 - Şiddetli Sepsis için Sepsis + Sofa Score + Hypertansion + Lactate
  4 - Septik Shock için Şiddetli Sepsis + Sofa Score + Lactate + Hypertansion

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

    #print(key)

    prediction = model.predict([[155,154,key,item_veri[key]]])
    #print(prediction)
    prediction = prediction.tolist()[0]

    # handle etme işlemi.
    # listenin max'ını bul ve ceil fonksiyonuyla değiştir.
    max_value = max(prediction)
    max2 = math.ceil(max_value)

    prediction[prediction.index(max_value)]=max2

    #print(prediction)
    results.append(prediction)

    #print("\n")

  tanılar = []

  for result in results:
    #print(result)
    tanılar.append(result.index(1))

  last = most_common(tanılar)

  if last == 0:
      return ("Sepsis dışı")

  if last == 1:
      return ("Sepsis")

  if last == 2:
      return ("Şiddetli Sepsis")

  if last == 3:
      return ("Septik Şok")

# Create your views here.

item_id = [1,2,3,4,5,6,7,8,9]

dict_item = {
    1: "Temperature (°C) ",
    2: "Heart Rate (bpm) ",
    3: "Respiratory Rate (bpm)",
    4: "PaCO2 Count (mmHg)",
    5: "SBP (mmHg)",
    6: "Bilirubin (mg/dL)",
    7: "Creatinine (mg/dL)",
    8: "Platelets (/mcL)",
    9: "Lactate (mmol/L)",

}

teshis=5

def home(request):

    if request.method == 'POST':

        context={}   
        liste = []
        for i in item_id:
            deger = request.POST.get(str(i))
            liste.append(int(deger))

        context["liste"] = liste
        
        global teshis
        teshis = new_cont(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7],liste[8])
        context["teshis"] = teshis

        return render(request,"sonucpage.html",context=context)

    else:
        context={}
        context["item_id"] = item_id
        context["dict_item"] = dict_item

        return render(request,"homepage.html",context=context)

def tedavi(request):

    if request.method == 'POST':

        context={}   
        liste = []
        a=554

        for i in range(1,6):
            deger = request.POST.get("soru"+str(i))
            liste.append(float(deger))

        context["liste"] = liste

        if teshis == "Sepsis dışı":
            a = 0

        elif teshis == "Sepsis":
            a = 1

        elif teshis == "Şiddetli Sepsis":
            a = 2

        elif teshis == "Septik Şok":
            a = 3

        tedavi=call_destree(a,liste[0],liste[1],liste[2],liste[3],liste[4])

        print(tedavi)

        context["tedavi"] = tedavi

        return render(request,"ensonsayfa.html",context=context)

    else:
        context={}      
        context["teshis"] = teshis
        return render(request,"tedavianket.html",context=context)