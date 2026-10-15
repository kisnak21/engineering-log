---
date: "2026-10-16"
track: "web-development"
topic: "auth-jwt-oauth2"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "cohere/north-mini-code:free"
evidence_count: 0
---

# Daily Study Brief: Modern Auth: JWT dan OAuth2

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Modern Auth: JWT dan OAuth2

## Konsep inti

### Stateless authentication

Server tidak perlu menyimpan sesi aktif karena payload JWT sudah di-sign dan cukup untuk membuktikan hak akses.

### Access vs Refresh tokens

Access token berumur pendek untuk akses harian, refresh token dipakai memperbarui access token di latar belakang.

## Latihan

1. Dekode JWT (tanpa verifikasi) dan baca isi payload-nya menggunakan debugger online atau skrip.

2. Pahami proses signing dengan mencoba memodifikasi payload lalu memverifikasinya kembali.

3. Gambarkan alur dasar dari OAuth 2 authorization code flow.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa menyimpan JWT di localStorage berisiko rentan terhadap XSS?
- [ ] Apa fungsi dari signature dalam sebuah token?

## Langkah berikutnya

Lanjutkan ke siklus berikutnya dari kurikulum Modern Auth.

## Referensi

- [JWT.io Debugger](https://jwt.io/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
