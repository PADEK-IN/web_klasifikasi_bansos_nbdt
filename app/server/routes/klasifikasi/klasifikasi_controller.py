# import os
from flask import request
from app.server import db
from app.server.model.warga import Warga
from app.server.helper.formating import dataWarga

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def predict(nik):
    try:
        warga = Warga.query.filter_by(nik=nik).first()
        wargaData = dataWarga(warga)
        penghasilan = wargaData["penghasilan"]
        tanggungan = wargaData["tanggungan"]
        materialRumah = wargaData["kondisi_rumah"]
        statusRumah = wargaData["status_rumah"]
        
        
        if materialRumah == "bambu anyam":
            materialRumah = 1
        if materialRumah == "papan":
            materialRumah = 2
        if materialRumah == "batu semen":
            materialRumah = 3
        if materialRumah == "batu permanen":
            materialRumah = 4
        
        if statusRumah == "sewa":
            statusRumah = 1
        if statusRumah == "milik sendiri":
            statusRumah = 2
        
        # Train model
        data = pd.read_excel('dataset_nonlabel_test.xlsx')
        scaler = StandardScaler()
        data['penghasilan'] = scaler.fit_transform(data[['penghasilan']])
        X = data[['penghasilan', 'tanggungan', 'kondisi_rumah', 'status_rumah']]
        y = data['jenis']
        selector = SelectKBest(f_classif, k='all')
        X_selected = selector.fit_transform(X, y)
        X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
        model = GaussianNB()
        model.fit(X_train, y_train)
        
        #data Baru
        new_data = np.array([[penghasilan, tanggungan, materialRumah, statusRumah]])
        # Membuat DataFrame
        df = pd.DataFrame(new_data, columns=['penghasilan', 'tanggungan', 'kondisi_rumah', 'status_rumah'])
        # Standarisasi nilai penghasilan
        df['penghasilan'] = df['penghasilan'].astype(int)
        scaler = StandardScaler()
        df['penghasilan'] = scaler.fit_transform(df[['penghasilan']])
        Z = df[['penghasilan', 'tanggungan', 'kondisi_rumah', 'status_rumah']]
        # Memprediksi kelas untuk data baru
        print(Z["penghasilan"])
        new_prediction = model.predict(Z)
        result={"status": "pending", "nama": wargaData["nama"]}
        print(new_prediction)
        if new_prediction[0] == 1:
            result["status"]="Miskin Extreme"
        elif new_prediction[0] == 0:
            result["status"]="CBP"
        elif new_prediction[0] == 2:
            result["status"]="PKH"
        elif new_prediction[0] == 3:
            result["status"]="Tidak Layak"
        else:
            return False
        
        print(new_prediction)
        print(result["status"])

        # Update data warga
        warga.jenis = result["status"]
        db.session.commit()
        
        return result
    except Exception as e:
        print(e)
        return False

def create():
    try:
        nik = request.form.get("nik")
        nama = request.form.get("nama")
        alamat = request.form.get("alamat")
        no_rt = request.form.get("no_rt")
        pekerjaan = request.form.get("pekerjaan")
        penghasilan = request.form.get("penghasilan")
        tanggungan = request.form.get("tanggungan")
        kondisi_rumah = request.form.get("kondisi_rumah")
        status_rumah = request.form.get("status_rumah")
        
        warga = Warga(
            nik=nik,
            nama=nama,
            alamat=alamat,
            no_rt=no_rt,
            pekerjaan=pekerjaan,
            penghasilan=penghasilan,
            tanggungan=tanggungan,
            kondisi_rumah=kondisi_rumah,
            status_rumah=status_rumah
        )

        db.session.add(warga)
        db.session.commit()

        return True
    except Exception as e:
        print(e)
        return False

def naiveBayesReport():
    try:
        #Import data dari CSV
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
        acc = accuracy * 100

        # Menampilkan laporan klasifikasi
        classReport = classification_report(y_test, y_pred)

        # Menampilkan matriks kebingungan
        confMatrix = confusion_matrix(y_test, y_pred)

        # Cross-Validation
        cv_scores = cross_val_score(model, X, y, cv=5)
        cvMean = np.mean(cv_scores) * 100
        
        result = {
            "acc": round(acc, 1),
            "classReport": classReport,
            "confMatrix": confMatrix,
            "cv": cv_scores,
            "cvMean": round(cvMean, 1)
        }
        
        return result
    except Exception as e:
        print(e)
        return False

def decisionTreeReport():
    try:
        # Import data dari CSV
        data = pd.read_excel('dataset_nonlabel_test.xlsx')

        # Memisahkan fitur dan label
        X = data.iloc[:, [3,4,5,6]].values  # Independent Feature
        y = data.iloc[:, -1].values

        # Standardisasi feature
        scaler = StandardScaler()
        data['penghasilan'] = scaler.fit_transform(data[['penghasilan']])

        # Misalkan kolom target adalah 'Status'
        X = data[['penghasilan', 'tanggungan', 'kondisi_rumah', 'status_rumah']]
        y = data['jenis']

        # Seleksi fitur terbaik
        selector = SelectKBest(f_classif, k='all')
        X_selected = selector.fit_transform(X, y)

        # Membagi data menjadi data pelatihan dan pengujian
        X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.25, random_state=0)

        # Membuat model Decision Tree
        model = DecisionTreeClassifier(max_depth=4)

        # Melatih model
        model.fit(X_train, y_train)

        # Memprediksi data pengujian
        y_pred = model.predict(X_test)

        # Memprediksi data pengujian
        y_pred = model.predict(X_test)

        # Menghitung akurasi
        accuracy = accuracy_score(y_test, y_pred)
        acc = accuracy * 100

        # Menampilkan laporan klasifikasi
        # classReport = classification_report(y_test, y_pred, output_dict=True)
        classReport = classification_report(y_test, y_pred)

        # Menampilkan matriks kebingungan
        confMatrix = confusion_matrix(y_test, y_pred)

        # Cross-Validation
        cv_scores = cross_val_score(model, X, y, cv=5)
        cvMean = np.mean(cv_scores) * 100
        
        result = {
            "acc": round(acc, 1),
            "classReport": classReport,
            "confMatrix": confMatrix,
            "cv": cv_scores,
            "cvMean": round(cvMean, 1)
        }
        
        # # gambar belum berhasil
        # plt.rcParams['figure.dpi'] = 85
        # plt.subplots(figsize=(15,15))
        # tree.plot_tree(model, fontsize=10)
        # image_path = os.path.join('public', 'images', 'tree_plot.png')
        # plt.savefig(image_path)
        # plt.close()
        
        return result
    except Exception as e:
        print(e)
        return False
    
