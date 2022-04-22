from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from dfs_app.models import Dfs_model
from dfs_app.utility import insertRec,insertRecCsv
# Create your views here.

def get_record(request, tab, id):
    rec = Dfs_model.objects.filter(id=id).values()
    html = "<html>Hello_record</html>"
    print(rec)
    # return HttpResponse(html)
    return render(request, 'display.html', {'lst' : rec, 'cnt': range(len(rec[0]))})

def get_table(request, tab):
    # return render(request, 'result.html', {'para' : para})
    rec = Dfs_model.objects.all().values()
    html = "<html>Hello_record</html>"
    # print(rec)
    print(rec)
    # return HttpResponse(html)
    return render(request, 'display.html', {'lst' : rec, 'cnt': range(len(rec[0]))})

def insert_rec(request):
    # print('in views')
    path='images'
    record = [['Parth',123,path+'/1.jpeg','Jpr',9273],['Abhisek',456,path+'/2.jpeg','Bnglr',9254],['Paras',789,path+'/3.jpeg','Pilani',9243],['Purorapatra',234,path+'/4.jpeg','Hyd',9243],['Naranambi',910,path+'/5.jpeg','Hyd',9254]]
    # record=[['Abhijeet',874,'bsd.jpg','Kanpur',8609]]
    for rec in record:
        insertRec(rec)

    html = "<html>Record Inserted!</html>"
    return HttpResponse(html)

def insert_rec_csv(request):

    path='/home/parth/411_patient_data.csv'

    insertRecCsv(path)

    html = "<html>Record Inserted!</html>"
    return HttpResponse(html)