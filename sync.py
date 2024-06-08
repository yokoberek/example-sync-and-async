import time
import random

def kirim_pesan_sinkron(wanita, pesan):
    print(f"Mengirim pesan kepada {wanita}: {pesan}")
    time.sleep(2)  # Mensimulasikan penundaan pengiriman pesan
    balasan = random.choice(["Ya, aku mau jadi pacarmu!", "Maaf, aku tidak tertarik."])
    return f"Balasan dari {wanita}: {balasan}"

def chat_sinkron():
    wanita_list = ["Wanita 1", "Wanita 2", "Wanita 3", "Wanita 4", "Wanita 5"]
    pesan = "Apakah kamu mau jadi pacarku?"
    
    for wanita in wanita_list:
        respon = kirim_pesan_sinkron(wanita, pesan)
        print(f"Menerima balasan: {respon}")
        time.sleep(1)  # Mensimulasikan penundaan antar pesan

# Menjalankan chat sinkron
print("Komunikasi Sinkron")
chat_sinkron()
