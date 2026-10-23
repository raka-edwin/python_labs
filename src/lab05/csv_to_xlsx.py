from collections import Counter
from pathlib import Path
from openpyxl import Workbook
import csv
import json
from src.lab04.io_txt_csv import read_text,write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n,alf_ord,flatten
import math
from typing import Iterable, Sequence
from src.lab03.test_case_text import top_n_table
from src.lab04.text_report import frequencies_from_text,ready_text,sorted_word_counts,write_multiple_csvs

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    with open(csv_path,"r", encoding="utf-8") as f:
        r=csv.reader(f)
        if r is None:
            raise FileNotFoundError
        elif csv_path[-4:]!=".csv":
            raise TypeError
        else:
            length=[]
            for row in r:
                length.append(len(row))
            if len(set(length))>1:
                raise ValueError   
        max_len=0
        row_len=0
        with open(csv_path,"r", encoding="utf-8") as f:
            r=csv.reader(f)
            for row in r:
                ws.append(row)
                for i in range(len(row)):
                    row_len=len(row[i])
                    if max_len<len(row[i]):
                        max_len=len(row[i])
        alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(row_len):
            ws.column_dimensions[alf[i]].width=max_len+2
    wb.save(xlsx_path)

csv_to_xlsx("data/lab05/samples/cities.csv","data/lab05/out/cities.xlsx")
#   python -m src.lab05.csv_to_xlsx