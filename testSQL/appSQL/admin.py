from django.contrib import admin
from . import models

# Register your models here.

class LogAdmin(admin.ModelAdmin):
    list_display = ('msg_sender', 'epoch_index', 'input_index' ,'block_number' , 'time_stamp', 'payload', '__payload_converted__')
admin.site.register(models.Log, LogAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender' ,'BloodTipy' , 'Religion')
admin.site.register(models.User, UserAdmin)

    