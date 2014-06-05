from django import forms 
from django.contrib.auth.models import User
from moocadmin.models import University, Student
from django.forms import widgets

common_attrs={'onkeyup':'handleInput(this);',
              'onchange':'handleInput(this);',
              'maxlength':255,} 
# class to generate form 

class SignInForm(forms.Form):
   username = forms.CharField(max_length=30)
   password = forms.CharField(max_length=30,widget=forms.PasswordInput)

#class to generate form from model   
class UserForm(forms.ModelForm):
  
   password_attrs={'cols':30,'class':'field text medium',}
   last_name_attrs={'class':'field text medium',}
   first_name_attrs={'class':'field text medium',}
   
   password_attrs.update(common_attrs)
   last_name_attrs.update(common_attrs) 
   first_name_attrs.update(common_attrs) 
  
   first_name=forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs=first_name_attrs))
   last_name=forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs=last_name_attrs))
   password=forms.CharField(required=True,widget=forms.PasswordInput(attrs=password_attrs)) 
   class Meta:
      
     
      model = User
      fields = ['username','first_name','last_name','password',] # choose fields that you want
      
      
      # excludes = ['fields',...] this will display everything excluding the named fields  
      
      # overrides default widgte for a particular field 
      # attrs dict to set attributes for the field tag 
      #widgets =  {'password':forms.PasswordInput(attrs=password_attrs),}


      
class StudentForm(forms.ModelForm):
  
   class Meta:
      
      
      phone_number_attrs = {'min':0,'class':'field text medium'}
      phone_number_attrs.update(common_attrs)                        
      
      
      age_attrs={'min':0,
                 'max':120,
                 'class':'field text medium',}
      age_attrs.update(common_attrs)
      
      occupation_attrs  = {'class':'field text large',}
      occupation_attrs.update(common_attrs)     
      
      model = Student
      fields = ['phone_number','occupation','age','user']
      widgets ={'phone_number':forms.NumberInput(attrs=phone_number_attrs),
                'age':forms.NumberInput(attrs=age_attrs),
                'occupation':forms.Select(attrs=occupation_attrs)}
     
     
class ContactForm(forms.Form):
   name = forms.CharField(max_length=30,help_text='Blah blah')
   subject = forms.CharField(max_length=30,help_text='Blah blah')
   email = forms.EmailField(help_text='Blah blah')
   message= forms.CharField(widget=forms.Textarea(),help_text='Blah blah')
   

class UploadTaskForm(forms.Form):
   file=forms.FileField()