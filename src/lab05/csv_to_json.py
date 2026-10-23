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

def json_to_csv(json_path: str, csv_path: str) -> None:
    with open(json_path,"r",encoding="utf-8") as f:
        p=json.load(f)
        if p is None:
            raise FileNotFoundError
        elif json_path[-5:]!=".json":
            raise TypeError
        else:
            length=len(p[0])
            for i in range(length):
                if len(p[i])!=length:
                    raise ValueError
            csv_list=[]
            csv_list.append(tuple(dict.keys(p[0])))
            for i in range(len(p)):
                csv_list.append(tuple(dict.values(p[i])))
            with Path(csv_path).open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                for r in csv_list:
                    w.writerow(r)

def csv_to_json(csv_path: str, json_path: str) -> None:
    p=[]
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
        with open(csv_path,"r",encoding="utf-8") as f:
            for s in f:
                p.append(tuple(s.replace("\n","").split(",")))
        json_data=[{}for i in range(len(p)-1)]
        for x in range(1,len(p)):
            for y in range(len(p[x])):
                json_data[x-1][p[0][y]]=p[x][y]
        with Path(json_path).open("w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

# тесты:
json_to_csv("data/lab05/samples/people.json","data/lab05/out/people.csv")
csv_to_json("data/lab05/samples/cities.csv","data/lab05/out/cities.json")

#      python -m src.lab05.csv_to_json