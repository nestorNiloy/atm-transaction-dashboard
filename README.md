# ATM Transaction Dashboard 🏧

A full-stack analytics dashboard for Bank of Baroda ATM operations across Northeast India — built with a Python Flask REST API backend and a Chart.js frontend.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://nestorniloy.github.io/atm-transaction-dashboard/Web%20dashboard/atm-dashboard.html)
[![Python](https://img.shields.io/badge/Python-3.13-yellow?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-pink?style=for-the-badge&logo=chart.js)](https://chartjs.org)

---

![ATM Transaction Dashboard Screenshot](Dashboard%20screenshot.png)

---

## Overview

This dashboard visualises ATM performance data across **11 states in Northeast India**, covering **2,790 ATMs** and **11,076 transaction records** from FY 2024. It includes live filtering by state, month, and ATM type — all powered by a REST API backend.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Data processing | Pandas |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js 4.4 |
| Data source | Excel (BOB_Source.xlsx) |
| Hosting | GitHub Pages (frontend) |

## Features

- **5 KPI cards** — Total Cost, Avg TXN, Gross Profit %, Avg Uptime, Avg EBILL
- **Cost breakdown** — Donut charts by CRA, AMC, Site Maintenance, Spare Replacement, UPS, VSAT
- **Revenue by state** — Grouped bar chart for ATM / MHA / Monthly revenue across 11 states
- **Transaction trends** — Financial vs Non-Financial TXN comparison by month
- **Revenue vs Cost trend** — Multi-line chart across months
- **ATM leaderboard** — Top / Bottom 10 ATMs ranked by gross profit
- **Detail page** — Horizontal state breakdown, cost pie chart, transaction trend
- **Live filters** — State, ATM type, and month filters update all charts simultaneously
- **Graceful fallback** — Works in static mode if the backend is not running

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server status and row count |
| GET | `/api/kpis` | KPI metrics (cost, profit %, uptime) |
| GET | `/api/revenue` | Revenue by state — ATM, MHA, Monthly |
| GET | `/api/transactions` | Fin vs Non-Fin transactions by month |
| GET | `/api/costs` | Cost breakdown and monthly trend |
| GET | `/api/filters` | Available filter options |
| GET | `/api/atms` | Top / bottom ATMs by gross profit |

All endpoints support query parameters: `?state=Assam&month=Aug&atm_type=Regular`

## Project Structure

```
atm-transaction-dashboard/
├── Web dashboard/
│   └── atm-dashboard.html      ← Frontend (open in browser)
├── backend/
│   ├── app.py                  ← Flask REST API
│   ├── BOB_Source.xlsx         ← Source dataset
│   └── requirements.txt
├── Dashboard screenshot.png
└── README.md
```

## Run Locally

```bash
# 1. Install backend dependencies
cd backend
pip install -r requirements.txt

# 2. Start the API server
py app.py
# → Running at http://localhost:5000

# 3. Open the dashboard
# Double-click Web dashboard/atm-dashboard.html in your file explorer
```

The dashboard auto-detects the API. When the backend is running, all filters query live data. When it's off, the dashboard loads pre-computed static data.

## Dataset

- **Source:** Bank of Baroda ATM operations data, FY 2024
- **Records:** 11,076 rows × 53 columns
- **Coverage:** 11 states — Assam, Punjab, Jammu & Kashmir, Manipur, Tripura, Nagaland, Meghalaya, Mizoram, Arunachal Pradesh, Ladakh, Sikkim
- **ATMs:** 2,790 unique machines
- **Metrics:** Transaction volumes, revenue streams, cost categories, uptime, gross profit

---

> Built by [@nestorNiloy](https://github.com/nestorNiloy)
