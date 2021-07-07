from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange

# DECLARAÇÃO DE VARIÁVEIS
WPP_URL = 'https://web.whatsapp.com/'
NEW_CHAT_XPATH = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
SEARCH_CONTACT_XPATH = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
FIRST_CONTACT_XPATH = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div'
TYPE_FIELD_XPATH = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
SEND_MSG_XPATH = '//*[@id="main"]/footer/div[1]/div[3]/button/span'

# ABRO O CHROME
driver = webdriver.Chrome(ChromeDriverManager().install())
# abro o whatsapp
driver.get(WPP_URL)

# ENCONTRO O CAMPO DE NOVO CHAT
new_msg_button = driver.find_element_by_xpath(NEW_CHAT_XPATH)
# clico nele
new_msg_button.click()
sleep(1)

search_field = driver.find_element_by_xpath(SEARCH_CONTACT_XPATH)
search_field.click()
search_field.send_keys('Robô do zapzap')
sleep(1)

first_contact = driver.find_element_by_xpath(FIRST_CONTACT_XPATH)
first_contact.click()
sleep(1)


def send_message(message):

    type_field = driver.find_element_by_xpath(TYPE_FIELD_XPATH)
    type_field.click()
    type_field.send_keys(message)
    sleep(1)

    send_msg = driver.find_element_by_xpath(SEND_MSG_XPATH)
    send_msg.click()
    

send_message('coé rapaziada')

#array
lista_de_mensagens = ["Lukinha", "Você é um amigo incrível.", "Você é um presente para aqueles ao seu redor.", "Você é inteligente.", "Você é demais!", "Você tem maneiras impecáveis.", "Eu gosto do seu estilo.", "Você tem a melhor risada.", "Eu gosto de você.", "Você é o mais perfeito que existe.", "Você é o suficiente.", "Você é forte.", "Sua perspectiva é impecável.", "Sou grato por conhecê-lo.", "Você ilumina a sala.", "Você merece um abraço agora.", "Você deve se orgulhar de si mesmo.", "Você é mais útil do que imagina.", "Você tem um ótimo senso de humor.", "Você tem um incrível senso de humor!", "Você é realmente corajoso.", "Sua bondade é um bálsamo para todos que a encontram.", "Em uma escala de 1 a 10, você é um 11.", "Você é forte.", "Você é ainda mais bonito por dentro do que por fora.", "Você tem a coragem de suas convicções.", "Eu sou inspirado por você.", "Você é como um raio de sol em um dia realmente triste.", "Você está fazendo a diferença.", "Obrigado por estar lá para mim.", "Você traz o melhor para as outras pessoas.",
                      "Você é realmente gentil com as pessoas ao seu redor.", "Você é único!", "Sua capacidade de recordar fatos aleatórios no momento certo é impressionante.", "Você é um ótimo ouvinte.", "Tudo seria melhor se mais pessoas fossem como você!", "Eu aposto que você suou glitter.", "Você era legal antes dos descolados serem legais.", "Essa cor é perfeita para você.", "Sair com você é sempre uma emoção.", "Você sempre sabe – e diz – exatamente o que preciso ouvir quando preciso ouvir.", "Você me ajuda a sentir mais alegria na vida.", "Você pode dançar como ninguém, mas todo mundo está assistindo porque você é um dançarino incrível!", "Estar perto de você torna tudo melhor!", "Quando você diz: “Eu pretendia fazer isso”, acredito totalmente em você.", "Quando você não tem medo de ser você mesmo, é o mais incrível.", "As cores parecem mais brilhantes quando você está por perto.", "O que você não gosta em si mesmo é o que o torna tão interessante.", "Você é maravilhoso.", "Você tem cotovelos fofos.", "Piadas são mais engraçadas quando você conta."]

lista_de_comida = ["Arroz", "Feijao", "mandioca" ,"peixe", "carne", "ovo"]

len(lista_de_mensagens) #saber o tamanho do seu array

for loop in range(100):
    send_message(f"{lista_de_comida[randrange(0,4)]}")















