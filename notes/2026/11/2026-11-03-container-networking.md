---
date: "2026-11-03"
track: "homelab"
topic: "container-networking"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-ultra-550b-a55b:free"
evidence_count: 0
---

# Daily Study Brief: Docker network dan komunikasi service

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Docker network dan komunikasi service

## Konsep inti

### Service discovery

Container pada network Compose yang sama dapat menggunakan nama service sebagai hostname.

### Published port

Port hanya perlu dipublikasikan ketika koneksi harus datang dari luar network container.

## Latihan

1. Buat dua service pada network Compose yang sama.

2. Uji komunikasi menggunakan nama service.

3. Identifikasi port yang dapat tetap internal dan tidak perlu dipublikasikan.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa beda expose dan publish port?
- [ ] Mengapa database sering tidak perlu dipublikasikan ke seluruh jaringan?

## Langkah berikutnya

Terapkan pengetahuan ini pada proyek homelab berikutnya.

## Referensi

- [Docker networking overview](https://docs.docker.com/engine/network/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
