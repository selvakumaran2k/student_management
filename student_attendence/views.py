from django.shortcuts import render
import student_attendence.student_data_processing as list
import pandas as pd
# Create your views here.
def base(request):
    return render(request,'base.html')
def marking(request):
    if request.method == "POST":
        file = request.FILES['dat']
        list.data(file)
        print('put in')
    return  render(
        request,'marking.html',{'data':list.get_list()}
    )
def attendence_submit(request):
    attendence_result=request.GET.getlist('attendence_result')
    list.rewrite(attendence_result,request.GET['date'])
    return render(
        request,'display_attendence_result.html',
        {
            'attendence_list':request.GET.getlist('attendence_result'),
            'date':request.GET['date']
        }
    )