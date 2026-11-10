---
date: "2026-11-11"
track: "web-development"
topic: "caching-strategies"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "cohere/north-mini-code:free"
evidence_count: 0
---

# Daily Study Brief: Strategi caching dan Cache-Control

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Strategi caching dan Cache-Control

## Konsep inti

### Cache busting

Menambahkan hash pada nama file statis agar browser mengunduh versi baru secara otomatis ketika file berubah.

### Cache-Control headers

Instruksi yang diberikan server kepada klien dan proxy tentang berapa lama respons bisa digunakan kembali.

## Latihan

1. Analisis header Cache-Control pada beberapa asset di situs populer.

2. Konfigurasi server lokal untuk mengirim instruksi max-age.

3. Amati behavior browser (Network tab) saat me-reload halaman dengan cache.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa perbedaan no-cache dan no-store?
- [ ] Kapan kita harus menggunakan immutable cache policy?

## Langkah berikutnya

Terapkan strategi caching yang dipelajari ke proyek web pengembangan Anda saat ini.

## Referensi

- [MDN HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
