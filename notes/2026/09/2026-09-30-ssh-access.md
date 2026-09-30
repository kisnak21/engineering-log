---
date: "2026-09-30"
track: "homelab"
topic: "ssh-access"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
evidence_count: 0
---

# Daily Study Brief: SSH dan autentikasi berbasis key

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Mengenali dan mengkonfigurasi SSH menggunakan public key authentication

## Konsep inti

### Public key authentication

Server menyimpan public key, sedangkan private key tetap berada pada perangkat pengguna dan tidak pernah dikirim.

### Host verification

Fingerprint host membantu mendeteksi ketika koneksi diarahkan ke server yang berbeda dari sebelumnya.

## Latihan

1. Buat pasangan key khusus latihan tanpa membagikan private key.

2. Periksa fingerprint public key yang dibuat.

3. Tulis daftar permission aman untuk folder .ssh dan authorized_keys.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa private key tidak boleh masuk repository?
- [ ] Apa tujuan file known_hosts?

## Langkah berikutnya

Melanjutkan dengan memverifikasi fingerprint host dan menetapkan permission aman pada .ssh

## Referensi

- [OpenSSH manual pages](https://www.openssh.com/manual.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
