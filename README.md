# Engineering Log

Repository ini menerbitkan satu *daily study brief* setiap malam. Materi bergantian antara homelab dan web development, lalu diperkaya menggunakan aktivitas GitHub publik yang benar-benar terdeteksi.

Catatan otomatis bukan klaim bahwa seluruh materi sudah dipelajari atau dikuasai. Setiap catatan baru memiliki status `pending` sampai ditinjau secara manual.

## Catatan terbaru

<!-- latest-entry:start -->
[2026-09-24: Process, service, dan systemd](notes/2026/09/2026-09-24-processes-and-systemd.md)

Track: `homelab` | Review: `pending` | Generator: `openrouter`
<!-- latest-entry:end -->

## Yang dijalankan otomatis

Setiap hari pukul 22:37 WIB, workflow akan:

1. Memilih topik berikutnya dari [`config/curriculum.json`](config/curriculum.json).
2. Membaca aktivitas publik akun `kisnak21` dari GitHub Events API.
3. Meminta `openrouter/free` menyusun materi berbasis data tersebut.
4. Menggunakan materi kurikulum lokal jika OpenRouter gagal atau dibatasi.
5. Membuat catatan di `notes/YYYY/MM/` dan laporan bukti di `reports/activity/`.
6. Menjalankan test, validasi format, dan pemindaian pola secret.
7. Commit dan push langsung ke `main`.

Workflow juga dapat dijalankan manual dari tab **Actions**. Opsi `force` hanya digunakan jika catatan pada tanggal yang sama memang ingin dibuat ulang. Secara default, catatan yang sudah ada tidak disentuh sehingga edit manual tetap aman.

## Sumber dan batasan data

- Aktivitas proyek berasal dari GitHub public events. Aktivitas privat dan pekerjaan di luar GitHub tidak disimpulkan.
- Referensi belajar disimpan di kurikulum dan berasal dari dokumentasi teknis yang dapat dibuka langsung.
- Raw response model tidak disimpan ke repository.
- Source code repository lain tidak dikirim ke OpenRouter. Model hanya menerima topik kurikulum dan ringkasan metadata aktivitas publik.
- Secret GitHub dan OpenRouter hanya tersedia sebagai environment variable selama workflow berjalan.

## Review catatan

Front matter catatan baru berisi:

```yaml
generated: true
reviewed: false
review_status: "pending"
```

Setelah membaca atau mencoba latihan, ubah menjadi:

```yaml
reviewed: true
review_status: "approved"
```

Isi catatan dapat dikoreksi langsung dari editor GitHub. Workflow berikutnya tidak menimpa catatan dari tanggal sebelumnya.

## Konfigurasi repository

Secret yang dibutuhkan:

```text
OPENROUTER_API_KEY
```

Repository variables yang dibutuhkan:

```text
GIT_AUTHOR_NAME=kisnak21
GIT_AUTHOR_EMAIL=<alamat noreply GitHub>
```

Workflow memerlukan `Read and write permissions` pada **Settings > Actions > General > Workflow permissions**.

## Menjalankan secara lokal

Generator hanya menggunakan Python standard library.

```bash
python -m unittest discover -s tests -v
python -m scripts.generate_daily_note --offline --date 2026-09-20
python -m scripts.validate_repository
```

Mode `--offline` tidak menghubungi GitHub atau OpenRouter dan selalu menggunakan materi kurikulum lokal.
