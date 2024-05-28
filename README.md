# Web Klasifikasi Bantuan
Program penentuan kelayakan bantuan berbasis website dengan menggunakan metode naive bayes dan desicion tree.

# How to Start Program
 - Pastikan Python telah terinstall dan pip juga (biasanya include)
 - Lengkapi file .env sesuai keperluan teman-teman
 - Buka terminal dari editor, kemudian buat virtual environment dengan menjalankan perintah ```python -m venv .venv```
 - Kemudian masuk ke dalam virtual environment dengan perintah ```.venv\Scripts\activate```, dan perintah ```deactivate``` untuk keluar dari virtual environment
 - Setelah itu install semua library yang digunakan dengan menjalan kan perintah ```pip install -r requirements.txt```
 - Buat database terlebih dahulu dengan nama yang sama dengan yang ada di file .env
 - Jalan kan perintah ```flask db init```, kemudian ```flask db migrate -m "init migration"```, dan ```flask db upgrade```.
 - Lalu jalankan program dengan perintah ```flask run```
 - Happy coding ^,^