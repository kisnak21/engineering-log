---
date: "2026-10-24"
track: "homelab"
topic: "linux-filesystem"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Linux filesystem dan path

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Struktur filesystem membantu menentukan lokasi konfigurasi, data aplikasi, log, dan berkas sementara secara konsisten. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Filesystem hierarchy

Direktori seperti /etc, /var, /home, dan /tmp memiliki fungsi berbeda sehingga data aplikasi tidak diletakkan sembarangan.

### Absolute dan relative path

Absolute path dimulai dari root, sedangkan relative path dihitung dari working directory saat ini.

## Latihan

1. Gunakan pwd dan ls untuk mengenali working directory.

2. Bandingkan hasil membaca berkas dengan absolute path dan relative path.

3. Petakan lokasi konfigurasi, data, dan log dari satu aplikasi yang sudah dikenal.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa konfigurasi sistem biasanya berada di /etc?
- [ ] Kapan relative path lebih berisiko daripada absolute path?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
