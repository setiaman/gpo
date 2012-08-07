from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from mobile.models import Kebaktian
from datetime import date
from django import forms
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import Context, loader
from django.core.mail import send_mail


class FeedbackForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(required=False, initial="setiaman.lee@gmail.com")

#@csrf_protect
def feedback(request):
    if request.method == 'POST':
       form = FeedbackForm(request.POST)
       if form.is_valid():
           subject = form.cleaned_data['subject']
           message = form.cleaned_data['message']
           sender = form.cleaned_data['sender']
           recipients = ['setiaman.lee@gmail.com']
           send_mail(subject, message, 'setiaman@softship.com', recipients)
           return redirect('http://localhost:8000/mobile')
            
    else:
        form = FeedbackForm()
     #in case of form is invalid it will go to this function
        c = Context({'form':form })    
        return render_to_response('feedback.html', c )
    #return render_to_response('feedback.html', {'form':form }, context_instance = RC ( request))
    #return     render(request, 'feedback.html', c)    
	 	
	 
def index(request):
    #get latest Kebaktian schedule
    kset = Kebaktian.objects.filter(tanggal__gte=date.today()).order_by("tanggal")
    if kset.count() > 0:
        k = kset[0]
    else:
        kset = Kebaktian.objects.filter(tanggal__lte=date.today()).order_by("-tanggal")        
        k = kset[0]

    pujianList = k.kebaktianitem_set.filter(type='P')
    ayatList = k.kebaktianitem_set.filter(type='A')
    
    t = loader.get_template('index.html')
    #passing Kebaktian Object to the template
    c = Context({'Keb': k, 'pujianList': pujianList, 'ayatList': ayatList}) 
    return HttpResponse(t.render(c))
