<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fantovex HQ | Play Beyond Limits</title>
  <style>

       
    :root {
      --bg: #050505;
      --card-bg: #0D0D0D;
      --border: #1A1A1A;
      --emerald: #00FF87;
      --white: #FFFFFF;
      --silver: #A0A0A0;
    }


    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      color: var(--white);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      padding: 16px;
      line-height: 1.5;
    }

    .container { max-width: 600px; margin: 0 auto; }

    /* Hero Section */
      
    .hero {
      text-align: center;
      padding: 36px 16px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: linear-gradient(180deg, #0A0A0A 0%, #050505 100%);
      margin-bottom: 24px;
    }

                                  }
    .brand-title {
      font-size: 2.2rem;
      font-weight: 900;
      letter-spacing: 2px;
      color: var(--white);
    }

    .brand-title span { color: var(--emerald); }

    .tagline {
      color: var(--emerald);
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 4px;
      margin-top: 6px;
      text-transform: uppercase;
    }

    .subtitle {
      color: var(--silver);
      font-size: 0.9rem;
      margin-top: 12px;
    }

    .btn-primary {
      display: inline-block;
      background-color: var(--emerald);
      color: #050505;
      font-weight: 800;
      font-size: 0.95rem;
      text-decoration: none;
      padding: 14px 28px;
      border-radius: 8px;
      margin-top: 20px;
      box-shadow: 0 0 18px rgba(0, 255, 135, 0.35);
      width: 100%;
      text-align: center;
    }

    /* Sections */
    .section-header {
      font-size: 1rem;
      font-weight: 800;
      color: var(--emerald);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin: 24px 0 12px 0;
      border-left: 3px solid var(--emerald);
      padding-left: 10px;
    }

    .card {
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 12px;
    }

    /* Schedule Table */
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
    th { text-align: left; color: var(--silver); padding-bottom: 8px; font-weight: 600; }
    td { padding: 10px 0; border-top: 1px solid var(--border); color: var(--white); }
    .slot-status { color: var(--emerald); font-weight: 700; }

    /* Rules List */
    ul { list-style: none; padding: 0; font-size: 0.88rem; }
    li { position: relative; padding-left: 20px; margin-bottom: 8px; color: var(--silver); }
    li::before { content: "•"; color: var(--emerald); font-weight: bold; position: absolute; left: 0; }

    .footer {
      text-align: center;
      color: var(--silver);
      font-size: 0.75rem;
      margin-top: 40px;
      padding-bottom: 20px;
    }
        .brand-logo {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin-bottom: 20px;
  </style>
</head>
<body>

  <div class="container">
    <!-- Hero -->
    <div class="hero">
      
      <img src="logo.png" alt="VOLTRIX"
                 class="brand-logo">
   

      <div class="brand-title">FANTOVEX <span>HQ</span></div>
      <div class="tagline">PLAY BEYOND LIMITS</div>
      <p class="subtitle">Grassroots Mobile Esports & Daily Scrims Arena</p>
      <a href="https://t.me/FantovexHQ" class="btn-primary">BOOK SCRIM SLOT ON TELEGRAM</a>
    </div>

    <!-- Scrim Schedule -->
    <div class="section-header">Daily Scrim Schedule</div>
    <div class="card">
      <table>
        <thead>
          <tr>
            <th>Match</th>
            <th>Time</th>
            <th>Slots</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Match 1 (Squad)</td>
            <td>04:00 PM IST</td>
            <td class="slot-status">OPEN</td>
          </tr>
          <tr>
            <td>Match 2 (Squad)</td>
            <td>07:00 PM IST</td>
            <td class="slot-status">OPEN</td>
          </tr>
          <tr>
            <td>Match 3 (Night Scrim)</td>
            <td>09:30 PM IST</td>
            <td class="slot-status">OPEN</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Quick Rules -->
    <div class="section-header">Match Rules</div>
    <div class="card">
      <ul>
        <li>Room ID & Password shared 15 minutes before match on Telegram.</li>
        <li>Emulators and hacks result in an immediate permanent ban.</li>
        <li>Must register full squad details via Google Form/Telegram.</li>
      </ul>
    </div>

    <div class="footer">
      © Fantovex HQ • PLAY BEYOND LIMITS
    </div>
  </div>

</body>
</html>
