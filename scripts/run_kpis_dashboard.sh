#!/bin/bash
# run_kpis_dashboard.sh — Wrapper para executar generate_kpis_dashboard.py
# Carrega .env e roda o script Python.
# Uso: crontab executa toda segunda 23:59

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
ENV_FILE="$PROJECT_DIR/.env"
LOG_FILE="$SCRIPT_DIR/../painel/metas-kpis/last_run.log"

# Carregar .env
if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' "$ENV_FILE" | grep -v '^$' | xargs)
fi

# Rodar script
python3 "$SCRIPT_DIR/generate_kpis_dashboard.py" > "$LOG_FILE" 2>&1

echo "$(date '+%Y-%m-%d %H:%M') — Dashboard KPIs atualizado" >> "$LOG_FILE"
