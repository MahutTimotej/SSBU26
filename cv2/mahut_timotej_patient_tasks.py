import csv
import os
import pandas as pd
from PIL import Image

"1. úloha"
ages = [14, 29, 68, 38, 1]

def putInCategory(ages):
    dictAges = {
        "minor": 0,
        "adult": 0,
        "senior": 0
    }

    for a in ages:
        if a < 18:
            dictAges["minor"] += 1
        elif a < 65:
            dictAges["adult"] += 1
        else:
            dictAges["senior"] += 1

    return dictAges

print(putInCategory(ages))


"2. úloha"
os.makedirs("data", exist_ok=True)

patients = [
    ("Peter Novak", "zapalmozgovychblan"),
    ("Matus Mahut", "chripka"),
    ("Jan Hrach", "cukrovka"),
    ("Lucia Kralova", "chripka"),
    ("Adam Pol", "cukrovka"),
    ("Nina Tothova", "angina"),
    ("Tomas Sabo", "chripka"),
    ("Eva Hlinkova", "alergia"),
    ("Filip Urban", "chripka"),
    ("Sandra Kovacova", "cukrovka"),
    ("Jozef Blaha", "alergia"),
    ("Veronika Kmetova", "angina"),
    ("Martin Sykora", "chripka"),
    ("Dominika Benkova", "angina"),
    ("Karol Niznansky", "cukrovka"),
    ("Zuzana Fialova", "chripka"),
    ("Roman Kubo", "alergia"),
    ("Ivana Hruskova", "chripka"),
    ("Marek Varga", "angina"),
    ("Beata Maly", "chripka"),
]

"3. uloha"
path = "data/patients.csv"

with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["name", "diagnosis"])
    w.writerows(patients)

df = pd.read_csv(path)
df["ID"] = range(0, 20)

print(df["diagnosis"].tolist())
print(df["diagnosis"].value_counts())

"4. uloha"
img_path = "data/microscope_g.jpg"
if os.path.exists(img_path):
    img = Image.open(img_path)
    cropped = img.crop((300, 550, 1000, 1250))
    zoomed = cropped.resize((int(cropped.width * 1.5), int(cropped.height * 1.5)))
    zoomed.show()

"5. uloha"
class PatientData:
    def __init__(patientDF, csv_file="data/patients.csv"):
        patientDF.df = pd.read_csv(csv_file)

    def count_diagnoses(patientDF):
        return patientDF.df["diagnosis"].value_counts()

    def get_most_common_diagnosis(patientDF, n):
        return patientDF.df["diagnosis"].value_counts().head(n)

    def display_summary(patientDF):
        print("rows:", len(patientDF.df))
        print(patientDF.count_diagnoses())
        print(patientDF.df.head())

p = PatientData(path)
print(p.count_diagnoses())
print(p.get_most_common_diagnosis(1))
print(p.display_summary())
