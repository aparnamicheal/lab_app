from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import re
from django.utils.crypto import get_random_string

import pymysql

from django.core.mail import send_mail
from lab.settings import EMAIL_HOST_USER

# Create your views here.
con = pymysql.connect("localhost","root","","lab")
c = con.cursor()
def log(request):
    msg=""
    if(request.POST):
        email=request.POST.get("email")
        pwd=request.POST.get("pass")
        s="select count(*) from login where email='"+email+"'"
        c.execute(s)
        r=c.fetchone()
        if(r[0]>0):
            s="select * from login where email='"+email+"'"
            c.execute(s)
            r=c.fetchone()
            if(r[1]==pwd):
                request.session['email']='email'
                if(r[2]=='admin'):
                 msg="success !"
                 #admin home page
                elif (r[2]=='user'):
                    msg="success"
                    # user home page
                    return render(request,'User_Registration.html')
                elif (r[2]=='staff'):
                    msg='success'
                    return render(request,'Add_Staff.html')
                    # staff home page
                elif(r[2]=='lab'):
                    msg='success'
                    # lab home page
                    return render(request,'Add_Lab.html')

            else:
                msg=("incorrect password")
        else:
            msg=("user doesnot exist")
        
    return render(request,'Login.html',{"msg":msg})

def ureg(request):
    if 'user' in request.POST:
        u='user'
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        address=request.POST.get('addr')
        state=request.POST.get('state')
        district=request.POST.get('dis')
        place=request.POST.get('place')
        pincode=request.POST.get('pin')
        contactnum=request.POST.get('phnum1')
        alternatenum=request.POST.get('phnum2')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        uslg="insert into login(email,password,type) values('"+str( email)+"','"+str(password)+"','"+str(u)+"');"
        urg="insert into user_reg(firstname,lastname,dob,gender,address,state,district,place,pincode,contactnum,alternatenum,email,password) values('"+str(fname)+"','"+str(lname)+"','"+str(dob)+"','"+str(gender)+"','"+str(address)+"','"+str(state)+"','"+str(district)+"','"+str(place)+"','"+str(pincode)+"','"+str(contactnum)+"','"+str(alternatenum)+"','"+str( email)+"','"+str(password)+"');"
        c.execute(uslg)
        c.execute(urg)
        con.commit()
     
    return render(request,'User_Registration.html')


def stafreg(request):
    if 'staff' in request.POST:
        s='staff'
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        qualification=request.POST.get('quali')
        address=request.POST.get('addr')
        state=request.POST.get('state')
        district=request.POST.get('dis')
        place=request.POST.get('place')
        pincode=request.POST.get('pin')
        contactnum=request.POST.get('num1')
        alternatenum=request.POST.get('num2')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        stflg="insert into login(email,password,type) values('"+str( email)+"','"+str(password)+"','"+str(s)+"');"
        stfrg="insert into staff_reg(firstname,lastname,dob,gender,qualification,address,state,district,place,pincode,contactnum,alternatenum,email,password) values('"+str(fname)+"','"+str(lname)+"','"+str(dob)+"','"+str(gender)+"','"+str(qualification)+"','"+str(address)+"','"+str(state)+"','"+str(district)+"','"+str(place)+"','"+str(pincode)+"','"+str(contactnum)+"','"+str(alternatenum)+"','"+str(email)+"','"+str(password)+"');"
        c.execute(stfrg)
        c.execute(stflg)
        con.commit()
    return render(request,'Add_Staff.html')



def validateEmail(email):   
        if len(email) > 6:
            if re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email) != None:
                return 1
        return 0
def labreg(request):
    if 'labsub' in request.POST:
        l='lab'
        labname=request.POST.get('labname')
        address=request.POST.get('addr')
        state=request.POST.get('state')
        district=request.POST.get('dis')
        place=request.POST.get('place')
        pincode=request.POST.get('pin')
        contactnum=request.POST.get('phnum1')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        lblg="insert into login(email,password,type) values('"+str(email)+"','"+str(password)+"','"+str(l)+"');"
        lbrg="insert into lab_reg(labname,address,state,district,place,pincode,contactnum,email,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        c.execute(lblg)
        c.execute(lbrg,(labname,address,state,district,place,pincode,contactnum,email,password))
        con.commit()
        email=request.POST.get('email')
        n=validateEmail(email)
       
        if(n==1):
            p=request.POST.get('pass')
            subject = 'Welocme........!'
            message = "your login password:%s" % (p)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently = False)          
            return HttpResponse("mail send")
        else:
            return HttpResponse("mail id invalid")
    rand_password = get_random_string(length=10)
    return render(request,'Add_Lab.html',{'rand_password':rand_password})
        
      
def addoct(request):
    return render(request,'Add_Doctor.html')

def category(request):
    if 'category' in request.POST:
        tstcat=request.POST.get('cat')
        adtst="insert into test_category(category_name) values('"+str(tstcat)+"');"
        c.execute(adtst)
        con.commit()
    return render(request,"Add_TestCategory.html")

def newtst(request):
    q="select * from test_category"
    c.execute(q)
    result=c.fetchall()
    if 'save' in request.POST:
        catid=request.POST.get('cat')
        tsttype=request.POST.get('type')
        rate=request.POST.get('rate')
        addnwtst="insert into test_type(category_id,type_name,rate) values('"+str(catid)+"','"+str(tsttype)+"','"+str(rate)+"');"
        c.execute(addnwtst)
        con.commit()  
    return render(request,"Add_NewTest.html",{'cat':result})
       
    
    


