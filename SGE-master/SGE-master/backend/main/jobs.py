from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import apps
import pandas as pd

def StartChatBotScheduler():
    # Inicializar o Django para garantir que os aplicativos estejam prontos
    apps.check_apps_ready()

    # Importe os modelos aqui, após garantir que os aplicativos estejam prontos
    from .models import ChatBot

    # Criar o agendador
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(ChatBotJob, 'interval', seconds=12, args=[ChatBot])
    scheduler.start()

def ChatBotJob(ChatBotModel):
    objetos_filtrados = ChatBotModel.objects.all()
    for objeto in objetos_filtrados:
        lista = []
        if objeto.done == False and objeto.scheduledDate <= timezone.now():
            objeto.done = True
            objeto.save()
            teste = objeto.file.read()
            lista.append(teste)
            nomes = []
            numeros = []
            tamanho_dados = len(lista)
            contador = range(tamanho_dados)
            for i in contador:
                arquivo = lista[i]
                dados_originais = pd.read_excel(arquivo, header=0) # le o arquivo a partir do cabeçalho da linha 1
                dados = dados_originais.to_dict("list")
                tamanho_dados = len(dados["nome"])
                contador = range(tamanho_dados)
                for i in contador:  
                    nomes.append(dados["nome"][i])
                    numeros.append(dados["numero"][i])
                tamanho_dados = len(nomes)
                contador = range(tamanho_dados)
                for cont in contador:
                    print(f"nomes: {nomes[cont]} - numeros: {numeros[cont]}")
        else:
            return None
    

                
    

