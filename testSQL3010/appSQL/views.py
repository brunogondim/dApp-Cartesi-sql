from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from . import models

import logging
import requests
import json

# Create your views here.

class Portal(View):
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
        response = requests.post(dispatcher_url + "/notice", json={"payload": json.loads(request.body)['payload']})
        self.logger.warning('Received notice status %s body %s', response.status_code, response.content)

        self.logger.warning("Finishing")
        response = requests.post(dispatcher_url + "/finish", json={"status": "accept"})
        self.logger.warning('Received finish status %s', response.status_code)

        return HttpResponse(status=202) 