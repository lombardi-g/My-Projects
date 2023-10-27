import openpyxl
from openpyxl import load_workbook
import requests
import re
from datetime import datetime
# import os
# import tkinter as tk
# from tkinter import messagebox
from bs4 import BeautifulSoup

# def defineURL(): #set URL everytime the program runs. use tkinter? verify if main domain is fcf
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
        "COMPETIÇÃO":5,
        "FIGUEIRENSE":6,
        "G.F.":7,
        "G.A.":8,
        "ADVERSÁRIO":9,
        "MANDO":10,
        "LOCAL":11,
        "Cidade":12,
        "UF":13,
        "JOGOS":14,
        "VITÓRIA":15,
        "EMPATE":16,
        "DERROTA":17,
        "MINUTOS JOGADOS":18,
        "1º A MARCAR FIGUEIRENSE":19,
        "1º A MARCAR ADVERSÁRIO":20,
        "GOLS MARCADOS 1ºT - 0'-15'":21,
        "GOLS MARCADOS 1ºT - 15'-30'":22,
        "GOLS MARCADOS 1ºT - 30'-45'":23,
        "GOLS MARCADOS 2ºT - 0'-15'":24,
        "GOLS MARCADOS 2ºT - 15'-30'":25,
        "GOLS MARCADOS 2ºT - 30'-45'":26,
        "GOLS SOFRIDOS 1ºT - 0'-15'":27,
        "GOLS SOFRIDOS 1ºT - 15'-30'":28,
        "GOLS SOFRIDOS 1ºT - 30'-45'":29,
        "GOLS SOFRIDOS 2ºT - 0'-15'":30,
        "GOLS SOFRIDOS 2ºT - 15'-30'":31,
        "GOLS SOFRIDOS 2ºT - 30'-45'":32
    }
    staff = {
        "Sub14":"Guilherme Pereira",
        "Sub15":"Guilherme Pereira",
        "Sub17":"Lucas Ligio",
        "Sub20":"Jhonatas Reis",
        "Sub21":"Jhonatas Reis"
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
    sheet.cell(row=new_row, column=column_labels['DATA JOGO'],value=date)
    sheet.cell(row=new_row, column=column_labels['TREINADOR'],value=staff[category])
    sheet.cell(row=new_row, column=column_labels['CATEGORIA'],value=category)
    sheet.cell(row=new_row, column=column_labels['COMPETIÇÃO'],value=tournament)
    sheet.cell(row=new_row, column=column_labels['FIGUEIRENSE'],value="Figueirense")
    sheet.cell(row=new_row, column=column_labels['G.F.'],value=figueira_final_score)
    sheet.cell(row=new_row, column=column_labels['G.A.'],value=opponent_final_score)
    sheet.cell(row=new_row, column=column_labels['ADVERSÁRIO'],value=opponent)
    sheet.cell(row=new_row, column=column_labels['MANDO'],value=home)
    sheet.cell(row=new_row, column=column_labels['LOCAL'],value=place)
    sheet.cell(row=new_row, column=column_labels['Cidade'],value=city)
    sheet.cell(row=new_row, column=column_labels['UF'],value="SC")
    sheet.cell(row=new_row, column=column_labels['JOGOS'],value=1)
    sheet.cell(row=new_row, column=column_labels['VITÓRIA'],value=1 if figueira_final_score > opponent_final_score else 0)
    sheet.cell(row=new_row, column=column_labels['EMPATE'],value=1 if figueira_final_score == opponent_final_score else 0)
    sheet.cell(row=new_row, column=column_labels['DERROTA'],value=1 if figueira_final_score < opponent_final_score else 0)
    sheet.cell(row=new_row, column=column_labels['MINUTOS JOGADOS'],value = int(first_half_minutes) + int(second_half_minutes))
    sheet.cell(row=new_row, column=column_labels['1º A MARCAR FIGUEIRENSE'],value=1 if figueira_first else 0)
    sheet.cell(row=new_row, column=column_labels['1º A MARCAR ADVERSÁRIO'],value=1 if figueira_first else 0)

    workbook.save("Banco de Dados Figueirense Base.xlsx")

url = 'https://egol.fcf.com.br/SISGOL/WDER0700_Sumula.asp?SelStart1=2023&SelStop1=2023&SelStart2=557&SelStop2=557&SelStart3=70&SelStop3=70&Index=1&RunReport=Run+Report'
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
    home = "Casa"
    figueira_final_score = int(final_score[0])
    opponent_final_score = int(final_score[1])
else:
    home = "Fora"
    figueira_final_score = int(final_score[1])
    opponent_final_score = int(final_score[0])


# Find category
full_tournament = targetURL.find(string=caps_lock_ignore('sub-'))
category = "Sub"+full_tournament[full_tournament.upper().find("SUB-")+4:full_tournament.upper().find("SUB-")+6]
tournament = "Campeonato Catarinense"

# Which round
round_number = full_tournament.find_next(string='Rodada:').find_next()
round_number = round_number.get_text()

# Find date
date_locator = targetURL.find(string="Data:")
date = date_locator.find_next(string=caps_lock_ignore('/202'))
time_locator = date.find_next(string='Horário:')
time = time_locator.find_next().get_text()

# Find place
place_locator = time_locator.find_next(string="Local:").find_next()
place = place_locator.get_text().split(' / ')
city = place[1]
place = place[0]

# Find minutes played
def minute_calculator(start: str, end: str, added: str):
    format = '%H:%M'
    match_start = datetime.strptime(start,format)
    match_end = datetime.strptime(end,format)
    added_time = datetime.strptime(added,format)
    return match_end - match_start + added_time
    
first_half_locator = targetURL.find(name="td",string="Início 1° Tempo:").find_next()
first_half_started = first_half_locator.get_text()
first_half_finished = targetURL.find(name="td",string="Término do 1º Tempo:").find_next()
first_half_added_time = first_half_finished.find_next(name="td",string="Acréscimo:").find_next().get_text()
first_half_finished = first_half_finished.get_text()
first_half_minutes = datetime.strftime(minute_calculator(first_half_started, first_half_finished, first_half_added_time),'%M')
second_half_locator = targetURL.find(name="td",string="Início 2° Tempo:").find_next()
second_half_started = second_half_locator.get_text()
second_half_finished = targetURL.find(name="td", string="Término do 2º Tempo:").find_next()
second_half_added_time = second_half_finished.find_next(name="td",string="Acréscimo:").find_next().find_next().get_text()
second_half_finished = second_half_finished.get_text()
second_half_minutes = datetime.strftime(minute_calculator(second_half_started,second_half_finished, second_half_added_time),'%M')

#Scoring information
score_locator_beginning = targetURL.find(string=caps_lock_ignore("5.0 - GOLS"))
score_locator_end = targetURL.find(name="td",string=caps_lock_ignore("6.0 - "))
goal_reader = score_locator_beginning.findNext(name="td",string="Equipe")
goal_minute_locator = goal_reader
goals_info=[]
total_goals=0
if figueira_final_score or opponent_final_score != 0:
    while goal_minute_locator is not score_locator_end:
        goal_minute_locator = goal_reader.find_next(name="td")
        goal_minute = goal_minute_locator.get_text()
        goal_half_locator = goal_minute_locator.find_next(name="td")
        goal_half = goal_half_locator.get_text()
        goal_team_locator = goal_half_locator.find_next(name="td").find_next(name="td").find_next(name="td").find_next(name="td")
        goal_team = goal_team_locator.get_text().capitalize()
        if total_goals==0:
            figueira_first = True if goal_team == "Figueirense" else False
        goal_info = {
            "minute":goal_minute,
            "half":goal_half,
            "team":goal_team
        }
        goals_info.append(goal_info)
        total_goals+=1
        goal_reader = goal_team_locator
        goal_minute_locator = goal_reader.find_next(name="td")
else:
    figueira_first=False

pass_to_excel()