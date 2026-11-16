---
date: "2026-11-17"
track: "web-development"
topic: "postgresql-indexes"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "particle-ai/particle-1:free"
evidence_count: 0
---

# Daily Study Brief: Index PostgreSQL dan query plan

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Index PostgreSQL dan query plan: memilih index berdasarkan query nyata dengan mempertimbangkan biaya penyimpanan dan penulisan.

## Konsep inti

### Index lookup

Planner dapat memakai index untuk mengurangi jumlah row yang perlu diperiksa.

### Write overhead

Setiap perubahan data juga perlu memperbarui index terkait.

## Latihan

1. Buat tabel latihan dengan data non-sensitif.

2. Bandingkan EXPLAIN sebelum dan setelah menambahkan index yang relevan.

3. Catat query yang terbantu dan operasi tulis yang menerima biaya tambahan.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa tidak semua kolom perlu diberi index?
- [ ] Apa informasi utama yang dicari dari EXPLAIN?

## Langkah berikutnya

Bandingkan EXPLAIN sebelum dan setelah menambahkan index yang relevan pada tabel latihan berisi data non-sensitif.

## Referensi

- [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
