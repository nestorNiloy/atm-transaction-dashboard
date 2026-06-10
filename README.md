# 🏧 ATM Transaction Dashboard

<div align="center">

**A full-stack analytics dashboard for Bank of Baroda ATM operations across Northeast India**

[![Live Dashboard](https://img.shields.io/badge/🚀%20Live%20Dashboard-GitHub%20Pages-2ea44f?style=for-the-badge)](https://nestorniloy.github.io/atm-transaction-dashboard/Web%20dashboard/atm-dashboard.html)
[![Live API](https://img.shields.io/badge/⚙️%20Live%20API-Render-4fc3f7?style=for-the-badge)](https://atm-dashboard-api.onrender.com)
[![GitHub](https://img.shields.io/badge/Source%20Code-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/nestorNiloy/atm-transaction-dashboard)

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat-square&logo=flask&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=flat-square&logo=chart.js&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat-square&logo=pandas&logoColor=white)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=flat-square)
![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub%20Pages-222222?style=flat-square&logo=github)

</div>

---

![ATM Dashboard Demo](demo.gif)

---

## 📌 Overview

This project visualises ATM performance data across **11 states in Northeast India**, covering **2,790 ATMs** and **11,076 transaction records** from FY 2024.

The frontend is hosted on **GitHub Pages** and talks to a **Flask REST API** deployed on **Render** — a fully decoupled, production-style architecture.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      User's Browser                      │
│              GitHub Pages (HTML/CSS/JS)                  │
└──────────────────────────┬──────────────────────────────┘
                           │  HTTP requests
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Flask REST API · Render.com                 │
│         atm-dashboard-api.onrender.com/api/*             │
└──────────────────────────┬──────────────────────────────┘
                           │  Pandas reads
                           ▼
                  BOB_Source.xlsx
               (11,076 rows · 53 columns)
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 KPI Cards | Total Cost, Avg TXN, Gross Profit %, Avg Uptime, Avg EBILL |
| 🍩 Cost Donuts | Breakdown by CRA, AMC, Site Maintenance, Spare Rep, UPS, VSAT |
| 🗺️ Revenue by State | Grouped bar chart across 11 states |
| 📈 Trend Analysis | Revenue vs Cost multi-line chart by month |
| 🔁 Txn Comparison | Financial vs Non-Financial transactions by month |
| 🏆 ATM Leaderboard | Top / Bottom 10 ATMs by gross profit |
| 🔍 Live Filters | State, ATM type, and month — updates all charts simultaneously |
| 📱 Detail Page | Horizontal state breakdown, cost pie, transaction trend |
| ⚡ Smart Fallback | Works in static mode if backend is offline |

---

## 🌐 Live Links

| | URL |
|--|-----|
| 📊 **Dashboard** | [nestorniloy.github.io/.../atm-dashboard.html](https://nestorniloy.github.io/atm-transaction-dashboard/Web%20dashboard/atm-dashboard.html) |
| ⚙️ **API Root** | [atm-dashboard-api.onrender.com](https://atm-dashboard-api.onrender.com) |
| 📡 **API Health** | [atm-dashboard-api.onrender.com/api/health](https://atm-dashboard-api.onrender.com/api/health) |

---

## ⚙️ API Reference

Base URL: `https://atm-dashboard-api.onrender.com`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | API documentation and metadata |
| `GET` | `/api/health` | Server status and row count |
| `GET` | `/api/kpis` | KPI metrics — cost, profit %, uptime |
| `GET` | `/api/revenue` | Revenue by state — ATM, MHA, Monthly |
| `GET` | `/api/transactions` | Fin vs Non-Fin transactions by month |
| `GET` | `/api/costs` | Cost breakdown and monthly trend |
| `GET` | `/api/filters` | Available filter options |
| `GET` | `/api/atms` | Top / bottom ATMs ranked by gross profit |

### Query Parameters
All endpoints accept:
```
?state=Assam          # Filter by state
?month=Aug            # Filter by month (Mar, Aug, Nov, Dec)
?atm_type=Regular     # Filter by ATM type
```

### Example Requests
```bash
# Get KPIs for Assam in August
curl "https://atm-dashboard-api.onrender.com/api/kpis?state=Assam&month=Aug"

# Get top 5 performing ATMs
curl "https://atm-dashboard-api.onrender.com/api/atms?sort=desc&limit=5"

# Get revenue breakdown for all states
curl "https://atm-dashboard-api.onrender.com/api/revenue"
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/nestorNiloy/atm-transaction-dashboard.git
cd atm-transaction-dashboard

# 2. Install backend dependencies
cd backend
pip install -r requirements.txt

# 3. Start the API server
py app.py
# → Running at http://localhost:5000

# 4. Open the dashboard
# Open "Web dashboard/atm-dashboard.html" in your browser
```

---

## 📁 Project Structure

```
atm-transaction-dashboard/
├── Web dashboard/
│   └── atm-dashboard.html      ← Frontend UI
├── backend/
│   ├── app.py                  ← Flask REST API (7 endpoints)
│   ├── BOB_Source.xlsx         ← Source dataset
│   └── requirements.txt        ← Python dependencies
├── demo.gif                    ← Dashboard demo
├── Dashboard screenshot.png    ← Static screenshot
└── README.md
```

---

## 📊 Dataset

- **Source:** Bank of Baroda ATM operations, FY 2024
- **Records:** 11,076 rows × 53 columns
- **ATMs:** 2,790 unique machines
- **States:** Assam, Punjab, Jammu & Kashmir, Manipur, Tripura, Nagaland, Meghalaya, Mizoram, Arunachal Pradesh, Ladakh, Sikkim
- **Metrics:** Transaction volumes, revenue streams, cost categories, uptime, gross profit

---

<div align="center">

Built by [@nestorNiloy](https://github.com/nestorNiloy)

</div>
