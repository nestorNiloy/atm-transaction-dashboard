# ATM Transaction Dashboard 🏧

A full-stack analytics dashboard for Bank of Baroda ATM operations across Northeast India.

## Tech Stack
- **Backend**: Python + Flask REST API (7 endpoints)
- **Frontend**: Vanilla HTML/CSS/JS + Chart.js
- **Data**: BOB_Source.xlsx (11,076 rows · 11 states · 2,790 ATMs)

## Project Structure
```
atm-dashboard/
├── backend/
│   ├── app.py              ← Flask REST API
│   ├── BOB_Source.xlsx     ← Source data
│   └── requirements.txt
└── frontend/
    └── index.html          ← Dashboard UI
```

## Quick Start

### 1. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the API server
```bash
python app.py
# → Running at http://localhost:5000
```

### 3. Open the dashboard
Open `frontend/index.html` in your browser.  
The dashboard auto-detects the API and falls back to static data if it's not running.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server health + row count |
| GET | `/api/kpis` | KPI cards (cost, profit %, uptime…) |
| GET | `/api/revenue` | Revenue by state (ATM / MHA / Monthly) |
| GET | `/api/transactions` | Fin vs Non-Fin TXN by month |
| GET | `/api/costs` | Cost breakdown + monthly trend |
| GET | `/api/filters` | Available filter options |
| GET | `/api/atms` | Top/bottom ATMs by profit |

### Query Parameters (all endpoints)
- `state` — filter by state name (e.g. `?state=Assam`)
- `month` — filter by month (e.g. `?month=Aug`)
- `atm_type` — filter by ATM type (`Regular`, `Captive`…)
- `sort` — for `/api/atms`: `desc` (top) or `asc` (bottom)
- `limit` — for `/api/atms`: number of results (default 10)

### Example
```bash
curl "http://localhost:5000/api/kpis?state=Assam&month=Aug"
curl "http://localhost:5000/api/atms?sort=desc&limit=5"
```

## Dashboard Features
- **5 KPI cards**: Total Cost, Avg TXN, Gross Profit %, Avg Uptime, Avg EBILL
- **Cost donut charts**: Breakdown by CRA, AMC, Site Maint, Spare Rep, UPS, VSAT
- **Revenue by state**: Grouped bar chart for ATM/MHA/Monthly revenue
- **Txn by month**: Fin vs Non-Fin transaction comparison
- **Revenue vs Cost trend**: Line chart across months
- **ATM leaderboard**: Top/Bottom 10 ATMs by gross profit with live filters
- **Detail page**: Horizontal state breakdown, cost pie, txn trend
- **Live filters**: State, ATM type, and month filters update all charts

## For Your CV
- **REST API design** with proper resource naming, query parameters, and error handling
- **Data pipeline**: Raw Excel → Pandas cleaning → JSON API → Chart.js visualization
- **Full-stack separation**: Backend API + Frontend independently deployable
- **Production patterns**: CORS headers, data loading at startup, graceful fallback
- **Real dataset**: 11,076 records, 53 columns, multi-dimensional filtering

## Deployment (optional)
- Backend → Deploy to Railway, Render, or any Python host
- Frontend → Deploy to GitHub Pages, Netlify, or Vercel
- Update `API_BASE` in `index.html` to your deployed backend URL
