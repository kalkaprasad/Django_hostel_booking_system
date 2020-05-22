from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render,redirect
from kp1.forms import Employeeform
from kp1.models import Employee
from kp1.models import useraccount
from kp1.models import upload_data
from kp1.models import mylogin
from kp1.models import models
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from kp1.models import bookservice
from  django.contrib.sessions.models import Session


# here this is the normal Form

def emp(request):
    if request.method=="POST":
        form=Employeeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return  redirect()
            except:
                pass
    else:
        form=Employeeform()
    return  render(request,"sendta.html",{'form':form})

def show(request):
    employees=Employee.objects.all()
    emmp1="employees"
    emmp2=""
    data= Employee.objects.raw('SELECT id,eemail FROM employee')
    for check in data:
        if(check.eemail=="kalka89@gmail.com" and check.id==8):
            emmp2="Matched"
        else:
            emmp2="failed"


    return render(request,"show.html",{'employees':data,'check':emmp2})




def index(request):
    return  render(request,'index.html',{'hostellink':'''http://127.0.0.1:8000/hostel
''','contactus':'http://127.0.0.1:8000/contact','about':'http://127.0.0.1:8000/about','signup':'http://127.0.0.1:8000/signup','login':'http://127.0.0.1:8000/login','hostelfind':'http://127.0.0.1:8000/hostelfound','mylogin':'http://127.0.0.1:8000/mylogin.go'})

def hostelfound(request):
    if request.method=="POST":
        hostelname=request.POST['hname']
        hostelphone=request.POST['hphone']
        hostelemail=request.POST['hemail']
        hosteladdress=request.POST['haddress']
        hosteltime=request.POST['htime']
        #names="kalka"
        upload_data=bookservice(cname=hostelname,cphone=hostelphone,cemail=hostelemail,caddress=hosteladdress,ctime=hosteltime)
        upload_data.save()
        return redirect('success')
       # return render(request,'hostel.html',{"hostel_Confirm_pop":"success"})
    else:

        return  render(request,'hostel.html',{"hostel_Confirm_pop":"fail"})



    return render(request,'hostel.html')
def contact(request):

    if request.method=="POST":
        fname=request.POST['fname']
        emal=request.POST['email']
        cmmt=request.POST['comment']

        email = 'hxxhack890@gmail.com'
        password = 'prasad786786'
        send_to_email = emal
        subject = 'testing Email'
        messageHTML =emal
        messagePlain = 'Visit nitratine.net for some great tutorials and projects!'

        msg = MIMEMultipart('alternative')
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        # Attach both plain and HTML versions
        msg.attach(MIMEText(messagePlain, 'plain'))
        msg.attach(MIMEText(messageHTML, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        #return render(request,"index.html",)
        return redirect("http://127.0.0.1:8000/",{"send":"ok"})
    else:
        return HttpResponse("Something went wrong")

    return  render(request,'contactform.html')

def hostels(request):

   # it store the sessions Id and check if the session are store inside the  cookies and then redriect the next page..

    return redirect('login')

def success(request):

   # if request.session.has_key('kp'):
    if 'kp' in request.session: # here I getted the Session Variable
        useremail=request.session.get('kp') # get() method use for get the the session variable...
        query="SELECT id,name,email,phone FROM `useraccount` WHERE email='{}'".format(useremail)
        userdata=useraccount.objects.raw(query)
        for checked in userdata:
            checked.email
            checked.name
            checked.phone
            print(checked.email)
        return render(request,'success.html',{'username':checked.name,'useremail':checked.email,'userphone':checked.phone,'bookhostel':'http://127.0.0.1:8000/hostelfound'})


    else:
        return redirect('login')


def about(request):

    return  render(request,'about.html')

# singup user
def signup(request):
    # this is the Method for the Signup user
    if request.method == "POST":
        name = request.POST['name']
        emails = request.POST['email']
        phones = request.POST['phone']
        passwords = request.POST['password']
        # query=[name,emails,phones,passwords]
        id=10
        p = useraccount(name=name, email=emails, phone=phones, password=passwords)
       # p.name="Akanksha sahu update" # This  is use for the update the data from the database...
        p.save()

        return  redirect("http://127.0.0.1:8000/login")

    return render(request,'signup.html',{'loginredirect':'http://127.0.0.1:8000/login'})




def userpage(request,username):

       # return render(request, 'success.html', {'username': username, 'bookhostel': 'http://127.0.0.1:8000/hostelfound','redirectlogin': 'http://127.0.0.1:8000/login'})
        return redirect("http://127.0.0.1:8000/login")



# login user
def login(request):

    if request.session.has_key('kp'): # this function check  the session  if the session are matched then redirect the main page..
        return  redirect('success')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
       # checkcred=useraccount.objects.raw('select id, email, password from useraccount')
        #print(checkcred.email)
          #print(checkcred)
       # for chekevalue in checkcred :
           # if(chekevalue.email == username and chekevalue.password == password):
        count=useraccount.objects.filter(email=username,password=password).count()
        # here we are  use the count for the count number of the fetch and  match data from the database and then start the login
        if(count>0):
            request.session['kp']= username
            return  redirect('success')
            # return render(request, 'success.html', {'username': username, 'bookhostel': 'http://127.0.0.1:8000/hostelfound','redirectlogin': 'http://127.0.0.1:8000/login'})

        else:
                # return render(request,'login.html')
             return HttpResponse("Something went wrong")

    return render(request, 'login.html',{'signup':'http://127.0.0.1:8000/signup'})


# upload hostel details

def upload(request):

    if request.method=="POST":
        hosteln=request.POST['hostelname']
        hosteadd = request.POST['address']
        hostelrat = request.POST['rate']
        hostedesc = request.POST['disc']
        hostefile = request.FILES['file']
        fs = FileSystemStorage() # this
        filename = fs.save(hostefile.name, hostefile)
        uploaded_file_url = fs.url(filename)
        ids=1
        uplod_todata=upload_data(files=hosteln,hostelname=hosteadd,hostelad=hostelrat,hosterate=hostedesc,hosteldes=uploaded_file_url)
        uplod_todata.id
        uplod_todata.save()
        return render(request,'uploadh.html',{"uploaded_file_url":'H:\webframework\env\kp1{}'.format(uploaded_file_url),"upload":"kp"})




    return render(request,'uploadh.html')
     #return HttpResponse(request,"Hello kp")
def fetchhostel(request):

    if request.method=="post":

        valueget=upload.objects.all()
        for i in valueget:
            abc=valueget.hostename
            print(abc)


    return  render(request,"fetchhosteldetails.html",{"hostelvalue":abc})

# Admin Login

def AdminLogin(request):

    if(request.method=="POST"):

        adminemail=request.POST["email"]
        adminpass=request.POST["password"]
        checkcre=mylogin.objects.raw("select id,email,password from mylogin")

        for ck in checkcre:

            if(ck.email==adminemail and ck.password==adminpass):

                return  render(request,"uploadh.html")
            else:
                return  render(request,"AdminLogin.html",{"popup":"kalka"})

    return  render(request,"AdminLogin.html")

def logout(request):
    del request.session['kp']
    return  redirect('login')

def dashboard(request):

    return  render(request,'Dashboard.html')

def searchhostel(request):
    return render(request,"searchhostel.html")
def camera(request):
    return  render(request,"camera.html")