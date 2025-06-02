import tkinter as tk
from PIL import Image, ImageTk

# Quiz questions list with image choices
pertanyaan_kuis = [
    {
        "question": "Bentuk: Lapangan Sepak Bola, Warna: Langit",
        "choices": [
            "Persegipanjangbirumuda.png",
            "Lingkaranbirutua.png",
            "Persegipanjanghijau.png",
            
        ],
        "answer": "Persegipanjangbirumuda.png"
    },
    {
        "question": "Bentuk: Papan catur, Warna: Pisang",
        "choices": [
            "Bintangkuning.png",
            "belahketupatorange.png",
            "Persegikuning.png",
         
        ],
        "answer": "Persegikuning.png"
    },
    {
        "question": "Bentuk: Benda di langit malam hari, Warna: kertas",
        "choices": [
            "Bulanbirumuda.png",
            "bintangputih.png",
            "Lingkaranpink.png",
            
        ],
        "answer": "bintangputih.png"
    },
    {
        "question": "Bentuk: Jam dinding, Warna: Laut",
        "choices": [
            "Lingkaranbirutua.png",
            "Persegipanjangbirumuda.png",
            "Lingkaranpink.png",
            
        ],
        "answer": "Lingkaranbirutua.png"
    },
    {
        "question": "Bentuk: Atap rumah , Warna: pohon",
        "choices": [
            "persegipanjanghijau.png",
            "Segitigahijau.png",
            "Segitigapink.png",
            
        ],
        "answer": "Segitigahijau.png"
    },
    {
        "question": "Bentuk: Ketupat , Warna: Jeruk",
        "choices": [
            "belahketupatorange.png",
            "persegiorange.png",
            "belahketupatpink.png",
            
        ],
        "answer": "belahketupatorange.png"
    },
]

def tampilkan_pertanyaan(index):
    if index >= len(pertanyaan_kuis):
        hasil_label.config(text=f"Kuis selesai! Skor akhir: {skor[0]} dari {len(pertanyaan_kuis)}")
        # Unbind clicks after quiz ends
        for lbl in gambar_labels:
            lbl.unbind("<Button-1>")
        return

    soal = pertanyaan_kuis[index]
    soal_label.config(text=f"Pertanyaan {index + 1}: {soal['question']}")
    hasil_label.config(text="")
    
    # Show all choices as clickable images
    for i, filename in enumerate(soal['choices']):
        try:
            img = Image.open(filename)
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            
            gambar_labels[i].config(image=img_tk)
            gambar_labels[i].image = img_tk  # Keep reference
            # Bind click event: use default arg to capture filename
            gambar_labels[i].bind("<Button-1>", lambda e, f=filename: jawab(f, index))
        except Exception as e:
            gambar_labels[i].config(text=f"Gambar tidak ditemukan\n{filename}")
            gambar_labels[i].image = None
            print(f"Error membuka gambar '{filename}': {e}")

def jawab(pilihan_file, index):
    if pilihan_file == pertanyaan_kuis[index]['answer']:
        hasil_label.config(text="Benar!")
        skor[0] += 1
    else:
        hasil_label.config(text=f"Salah! Jawaban benar: {pertanyaan_kuis[index]['answer']}")
    
    # Temporarily disable clicks to avoid multiple answers
    for lbl in gambar_labels:
        lbl.unbind("<Button-1>")
    
    root.after(1500, lambda: tampilkan_pertanyaan(index + 1))

# Setup main window
root = tk.Tk()
root.title("Kuis Bentuk & Warna")
skor = [0]  # Using list to have mutable integer

soal_label = tk.Label(root, text="", font=("Helvetica", 16))
soal_label.pack(pady=15)

gambar_frame = tk.Frame(root)
gambar_frame.pack(pady=10)

gambar_labels = []
for i in range(4):
    lbl = tk.Label(gambar_frame, cursor="hand2", bd=2, relief="ridge")
    lbl.grid(row=0, column=i, padx=15)
    gambar_labels.append(lbl)

hasil_label = tk.Label(root, text="", font=("Helvetica", 14))
hasil_label.pack(pady=10)

tampilkan_pertanyaan(0)

root.mainloop()