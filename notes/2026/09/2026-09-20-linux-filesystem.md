---
date: "2026-09-20"
track: "homelab"
topic: "linux-filesystem"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nex-agi/nex-n2.5-pro:free"
evidence_count: 0
---

# Daily Study Brief: Linux filesystem dan path

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Memahami hierarki filesystem Linux serta perbedaan absolute dan relative path.

## Konsep inti

### Filesystem hierarchy

Direktori seperti /etc, /var, /home, dan /tmp memiliki fungsi berbeda sehingga konfigurasi, data, log, dan berkas sementara dapat ditempatkan secara konsisten.

### Absolute dan relative path

Absolute path dimulai dari root, sedangkan relative path dihitung dari working directory saat ini.

## Latihan

1. Gunakan pwd dan ls untuk mengenali working directory.
2. Tentukan letak suatu berkas di dalam hierarki filesystem.
3. Bandingkan pembacaan berkas yang sama menggunakan absolute path dan relative path.
4. Petakan lokasi konfigurasi, data, dan log dari satu aplikasi yang sudah dikenal.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa konfigurasi sistem biasanya berada di /etc?
- [ ] Kapan relative path lebih berisiko daripada absolute path?
- [ ] Apa perbedaan titik awal absolute path dan relative path?

## Langkah berikutnya

Latih penentuan lokasi konfigurasi, data, dan log aplikasi dengan membedakan absolute path dari relative path.

## Referensi

- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
