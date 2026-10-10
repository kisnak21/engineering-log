---
date: "2026-10-10"
track: "homelab"
topic: "storage-zfs-raid"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-ultra-550b-a55b:free"
evidence_count: 0
---

# Daily Study Brief: Manajemen Storage dan ZFS

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Manajemen Storage dan ZFS

## Konsep inti

### Copy-on-write

Data lama tidak langsung ditimpa, memungkinkan snapshot yang efisien tanpa beban kinerja.

### RAID-Z

Implementasi RAID dari ZFS yang menggabungkan disk redundancy dengan filesystem integrity.

## Latihan

1. Buat zpool sederhana dari satu atau dua block device.

2. Buat snapshot dari dataset dan ubah isi foldernya.

3. Rollback filesystem ke snapshot tersebut.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa copy-on-write sangat bermanfaat untuk backup?
- [ ] Apa beda RAID tradisional dengan ZFS?

## Langkah berikutnya

Pelajari pengaturan dataset dan properti ZFS lanjutan.

## Referensi

- [OpenZFS Documentation](https://openzfs.github.io/openzfs-docs/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
