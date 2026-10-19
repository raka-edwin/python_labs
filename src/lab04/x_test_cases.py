from collections import Counter
from pathlib import Path
import csv
from src.lab04.io_txt_csv import read_text,write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n,alf_ord,flatten
import math
from typing import Iterable, Sequence
from src.lab03.test_case_text import top_n_table
from src.lab04.text_report import frequencies_from_text,ready_text,sorted_word_counts,write_multiple_csvs

print("Задание A:")
print("read_text:")
print(read_text("data/lab04/input.txt"))
print(" ")
print("таблица к функции write_csv:")
write_csv(ready_text("data/lab04/input.txt"),"data/lab04/check.csv",("word","count"))
top_n_table(read_text("data/lab04/input.txt"),1)   # Этот модуль взят из Л3, он делает ровную таблицу в выводе
# Если второй аргумент этой функции равен 1 - таблица включена, если 0 - таблица выключена

print(" ")
print("Задание B - пустой файл empty.txt -> empty.csv (заголовок я добавил вручную, но это необязательно)")
write_csv(ready_text("data/lab04/empty.txt"),"data/lab04/empty.csv",("word","count"))

write_csv([(read_text("data/lab04/input1.txt")).encode("cp1251")],"data/lab04/encoding.csv",("word","count"))

files_in=["data/lab04/a.txt","data/lab04/b.txt"]
files_out=["data/lab04/report_per_file.cvs","data/lab04/report_total.cvs"]
write_multiple_csvs(datasets=files_in, paths=files_out, headers=("word","count"))

#       python -m src.lab04.x_test_cases