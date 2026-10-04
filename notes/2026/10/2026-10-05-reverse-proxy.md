---
date: "2026-10-05"
track: "homelab"
topic: "reverse-proxy"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Reverse proxy untuk beberapa service

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Reverse proxy menyediakan satu pintu masuk dan meneruskan request ke service yang tepat berdasarkan host atau path. Gunakan putaran ini untuk membangun dasar yang dapat diuji.

## Konsep inti

### Request forwarding

Proxy menerima request klien lalu membuat request baru menuju upstream yang dipilih.

### Forwarded headers

Header proxy membawa informasi seperti host dan alamat klien, tetapi hanya boleh dipercaya dari proxy yang dikenal.

## Latihan

1. Gambar alur browser, reverse proxy, dan dua upstream service.

2. Buat konfigurasi lokal untuk meneruskan satu hostname ke satu service.

3. Periksa Host dan X-Forwarded-For yang diterima aplikasi.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa beda reverse proxy dan forward proxy?
- [ ] Mengapa aplikasi perlu mengetahui proxy mana yang dapat dipercaya?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [NGINX reverse proxy guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
