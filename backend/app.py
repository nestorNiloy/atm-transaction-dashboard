"""
ATM Transaction Dashboard - REST API Backend
Built with Flask + Pandas
Endpoints: /api/kpis, /api/revenue, /api/transactions, /api/costs, /api/filter
"""

from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import json
import os

app = Flask(__name__)

# ── CORS headers (no flask-cors needed) ────────────────────────────────────
@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    return response

# ── Load & clean data once at startup ──────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df_raw = pd.read_excel(os.path.join(BASE_DIR, "BOB_Source.xlsx"))

NUM_COLS = [
    "AVG Total TXN", "GROSS PROFIT %", "Up Time", " EBILL ",
    "ATM Rev Total", "MHA Revenue", "Monthly Rev",
    "CRA", "UPS AMC", "ATM AMC", "VSAT AMC",
    "Site Maint\n (Non Asset)", "Spare Rep. (SLM)\n (AssetOEM)",
    " Total Cost  ", " Gross Profit ", "Fin Txn", "Non Fin Txn", "Monthly Txn",
]
for c in NUM_COLS:
    df_raw[c] = pd.to_numeric(df_raw[c], errors="coerce")

months_sorted = sorted(df_raw["Month"].unique())
MONTH_MAP = {months_sorted[0]: "Aug", months_sorted[1]: "Dec",
             months_sorted[2]: "Mar",  months_sorted[3]: "Nov"}
MONTH_ORDER = ["Mar", "Aug", "Nov", "Dec"]
df_raw["MonthName"] = df_raw["Month"].map(MONTH_MAP)

STATE_ORDER = ["Assam","Punjab","Jammu & Kashmir","Manipur","Tripura",
               "Nagaland","Meghalaya","Mizoram","Arunachal Pradesh","Ladakh","Sikkim"]

def safe(val):
    """Convert numpy types to Python native for JSON serialisation."""
    if pd.isna(val): return 0
    if isinstance(val, (np.integer,)): return int(val)
    if isinstance(val, (np.floating,)): return round(float(val), 2)
    return val

def filter_df(state=None, month=None, atm_type=None):
    df = df_raw.copy()
    if state and state != "All":
        df = df[df["STATE"] == state]
    if month and month != "All":
        df = df[df["MonthName"] == month]
    if atm_type and atm_type != "All":
        df = df[df["ATM TYPE"] == atm_type]
    return df


# ── API Routes ──────────────────────────────────────────────────────────────

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "rows": len(df_raw), "states": len(STATE_ORDER)})


@app.route("/api/kpis")
def kpis():
    """Top KPI cards: total cost, avg TXN, gross profit %, uptime, EBILL."""
    state  = request.args.get("state")
    month  = request.args.get("month")
    atm    = request.args.get("atm_type")
    df = filter_df(state, month, atm)

    return jsonify({
        "total_cost":       safe(df[" Total Cost  "].sum()),
        "avg_txn":          safe(df["AVG Total TXN"].mean()),
        "gross_profit_pct": safe(df["GROSS PROFIT %"].dropna().mean() * 100),
        "avg_uptime":       safe(df["Up Time"].dropna().mean() * 100),
        "avg_ebill":        safe(df[" EBILL "].dropna().mean()),
        "total_atms":       int(df["ATM id"].nunique()),
        "total_gross_profit": safe(df[" Gross Profit "].sum()),
    })


@app.route("/api/revenue")
def revenue():
    """Revenue by state (ATM Rev, MHA Rev, Monthly Rev) + summary totals."""
    state = request.args.get("state")
    month = request.args.get("month")
    df = filter_df(state, month)

    by_state = []
    for s in STATE_ORDER:
        sub = df[df["STATE"] == s]
        if len(sub) == 0:
            continue
        by_state.append({
            "state":       s,
            "atm_rev":     safe(sub["ATM Rev Total"].sum()),
            "mha_rev":     safe(sub["MHA Revenue"].sum()),
            "monthly_rev": safe(sub["Monthly Rev"].sum()),
        })

    return jsonify({
        "by_state": by_state,
        "totals": {
            "atm":     safe(df["ATM Rev Total"].sum()),
            "mha":     safe(df["MHA Revenue"].sum()),
            "monthly": safe(df["Monthly Rev"].sum()),
        }
    })


@app.route("/api/transactions")
def transactions():
    """Fin vs Non-Fin TXN by month + date-level trend."""
    state = request.args.get("state")
    df = filter_df(state)

    by_month = []
    for m in MONTH_ORDER:
        sub = df[df["MonthName"] == m]
        by_month.append({
            "month":   m,
            "fin":     safe(sub["Fin Txn"].sum()),
            "non_fin": safe(sub["Non Fin Txn"].sum()),
            "total":   safe(sub["Monthly Txn"].sum()),
        })

    return jsonify({"by_month": by_month})


@app.route("/api/costs")
def costs():
    """Cost breakdown by category + cost vs revenue by month."""
    state = request.args.get("state")
    month = request.args.get("month")
    df = filter_df(state, month)

    breakdown = {
        "CRA":        safe(df["CRA"].sum()),
        "ATM AMC":    safe(df["ATM AMC"].sum()),
        "Site Maint": safe(df["Site Maint\n (Non Asset)"].sum()),
        "Spare Rep":  safe(df["Spare Rep. (SLM)\n (AssetOEM)"].sum()),
        "UPS AMC":    safe(df["UPS AMC"].sum()),
        "VSAT AMC":   safe(df["VSAT AMC"].sum()),
    }

    by_month = []
    for m in MONTH_ORDER:
        sub = df_raw[df_raw["MonthName"] == m]  # always full dataset for trend
        by_month.append({
            "month":   m,
            "cost":    safe(sub[" Total Cost  "].sum()),
            "revenue": safe(sub["ATM Rev Total"].sum()),
            "profit":  safe(sub[" Gross Profit "].sum()),
        })

    return jsonify({"breakdown": breakdown, "by_month": by_month})


@app.route("/api/filters")
def filters():
    """Available filter options for dropdowns."""
    return jsonify({
        "states":    ["All"] + STATE_ORDER,
        "months":    ["All"] + MONTH_ORDER,
        "atm_types": ["All"] + sorted(df_raw["ATM TYPE"].dropna().unique().tolist()),
    })


@app.route("/api/atms")
def atms():
    """Top/bottom performing ATMs by gross profit (paginated)."""
    state  = request.args.get("state")
    month  = request.args.get("month")
    sort   = request.args.get("sort", "desc")   # asc | desc
    limit  = int(request.args.get("limit", 10))

    df = filter_df(state, month)
    grp = (df.groupby("ATM id")
             .agg(state=("STATE","first"),
                  total_cost=(" Total Cost  ","sum"),
                  gross_profit=(" Gross Profit ","sum"),
                  gross_pct=("GROSS PROFIT %","mean"),
                  avg_txn=("AVG Total TXN","mean"))
             .reset_index())
    grp = grp.sort_values("gross_profit", ascending=(sort == "asc")).head(limit)

    records = []
    for _, row in grp.iterrows():
        records.append({
            "atm_id":       row["ATM id"].strip(),
            "state":        row["state"],
            "total_cost":   safe(row["total_cost"]),
            "gross_profit": safe(row["gross_profit"]),
            "gross_pct":    safe(row["gross_pct"] * 100),
            "avg_txn":      safe(row["avg_txn"]),
        })
    return jsonify({"atms": records})


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print(f"🚀 ATM Dashboard API running on port {port}")
    print("   Endpoints: /api/health /api/kpis /api/revenue /api/transactions /api/costs /api/filters /api/atms")

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
