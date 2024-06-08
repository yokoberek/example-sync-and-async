Synchronous

- Dalam fungsi `chat_sinkron`, pria mengirim pesan ke satu wanita dan menunggu balasannya sebelum melanjutkan ke wanita berikutnya
- Fungsi `kirim_pesan_sinkron` mensimulasikan pengiriman pesan dengan`time.sleep(2)` untuk menunggu selama 2 detik sebelum mengembalikan balasan yang dihasilkan secara acak.

Asynchronous

- Dalam fungsi `chat_asinkron`, pria mengirim pesan ke semua wanita secara bersamaan tanpa menunggu balasan satu per satu
- Fungsi `kirim_pesan_asinkron` menggunakan `await asyncio.sleep(2)` untuk menunggu selama 2 detik sebelum mengembalikan balasan yang dihasilkan secara acak, dan semua tugas dijalankan secara paralel menggunakan `asyncio.gather`.
