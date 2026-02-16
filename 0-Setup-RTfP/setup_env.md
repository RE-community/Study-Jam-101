# Cara Setup Environment untuk Study Jam

## Tentang Package

Robotics Toolbox for Python, Spatial Maths for Python, dsb. yang di-bundle dalam package `rvc3python` adalah sebuah software tools berbentuk Python package untuk melakukan simulasi robotika dan mempelajari manipulasi matematika dibaliknya. Informasi selengkapnya dapat dilihat sini:

- [Official Github Page](https://github.com/petercorke/RVC3-python)
- [Documentation Page 1](https://petercorke.github.io/robotics-toolbox-python/)
- [Documentation Page 2](https://bdaiinstitute.github.io/spatialmath-python/)

## Python Virtual Environment Setup

[Virtual environment](https://docs.python.org/3/library/venv.html) digunakan untuk mengisolasi Python package yang akan digunakan sehingga tidak menimbulkan conflict. Contohnya, ketika ada tiga project yang membutuhkan `numpy` dengan versi berbeda, ketiganya tidak diinstal secara global, tetapi pada masing-masing virtual environment.

### Windows

Pertama-tama, buat sebuah folder (misalnya, `temp`). Lalu, buka terminal PowerShell di bawah folder tsb. dengan klik "Open in Terminal":

![File Folder Interface Windows 11](/0-Setup-RTfP/assets/0_1.jpg)

Lalu, cek versi Python dengan command berikut:
```
python --version
```

Contoh dari output command-nya adalah sebagai berikut:
```
Python 3.11.9
```
Pastikan versi Python yang terinstalasi sesuai dengan supported version di [Github Page dari Robotics Toolbox for Python](https://github.com/petercorke/robotics-toolbox-python).

Lalu, buat virtual environment dengan command berikut:
```
py --3.11.9 -m venv .venv
```
Penjelasan: command tsb. menggunakan Python module `venv` dari Python versi `3.11.9` untuk membuat virtual environment di bawah folder `temp/.venv`.

Di bawah folder `temp`, jalankan command `ls` di terminal untuk mengecek eksistensi folder `.venv`:
```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2/16/2026   7:22 AM                .venv
```

Sebelum digunakan, Virtual environment harus [diaktivasi](https://docs.python.org/3/library/venv.html#how-venvs-work). Caranya adalah dengan menjalankan command berikut:
```
.\.venv\Scripts\Activate.ps1
```
Setelahnya, terminal prompt text seharusnya terlihat seperti berikut:
```
(.venv) PS C:\Users\User\RE-Community\temp>
```

## Instalasi `rvc3python`

Tutorial ini dibuat menggunakan Python versi 3.11.9 dan `pip` versi 24.0.

### Windows

> Note: Pastikan virtual environment telah diaktivasi

Pertama-tama, install package dengan invoke command berikut (`pip` dan `pip3` akan memberikan hasil yang sama):
```
pip install rvc3python
```
Verifikasi hasil instalasi dengan command berikut:
```
pip list
```
Beberapa package yang harus ada di antaranya `roboticstoolbox-python 1.1.1`, `numpy 1.26.4`, `spatialmath-python 1.1.15` dan `matplotlib 3.10.8`. Selama proses setup, ternyata ada beberapa package tambahan yang harus diinstal tetapi tidak dicantumkan sebagai dependency, seperti `ipympl` dan `ffmpeg`.

Untuk menginstal `ipympl`:
```
pip install ipympl
```
Lalu, untuk menginstal `ffmpeg`:
```
winget install ffmpeg
```
Verifikasi hasil instalasi `ffmpeg` dengan invoke command `ffmpeg -version` via terminal PowerShell.

## Instalasi Jupyter Notebook

Tutorial ini dibuat menggunakan Python versi 3.11.9 dan `pip` versi 24.0.

### Windows

Ada dua pilihan dalam menggunakan Jupyter Notebook. Pertama, bisa dengan plugin di VS Code ([tutorial](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)). Kedua, bisa dengan menggunakan `pip`. Berikut adalah command-nya:
```
pip install notebook
```
Lalu, untuk menjalankannya, invoke command berikut:
```
jupyter notebook --no-browser
```
Flag `--no-browser` digunakan agar user bisa memilih browser yang digunakan untuk membuka interface dari notebook.

Untuk verifikasi setup, jalankan notebook berikut (jangan di platform Google Colab): [Link notebook](https://drive.google.com/drive/folders/1QW8fyd0WgHmspFJrLuX2b5xBOi4mgf1T?usp=drive_link).

Common Issue:
1. Gagal build `roboticstoolbox-python` ([solusi](/0-Setup-RTfP/known_issues.md#no-microsoft-visual-c-140-or-greater-windows)).
2. Versi `numpy` tidak kompatibel "A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.4.2 as it may crash ..." ([solusi](/0-Setup-RTfP/known_issues.md#numpy-error)).
