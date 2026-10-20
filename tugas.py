import tkinter as tk
def prediction_result():
    result_label.config(text="Teknologi Informasi")
top = tk.Tk()
title_label = tk.Label(top, text="Prediksi Prodi Pilihan")
title_label.pack(pady=10)
subjects = ["Masukkan nilai mapel 1: ",
"Masukkan nilai mapel 2: ",
"Masukkan nilai mapel 3: ",
"Masukkan nilai mapel 4: ",
"Masukkan nilai mapel 5: ",
"Masukkan nilai mapel 6: ",
"Masukkan nilai mapel 7: ",
"Masukkan nilai mapel 8: ",
"Masukkan nilai mapel 9: ",
"Masukkan nilai mapel 10: "]
for name in subjects:
    frame = tk.Frame(top)
    frame.pack()
    L = tk.Label(frame, text=name, width=20)
    L.pack(side=tk.LEFT)
    E = tk.Entry(frame, bd=5)
    E.pack(side=tk.RIGHT)

B = tk.Button(top, text="Hasil Prediksi", command =prediction_result)
B.pack(pady=10)

result_label = tk.Label(top, text="", relief=tk.RAISED, width=30)
result_label.pack(pady=10)
top.mainloop()