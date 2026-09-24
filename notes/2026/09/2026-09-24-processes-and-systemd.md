---
date: "2026-09-24"
track: "homelab"
topic: "processes-and-systemd"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
evidence_count: 0
---

# Daily Study Brief: Process, service, dan systemd

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Pemantauan dan pemulihan layanan systemd

## Konsep inti

### Process lifecycle

Process memiliki PID, status, resource usage, dan exit code yang membantu diagnosis kegagalan.

### Service unit

Systemd unit mendeskripsikan cara service dimulai, dihentikan, direstart, dan diurutkan terhadap dependency.

## Latihan

1. Cari process yang sedang berjalan menggunakan ps.
2. Periksa status satu service dengan systemctl status.
3. Baca log service tersebut melalui journalctl tanpa mengubah konfigurasi.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa arti exit code nol?
- [ ] Apa beda restart policy dengan menjalankan process secara manual?

## Langkah berikutnya

Pantau dan pulihkan layanan setelah reboot mesin.

## Referensi

- [systemd service documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
