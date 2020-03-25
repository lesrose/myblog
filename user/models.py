# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    u_tel = models.CharField(max_length=11, blank=True, null=True)
    u_email = models.CharField(max_length=20, blank=True, null=True)
    u_nike_name = models.CharField(max_length=20, blank=True, null=True)
    u_pwd = models.CharField(max_length=50, blank=True, null=True)
    u_is_delete = models.IntegerField(blank=True, null=True,default=0)

    class Meta:
        managed = True
        db_table = 't_user'
