"""
run_pipeline.py
Orquestra o pipeline completo:
  1. fetch_meta.py  → /tmp/meta_data.json
  2. fetch_rd.py    → /tmp/rd_data.json
  3. generate_dashboard.py → relatorio_abril_2026_boost.html

Executado pelo GitHub Actions toda segunda às 9h BRT (12h UTC).
"""
import os, sys, json, subprocess, shutil
from datetime import datetime

# ─── Configuração ─────────────────────────────────────────────
REPO_ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

now   = datetime.now()
MONTH = now.strftime('%B').lower()     # abril, maio...
YEAR  = now.strftime('%Y')            # 2026

# Meses em português para o nome do arquivo
MESES_PT = {
    'january': 'janeiro', 'february': 'fevereiro', 'march': 'marco',
    'april': 'abril', 'may': 'maio', 'june': 'junho',
    'july': 'julho', 'august': 'agosto', 'september': 'setembro',
    'october': 'outubro', 'november': 'novembro', 'december': 'dezembro'
}
MONTH_PT = MESES_PT.get(MONTH, MONTH)
OUTPUT_FILENAME = f'relatorio_{MONTH_PT}_{YEAR}_boost.html'
OUTPUT_PATH     = os.path.join(REPO_ROOT, OUTPUT_FILENAME)

# ─── Helpers ──────────────────────────────────────────────────
def step(msg):
    print(f'\n{"="*60}')
    print(f'  {msg}')
    print(f'{"="*60}')

def run_script(script_name):
    """Executa um script Python e retorna True se OK."""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False,
        text=True,
        env=os.environ
    )
    if result.returncode != 0:
        print(f'  ❌ {script_name} falhou (exit {result.returncode})', file=sys.stderr)
        return False
    return True

def check_json(path, required_keys):
    """Verifica se um JSON foi gerado com as chaves esperadas."""
    if not os.path.exists(path):
        print(f'  ❌ Arquivo não encontrado: {path}', file=sys.stderr)
        return False
    try:
        with open(path) as f:
            data = json.load(f)
        for k in required_keys:
            if k not in data:
                print(f'  ❌ Chave ausente no JSON: {k}', file=sys.stderr)
                return False
        print(f'  ✅ {os.path.basename(path)} OK')
        return True
    except Exception as e:
        print(f'  ❌ JSON inválido {path}: {e}', file=sys.stderr)
        return False

# ─── Pipeline ─────────────────────────────────────────────────
def main():
    print(f'\n🚀 Pipeline dashboard Boost Research')
    print(f'   Arquivo de saída: {OUTPUT_FILENAME}')
    print(f'   Data: {now.strftime("%d/%m/%Y %H:%M")}')

    # ── STEP 1: Meta Ads ─────────────────────────────────────
    step('STEP 1/3 — Buscando dados Meta Ads')
    if not run_script('fetch_meta.py'):
        sys.exit(1)
    if not check_json('/tmp/meta_data.json', ['campaigns', 'ads', 'weeks', 'groups']):
        sys.exit(1)

    # ── STEP 2: RD Station ───────────────────────────────────
    step('STEP 2/3 — Buscando leads RD Station')
    rd_ok = run_script('fetch_rd.py') and check_json('/tmp/rd_data.json', ['lp_mentoria_boost', 'lp_ir_cripto'])
    if not rd_ok:
        print('  ⚠️  RD Station falhou — dashboard será gerado sem dados de leads')
        # Cria JSON vazio para não travar o generate_dashboard.py
        empty_qual = {'total':0,'investe_cripto':0,'nao_cripto':0,'investe_trad':0,
                      'pat_cripto':{},'pat_trad':{},'qualif_cripto':0,'qualif_trad':0,'pct_qualif':0}
        with open('/tmp/rd_data.json', 'w') as f:
            json.dump({'lp_mentoria_boost': {'contacts': 0, 'qualification': empty_qual},
                       'lp_ir_cripto':      {'contacts': 0, 'qualification': empty_qual}}, f)

    # ── STEP 3: Gerar Dashboard ──────────────────────────────
    step('STEP 3/3 — Gerando dashboard HTML')

    # Passa o caminho de saída via variável de ambiente
    env = os.environ.copy()
    env['DASHBOARD_OUTPUT'] = OUTPUT_PATH
    env['DASHBOARD_MONTH']  = MONTH_PT
    env['DASHBOARD_YEAR']   = YEAR

    script_path = os.path.join(SCRIPTS_DIR, 'generate_dashboard.py')
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False,
        text=True,
        env=env
    )
    if result.returncode != 0:
        print(f'  ❌ generate_dashboard.py falhou', file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(OUTPUT_PATH):
        print(f'  ❌ HTML não foi gerado em: {OUTPUT_PATH}', file=sys.stderr)
        sys.exit(1)

    size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f'  ✅ Dashboard gerado: {OUTPUT_FILENAME} ({size_kb:.0f} KB)')

    # ── Sumário final ────────────────────────────────────────
    with open('/tmp/meta_data.json') as f:
        meta = json.load(f)
    with open('/tmp/rd_data.json') as f:
        rd = json.load(f)

    total_spend = sum(c['spend'] for c in meta['campaigns'])
    total_leads = sum(c['leads'] for c in meta['campaigns'])
    cpl_total   = round(total_spend / total_leads, 2) if total_leads else 0
    rd_leads    = rd['lp_mentoria_boost']['contacts']

    print(f'\n{"="*60}')
    print(f'  ✅ PIPELINE CONCLUÍDO')
    print(f'  📊 Meta Ads: R${total_spend:,.0f} · {total_leads} leads · CPL R${cpl_total}')
    print(f'  📋 RD Station (LP Análise): {rd_leads} leads')
    print(f'  🌐 Arquivo: {OUTPUT_PATH}')
    print(f'{"="*60}\n')

if __name__ == '__main__':
    main()
