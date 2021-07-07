from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange
import io
from time import sleep



#URL = 'https://www.projetoagathaedu.com.br/questoes-enem/matematica/aritmetica-1.php'
URL = 'https://www.projetoagathaedu.com.br/questoes-enem/matematica/aritmetica-2.php'

SUBJECT_LEVEL_1_XPATH = '/html/body/div[2]/h3[1]/a[3]'
SUBJECT_LEVEL_2_XPATH = '/html/body/main/article/div[1]/h1'

correct_answers = []
question_texts = []
question_options = []

driver = webdriver.Chrome(ChromeDriverManager().install())

f_links = open("SubjectLinks.txt", "r")
for URL in f_links:


    
    driver.get(URL)
    
    subject_level_1 = driver.find_element_by_xpath(SUBJECT_LEVEL_1_XPATH).text
    subject_level_2 = driver.find_element_by_xpath(SUBJECT_LEVEL_2_XPATH).text
    
    
    ## Get Correct Answer
    sleep(2)
    gabarito_buttton = driver.find_element_by_xpath('/html/body/main/article/div[1]/button')
    gabarito_buttton.click()
    sleep(0.5)
    
    answers = []
    correct_answers = []
    
    correct_answer_table = driver.find_elements_by_id('tabela-respostas')
    answers = correct_answer_table[1].find_element_by_tag_name('tbody').text.replace('\n', ' ')
    print(answers)
    
    for answer in answers.split():
        correct_answers.append(answer.split('.')[1])
        
    print(correct_answers)
    
    questions = driver.find_elements_by_class_name('questoes-enem-vestibular')
    
    correct_answers_index = 0
    f = open("enem_questions.csv", "a", encoding="utf-8")
    
    for question in questions:
        image = question.find_elements_by_tag_name("img")
        
        
        question_html = question.get_attribute('innerHTML')
        #print(question_html.lstrip().replace("</p><img","</p>\n<img"))
        #print(question_html.lstrip().replace("<img","\n<img").splitlines())
        
        #####################
        ## Get Question Text
        #####################
        i = 0
        question_texts = []
        for line in question_html.lstrip().replace("</p><img","</p>\n<img").splitlines():
            if line.find("<ol type=\"A\">") != -1 \
            or line.find("<li>") != -1 \
            or line.find("</ol>") != -1\
            or line.find("<p class=") != -1 \
            : #change images
                continue
            elif line.find("<img class=") != -1: #change images
                question_texts.append(f"<img src=\"{image[i].get_attribute('src')}\">")
                i += 1
            elif line.find("<button class=") != -1: #change buttons
                continue
            elif line == '':
                continue
            else:
                question_texts.append(line.lstrip())
    
    
        #####################
        ## Get options
        #####################
        question_options_element = question.find_element_by_tag_name("ol")
        question_options_html = question_options_element.get_attribute('innerHTML')
        question_options = []
        for options in question_options_html.splitlines():
            if options.find("<img class=") != -1: #change images
                question_options.append(f"<img src=\"{image[i].get_attribute('src')}\">")
                i += 1
            elif options == '':
                continue
            else:
                question_options.append(options.lstrip().replace("<li>","").replace("</li>",""))
                
        #####################
        ## Print Final File
        #####################
        question_text = ''.join(question_texts)
        question_year = ''.join(filter(lambda i: i.isdigit(), question_text.split('(')[1].split(')')[0]))
        print(question_texts)
        print(question_text)
        
        final = []
        final.append(subject_level_1)
        final.append(subject_level_2)
        final.append(question_year)
        final.append(question_text)
        final.append(correct_answers[correct_answers_index])
        
        #print(final)
        
        f.write('|'.join(final))
        f.write("\n")
        
        correct_answers_index += 1
        
    f.close()
    
    print("fim")

f_links.close()













