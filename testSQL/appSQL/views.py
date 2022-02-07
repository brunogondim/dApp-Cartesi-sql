from django.http import HttpResponse, HttpRequest
from django.views import View

# Create your views here.

class Teste(View):
    def get(self, request):
        # <view logic>
        body = HttpRequest.body
        return HttpResponse('result')
    def post(self,request):
        body = HttpRequest.body 
        
        
        
        retorno = ''

        # if (request.POST['tipo_de_atualizacao']=='manual'):
        #     try:
        #         n_record = models.Lancamento.objects.atualizacao_manual()
        #         retorno+= "atualização manual concluída. " + n_record + ' lançamentos.'
        #     except Exception as error:
        #         retorno+= "Erro: " + str(error) + "   "        
        # elif (request.POST['tipo_de_atualizacao']=='apagar'):
        #     models.Lancamento.objects.apagar_lancamentos()
        #     retorno+= "lançamentos apagados."
        # else:
        #     retorno+= models.Lancamento.objects.atualizacao_auto_DB_ecidade(request.POST['ip'],
        #                                                                     request.POST['porta'],
        #                                                                     request.POST['nome_do_banco'])
        return HttpResponse(retorno)