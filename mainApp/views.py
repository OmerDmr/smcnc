from django.shortcuts import render,HttpResponse, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail



def emailSend(request):


    if request.method == 'POST':
        print("email sended")
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        recipient_list = ['omer.1991.demir@gmail.com',]
        send_mail(subject, message, email, recipient_list)

        return render(request,'mainApp/homeEn.html',{})
    else:
        return render(request, 'mainApp/homeEn.html', {})




def emailSendTr(request):


    if request.method == 'POST':
        print("email sended")
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        recipient_list = ['omer.1991.demir@gmail.com',]
        send_mail(subject, message, email, recipient_list)

        return render(request,'mainApp/homeTr.html',{})
    else:
        return render(request, 'mainApp/homeTr.html', {})




def emailSendDt(request):


    if request.method == 'POST':
        print("email sended")
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        recipient_list = ['omer.1991.demir@gmail.com',]
        send_mail(subject, message, email, recipient_list)

        return render(request,'mainApp/homeDt.html',{})
    else:
        return render(request, 'mainApp/homeDT.html', {})





class HomePageEnView(TemplateView):
    template_name = 'mainApp/homeEn.html'

class HomePageDtView(TemplateView):
    template_name = 'mainApp/homeDt.html'

class HomePageTrView(TemplateView):
    template_name = 'mainApp/homeTr.html'






class MachineryEnView(TemplateView):
    template_name = 'mainApp/machineryEn.html'

class MachineryDtView(TemplateView):
    template_name = 'mainApp/machineryDt.html'

class MachineryTrView(TemplateView):
    template_name = 'mainApp/machineryTr.html'





class AboutUsEnView(TemplateView):
    template_name = 'mainApp/aboutUsEn.html'

class AboutUsDtView(TemplateView):
    template_name = 'mainApp/aboutUsDt.html'

class AboutUsTrView(TemplateView):
    template_name = 'mainApp/aboutUsTr.html'



