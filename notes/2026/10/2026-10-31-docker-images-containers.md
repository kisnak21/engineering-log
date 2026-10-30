---
date: "2026-10-31"
track: "homelab"
topic: "docker-images-containers"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "poolside/laguna-xs-2.1:free"
evidence_count: 0
---

# Daily Study Brief: Docker image dan container

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Memahami perbedaan antara Docker image dan container untuk membangun, menjalankan, serta mengelola aplikasi secara efisien.

## Konsep inti

### Immutable image

Image berisi layer aplikasi yang digunakan sebagai template untuk membuat container.

### Container lifecycle

Container dapat dibuat, dijalankan, dihentikan, dan dihapus tanpa mengubah image asalnya.

## Latihan

1. Jalankan image ringan lalu periksa container yang terbentuk.

2. Bandingkan daftar image dengan daftar container.

3. Hapus container latihan dan pastikan image masih tersedia.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa perbedaan image dan container?
- [ ] Mengapa data penting tidak sebaiknya hanya disimpan pada writable layer container?

## Langkah berikutnya

Eksplorasi cara menyimpan data secara persisten menggunakan volume atau bind mount.

## Referensi

- [Docker container concepts](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
