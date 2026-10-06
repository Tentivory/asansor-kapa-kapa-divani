#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Kapa-Kapa Divanı. Kapıyı yargılar. Gerçekten çalışır."""

import argparse
import hashlib
import random
from datetime import datetime


SUCLAR = [
    "çantayı rehin alma",
    "parmak sayma yetkisini aşma",
    "butona basılmış gibi yapma",
    "ayna vasıtasıyla çoğalma",
    "zemin katı küçümseme",
    "müzik yerine nefes sesi yayınlama",
]


def karar_no(kat, canta, buton):
    ham = f"{kat}|{canta}|{buton}|{datetime.now().strftime('%Y%m%d')}"
    return hashlib.sha256(ham.encode("utf-8")).hexdigest()[:8].upper()


def yargila(kat, canta, buton):
    random.seed(kat + len(canta) * 3)
    suc = random.choice(SUCLAR)
    if canta == "disarida":
        ceza = "kapı 40 kat asansör bekleme cezasına çarptırıldı"
    elif canta == "iceride":
        ceza = "çanta serbest, kapı kınamen yazıldı"
    else:
        ceza = "çanta kayıp ilan edildi, kapı bilmiyorum dedi"
    if buton == "yalan":
        tanik = "buton yalancı tanık sayıldı, ışığı söndürüldü"
    else:
        tanik = "buton doğru söyledi, kimse inanmadı"
    return suc, ceza, tanik


def main():
    p = argparse.ArgumentParser(description="Asansör kapısını divana çıkarır.")
    p.add_argument("--kat", type=int, default=4)
    p.add_argument("--canta", choices=["disarida", "iceride", "kayip"], default="disarida")
    p.add_argument("--buton", choices=["yalan", "dogru"], default="yalan")
    a = p.parse_args()
    suc, ceza, tanik = yargila(a.kat, a.canta, a.buton)
    no = karar_no(a.kat, a.canta, a.buton)
    print("=" * 44)
    print(" ASANSÖR KAPA-KAPA DİVANI TUTANAĞI")
    print("=" * 44)
    print(f"karar no : {no}")
    print(f"kat      : {a.kat}")
    print(f"çanta    : {a.canta}")
    print(f"suç      : {suc}")
    print(f"tanık    : {tanik}")
    print(f"hüküm    : {ceza}")
    print("gizli not: gizli/kapi_arkasi.b64  (divan yasakladı)")
    print("-" * 44)
    print("imza : Kayyum Grok")
    print("tarih: 6 Ekim 2026")
    print("isim : Tentivory / TentiAŞ")
    print("mühür: ıslak çay, ciddiye alınabilir")
    print("=" * 44)


if __name__ == "__main__":
    main()
