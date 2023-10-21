import openpyxl
import requests
import re
import datetime
# import os
# import tkinter as tk
# from tkinter import messagebox
from bs4 import BeautifulSoup

# def defineURL(): #set URL everytime the program runs. use tkinter?
#     entry = tk.Entry()
#     site = entry.get()

def caps_lock_ignore(text):
    return re.compile(text,re.I)

url = 'https://egol.fcf.com.br/SISGOL/WDER0700_Sumula.asp?SelStart1=2023&SelStop1=2023&SelStart2=557&SelStop2=557&SelStart3=16&SelStop3=16&Index=1&RunReport=Run+Report'
response = requests.get(url)
targetURL = BeautifulSoup(response.text, 'html.parser')

# Determine opponent
match = targetURL.find(string=caps_lock_ignore('figueirense'))
teams = match.split(' x ')
opponent = [team for team in teams if team.upper() != 'FIGUEIRENSE'][0]

# Final score
final_score = match.find_next('p').find_next()
final_score = final_score.get_text().split(' x ')
if teams[0] == "FIGUEIRENSE":
    figueira_final_score = final_score[0]
    opponent_final_score = final_score[1]
else:
    figueira_final_score = final_score[1]
    opponent_final_score = final_score[0]


# Find category
full_tournament = targetURL.find(string=caps_lock_ignore('sub-'))
category = "SUB-"+full_tournament[full_tournament.upper().find("SUB-")+4:full_tournament.upper().find("SUB-")+6]

# Which round
round_number = full_tournament.find_next(string='Rodada:').find_next()
round_number = round_number.get_text()

# Find date
date_locator = targetURL.find(string="Data:")
date = date_locator.find_next(string=caps_lock_ignore('/202'))
time_locator = date.find_next(string='Horário:')
time = time_locator.find_next().get_text()

# Find local
place_locator = time_locator.find_next(string="Local:").find_next()
place = place_locator.get_text()

# tests
print (BeautifulSoup().PREFERRED_PARSER)
print (openpyxl.__version__)
print(opponent)
print(full_tournament)
print(figueira_final_score)
print(opponent_final_score)
print(round_number)
print(category)

print(date)
print(time)
print(place)