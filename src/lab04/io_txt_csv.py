from pathlib import Path
from src.lab03.test_case_text import top_n_table
from src.lib.text import normalize,tokenize,count_freq,top_n,alf_ord,flatten

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def ready_text(path: str | Path, encoding: str = "utf-8"):
    p=Path(path)
    k=p.read_text(encoding=encoding)
    b=top_n(count_freq(tokenize(normalize(k))),5)
    return list(b)

import csv
from typing import Iterable, Sequence

def write_csv(rows: list[tuple | list | str], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    rows1=[]
    if rows:
        if type(rows[0])==bytes:
                rows1=(top_n(count_freq(tokenize(normalize(rows[0].decode("cp1251")))),5))
                p = Path(path)
                with p.open("w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if header is not None:
                        w.writerow(header)
                    for r in rows1:
                        w.writerow(r)
        else:
            length=len(rows[0])
            for r in rows:
                if len(r)!=length:
                    raise ValueError
                if header is not None and len(header)!=length:
                    raise ValueError
                elif header is not None:
                    length=len(header)
                p=Path(path)
                with p.open("w", newline="", encoding="utf-8") as f:
                        w = csv.writer(f)
                        if header is not None:
                            w.writerow(header)
                        for r in rows:
                            w.writerow(r)
    else:
        length=None
        p = Path(path)
        rows = list(rows)
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if header is not None:
                w.writerow(header)
            for r in rows:
                w.writerow(r)

#     python -m src.lab04.io_txt_csv