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
                elif(r[2]=='doctor'):
                    msg="success !"
                    return render(request,'doctor_home.html',context)
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
    return render(request,'User_Registration.html',context)
            #.....................staff registration..........................#

def stafreg(request):
    v = list(context.values())[0]
    print(v)
    print(context)
    if 'staff' in request.POST:
        s ="select labid from lab_reg where email='"+str(v)+"'"
        c.execute(s)
        result = c.fetchone()
        a=result[0]
       
        print(result)
        print(a)
       
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
        stfrg="insert into staff_reg(labid,firstname,lastname,dob,gender,qualification,address,state,district,place,pincode,contactnum,alternatenum,email,password) values('"+str(a)+"','"+str(fname)+"','"+str(lname)+"','"+str(dob)+"','"+str(gender)+"','"+str(qualification)+"','"+str(address)+"','"+str(state)+"','"+str(district)+"','"+str(place)+"','"+str(pincode)+"','"+str(contactnum)+"','"+str(alternatenum)+"','"+str(email)+"','"+str(password)+"');"
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
            subject = 'Welcome........!'
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
    v = list(context.values())[0]
    print(v)
    
    if 'category' in request.POST:
        s ="select labid,email from lab_reg where email='"+str(v)+"'"
        c.execute(s)
        result = c.fetchone()
        a=result[0]
        b=result[1]
        print(result)
        print(a)
        print(b)
        tstcat=request.POST.get('cat')
        print(tstcat)
        adtst="insert into test_category(labid,email,category_name) values('"+str(a)+"','"+str(b)+"','"+str(tstcat)+"');"
        c.execute(adtst)
        con.commit()
       
    if 'back' in request.POST:
       #lab owner home page....#
       return render(request,"lab_owner.html") 
    return render(request,"Add_TestCategory.html")
     
     #...........................add test category...............................#
def newtest(request):
    result=""
    result1=""
    v = list(context.values())[0]
    print(context)
    if 'category' in request.POST:
        
        s ="select labid,email from lab_reg where email='"+str(v)+"'"
        c.execute(s)
        result = c.fetchone()
        a=result[0]
        b=result[1]
        print(result)
        print(a)
        print(b)
        #............................add test type.............#
        tstcat=request.POST.get('cat')
        print(tstcat)
        adtst="insert into test_category(labid,email,category_name) values('"+str(a)+"','"+str(b)+"','"+str(tstcat)+"');"
        c.execute(adtst)
        con.commit()
        
    q="select * from test_category"
    c.execute(q)
    result1=c.fetchall()
    print(result1)
    result=""
    if 'save' in request.POST:
       
        s ="select labid,email from lab_reg where email='"+str(v)+"'"
      
        c.execute(s)
        result = c.fetchone()
        a=result[0]
        b=result[1]
        print(result)
        print(a)
        print(b)
        catid=request.POST.get('cat') 
        print(catid)
        tsttype=request.POST.get('type')
        rate=request.POST.get('rate')
        addnwtst="insert into test_type(labid,email,category_id,type_name,rate) values('"+str(a)+"','"+str(b)+"','"+str(catid)+"','"+str(tsttype)+"','"+str(rate)+"');"
        c.execute(addnwtst)
        con.commit()  
    if 'back' in request.POST:
       #lab owner home page....#
       return render(request,"lab_owner.html") 
    return render(request,"Add_NewTest.html",{'cat':result1})
    
    #..............templates............#

def indx(request):
    return render(request,"index.html",context)

def index1(request):
    print(context)
    return render(request,"index1.html",context)



#........... user profile view....................................#
def userprofile(request):
    v = list(context.values())[0]
    print(context)
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
       return render(request,"index1.html",)
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
        
        return render(request,"index.html",context)
    if 'no' in request.POST:
        return render(request,"index1.html",context)

    return render(request,"delete.html",context)      
    #.......................deletion new........................#
def deletion(request):
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
        
        return render(request,"index.html",context)
    if 'no' in request.POST:
        return render(request,"index1.html",context)

    return render(request,"deletion_new.html",context)     

    
    #................home pages.................#

def user_home(request):
    return render(request,"user_home.html",context)
def labowner_home(request):
    return render(request,"lab_owner.html",context)
def admin_home(request):
    return render(request,"admin_home.html",context)
def staff_home(request):
   
    return render(request,"staff_home.html",context)

 #..................................................#


def change_password(request):
    
    return render(request,"Change_password.html",context)
    
             #..........lab profile..................#
def labownerprofile_index(request):
    return render(request,"labownerprofile_index.html",context)

#............................staff profile view............................#
def staff_view(request):
    v = list(context.values())[0]
    s="select * from staff_reg where email='"+str(v)+"'"
    c.execute(s)
    result=c.fetchone()
    context['fname']=result[2]
    context['lname']=result[3]
    context['dob']=result[4]
    context['gender']=result[5]
    context['quali']=result[6]
    context['address']=result[7]
    context['state']=result[8]
    context['district']=result[9]
    context['place']=result[10]
    context['pincode']=result[11]
    context['contactnum']=result[12]
    context['alternatenum']=result[13]
    #context['email']=result[12]
    
    if 'back' in request.POST:
       return render(request,"staff_home.html")
    return render(request,"staff_view.html",context)


#..........................find a lab..............................#
def find_lab(request):
    place1=" "
    if 'sub' in request.POST:
        district=request.POST.get('district')
        place=request.POST.get('place')
        s="select count(*) from lab_reg where district='"+str(district)+"'"
        c.execute(s)
        place1=c.fetchone()
        print(place1)
        s="select labname,address,contactnum,email from lab_reg where district='"+str(district)+"' and place='"+str(place)+"'"
        c.execute(s)
        place2 = c.fetchall()
        print(place2)
        return render(request,"find_lab.html",{'item':place2})
    if 'booknow' in request.POST:
        return render(request,"book_now.html")
    return render(request,"find_lab.html",{'item':place1})
#........................book now button ->    next page(book_now.html)......................#
def book_now(request):
    sku=request.GET.get('sku')
    s="select * from test_category where email='"+sku+"'"
    c.execute(s)
    result=c.fetchall()
    print(result)
    r=""
    #q="select * from test_category"
    #c.execute(q)
    #result=c.fetchall()
    #print(result)
    if 'ok' in request.POST:
        catid=request.POST.get('cat') 
        print(catid)
        s="select * from test_type where category_id='"+str(catid)+"'"
        c.execute(s)
        r=c.fetchall()
    if 'sub1' in request.POST:
        print("hi")
        return render(request,"book_confirm.html")
    return render(request,"book_now.html",{'cat1':result,'cat2':r})


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

#......................staff view lab tests.......................#
#def view_labtest(request):
    
    
    #if 'ok' in request.POST:
        
     #   catid=request.POST.get('cat') 
    #    print(catid)
   #     s="select type_name,rate from test_type where category_id='"+str(catid)+"'"
  #      c.execute(s)
 #       r=c.fetchall()
    #return render(request,"view_lab_test.html",{'cat':result,'cat1':r},context)


    #..........................doctor registration..................#
def doctreg(request):
    msg=""
    if 'doct' in request.POST:
        l='doctor'
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        qualification=request.POST.get('quali')
        address=request.POST.get('addr')
        state=request.POST.get('state')
        district=request.POST.get('dis')
        place=request.POST.get('place')
        pincode=request.POST.get('pin')
        contactnum1=request.POST.get('phnum1')
        contactnum2=request.POST.get('phnum2')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        lblg="insert into login(email,password,type) values('"+str(email)+"','"+str(password)+"','"+str(l)+"');"
        doctreg="insert into doct_reg(firstname,lastname,gender,dob,specilization,address,state,district,place,pincode,contactnum,alternatenum,email,password) values('"+str(fname)+"','"+str(lname)+"','"+str(gender)+"','"+str(dob)+"','"+str(qualification)+"','"+str(address)+"','"+str(state)+"','"+str(district)+"','"+str(place)+"','"+str(pincode)+"','"+str(contactnum1)+"','"+str(contactnum2)+"','"+str(email)+"','"+str(password)+"');"
        c.execute(lblg)
        c.execute(doctreg)
        con.commit()
        email=request.POST.get('email')
        n=validateEmail(email)
       
        if(n==1):
            p=request.POST.get('pass')
            subject = 'Welcome........!'
            message = "your login password:%s" % (p)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently = False)          
            #return HttpResponse("mail send")
            return render(request,"Add_staff.html",{"msg":msg})
        else:
            return HttpResponse("mail id invalid",context)
    rand_password = get_random_string(length=10)

    if 'back' in request.POST:
        return render(request,"lab_owner.html")
    return render(request,'Add_Doctor.html',{'rand_password':rand_password},context)

#.........................doctor home page..................#
def doctor_home(request):
    return render(request,"doctor_home.html",context)



def addstaff_home(request):
    return render(request,"addstaff_home.html",context)

def lbowner_staffView(request):
    
    
    k=""
    i=""
    n=""
    m = list(context.values())[0]
    print(m)
    i="select labid from lab_reg where email='"+str(m)+"'"
    c.execute(i)
    n=c.fetchone()
    k=str(n[0])
    print(k)
    s ="select staffid,firstname,lastname,address,email,contactnum from staff_reg where labid='"+str(k)+"'"
    c.execute(s)
    result = c.fetchall()
    print(result)
    return render(request,"lbowner_staffView.html",{'dict':result})

def staff_delete(request):
    if 'yes' in request.POST:
        sku=request.GET.get('sku')
        print(sku)
        sid="DELETE FROM staff_reg WHERE email='"+str(sku)+"'"
        c.execute(sid)
        con.commit()
    return render(request,"staff_delete.html")

def book_test(request):
    if 'book_test' in request.POST:
        # get category from request
        # sub_categories = fetch all sub category which is under the 'category' from db
        # for sub_cat in sub_categories
        #   if(sub_cat is checked in request variable)
        #       add entry fro the sub_cat
        # return a template




