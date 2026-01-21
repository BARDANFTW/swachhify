<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Swachhify | Environmental Monitoring Dashboard</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="swachhify_logo.png">

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<!-- Leaflet -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css">
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<style>
:root{
  --primary:#B6D83D;
  --accent:#3c8c18;
  --dark:#1c1c1c;
  --glass:rgba(255,255,255,0.7);
}

*{box-sizing:border-box}
body{margin:0;font-family:'Poppins',sans-serif;background:var(--primary);color:var(--dark);overflow-x:hidden}

/* ---------- HEADER ---------- */
header{text-align:center;padding:50px 20px;animation:dropIn 1s ease}
header img{width:140px;animation:floatLogo 4s ease-in-out infinite}
.slogan{margin-top:12px;font-size:1.4rem;font-weight:600;letter-spacing:6px;color:white}

/* ---------- SECTIONS ---------- */
section{width:95%;max-width:1250px;margin:40px auto;padding:28px;background:var(--glass);border-radius:18px;box-shadow:0 10px 22px rgba(0,0,0,0.18);backdrop-filter:blur(8px);opacity:0;transform:translateY(40px);transition:all 0.9s ease}
section.show{opacity:1;transform:translateY(0)}
h2{color:var(--accent);margin-bottom:18px;position:relative}
h2::after{content:'';position:absolute;left:0;bottom:-6px;width:70px;height:3px;background:var(--accent)}

/* ---------- LOCATION GRID ---------- */
.location-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:25px}
.location-info{display:grid;grid-template-columns:1fr;gap:15px}
.stat-card{padding:16px;border-radius:14px;background:rgba(255,255,255,0.85);box-shadow:0 6px 14px rgba(0,0,0,0.12);animation:fadeScale 0.9s ease}
.stat-title{font-size:0.9rem;opacity:0.7}
.stat-value{font-size:1.2rem;font-weight:600;margin-top:4px}

/* ---------- MAP ---------- */
#map{height:360px;border-radius:14px;animation:mapEnter 1.1s ease forwards;animation-delay:0.3s;opacity:0}

/* ---------- LIVE DATA ---------- */
.pulse{animation:pulseGlow 1.6s infinite;font-weight:600}

/* ---------- BUTTON ---------- */
button{padding:12px 26px;border:none;border-radius:12px;background:var(--accent);color:white;font-size:1rem;cursor:pointer;transition:all 0.25s ease}
button:hover{transform:translateY(-2px);box-shadow:0 8px 18px rgba(0,0,0,0.25)}

/* ---------- TABLES ---------- */
table{width:100%;border-collapse:collapse;margin-top:18px;font-size:0.95rem;animation:fadeScale 1s ease}
th,td{border:1px solid black;padding:10px}
th{background:var(--accent);color:black}

/* ---------- FOOTER ---------- */
footer{text-align:center;padding:30px;font-size:0.85rem;opacity:0.85}

/* ---------- ANIMATIONS ---------- */
@keyframes dropIn{from{opacity:0;transform:translateY(-30px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatLogo{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes fadeScale{from{opacity:0;transform:scale(0.95)}to{opacity:1;transform:scale(1)}}
@keyframes mapEnter{from{opacity:0;transform:scale(0.96)}to{opacity:1;transform:scale(1)}}
@keyframes pulseGlow{0%{text-shadow:0 0 0 rgba(60,140,24,0.6)}50%{text-shadow:0 0 14px rgba(60,140,24,0.9)}100%{text-shadow:0 0 0 rgba(60,140,24,0.6)}}

/* ---------- RESPONSIVE ---------- */
@media(max-width:900px){.location-grid{grid-template-columns:1fr}#map{height:300px}.slogan{font-size:1.1rem;letter-spacing:3px}}
</style>
</head>

<body>
<header>
  <img src="swachhify_logo.png" alt="Swachhify Logo">
  <div class="slogan">SENSE MORE · LIVE BETTER</div>
</header>

<section class="reveal">
  <h2>Location & Light Pollution Analysis</h2>
  <div class="location-grid">
    <div class="location-info">
      <div class="stat-card">
        <div class="stat-title">Coordinates</div>
        <div class="stat-value" id="coords">Detecting…</div>
      </div>
      <div class="stat-card">
        <div class="stat-title">Bortle Class</div>
        <div class="stat-value" id="bortle">Estimating…</div>
      </div>
      <div class="stat-card">
        <div class="stat-title">Estimation Method</div>
        <div class="stat-value">Satellite Ligh
