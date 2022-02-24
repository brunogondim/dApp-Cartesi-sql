from .models import Log
from .Serializers import LogSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

# class Teste(View):
#     def get(self, request):
#         # <view logic>
#         body = HttpRequest.body
#         return HttpResponse('result')
#     def post(self,request):
#         body = HttpRequest.body 
        
        
        
        # retorno = ''

        # return HttpResponse(retorno)

class Portal(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        metadata = request.data['metadata']
        payload = {'payload':request.data['payload']}
        metadata.update(payload)
        serializer = LogSerializer(data=metadata)
        if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=202)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     # permission_classes = [permissions.IsAuthenticated]