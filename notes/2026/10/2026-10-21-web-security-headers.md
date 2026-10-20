---
date: "2026-10-21"
track: "web-development"
topic: "web-security-headers"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
evidence_count: 0
---

# Daily Study Brief: Security header untuk aplikasi web

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Membuat header keamanan aplikasi web

## Konsep inti

### Content Security Policy

CSP membatasi sumber script, style, gambar, dan resource lain yang diizinkan.

### Transport and framing policy

HSTS dan frame restrictions membantu mencegah downgrade koneksi serta embedding yang tidak diinginkan.

## Latihan

1. Periksa response header aplikasi latihan.

2. Buat CSP dalam mode report-only sebelum memberlakukannya.

3. Catat resource yang diblokir dan perbaiki policy secara bertahap.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa CSP yang terlalu longgar memberi perlindungan terbatas?
- [ ] Mengapa HSTS perlu diterapkan dengan hati-hati?

## Langkah berikutnya

Teruskan memperbaiki policy setelah mengidentifikasi resource yang diblokir.

## Referensi

- [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
