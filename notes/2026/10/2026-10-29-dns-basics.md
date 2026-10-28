---
date: "2026-10-29"
track: "homelab"
topic: "dns-basics"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "cohere/north-mini-code:free"
evidence_count: 0
---

# Daily Study Brief: DNS dan resolusi nama

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

DNS dan resolusi nama

## Konsep inti

### Resolver dan authoritative server

Resolver mencari jawaban, sedangkan authoritative server menyediakan data resmi untuk sebuah zona.

### Record dan TTL

Record menyimpan data seperti alamat atau alias, sementara TTL mengendalikan berapa lama jawaban boleh di-cache.

## Latihan

1. Gunakan nslookup atau dig untuk membaca record sebuah domain.

2. Bandingkan record A, AAAA, dan CNAME.

3. Periksa TTL lalu jelaskan pengaruhnya terhadap perubahan DNS.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa beda resolver rekursif dan authoritative server?
- [ ] Mengapa perubahan DNS tidak selalu terlihat seketika?

## Langkah berikutnya

Lanjutkan ke materi siklus berikutnya.

## Referensi

- [RFC 1034 Domain Names](https://www.rfc-editor.org/rfc/rfc1034)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
