import pyautogui
import pyperclip
import pandas
import time

pyautogui.PAUSE = 2

# Passo 0: Abrir o navegador
def abrirNavegador() :
  pyautogui.hotkey("ctrl", "alt", "t") # abrir terminal
  time.sleep(4)
  pyautogui.write("opera") # escrever "opera" no terminal
  pyautogui.press("enter") # pressional enter

  acessarSistema()
    
# Passo 1: Acessar o sistema da empresa
def acessarSistema():
  pyautogui.hotkey("win", "up") # ir para barra de pesquisa
  pyautogui.hotkey("ctrl", "l") # ir para barra de pesquisa
  link = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"
  pyautogui.write(link) # digitar link no navegador
  pyautogui.press("enter") # pressionar enter

  login()

# Passo 2: Fazer login no sistema
def login():
  time.sleep(5)
  pyautogui.click(x = 715, y = 410) # clicar no espaço de login
  pyautogui.write("meu_login") # escrever o login
  pyautogui.click(x = 715, y = 485) # clicar no espaço de senha
  pyautogui.write("minha_senha") # escrever senha
  pyautogui.click(x = 715, y = 550) # clicar em acessar
  
  time.sleep(5)
  downloadDatabase()

# Passo 3: Baixar base de dados
def downloadDatabase():
  pyautogui.click(x = 555, y = 375) # clicar no arquivo do drive com a database
  pyautogui.click(x = 1265, y = 375) # clicar nos 3 pontinhos
  pyautogui.click(x = 955, y = 625) # fazer o download

  time.sleep(6)
  calclateData()


# Passo 4: Calcular os indicadores
def calclateData():
  tabela = pandas.read_csv(r"/home/teones/Downloads/Compras.csv", sep=";")

  total_gasto = tabela["ValorFinal"].sum()
  quantidade = tabela["Quantidade"].sum()
  preco_medio = total_gasto / quantidade

  enviarEmail(total_gasto, quantidade, preco_medio)

# Passo 5: Enviar o email para a diretoria/para o chefe
def enviarEmail(total_gasto, quantidade, preco_medio):
  pyautogui.hotkey("ctrl", "t")

  pyautogui.hotkey("ctrl", "l") # ir para barra de pesquisa
  pyautogui.write("https://mail.google.com/mail/u/0") # ir para o link
  pyautogui.press("enter") # pressiona enter

  time.sleep(5)

  pyautogui.click(x = 145, y = 235)
  time.sleep(1)
  pyautogui.write("teones.alex13@gmail.com") 
  pyautogui.press("tab") # escolher o destinatario

  pyautogui.press("tab") # passar para o campo assunto
  pyperclip.copy("Relatório de Vendas")
  pyautogui.hotkey("ctrl", "v")

  pyautogui.press("tab") # passando para o corpo do email

  texto = f"""Prezados,
  Segue o relatório de compras

  Total Gasto: R${total_gasto:,.2f}
  Quantidade de Produtos: {quantidade:,}
  Preço Médio: R${preco_medio:,.2f}

  Qualquer dúvida, é só falar.
  Att., Teones Alex"""

  pyperclip.copy(texto)
  pyautogui.hotkey("ctrl", "v")

  time.sleep(1)
  pyautogui.hotkey("ctrl", "enter")

  fechar()


# Passo Final: Fechar tudo
def fechar():
  time.sleep(8)
  pyautogui.hotkey("ctrl", "shift", "w")
  time.sleep(1)
  pyautogui.hotkey("ctrl", "d")


##########################################################
def mousePosition():
  while True:
    print(pyautogui.position())

abrirNavegador()