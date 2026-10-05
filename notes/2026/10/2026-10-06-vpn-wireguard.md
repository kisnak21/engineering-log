---
date: "2026-10-06"
track: "homelab"
topic: "vpn-wireguard"
cycle: 1
generated: true
reviewed: false
review_status: "pending"
generator: "openrouter"
model: "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"
evidence_count: 0
---

# Daily Study Brief: VPN dengan WireGuard

> Draf ini dibuat otomatis dari kurikulum dan aktivitas GitHub publik. Status pending berarti isinya belum dikonfirmasi sebagai pengalaman belajar pribadi.

## Fokus

Memahami WireGuard dan cara mengatur peer-to-peer VPN

## Konsep inti

### Cryptokey routing

WireGuard menggunakan kunci publik untuk autentikasi dan enkripsi routing antar node.

### Peer-to-peer VPN

Tidak ada arsitektur client-server murni; setiap titik adalah peer yang saling terhubung.

## Latihan

1. Buat sepasang private/public key.

2. Konfigurasi peer A dan peer B agar dapat saling ping melalui IP tunnel.

3. Tinjau log jika handshake gagal.

## Aktivitas GitHub publik

Tidak ada aktivitas publik GitHub yang terdeteksi pada tanggal ini. Aktivitas privat atau aktivitas di luar GitHub tidak disimpulkan.

## Pertanyaan review

- [ ] Apa keunggulan WireGuard dibandingkan OpenVPN?
- [ ] Bagaimana cara peer mengenali peer lainnya secara aman?

## Langkah berikutnya

Teruskan menguji konektivitas peer melalui ping

## Referensi

- [WireGuard Quick Start](https://www.wireguard.com/quickstart/)

## Review manual

Setelah membaca atau mencoba latihan, ubah metadata `reviewed` menjadi `true`, ubah `review_status` menjadi `approved`, lalu koreksi bagian yang tidak sesuai.
