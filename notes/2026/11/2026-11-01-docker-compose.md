---
date: "2026-11-01"
track: "homelab"
topic: "docker-compose"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "cohere/north-mini-code:free"
evidence_count: 0
---

# Daily Study Brief: Menata service dengan Docker Compose

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Menata service dengan Docker Compose

## Konsep inti

### Declarative services

Berkas Compose mendeskripsikan service, network, volume, dan dependency yang diinginkan.

### Environment configuration

Konfigurasi dapat dipisahkan dari image, tetapi secret tetap tidak boleh dimasukkan ke repository.

## Latihan

1. Buat Compose sederhana untuk satu web server lokal.

2. Validasi konfigurasi dengan docker compose config.

3. Hentikan dan buat ulang service untuk menguji reproducibility.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa keuntungan Compose dibanding rangkaian docker run panjang?
- [ ] Data apa yang tidak boleh ditulis langsung di compose.yaml?

## Langkah berikutnya

Lanjutkan ke langkah-langkah lab berikutnya.

## Referensi

- [Docker Compose documentation](https://docs.docker.com/compose/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
