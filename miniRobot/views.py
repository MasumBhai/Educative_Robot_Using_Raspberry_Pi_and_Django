import threading
import webbrowser as web
import datetime
import time
import pyautogui as pg
import threading

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.timezone import get_current_timezone

from .models import *


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, subject, message, sender, recipient, fail_silently):
        self.subject = subject
        self.message = message
        self.sender = sender
        self.recipient = recipient
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(self.subject, self.message, self.sender, self.recipient, self.fail_silently)


def whatsappMsg(phone, msg):
    web.open('https://web.whatsapp.com/send?phone=+88' + phone + '&text=' + msg)
    time.sleep(20)
    pg.press('enter')


def baseEverywhere(request):
    if request.POST.get('send-message'):
        messages.success(request, 'You successfully sent your msg')
        nameOfParent = request.POST.get('contact-name')
        emailAddress = request.POST.get('contact-email')
        phoneNumber = request.POST.get('contact-phone')
        msgOfContact = request.POST.get('contact-message')
        msgTime = str(datetime.datetime.now(tz=get_current_timezone()))
        try:
            newSurvillance = surveillance.objects.create(
                parent_name=nameOfParent,
                parent_phone=phoneNumber,
                parent_mail=emailAddress,
                contact_msg=msgOfContact,
                image_uploaed_time=msgTime,
                kid_image="Ekhanei Kaaj korte hobe",
                video_streaming_link="Same"
            )
            messages.success(request=request, message="An email is sent to your mailing address")

            companyInfo = SoftwareCompany.objects.get(company_code__exact="coded by Brainy_Fool(+8801551805248)")

            subject = f'Thanks {newSurvillance.s_parent_name} for watching your kid through our service'
            message = render_to_string(template_name='promotional_Advertise.html',
                                       context={'personName': newSurvillance.contact_name,
                                                'personPhone': newSurvillance.contact_phone,
                                                'companyName': companyInfo.company_name,
                                                'companyPhone': companyInfo.company_phone,
                                                'companyMail': companyInfo.company_mail,
                                                })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [newContact.contact_mail, ]
            EmailThread(subject=subject, message=message, sender=email_from, recipient=recipient_list,
                        fail_silently=False).start()
            # send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        except:
            messages.error(request=request, message="Something Went Wrong, Kindly Try Again")
        try:
            companyInfo = SoftwareCompany.objects.get(company_code__exact="coded by Masum phone(+8801551805248)")
            companyAddress = companyInfo.company_address
            companyName = companyInfo.company_name
            msgg = str(companyName + " company's Location: \n" + companyAddress)
            whatsappMsg(phone=phoneNumber, msg=msgg)
        except:
            messages.error("Wrong Mobile Info")


def home(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'index.html', context=context)
