---
date: "2026-11-15"
track: "web-development"
topic: "auth-jwt-oauth2"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Modern Auth: JWT dan OAuth2

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Aplikasi decoupling seperti SPA atau mobile apps membutuhkan state yang lebih fleksibel dibandingkan session cookie klasik. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

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

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [JWT.io Debugger](https://jwt.io/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
