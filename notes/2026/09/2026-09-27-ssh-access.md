---
date: "2026-09-27"
track: "homelab"
topic: "ssh-access"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-ultra-550b-a55b:free"
evidence_count: 0
---

# Daily Study Brief: SSH dan autentikasi berbasis key

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

SSH dan autentikasi berbasis key

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

Lanjutkan ke pembahasan konfigurasi server SSH untuk hanya menerima autentikasi kunci publik.

## Referensi

- [OpenSSH manual pages](https://www.openssh.com/manual.html)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
