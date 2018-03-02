import aiml
import os

ai = aiml.Kernel() # inicialização

if os.path.isfile("bot_brain.brn"):
    ai.bootstrap(brainFile = "bot_brain.brn")
else:
    ai.bootstrap(learnFiles = "start.xml", commands = "load aiml b")
    ai.saveBrain("bot_brain.brn")

def nameBot():
    return "Beth"

def comands(text):
    resposta = None
    if text == nameBot()+" atualize o cerebro":
        ai.bootstrap(learnFiles = "start.xml", commands = "load aiml b")
        ai.saveBrain("bot_brain.brn")
        resposta = "Cerebro atualizado com sucesso companheiro"
    return resposta


#ai.learn('start.xml') # lê o arquivo principal da AIML e faz referências aos outros
#ai.respond('load aiml b') # faz com que os outros arquivos da AIML sejam carregados

while True:
    frase = input('Você: ')
    resposta = comands(frase)
    if resposta == None:
        resposta = ai.respond(frase)
    print (nameBot() +": ", resposta)