import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Import data dari CSV
data = pd.read_excel('dataset_nonlabel_test.xlsx')

# Standarisasi nilai penghasilan
scaler = StandardScaler()
data['penghasilan'] = scaler.fit_transform(data[['penghasilan']])

X = data[['penghasilan', 'tanggungan', 'kondisi_rumah', 'status_rumah']]
y = data['jenis']

# # Seleksi fitur terbaik
selector = SelectKBest(f_classif, k='all')
X_selected = selector.fit_transform(X, y)

# Membagi data menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Membuat model Gaussian Naive Bayes
model = GaussianNB()

# Melatih model
model.fit(X_train, y_train)

# Memprediksi data pengujian
y_pred = model.predict(X_test)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi: {accuracy * 100:.2f}%")

# Menampilkan laporan klasifikasi
print("Laporan Klasifikasi:\n", classification_report(y_test, y_pred))

# Menampilkan matriks kebingungan
print("Matriks Kebingungan:\n", confusion_matrix(y_test, y_pred))

# Cross-Validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean Cross-Validation Score: {np.mean(cv_scores) * 100:.2f}%")