# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:28:46 2021

@author: mauri
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.uol.com.br/")

submanc = driver.find_elements_by_class_name("submanchete")

sub_manchetes = []
for sub in submanc:
    sub_manchetes.append(sub.text)
#    print(sub.text)
    
sub_manchetes

# outra forma de fazer o loop e guardar na lista.
sub_manchetes_2 = [sub.text for sub in submanc]

sub_manchetes_2

submanc[4].text
