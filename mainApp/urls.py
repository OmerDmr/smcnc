from django.urls import path,re_path

from .views import *

app_name = 'mainApp'

urlpatterns = [


    path('', HomePageEnView.as_view(), name='home'),
    path('HomeTr/', HomePageTrView.as_view(), name='homeTr'),
    path('HomeDt/', HomePageDtView.as_view(), name='homeDt'),





    path('MachineryEn/', MachineryEnView.as_view(), name='MachineryEn'),
    path('MachineryTr/', MachineryTrView.as_view(), name='MachineryTr'),
    path('MachineryDt/', MachineryDtView.as_view(), name='MachineryDt'),


    path('AboutUsEn/', AboutUsEnView.as_view(), name='AboutUsEn'),
    path('AboutUsTr/', AboutUsTrView.as_view(), name='AboutUsTr'),
    path('AboutUsDt/', AboutUsDtView.as_view(), name='AboutUsDt'),

    re_path('emailSend/', emailSend, name='emailSend'),
    re_path('emailSendTr/', emailSendTr, name='emailSendTr'),
    re_path('emailSendDt/', emailSendDt, name='emailSendDt'),



]