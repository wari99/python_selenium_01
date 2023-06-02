# Login simples na pagina de rastreamento do correios
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "xxxxxxxxxxxxxx"
userpwd = "yyyyyyyyyyyyy"
urlsite = "https://cas.correios.com.br/login?service=https%3A%2F%2Frastreamento.correios.com.br%2Fcore%2Fseguranca%2Fservice.php"

#Abrindo a pagina de login 
navegador = webdriver.Chrome()
navegador.get(urlsite)
#navegador.get("https://cas.correios.com.br/login?service=https%3A%2F%2Frastreamento.correios.com.br%2Fcore%2Fseguranca%2Fservice.php")

#Escrevendo credenciais
campo_username = navegador.find_element("xpath", '//*[@id="username"]')
campo_username.clear()
campo_username.send_keys(username) #username

campo_userpwd = navegador.find_element("xpath", '//*[@id="password"]')
campo_userpwd.clear()
campo_userpwd.send_keys(userpwd) #password

botao_entrar = navegador.find_element("xpath", '//*[@id="fm1"]/div[2]/button').click() #entrando
