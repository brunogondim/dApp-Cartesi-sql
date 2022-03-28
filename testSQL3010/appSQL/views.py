from django.core.serializers import serialize

from django.http import HttpResponse, JsonResponse
from django.views import View
from . import models

import logging
import requests
import json
import binascii

# Create your views here.

class Advance(View):
    # parser_classes = [JSONParser]
    logger = logging.getLogger(__name__)
    # logger.addHandler('console')
    #logger.setLevel(logging.INFO)
    
    def get(self, request):
        self.logger.warning('teste')
        return HttpResponse("teste",status=202)

    def post(self, request):

        dispatcher_url = 'http://127.0.0.1:5004'

        #aquire all incoming data
        metadata = json.loads(request.body)['metadata']

        payloadHex = {'payload':json.loads(request.body)['payload']}
        payload = bytes.fromhex(payloadHex['payload'][2:]).decode('utf-8')
        metadata.update(payloadHex)    

        # save all data as log to the DB
        reg = models.Log(
            msg_sender=metadata['msg_sender'], 
            epoch_index=metadata['epoch_index'], 
            input_index=metadata['input_index'], 
            block_number= metadata['block_number'], 
            time_stamp= metadata['time_stamp'], 
            payload=metadata['payload'] 
        )
        reg.save()
        self.logger.warning('metadata and payload saved as log')
        
        self.logger.warning('adding notice')
        noticePayload = serialize("json",models.Log.objects.all())
        noticePayloadBytes = noticePayload.encode('utf-8')
        noticePayloadHex = "0x{0}".format(binascii.hexlify(noticePayloadBytes).decode('utf-8'))
        response = requests.post(dispatcher_url + "/notice", json={"payload": noticePayloadHex})
        self.logger.warning('Received notice status %s body %s', response.status_code, response.content)

        self.logger.warning("Finishing")
        response = requests.post(dispatcher_url + "/finish", json={"status": "accept"})
        self.logger.warning('Received finish status %s', response.status_code)

        return HttpResponse(status=202)


# https://www.online-toolz.com/tools/hex-to-text-converter.php
class Inspect(View):
    
    logger = logging.getLogger(__name__)
    
    def get(self, request, whatHex):

        #what = bytes.fromhex(whatHex['payload'][2:]).decode('utf-8')
        what = whatHex
        self.logger.warning(f"Received inspect request payload Hex {whatHex}")
        self.logger.warning(f"Received inspect request payload {what}")

        payload = serialize("json",models.Log.objects.all())

        return  JsonResponse(data={"reports": [{"payload": payload}]},status=202)

