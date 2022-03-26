from asyncio.log import logger
from . import models
from . import Serializers

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import connection

import logging
import requests

class Portal(APIView):
    parser_classes = [JSONParser]
    logger = logging.getLogger()
    logger.addHandler('console')
    
    
#     def options(self, request):
#         pass

    def post(self, request):

        dispatcher_url = 'http://127.0.0.1:5004'

        #aquire all incoming data
        metadata = request.data['metadata']
        payloadHex = {'payload':request.data['payload']}
        payload = bytes.fromhex(payloadHex['payload'][2:]).decode('utf-8')
        metadata.update(payloadHex)    

        # save all data as log to the DB
        logserializer = Serializers.LogSerializer(data=metadata)
        if logserializer.is_valid():
                logserializer.save()      
        else:
                return Response(logserializer.errors, status=status.HTTP_202_ACCEPTED)
        logger.info('metadata and payload saved as log')
        
        logger.info('adding notice')
        response = requests.post(dispatcher_url + "/notice", json={"payload": request.data['payload']})
        logger.info('Received notice status %s body %s', response.status_code, response.content)

        logger.info("Finishing")
        response = requests.post(dispatcher_url + "/finish", json={"status": "accept"})
        logger.info('Received finish status %s', response.status_code)

        return Response(status=status.HTTP_202_ACCEPTED)        

        # @app.route("/advance", methods=["POST"])
        # def advance():
        #         body = request.get_json()
        #         app.logger.info(f"Received advance request body {body}")
        #         app.logger.info("Adding notice")
        #         response = requests.post(dispatcher_url + "/notice", json={"payload": body["payload"]})
        #         app.logger.info(f"Received notice status {response.status_code} body {response.content}")
        #         app.logger.info("Finishing")
        #         response = requests.post(dispatcher_url + "/finish", json={"status": "accept"})
        #         app.logger.info(f"Received finish status {response.status_code}")
        #         return "", 202
        

        # # secure SQL Operations
        # """Pattern:
        #         User Action: Insert ; Select ; Update ; Delete ; none ;
        #         Table: Users ;
        #         Columns: Columns of the selected Table ; none
        #         Conditions: Column ;
        #         Conditions_Operator: = ; none ;
        #         Conditions_Paremeter: arg ; none ;
        #         Admin_Action: Free SQL ; none ;
        #         """
        # userAction = payload['User Action']
        # table = payload['Table']
        # columns = payload['Columns']
        # conditions = payload['Conditions']
        # conditions_Operator = payload['Conditions_Operator']
        # conditions_Paremeter = payload['Conditions_Paremeter']
        # admin_Action = payload['Admin_Action']

        # if userAction == 'Insert':
        #         if table == 'User':
        #                 userSelializer = Serializers.UserSerializer(columns)
        #                 if userSelializer.is_valid():
        #                         userSelializer.save()      
        #                 else: return Response(userSelializer.errors, status=status.HTTP_202_ACCEPTED)
        #         else: Response('table not found', status=status.HTTP_202_ACCEPTED)

        # elif userAction == 'Select':
        #         #TODO
        #         pass
        # elif userAction == 'Update':
        #         #TODO
        #         pass
        # elif userAction == 'Delete':
        #         #TODO
        #         pass
        
        # # risky SQL Operations: free sql commands has risk of SQL attacks!
        # elif admin_Action != 'none':

        #         #gerneral
        #         try:
        #                 connection.cursor().execute(admin_Action)
        #         except Exception as e:
        #                 return Response('something went wrong: ' + e, status=status.HTTP_202_ACCEPTED)

        #         try:
        #                 raw = connection.cursor().fetchall()
        #                 return Response(raw, status=status.HTTP_202_ACCEPTED)
        #         except Exception as e:
        #                 return Response('something went wrong? ' + e, status=status.HTTP_202_ACCEPTED)
                               
        #         # # or specific select statemants select?
        #         # if table == "Log":
        #         #         models.Log.objects.raw(admin_Action)
        #         # if table == "User":
        #         #         models.User.objects.raw(admin_Action)


        # else: return Response('nothing done', status=status.HTTP_202_ACCEPTED)

        # return Response('all done correctly', status=status.HTTP_202_ACCEPTED)