#Importar biblioteca do Google Translator
from googletrans import Translator

#Instanciando o objeto tradutor
tradutor = Translator()

#Criação de uma função que receberá um texto em inglês e resultará o texto tradudo em Inglès
def Traduzir(textoOriginal) : return  tradutor.translate(textoOriginal, dest='pt').text

#Testes
print(Traduzir('First Translation'))
#Primeira Tradução
print(Traduzir('How are you?'))
#Como você está?
