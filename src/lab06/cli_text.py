import argparse
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

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", type=Path, required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        if Path(args.input):
            path=Path(args.input)
            f=read_text(path)
            a=(f.split("\n"))
            if args.n:
                for i in range(len(a)):
                    a[i]=str(i+1)+") "+a[i]
                for i in range(len(a)):
                    print(a[i])
            else:
                for i in range(len(a)):
                    print(a[i])
        else:
            raise FileNotFoundError
    
    elif args.command == "stats":
        if Path(args.input):
            if type(args.top)==int:
                a=read_text(Path(args.input))
                print(top_n(count_freq(tokenize(normalize(a))),args.top))
            else:
                parser.error(...)
        else:
            raise FileNotFoundError
main()
#   python -m src.lab06.cli_text cat --input data/lab05/samples/people.csv -n
#   python -m src.lab06.cli_text stats --input data/lab05/samples/people.csv --top 5