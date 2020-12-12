from django.shortcuts import render
from django.core.mail import EmailMessage,send_mail

def index(request):
     return render(request,'portf.html')

def contact(request):
     if request.method == 'POST':
          full_name1 = request.POST.get('full_name1')
          email1 = request.POST.get('email1')
          message1 = request.POST.get('message1')
          subject = request.POST.get('subject')
          if email1 == 'hamzaansarics@gmail.com':
               return render(request,'contact.html',{'email1':email1,'full_name1':full_name1})
          else:
          
               send_mail(
                    subject=subject,
                    message= subject+"\n"+full_name1+"\n"+email1+"\n"+message1,
                    from_email= email1,
                    
                    recipient_list=['hamzaansarics@gmail.com']
               )
          
               return render(request,'contact.html',{'full_name1':full_name1 })
     else:
          return render(request,'contact.html')
          

def home(request): 
     if request.method == 'POST':
          full_name=request.POST.get('full_name')
          email = request.POST.get('email')
          if email == 'hamzaansarics@gmail.com':
               return render(request,'home.html',{'email':email,'full_name':full_name})
          else:

               message = request.POST.get('message')

               send_mail(
                    subject='Testing',
                    message= "Opinions"+"\n"+full_name+"\n"+email+"\n"+message,
                    from_email= email,
                    
                    recipient_list=['hamzaansarics@gmail.com']
               )
          
               return render(request,'home.html',{'full_name':full_name})
     else:
          return render(request,'home.html',{})