<?php
// Koneksi ke database
$host = "localhost";
$user = "root"; // sesuaikan username MySQL
$pass = "";     // sesuaikan password MySQL
$db   = "web_kelas";

$conn = new mysqli($host, $user, $pass, $db);

// Cek koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}

// Ambil data pengumuman dari database
$sql = "SELECT * FROM pengumuman ORDER BY tanggal DESC";
$result = $conn->query($sql);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X-2 Jaya</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<header>
    <div class="container">
        <h1>X-2</h1>
        <p>Tahun ajaran 2025/2026</p>
    </div>
    <nav>
        <div class="container">
            <ul>
                <li><a href="index.php">Beranda</a></li>
                <li><a href="struktur.html">Struktur Kelas</a></li>
                <li><a href="galeri.html">Galeri Kelas</a></li>
            </ul>
        </div>
    </nav>
</header>

<main class="container">
    <section id="beranda">
        <h1>Selamat datang, Sugeng Rawuh, wilujeng</h1>
        <p>Ini adalah website Kelas jika web ini error bisa menghubungi Adnan ataupun Dzikru</p>
        
        <div class="Pengumuman">
            <h2>Pengumuman Kelas</h2>
            <table>
                <thead>
                    <tr>
                        <th>Tanggal</th>
                        <th>Judul</th>
                        <th>Isi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if ($result->num_rows > 0): ?>
                        <?php while($row = $result->fetch_assoc()): ?>
                            <tr>
                                <td><?= date("d-m-Y", strtotime($row['tanggal'])) ?></td>
                                <td><?= htmlspecialchars($row['judul']) ?></td>
                                <td><?= nl2br(htmlspecialchars($row['isi'])) ?></td>
                            </tr>
                        <?php endwhile; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="3">Belum ada pengumuman</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </section>
</main>

<footer class="footer">
    <p>Author: Adnan Hafidz<br>
        <a href="mailto:juraganadnan99@gmail.com">juraganadnan99@gmail.com</a>
    </p>
</footer>
</body>
</html>
<?php $conn->close(); ?>
