---
date: "2026-10-28"
track: "homelab"
topic: "firewall-basics"
cycle: 2
generated: true
reviewed: false
review_status: "pending"
generator: "curriculum-fallback"
model: "none"
evidence_count: 0
---

# Daily Study Brief: Dasar firewall (UFW/iptables)

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Firewall mencegah eksposur port yang tidak disengaja ke jaringan publik dan membatasi traffic ke aplikasi internal. Ini putaran ke-2; cari perbedaan dari pemahaman pada putaran sebelumnya.

## Konsep inti

### Default deny

Pendekatan keamanan di mana semua traffic ditolak kecuali secara eksplisit diizinkan.

### Stateless vs Stateful

Stateful firewall melacak koneksi aktif sehingga balasan untuk koneksi yang sah diizinkan otomatis.

## Latihan

1. Aktifkan ufw dengan aturan default deny inbound.

2. Izinkan port SSH agar tidak kehilangan akses.

3. Coba block ping (ICMP) untuk melihat efek dari rule.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Mengapa default deny lebih disarankan dari default allow?
- [ ] Apa bahayanya langsung mengaktifkan firewall tanpa mengizinkan SSH?

## Langkah berikutnya

Catat jawaban review dan satu hal yang masih belum jelas sebelum melanjutkan topik berikutnya.

## Referensi

- [UFW Essentials](https://help.ubuntu.com/community/UFW)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
