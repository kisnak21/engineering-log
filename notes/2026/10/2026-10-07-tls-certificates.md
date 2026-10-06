---
date: "2026-10-07"
track: "homelab"
topic: "tls-certificates"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
evidence_count: 0
---

# Daily Study Brief: TLS certificate dan HTTPS

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Mengenali rantai sertifikat TLS dan merencanakan renewal masa berlaku

## Konsep inti

### Certificate chain

Klien memverifikasi certificate server melalui rantai ke certificate authority yang dipercaya.

### Renewal

Certificate memiliki masa berlaku sehingga pembaruan dan pemantauan perlu diotomatisasi.

## Latihan

1. Periksa issuer dan masa berlaku certificate sebuah situs publik.

2. Catat domain yang tercakup pada Subject Alternative Name.

3. Rancang pengingat sebelum masa berlaku berakhir.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa yang diverifikasi oleh browser ketika membuka HTTPS?
- [ ] Mengapa private key TLS tidak boleh dikirim ke repository?

## Langkah berikutnya

Buat rencana pemantauan masa berlaku dan otomatisasi renewal

## Referensi

- [Let's Encrypt documentation](https://letsencrypt.org/docs/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
