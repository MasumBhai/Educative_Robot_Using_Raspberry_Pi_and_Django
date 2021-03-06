from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from phone_field import PhoneField

MAX_LENGTH = 500


class surveillance(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_parent_name = models.CharField(max_length=64, help_text="participant's name")
    s_parent_phone = PhoneField(help_text="parent's phone number")
    s_parent_mail = models.EmailField(max_length=120, help_text="Parent's email address", blank=True, null=True)
    s_kid_image = models.ImageField(upload_to='kid_image/%Y/%m/%d/', blank=True, null=True,
                                    verbose_name="Kid's image")
    s_kid_video_link = models.URLField(max_length=MAX_LENGTH,
                                       help_text="Github/GitLab repo link of Client work we have done", blank=True,
                                       null=True)
    s_image_upload_time = models.DateTimeField(help_text="Image Upload Time", blank=True, null=True)

    def image_tag(self):
        return mark_safe("<img src='/../../media/%s' width='150' height='150' />" % (self.s_kid_image))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Project_Hackathon'
        verbose_name_plural = 'Project_Hackathon'
        ordering = ['-s_image_upload_time']  # from top to bottom
        db_table = 'surveillance'

    def __str__(self):
        return "%s" % (self.s_parent_mail)


class project_team(models.Model):
    team_code = models.CharField(default='coded by Brainy_Fool(+8801551805248)', max_length=MAX_LENGTH,
                                 primary_key=True)
    team_name = models.CharField(verbose_name='Team-name', max_length=120, blank=True, null=True)
    team_mail = models.EmailField(verbose_name='Team-Leader-mail-address', max_length=120, blank=True,
                                  null=True)
    team_phone = PhoneField(verbose_name="Team-Leader-phone-number")

    class Meta:
        verbose_name = 'Project_Team'
        verbose_name_plural = 'Project_Team'
        db_table = "project_team"

    def __str__(self):
        return "%s" % (self.team_mail)