from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Solita o login do usuário
email = str(input('Digite seu e-mail do Linkedin: '))
senha = str(input('Digite sua senha do Linkedin: '))

# Abri o navegador para acessar o Linkedin
drive = webdriver.Chrome()
drive.get('https://www.linkedin.com/login')

# Preenche os campo de login
drive.find_element(By.ID,'username').send_keys(email)
drive.find_element(By.ID, 'password').send_keys(senha)
drive.find_element(By.XPATH, '//*[@type="submit"]').click()


# Aguarda a página inicial carregar
WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Pesquisar"]'))
)

# Escrever na barra de pesquisa "Desenvolvedor"
barra_de_pesquisa = drive.find_element(By.XPATH, '//*[@placeholder="Pesquisar"]')
barra_de_pesquisa.send_keys('desenvolvedor')
barra_de_pesquisa.send_keys(Keys.RETURN)

time.sleep(5)

# indo no botão "Pessoas"
botao_pessoa = WebDriverWait(drive, 11).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button'))
)
botao_pessoa.click()

# Esparar um pouco para carregar o resultado "Pessoas"
WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH,'//button[span[text()="Conectar"]]'))
)

time.sleep(5)

# LocaLIZA O botão "Conectar" e clica

botao_conectar = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Conectar"]]'))
)
botao_conectar.click()
print('Botão "Conectar" clicado!')
time.sleep(9)


# Adicionar uma nota
adicionar_nota = WebDriverWait(drive, 20).until(
EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Adicionar nota")]'))
)
adicionar_nota.click()
print('Botão de "Adicionar nota" clicado!')

time.sleep(4)

try:
    #Escrever uma mensagem
    escrever_nota = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    time.sleep(3)
    mensagem = 'Olá! Meu nome é Vitor Emanuel, Gostaria de me conectar a vc!'
    escrever_nota.send_keys(mensagem)
    print('Mensagem Escrita!')
except:
    print('Mensagem não enviada!')
#Enviar a mensagem

