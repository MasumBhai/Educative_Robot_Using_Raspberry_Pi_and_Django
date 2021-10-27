from django.contrib import admin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from cuteRobot import settings
from .models import *
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(project_team)
class Team(admin.ModelAdmin):
    list_display = ['team_name','team_mail','team_phone',]
    list_display_links = ['team_mail']
    fields = ['team_code',('team_name','team_mail'),'team_phone']
    readonly_fields = ['team_code',]
    pass

@admin.register(surveillance)
class Robot(admin.ModelAdmin):
    list_display = ['s_parent_mail','s_parent_name', 's_parent_phone', 's_image_upload_time', 's_kid_image','s_kid_video_link']
    list_filter = ['s_parent_mail']
    list_display_links = ['s_parent_mail']
    fields = [('s_kid_video_link','s_parent_phone'), ('s_parent_name', 's_parent_mail'),
              ('s_image_upload_time', 's_kid_image'),]
    # readonly_fields = ('s_parent_name', 's_parent_phone', 's_kid_video_link')
    list_per_page = 15
    paginator = Paginator
    pass

