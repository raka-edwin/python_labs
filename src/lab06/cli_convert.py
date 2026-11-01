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
from src.lab05.csv_to_json import json_to_csv,csv_to_json
from src.lab05.csv_to_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать json в csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Конвертировать csv в json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать csv в xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        if args.input and args.output:
            json_to_csv(args.input,args.output)
        else:
            raise FileNotFoundError

    if args.cmd == "csv2json":
        if args.input and args.output:
            csv_to_json(args.input,args.output)
        else:
            raise FileNotFoundError

    if args.cmd == "csv2xlsx":
        if args.input and args.output:
            csv_to_xlsx(args.input,args.output)
        else:
            raise FileNotFoundError
main()
#   python -m src.lab06.cli_convert json2csv --in data/lab05/samples/people.json --out data/lab05/out/people.csv
#   python -m src.lab06.cli_convert csv2json --in data/lab05/samples/cities.csv --out data/lab05/out/cities.json
#   python -m src.lab06.cli_convert csv2xlsx --in data/lab05/samples/cities.csv --out data/lab05/out/cities.xlsx