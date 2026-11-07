---
date: "2026-11-08"
track: "homelab"
topic: "ansible-basics"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Configuration management dengan Ansible

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Manajemen manual menyebabkan server menjadi "snowflake". Ansible membuat pengaturan dapat dideskripsikan sebagai kode yang dapat diulang. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Idempotency

Menjalankan playbook Ansible berkali-kali harus menghasilkan state yang sama seperti menjalankannya sekali.

### Agentless

Ansible tidak memerlukan agen di server target, cukup SSH dan Python.

## Latihan

1. Buat inventory file dengan localhost atau server lab.

2. Tulis satu tugas untuk memastikan sebuah file konfigurasi ada.

3. Jalankan playbook dan perhatikan bahwa task tidak mengubah apa pun pada eksekusi kedua.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa itu idempotency dalam konteks Ansible?
- [ ] Mengapa arsitektur agentless menguntungkan?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [Ansible Getting Started](https://docs.ansible.com/ansible/latest/getting_started/index.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
