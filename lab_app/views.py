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
 #........................login.........................#
context={}
def log(request):
    msg=""
    if(request.POST):
        email=request.POST.get("email")
        pwd=request.POST.get("pass")
        
        s="select count(*) from login where email='"+email+"'"
       
        c.execute(s)
        r=c.fetchone()
        print(r)
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
                    return render(request,'admin_home.html')
                    #db.commit
                elif(r[2]=='user'):
                    msg="success !"
                    # user home page #
                    return render(request,'user_home.html',context)
                elif(r[2]=='labowner'):
                    msg="success !"
                    # lab owner home page........#
                    return render(request,'lab_owner.html',context)
                elif(r[2]=='staff'):
                    msg="success !"
                    return render(request,'staff_home.html',context)
                    # staff home page...........#
            else:
                msg=("incorrect password")
        else:
            msg=("user doesnot exist")
        
    return render(request,'Login.html',{"msg":msg})
        #........................new user registration..............................#
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
        return render(request,"index.html")
    
    if 'back' in request.POST:
        return render(request,"index.html")
    return render(request,'User_Registration.html',{'v':321})
            #.....................staff registration..........................#

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
            msg=("mail send")
            p=request.POST.get('pass')
            subject = 'Welcome........!'
            message = "your login password:%s" % (p)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently = False)          
            #return HttpResponse("mail send")
           
            return render(request,"Add_staff.html",{"msg":msg})
            

        else:
            msg=("invalid")
            return render(request,"Add_Staff.html",{"msg":msg})
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
        #....................lab registration......................#
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
        
      
       #...................add test category...........................#

def category(request):
    if 'category' in request.POST:
        tstcat=request.POST.get('cat')
        adtst="insert into test_category(category_name) values('"+str(tstcat)+"');"
        c.execute(adtst)
        con.commit()
        return render(request,"lab_owner.html") 
    if 'back' in request.POST:
       #lab owner home page....#
       return render(request,"lab_owner.html") 
    return render(request,"Add_TestCategory.html")
     #...........................add new test...............................#
def newtst(request):
    q="select * from test_category"
    c.execute(q)
    result=c.fetchall()
    if 'save' in request.POST:
        catid=request.POST.get('cat') 
        print(catid)
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



#........... user profile view....................................#
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
       return render(request,"index1.html",context)
    return render(request,"user_profile.html",context)
    #.........................user profile delete......................#
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
        
        return render(request,"index.html")
    if 'no' in request.POST:
        return render(request,"index1.html")

    return render(request,"delete.html")      
    
    
    #................home pages.................#

def user_home(request):
    return render(request,"user_home.html",context)
def labowner_home(request):
    return render(request,"lab_owner.html")
def admin_home(request):
    return render(request,"admin_home.html")
def staff_home(request):
   
    return render(request,"staff_home.html",context)

 #..................................................#


def change_password(request):
    
    return render(request,"Change_password.html")
    
             #..........lab profile..................#
def labownerprofile_index(request):
    return render(request,"labownerprofile_index.html")

#............................staff profile view............................#
def staff_view(request):
    m = list(context.values())[0]
    
    s ="select firstname,lastname,dob,gender,qualification,address,state,district,place,pincode,contactnum,alternatenum,email from staff_reg where email='"+str(m)+"'"
    c.execute(s)
    
    result = c.fetchone()
    
    context['fname']=result[0]
    context['lname']=result[1]
    context['dob']=result[2]
    context['gender']=result[3]
    context['quali']=result[4]
    context['address']=result[5]
    context['state']=result[6]
    context['district']=result[7]
    context['place']=result[8]
    context['pincode']=result[9]
    context['contactnum']=result[10]
    context['alternatenum']=result[11]
    #context['email']=result[12]
    
    if 'back' in request.POST:
       return render(request,"staff_home.html", context)
    return render(request,"staff_view.html",context)


#..........................book a test..............................#
def book_test(request):
    result=" "
    if 'sub' in request.POST:
        
        district=request.POST.get('district')
        place=request.POST.get('place')
        
        s="select count(*) from lab_reg where district='"+str(district)+"'"
        c.execute(s)
        r=c.fetchone()
        print(r)
        s="select labname,address,contactnum,email from lab_reg where district='"+str(district)+"' and place='"+str(place)+"'"
        c.execute(s)
        result = c.fetchall()
        print(result)
    if 'booknow' in request.POST:
        return render(request,"book_now.html")
    return render(request,"book_test.html",{'item':result})

def book_now(request):
    r=""
    q="select * from test_category"
    c.execute(q)
    result=c.fetchall()
    print(result)
    if 'ok' in request.POST:
        catid=request.POST.get('cat') 
        print(catid)
        s="select * from test_type where category_id='"+str(catid)+"'"
        c.execute(s)
        r=c.fetchall()
   
    return render(request,"book_now.html",{'cat':result,'cat1':r})


def book_confirm(request):
    
    v = list(context.values())[0]
  
    s ="select firstname,lastname,dob,gender,address,state,district,place,contactnum,alternatenum,email from user_reg where email='"+str(v)+"'"
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
   
    context['contactnum']=result[8]
    context['alternatenum']=result[9]
    context['email']=result[10]
    

    return render(request,"book_confirm.html",context)

def view_labtest(request):
    r=""
    q="select * from test_category"
    c.execute(q)
    result=c.fetchall()
    print(result)
    if 'ok' in request.POST:
        catid=request.POST.get('cat') 
        print(catid)
        s="select * from test_type where category_id='"+str(catid)+"'"
        c.execute(s)
        r=c.fetchall()
   
    return render(request,"view_lab_test.html",{'cat':result,'cat1':r})
