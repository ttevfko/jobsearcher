# parser/cv_analyzer.py

import re

def extract_location(text):
    şehirler = ["İstanbul", "Ankara", "İzmir", "Bursa", "Kocaeli", "Antalya", "Konya", "Gaziantep", "Adana", "Kayseri"]
    for şehir in şehirler:
        if şehir.lower() in text.lower():
            return şehir
    return None

def extract_jobs(text):
    meslekler = ["CNC", "CAD-CAM", "Freze", "Torna", "Operatör", "Programcı", "Kalıpçı", "Zerspanung", "CAM", "Abteilungsleiter"]
    bulunan = []
    for kelime in meslekler:
        if kelime.lower() in text.lower():
            bulunan.append(kelime)
    return list(set(bulunan))

def extract_name(text):
    match = re.search(r"(?i)(tevfik\s+tiryaki)", text)
    return match.group(1) if match else None

def analyze_cv(text):
    return {
        "name": extract_name(text),
        "location": extract_location(text),
        "keywords": extract_jobs(text)
    }
