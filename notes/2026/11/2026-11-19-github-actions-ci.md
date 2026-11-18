---
date: "2026-11-19"
track: "web-development"
topic: "github-actions-ci"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: CI dengan GitHub Actions

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

CI menjalankan pemeriksaan yang sama pada perubahan kode sehingga kegagalan dapat ditemukan sebelum deployment. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Workflow trigger

Workflow dapat berjalan berdasarkan push, pull request, jadwal, atau pemicu manual.

### Least privilege token

GITHUB_TOKEN sebaiknya hanya diberi permission yang dibutuhkan oleh job.

## Latihan

1. Buat daftar pemeriksaan yang perlu berjalan pada pull request.

2. Pisahkan job cepat seperti lint dari test yang lebih berat.

3. Periksa permission token dan hapus akses tulis yang tidak diperlukan.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa beda trigger push dan pull_request?
- [ ] Mengapa workflow perlu timeout dan concurrency policy?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [GitHub Actions documentation](https://docs.github.com/en/actions)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
