---
date: "2026-11-16"
track: "web-development"
topic: "database-design-normalization"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Database normalization dan constraint

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Skema yang baik mencegah anomali data saat penulisan dan memastikan integritas hubungan antar entitas. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Normal forms

Aturan untuk mengurangi duplikasi data dan memastikan fungsionalitas ketergantungan kolom.

### Foreign keys

Constraint untuk memaksa agar baris yang dirujuk ada sebelum baris referensi dimasukkan.

## Latihan

1. Desain skema dengan tabel yang memiliki foreign key ke tabel lain.

2. Coba hapus baris yang sedang dirujuk tanpa cascading delete.

3. Identifikasi bagian mana dari skema yang berpotensi menyebabkan duplikasi data.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa kita terkadang melakukan denormalisasi di environment produksi?
- [ ] Apa risiko tidak menggunakan constraint secara eksplisit di level database?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [PostgreSQL Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
