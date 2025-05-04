import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Örnek veri seti yükleme (kendi dosya yolunuza göre değiştirin)
df = pd.read_csv("patient-feedback.csv")

# Varsayalım ki iki sayısal sütun var: 'ComplaintCount' ve 'ResolutionTime'
x = df['ComplaintCount']
y = df['ResolutionTime']

# Log-log grafik çizimi
plt.figure(figsize=(8,6))
plt.loglog(x, y, 'o', markersize=5)
plt.xlabel('Log(Complaint Count)')
plt.ylabel('Log(Resolution Time)')
plt.title('Log-Log Graph of Complaint Count vs Resolution Time')
plt.grid(True, which="both", ls="--")

