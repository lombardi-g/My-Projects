import openpyxl
import requests
import re
# import os
# import tkinter as tk
# from tkinter import messagebox
from bs4 import BeautifulSoup

# def defineURL(): #set URL everytime the program runs. use tkinter?
#     entry = tk.Entry()
#     site = entry.get()

def caps_lock_ignore(text):
    return re.compile(text,re.I)

url = 'https://egol.fcf.com.br/SISGOL/WDER0700_Sumula.asp?SelStart1=2023&SelStop1=2023&SelStart2=556&SelStop2=556&SelStart3=4&SelStop3=4&Index=1&RunReport=Run+Report'
response = requests.get(url)
targetURL = BeautifulSoup(response.text, 'html.parser')

# Determine opponent
match = targetURL.find(string=caps_lock_ignore('figueirense'))
teams = match.split(' x ')
opponent = [team for team in teams if team.upper() != 'FIGUEIRENSE'][0]

# Find category
full_tournament = targetURL.find(string=caps_lock_ignore('sub-'))
category = "SUB-"+full_tournament[full_tournament.upper().find("SUB-")+4:full_tournament.upper().find("SUB-")+6]

# tests
print (BeautifulSoup().PREFERRED_PARSER)
print (openpyxl.__version__)
print(opponent)
print(full_tournament)
print(category)