---
date: "2026-10-27"
track: "homelab"
topic: "ip-subnet-and-routing"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: IP address, subnet, dan routing

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Pemahaman jaringan dasar diperlukan untuk menghubungkan host, container, router, dan layanan tanpa menebak konfigurasi. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Subnet

Prefix jaringan menentukan bagian network dan host dari sebuah alamat IP.

### Routing table

Routing table memilih jalur berikutnya berdasarkan tujuan paket dan prefix yang paling spesifik.

## Latihan

1. Catat alamat IP dan prefix perangkat yang digunakan.

2. Baca routing table tanpa mengubahnya.

3. Identifikasi default gateway dan jelaskan kapan jalur itu dipakai.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa fungsi default gateway?
- [ ] Mengapa dua host dalam subnet yang sama biasanya tidak memerlukan router untuk saling berkomunikasi?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [ip-route manual](https://man7.org/linux/man-pages/man8/ip-route.8.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
