from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import re
from django.utils.crypto import get_random_string
import pymysql
from django.core.mail import send_mail
from lab.settings import EMAIL_HOST_USER

# Create your views here.
con = pymysql.connect("localhost","root","","lab")
c = con.cursor()

context={}
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
                #request.session['email']='email'
                context['email']=email
                
                if(r[2]=='admin'):
                    msg="success !"
                   # admin home page........#
                    return render(request,'admin_home.html',context)
                    #db.commit
                elif (r[2]=='user'):
                    msg="success !"
                    # user home page #
                    return render(request,'user_home.html',context)
                elif(r[2]=='labowner'):
                    msg="success !"
                    # lab owner home page........#
                    return render(request,'lab_owner.html',context)
                elif (r[2]=='staff'):
                    msg="success !"
                    # staff home page...........#
            else:
                msg=("incorrect password")
        else:
            msg=("user doesnot exist")
        
    return render(request,'Login.html',{"msg":msg})

def ureg(request):
    if 'submit' in request.POST:
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
        
    if 'back' in request.POST:
      return render(request,"index.html")
    return render(request,'User_Registration.html',{'v':321})


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
    if 'back' in request.POST:
        return render(request,"lab_owner.html")
    return render(request,'Add_Staff.html',{'rand_password':rand_password})

def addoct(request):
    return render(request,'Add_Doctor.html')

def validateEmail(email):   
        if len(email) > 6:
            if re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', email) != None:
                return 1
        return 0
def labreg(request):
   
    if 'labsub' in request.POST:
        l='labowner'
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
    if 'back' in request.POST:
        return render(request,"admin_home.html")
    return render(request,'Add_Lab.html',{'rand_password':rand_password})
        
      


def category(request):
    if 'category' in request.POST:
        tstcat=request.POST.get('cat')
        adtst="insert into test_category(category_name) values('"+str(tstcat)+"');"
        c.execute(adtst)
        con.commit()
    if 'back' in request.POST:
       #lab owner home page....#
       return render(request,"lab_owner.html") 
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
    
    if 'back' in request.POST:
       #lab owner home page....#
       return render(request,"lab_owner.html") 
    return render(request,"Add_NewTest.html",{'cat':result})
    
    #..............templates............#

def indx(request):
    return render(request,"index.html")

def index1(request):
    return render(request,"index1.html")

def index2(request):
    return render(request,"index2.html")

#...............................................#
def userprofile(request):
    v = list(context.values())[0]
   
    s ="select firstname,lastname,dob,gender,address,state,district,place,pincode,contactnum,alternatenum,email from user_reg where email='"+str(v)+"'"
    c.execute(s)
    result = c.fetchone()
    
    context['fname']=result[0]
    context['lname']=result[1]
    context['dob']=result[2]
    context['gender']=result[3]
    context['address']=result[4]
    context['state']=result[5]
    context['district']=result[6]
    context['place']=result[7]
    context['pincode']=result[8]
    context['contactnum']=result[9]
    context['alternatenum']=result[10]
    context['email']=result[11]
    
    if 'back' in request.POST:
       return render(request,"user_home.html",context)
    return render(request,"user_profile.html",context)
    
    
    
    

def user_home(request):
    return render(request,"user_home.html",context)
def labowner_home(request):
    return render(request,"lab_owner.html")
def admin_home(request):
    return render(request,"admin_home.html")

def delete(request):
    v = list(context.values())[0]
    s ="select email from user_reg where email='"+str(v)+"'"
    c.execute(s)
    #result = c.fetchone()
    if 'yes' in request.POST:
        #sql = "DELETE FROM login WHERE email='apsara@gmail.com'"
        sql = "DELETE FROM login WHERE email='"+str(v)+"'"
        sq = "DELETE FROM user_reg WHERE email='"+str(v)+"'"
        c.execute(sql)
        c.execute(sq)
        con.commit()
        
        return render(request,"index1.html")
    if 'no' in request.POST:
        return render(request,"index1.html")

    return render(request,"delete.html")   

def userprofile2(request):
    v = list(context.values())[0]
   
    s ="select firstname,lastname,dob,gender,address,state,district,place,pincode,contactnum,alternatenum,email from user_reg where email='"+str(v)+"'"
    c.execute(s)
    result = c.fetchone()
    
    context['fname']=result[0]
    context['lname']=result[1]
    context['dob']=result[2]
    context['gender']=result[3]
    context['address']=result[4]
    context['state']=result[5]
    context['district']=result[6]
    context['place']=result[7]
    context['pincode']=result[8]
    context['contactnum']=result[9]
    context['alternatenum']=result[10]
    context['email']=result[11]
    
    if 'back' in request.POST:
       return render(request,"index1.html",context)
    return render(request,"user_profile2.html",context)
    

