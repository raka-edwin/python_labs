from collections import Counter
from pathlib import Path
import csv
from src.lab04.io_txt_csv import read_text,write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n,alf_ord,flatten
import math
from typing import Iterable, Sequence
from src.lab03.test_case_text import top_n_table

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def ready_text(path: str | Path, encoding: str = "utf-8"):
    p=Path(path)
    if len(read_text(p))==0:
         return []
    else:
        k=p.read_text(encoding=encoding)
        b=top_n(count_freq(tokenize(normalize(k))),5)
        return list(b)

def write_multiple_csvs(datasets: Iterable[Iterable[Sequence]],paths: Iterable[str | Path],\
                        headers: Iterable[tuple[str, ...]] | tuple[str, ...] | None = None) -> None:
    data=[]
    for i in range(len(datasets)):
        data.append(ready_text(datasets[i]))
    file_name=["" for i in range(len(datasets))]
    for x in range(len(datasets)):
        for y in range(len(datasets[x])):
            if datasets[x][-1-y]!="/":
                file_name[x]+=datasets[x][-1-y]
            else:
                break
    for i in range(len(file_name)):
        file_name[i]=file_name[i][::-1]
    p=[]
    for i in range(len(paths)):
        p.append(Path(paths[i]))
    with p[0].open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if headers is not None:
                list(headers).insert(0,"file")
                w.writerow(headers)
            for i in range(len(data)):
                for r in data[i]:
                    w.writerow((file_name[i],r[0],r[1]))
    with p[1].open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                all_data=flatten(data)
                all_data_sort=[]
                for x in range(len(all_data)):
                    for y in range(all_data[x][1]):
                        all_data_sort.append(all_data[x][0])
                all_data_sort=top_n(count_freq(all_data_sort),5)
                if headers is not None:
                    w.writerow(headers)
                for i in range(len(all_data_sort)):
                    w.writerow((all_data_sort[i][0],all_data_sort[i][1]))

#     python -m src.lab04.text_report 