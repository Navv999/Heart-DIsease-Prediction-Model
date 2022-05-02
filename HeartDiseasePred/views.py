from msilib.schema import Shortcut
from pydoc import render_doc
from tkinter import Scale
import pickle
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def getPredictions(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall):
    model=pickle.load(open("C:\\Users\\navpa\\Downloads\\Heart_disease_pred__model.sav","rb"))
    scaled=pickle.load(open("scaler.sav","rb"))
    pred=model.predict(scaled.transform([[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]]))


    if pred==0:
        return "have a heart disease"
    elif pred==1:
        return "Dosen't have a heart disease"
    else:
        return "error"

def result(request):
    age=int(request.GET['age'])
    sex=int(request.GET['sex'])
    cp=int(request.GET['cp'])
    trtbps=int(request.GET['trtbps'])
    chol=int(request.GET['chol'])
    fbs=int(request.GET['fbs'])
    restecg=int(request.GET['restecg'])
    thalachh=int(request.GET['thalachh'])
    exng=int(request.GET['exng'])
    oldpeak=float(request.GET['oldpeak'])
    slp=int(request.GET['slp'])
    caa=int(request.GET['caa'])
    thall=int(request.GET['thall'])

    result=getPredictions(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall)
    return render(request,'result.html',{'result':result})

