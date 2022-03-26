from django.db import models

# Create your models here.

#b'{"metadata":{"msg_sender":"0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266","epoch_index":0,"input_index":0,"block_number":11,"time_stamp":1645664172},"payload":"0x636172746573690d0a"}'
class Log(models.Model):
    msg_sender = models.CharField(max_length=70)
    epoch_index = models.IntegerField()
    input_index = models.IntegerField()
    block_number = models.IntegerField()
    time_stamp = models.IntegerField()
    payload = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.block_number)
    
    def __payload_converted__(self):
        return bytes.fromhex(self.payload[2:]).decode('utf-8')

class User(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    gender = models.IntegerField()
    BloodTipy = models.CharField(max_length=3)
    Religion = models.CharField(max_length=70)

    def __str__(self):
        return str(self.name)