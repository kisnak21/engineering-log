---
date: "2026-10-23"
track: "web-development"
topic: "observability-logging"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "recursive/flint-v1.0:free"
evidence_count: 0
---

# Daily Study Brief: Observability dan Logging

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Observability dan Logging: structured logging serta Correlation ID

## Konsep inti

### Structured logging

Menulis log dalam format JSON agar parameter dan detail kontekstual mudah dikueri oleh sistem pemantauan.

### Correlation ID

Sebuah ID unik yang melintasi berbagai layanan untuk melacak jejak request tunggal secara end-to-end.

## Latihan

1. Ubah output print() biasa di skrip sederhana menjadi format JSON log.

2. Tambahkan field req_id untuk melacak eksekusi di beberapa level fungsi.

3. Analisa di mana sebaiknya sistem merotasi log.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa kelebihan struktur log JSON dibandingkan teks datar?
- [ ] Mengapa log aplikasi tidak boleh diandalkan sebagai penyimpanan audit tunggal?

## Langkah berikutnya

Analisa di mana sebaiknya sistem merotasi log.

## Referensi

- [The 12-Factor App - Logs](https://12factor.net/logs)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
