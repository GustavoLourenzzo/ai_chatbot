import aiml, os, wikipedia, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets,uic



ai = aiml.Kernel() # inicialização

#setar as variaveis antes da inicialização
ai.setPredicate("myName", "Beth")
ai.setPredicate("myAge", "25")

#ai.setPredicate()

#config wikipedia e definição
wikipedia.set_lang('pt') #definir linguagem
keywords = ['o que é ','o que e ', 'quem é ','quem e ', 'quem foi ', 'definição ', 'defina ']
categories = ['Sistema circulatório']

def get_answer(text):
    result = None
    for key in keywords:
        if text.startswith(key):
            result = text.replace(key, '')
    if result == None:
        result =  text
    try:
        WikiPage = wikipedia.page(title = result, auto_suggest = True)
        cat = WikiPage.categories
        cat2 = []
        for ct in cat:
            cat2.append(ct.replace('Categoria:', ''))
        for cat_seach in cat2:
            for categ_seach in categories:
                if categ_seach == cat_seach:
                    result = wikipedia.summary(wikipedia.search(WikiPage.title)[0], sentences=1)
                    return result
        result = "Desculpe mais esse assunto não faz parte do nosso contexto, por favor vamos falar de outra coisa."
        return result
        #results = wikipedia.search(result)
        #result = wikipedia.summary(results[0], sentences=1)
    except:
        result = "Desculpe a sua pergunta foi um pouco ambigua ou nao foi encontrada, refaça a pergunta, eu gostaria muito de poder ajudar."
    return result
#fim**

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
        resposta = "Cerebro atualizado com sucesso"
    return resposta


#ai.learn('start.xml') # lê o arquivo principal da AIML e faz referências aos outros
#ai.respond('load aiml b') # faz com que os outros arquivos da AIML sejam carregados

while True:
    frase = input('Você: ')
    resposta = comands(frase)
    if resposta == None:
        resposta = ai.respond(frase)
        if resposta == '###':
            print(nameBot()+': ', 'Hum ... não encontrei essa pergunta em minha base da dados.\nPorem posso verificar no wikipedia para você ...')
            resposta = get_answer(frase)
            print(resposta)
        else:
            print (nameBot() +": ", resposta)
    pass

"""
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle(nameBot())
        self.Enviar.clicked.connect(self.exibir)

        self.corpo.setReadOnly(True)
                

    def exibir(self):
        self.text = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.corpo.insertHtml('<div style="padding: 20px; text-align:Left;"><br><strong>Você:</strong><br><br>'+self.text+'<br><br></div>')
        resposta = comands(self.text)
        if resposta == None:
            resposta = get_answer(self.text)
            if resposta == None:
                resposta = ai.respond(self.text)
        self.corpo.insertHtml('<div style="padding: 20px; text-align: right;"><br><strong>'+ nameBot() +':</strong><br><br>'+ resposta +'<br><br></div>')
        #soup = BeautifulSoup('<div style="padding: 20px; text-align: right;"><br><strong>'+ nameBot() +':</strong><br><br>'+ resposta +'<br><br></div>', "lxml")
        #self.corpo.insertHtml(soup.get_text())
        


if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    programa = MainWindow()
    programa.show()
    sys.exit(app.exec_())
    



root = QApplication(sys.argv)
app = Window()
app.show()
sys.exit(root.exec_())
"""