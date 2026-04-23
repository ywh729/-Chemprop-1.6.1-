# -*- coding: utf-8 -*-
import csv

with open("data/data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["smiles", "activity"])
    data = [
        ["O=C=O", 89.2],
        ["C1=CC=CC=C1", 75.8],
        ["CC(=O)O", 83.6],
        ["[Cu]", 92.1],
        ["[Ni]", 81.5],
        ["C1=CC=C(C=C1)O", 94.7],
        ["N#CC1=CC=CC=C1", 86.3],
        ["CN=C=O", 88.1],
    ]
    writer.writerows(data)

with open("data/catalytic_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["smiles", "adsorption_energy", "overpotential", "activity", "selectivity"])
    data = [
        ["O=C=O", -1.34, 0.31, 89.5, 92.7],
        ["[Cu]", -1.12, 0.27, 93.8, 95.2],
        ["[Ni]", -0.96, 0.36, 82.4, 88.1],
        ["[Fe]", -0.88, 0.40, 80.6, 85.3],
        ["C1=CC=CC=C1", -1.29, 0.32, 87.3, 91.5],
        ["CC(=O)O", -1.45, 0.28, 91.7, 94.8],
    ]
    writer.writerows(data)

print("[OK] CSV files generated successfully!")
print("[OK] Generated: data.csv and catalytic_data.csv")