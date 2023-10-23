import openpyxl
from openpyxl import load_workbook
import requests
import re
# import datetime
# import os
# import tkinter as tk
# from tkinter import messagebox
from bs4 import BeautifulSoup

# def defineURL(): #set URL everytime the program runs. use tkinter?
#     entry = tk.Entry()
#     site = entry.get()

def caps_lock_ignore(text):
    return re.compile(text,re.I)
                      
def pass_to_excel():
    workbook = load_workbook("Banco de Dados Figueirense Base.xlsx")
    sheet = workbook['Jogos']
    # Assigned labels from sheet. Read them and dynamically make the dict?
    column_labels = {
        "CÓDIGO JOGO":1,
        "DATA JOGO":2,
        "TREINADOR":3,
        "CATEGORIA":4,
        "COMPETIÇÃO":6,
        "FIGUEIRENSE":7,
        "G.F.":8,
        "G.A.":9,
        "ADVERSÁRIO":10,
        "MANDO":11,
        "LOCAL":12,
        "Cidade":13,
        "UF":14,
        "JOGOS":15,
        "VITÓRIA":16,
        "EMPATE":17,
        "DERROTA":18,
        "MINUTOS JOGADOS":19,
        "1º A MARCAR FIGUEIRENSE":20,
        "1º A MARCAR ADVERSÁRIO":21,
        "GOLS MARCADOS 1ºT - 0'-15'":22,
        "GOLS MARCADOS 1ºT - 15'-30'":23,
        "GOLS MARCADOS 1ºT - 30'-45'":24,
        "GOLS MARCADOS 2ºT - 0'-15'":25,
        "GOLS MARCADOS 2ºT - 15'-30'":26,
        "GOLS MARCADOS 2ºT - 30'-45'":27,
        "GOLS SOFRIDOS 1ºT - 0'-15'":28,
        "GOLS SOFRIDOS 1ºT - 15'-30'":29,
        "GOLS SOFRIDOS 1ºT - 30'-45'":30,
        "GOLS SOFRIDOS 2ºT - 0'-15'":31,
        "GOLS SOFRIDOS 2ºT - 15'-30'":32,
        "GOLS SOFRIDOS 2ºT - 30'-45'":33
    }
    last_row = sheet.max_row
    last_row_value = 2
    while last_row > 1:
        last_row_value = sheet.cell(row=last_row,column=1).value
        if last_row_value is not None:
            break
        last_row -= 1
        
    last_row_value = sheet.cell(row=last_row, column=column_labels['CÓDIGO JOGO']).value
    print(last_row)
    print(last_row_value)
    new_row = last_row + 1
    sheet.cell(row=new_row, column=column_labels['CÓDIGO JOGO'],value=last_row_value+1)

    workbook.save("Banco de Dados Figueirense Base.xlsx")

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
category = "Sub"+full_tournament[full_tournament.upper().find("SUB-")+4:full_tournament.upper().find("SUB-")+6]

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
# print (BeautifulSoup().PREFERRED_PARSER)
# print (openpyxl.__version__)
print(opponent)
print(full_tournament)
print(figueira_final_score)
print(opponent_final_score)
print(round_number)
print(category)
print(date)
print(time)
print(place)
pass_to_excel()