import asyncio
import random

async def kirim_pesan_asinkron(wanita, pesan):
    print(f"Mengirim pesan kepada {wanita}: {pesan}")
    await asyncio.sleep(2)  # Mensimulasikan penundaan pengiriman pesan
    balasan = random.choice(["Ya, aku mau jadi pacarmu!", "Maaf, aku tidak tertarik."])
    return f"Balasan dari {wanita}: {balasan}"

async def chat_asinkron():
    wanita_list = ["Wanita 1", "Wanita 2", "Wanita 3", "Wanita 4", "Wanita 5"]
    pesan = "Apakah kamu mau jadi pacarku?"
    
    tugas = [asyncio.create_task(kirim_pesan_asinkron(wanita, pesan)) for wanita in wanita_list]

    for respon in await asyncio.gather(*tugas):
        print(f"Menerima balasan: {respon}")

# Menjalankan chat asinkron
print("Komunikasi Asinkron")
asyncio.run(chat_asinkron())
