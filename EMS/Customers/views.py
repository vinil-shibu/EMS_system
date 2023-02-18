from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        b_id=request.POST['']
        e_id=request.POST['']
        b_date=request.POST['']
        name=request.POST['']
        email=request.POST['']
        phone=request.POST['']
        sup=register.objects.create(book_id=b_id,event_id=e_id,booked_date=b_date,p_name=name,p_email=email,p_phone=phone)
        sup.save()
        return render(request,'home.html')

def events(request):
    if request.method=='POST':
        eid=request.POST['']
        ename=request.POST['']
        edate=request.POST['']
        o_email=request.POST['']
        o_phone=request.POST['']
        desc=request.POST['']
        etype=request.POST['']
        location=request.POST['']
        status=request.POST['']
        seats=request.POST['']
        e=events.objects.create(event_id=eid,event_name=ename,event_date=edate,org_mail=o_email,org_email=o_email,org_phone=o_phone,event_desc=desc,event_type=etype,event_loc=location,event_status=status,max_seats=seats)
        e.save()
        return render(request,'index.html')
    else:
        return render(request,'')

def home(request):
    objects = events.objects.filter(event_id=request.GET['eventid'])
    return render(request, "home.html",)# context={'objects': objects})