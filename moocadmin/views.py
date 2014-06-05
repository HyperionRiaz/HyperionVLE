from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from moocadmin.myforms import SignInForm, UserForm,StudentForm, ContactForm, UploadTaskForm
# Create your views here.
from django.forms.models import inlineformset_factory

'''
    Basic outer pages.
'''

def index(request):
    if request.user.is_authenticated():
        return render_to_response('moocadmin/join.html',{'user':True})
    else:
        return render_to_response('moocadmin/join.html',{'user':False})
    

def setup(request):
    pass

'''
def signup_process(request):
    name = request.POST.get('Field1')
    surname = request.POST.get('Field2')
    password = request.POST.get('password')
    user = User()
    user.username = name
    user.set_password(password)
    user.save()
    context = {'name':name,'surname':surname}
    return render_to_response('moocadmin/mocktemplate.html',context)
'''



def login(request):
    form=SignInForm    
    formModel = SignInForm()
    c = {'form':form,'formModel':formModel, }
    c.update(csrf(request))
    
    return render_to_response('moocadmin/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/moocadmin')
    else:
        return HttpResponse("sorry invalid details")
   
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/moocadmin')

def student_signup(request):
    valid = True
    if request.method=='POST':
        forms=[UserForm(request.POST),StudentForm(request.POST)] #form must be bound to posted data to use validation
        for form in forms:
            valid = valid and form.is_valid()
        if valid:
            forms[0].save()
            
            num = User.objects.filter(username=request.POST['username'])[0].pk
            #return HttpResponse(num)
            forms[1].user = num
            forms[1].save()
            return HttpResponseRedirect('/moocadmin')
    else:
        forms = [UserForm(),StudentForm()]
        
    context = {'forms':forms,'error':not valid,}
    context.update(csrf(request))        
    return render_to_response('moocadmin/student_reg_form.html',context)

def contact(request):
    valid = True
    if request.method=='POST':
        forms=[ContactForm(request.POST)] #form must be bound to posted data to use validation
        for form in forms:
            valid = valid and form.is_valid()
        if valid:
            '''
                send email 
            '''
         
             
            #subject, from_email = 'Account created', 'admin@mywebsite.com'
            #html_content = render_to_string('email.html')
            #text_content = strip_tags(html_content)
            #msg = EmailMultiAlternatives(subject, text_content, from_email, [user@somewebsite.com])
            #msg.attach_alternative(html_content, 'text/html')
            #msg.send()  
            send_mail('Subject here', 'Here is the message.', 'from@example.com',
                ['to@example.com'], fail_silently=False)            
            return HttpResponseRedirect('/moocadmin')
    else:
        forms = [ContactForm]
        
    context = {'forms':forms,'error':not valid,}
    context.update(csrf(request))        
    return render_to_response('moocadmin/contact_form.html',context)    

def handle_uploaded_file(f):
 
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_task(request):
    
    if request.user.is_authenticated():
        valid=True
        if request.method=='POST':
            form = UploadTaskForm(request.POST,request.FILES)
            valid=form.is_valid()
            if valid:
                handle_uploaded_file(request.FILES['file'])        
                return HttpResponseRedirect('/moocadmin')
        else:
            form = UploadTaskForm()
                
        context = {'forms':form,'error':not valid,}
        context.update(csrf(request))        
        return render_to_response('moocadmin/student_task_submit_form.html',context)        
    else:
        return HttpResponse('Access Denied:')