# Introduction to Graph Theory

Repositori ini menyajikan implementasi dasar teori graf dengan fokus pada dua kelompok permasalahan utama:

1. Menentukan jalur terpendek (shortest path).
2. Menentukan pohon merentang minimum (minimum spanning tree/MST).

Selain implementasi kode, materi pada repositori ini menekankan pemahaman konsep, perbandingan antaralgoritma, serta konteks penggunaan yang tepat.

## Gambaran Materi

Contoh graf berbobot yang digunakan sebagai dasar pembahasan:

![Contoh Graf](assets/image.png)

Visualisasi tambahan untuk algoritma shortest path dan traversal dapat dilihat pada aset GIF di folder assets.

## Representasi Graf

Materi menggunakan graf berbobot dengan representasi adjacency list sebagai struktur utama. Representasi ini efisien untuk graf sparse karena hanya menyimpan sisi yang benar-benar tersedia.

Sebagai pelengkap, repositori ini juga menampilkan konversi ke adjacency matrix untuk memudahkan analisis pada kasus tertentu, terutama ketika dibutuhkan akses bobot antarpasangan node secara langsung.

## Algoritma Minimum Spanning Tree

### Kruskal's Algorithm

Kruskal merupakan algoritma greedy yang membangun MST dengan memilih sisi berbobot terkecil secara bertahap, selama sisi tersebut tidak membentuk siklus.

Ringkasan cara kerja:

1. Urutkan semua sisi berdasarkan bobot dari kecil ke besar.
2. Ambil sisi satu per satu.
3. Tambahkan sisi ke MST hanya jika tidak membentuk siklus.
4. Berhenti saat jumlah sisi pada MST mencapai jumlah node dikurangi satu.

Kelebihan:

- Sederhana dan andal untuk berbagai jenis graf tak berarah berbobot.
- Sangat baik ketika data sisi tersedia dalam bentuk edge list.

Keterbatasan:

- Membutuhkan proses pengurutan sisi pada tahap awal.
- Untuk graf sangat padat, ukuran edge list bisa besar.

Kapan digunakan:

- Saat fokus pada pemilihan sisi minimum secara global.
- Saat struktur data union-find tersedia untuk deteksi siklus yang efisien.

### Prim's Algorithm

Prim juga merupakan algoritma greedy, tetapi dengan pendekatan berbeda: MST dibangun dari satu node awal, kemudian diperluas ke node lain melalui sisi termurah yang menghubungkan node di dalam tree ke node di luar tree.

Ringkasan cara kerja:

1. Pilih node awal.
2. Masukkan sisi-sisi kandidat ke priority queue.
3. Ambil sisi dengan bobot minimum yang valid.
4. Tambahkan node baru ke MST dan ulangi hingga semua node tercakup.

Kelebihan:

- Efektif untuk graf yang direpresentasikan sebagai adjacency list.
- Cocok dipadukan dengan priority queue sehingga proses pemilihan sisi menjadi cepat.

Keterbatasan:

- Pemilihan node awal dapat memengaruhi urutan pembentukan tree.
- Tetap membutuhkan pengelolaan struktur data yang baik agar efisien.

Kapan digunakan:

- Saat ingin membangun MST secara bertahap dari satu titik awal.
- Saat graf disimpan sebagai adjacency list dan ingin memanfaatkan heap.

## Algoritma Shortest Path

### Dijkstra's Algorithm

Dijkstra digunakan untuk mencari jarak terpendek dari satu node sumber ke seluruh node lain pada graf berbobot non-negatif.

Ringkasan cara kerja:

1. Inisialisasi jarak semua node sebagai tak hingga, kecuali node awal bernilai nol.
2. Gunakan priority queue untuk selalu memproses node dengan jarak sementara terkecil.
3. Lakukan relaksasi ke tetangga: perbarui jarak jika ditemukan jalur yang lebih pendek.
4. Ulangi hingga semua node relevan diproses.

Kelebihan:

- Cepat dan stabil untuk graf tanpa bobot negatif.
- Menjadi acuan dasar yang penting dalam studi shortest path.

Keterbatasan:

- Tidak valid untuk graf dengan bobot negatif.

Kapan digunakan:

- Saat semua bobot sisi bernilai nol atau positif.
- Saat membutuhkan jarak terpendek dari satu sumber.

### A* Algorithm

A* memperluas gagasan Dijkstra dengan menambahkan komponen heuristik agar pencarian menuju goal menjadi lebih terarah.

Konsep nilai pada A*:

- g(n): biaya aktual dari start ke node n.
- h(n): estimasi biaya dari node n ke goal.
- f(n) = g(n) + h(n): prioritas pemrosesan node.

Kelebihan:

- Dapat lebih cepat daripada Dijkstra jika fungsi heuristik baik.
- Sangat populer pada pathfinding (misalnya game dan navigasi).

Keterbatasan:

- Kualitas hasil dan efisiensi sangat dipengaruhi kualitas heuristik.
- Tidak cocok untuk bobot negatif.

Kapan digunakan:

- Saat memiliki goal spesifik.
- Saat tersedia heuristik yang cukup akurat seperti Manhattan atau Euclidean.

![A Star](assets/gif2.gif)

### Bellman-Ford Algorithm

Bellman-Ford menghitung shortest path dari satu sumber dan mampu menangani bobot negatif, selama tidak terdapat negative cycle yang dapat dicapai dari sumber.

Ringkasan cara kerja:

1. Inisialisasi jarak seperti Dijkstra.
2. Lakukan relaksasi semua sisi sebanyak jumlah node dikurangi satu putaran.
3. Lakukan satu putaran tambahan untuk mendeteksi negative cycle.

Kelebihan:

- Dapat menangani bobot negatif.
- Dapat mendeteksi keberadaan negative cycle.

Keterbatasan:

- Umumnya lebih lambat dibanding Dijkstra pada graf tanpa bobot negatif.

Kapan digunakan:

- Saat graf mungkin memiliki bobot negatif.
- Saat deteksi negative cycle diperlukan.

![Bellman Ford](assets/bf.gif)

### Floyd-Warshall Algorithm

Floyd-Warshall merupakan algoritma dynamic programming untuk mencari shortest path seluruh pasangan node sekaligus (all-pairs shortest paths).

Ringkasan cara kerja:

1. Bentuk matriks jarak awal berdasarkan bobot sisi langsung.
2. Pertimbangkan setiap node sebagai perantara secara bertahap.
3. Perbarui jarak jika lintasan lewat node perantara lebih pendek.

Kelebihan:

- Memberikan jarak terpendek antar semua pasangan node dalam satu eksekusi.
- Dapat digunakan pada graf dengan bobot negatif tanpa negative cycle.

Keterbatasan:

- Kompleksitas waktu tinggi, kurang cocok untuk graf sangat besar.

Kapan digunakan:

- Saat dibutuhkan informasi jarak untuk seluruh pasangan node.
- Saat ukuran graf masih cukup kecil hingga menengah.

![Floyd Warshall](assets/fw.gif)

## Konsep Pendukung

### Priority Queue dan Heap

Implementasi menggunakan struktur heap melalui modul heapq untuk memilih kandidat node atau sisi dengan bobot minimum secara efisien. Konsep ini sangat penting pada Dijkstra, A*, dan Prim.

### Heuristic Function

Pada A*, heuristik digunakan untuk memperkirakan biaya menuju goal. Repositori ini mencontohkan heuristik zero, Manhattan, dan Euclidean untuk menunjukkan pengaruhnya terhadap arah pencarian.

### Bobot Negatif dan Negative Cycle

Materi ini juga menekankan bahwa tidak semua algoritma cocok untuk bobot negatif. Dijkstra dan A* tidak dirancang untuk kondisi tersebut, sedangkan Bellman-Ford dan Floyd-Warshall dapat digunakan dengan catatan tidak ada negative cycle yang merusak validitas solusi shortest path.

## Catatan

Seluruh implementasi dan contoh penggunaan dapat dipelajari pada notebook modul-tutorial-2.ipynb serta berkas kode Python pada folder graph.
