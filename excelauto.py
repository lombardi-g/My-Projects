from datetime import datetime
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from yahoo_fin import stock_info as si
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'priceimports.xlsx'

workbook = Workbook()
worksheet: Worksheet = workbook.active

worksheet.cell (1, 1, 'Ação')
worksheet.cell (1, 2, 'Data')
worksheet.cell (1, 3, 'Valor')

now = datetime.now()
date = f'{now.day}/{now.month}/{now.year}'

stocks=[
    ['BRCR11',date,si.get_live_price('BRCR11.SA')],
    ['HGCR11',date,si.get_live_price('HGCR11.SA')],
    ['KNCR11',date,si.get_live_price('KNCR11.SA')],
    ['MXRF11',date,si.get_live_price('MXRF11.SA')],
    ['CSAN3',date,si.get_live_price('CSAN3.SA')],
    ['WEGE3',date,si.get_live_price('WEGE3.SA')],
    ['COGN3',date,si.get_live_price('COGN3.SA')],
    ['CVCB3',date,si.get_live_price('CVCB3.SA')],
    ['BBAS3',date,si.get_live_price('BBAS3.SA')],
    ['ITUB4',date,si.get_live_price('ITUB4.SA')],
    ['ITSA4',date,si.get_live_price('ITSA4.SA')],
    ['IVVB11',date,si.get_live_price('IVVB11.SA')],
    ['BTAL11',date,si.get_live_price('BTAL11.SA')],
    ['BBPO11',date,si.get_live_price('BBPO11.SA')],
    ['GMAT3',date,si.get_live_price('GMAT3.SA')],
    ['MRVE3',date,si.get_live_price('MRVE3.SA')],
    ['RDOR3F',date,si.get_live_price('RDOR3F.SA')]
]

def export_to_sheet():
    for stock in stocks:
        worksheet.append(stock)
    workbook.save(WORKBOOK_PATH)

export_to_sheet()
