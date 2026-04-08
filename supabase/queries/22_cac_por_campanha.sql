-- ============================================================
-- CAC POR CAMPANHA — Custo real por deal fechado
-- ============================================================
-- Cruza gasto Meta × deals ganhos no CRM
-- Requer: tabelas campaigns + ads populadas (sync Meta Ads)

WITH campaign_deals AS (
  SELECT
    l.first_campaign AS campanha_name,
    COUNT(DISTINCT l.id) AS leads_totais,
    COUNT(DISTINCT l.id) FILTER (WHERE l.is_qualified) AS leads_qualificados,
    COUNT(DISTINCT d.id) AS deals_totais,
    COUNT(DISTINCT d.id) FILTER (WHERE d.deal_status = 'won') AS deals_ganhos,
    COALESCE(SUM(d.amount_total) FILTER (WHERE d.deal_status = 'won'), 0) AS receita
  FROM leads l
  LEFT JOIN deals d ON d.lead_id = l.id
  WHERE l.first_campaign IS NOT NULL
  GROUP BY l.first_campaign
)
SELECT
  cd.campanha_name,
  c.total_spend AS gasto_meta,
  cd.leads_totais,
  cd.leads_qualificados,
  cd.deals_ganhos,
  cd.receita,
  CASE
    WHEN cd.leads_totais > 0 THEN ROUND(c.total_spend / cd.leads_totais, 2)
    ELSE NULL
  END AS cpl_real,
  CASE
    WHEN cd.leads_qualificados > 0 THEN ROUND(c.total_spend / cd.leads_qualificados, 2)
    ELSE NULL
  END AS cpl_qualificado,
  CASE
    WHEN cd.deals_ganhos > 0 THEN ROUND(c.total_spend / cd.deals_ganhos, 2)
    ELSE NULL
  END AS cac_real,
  CASE
    WHEN c.total_spend > 0 THEN ROUND(cd.receita / c.total_spend, 2)
    ELSE NULL
  END AS roas
FROM campaign_deals cd
LEFT JOIN campaigns c ON c.name = cd.campanha_name
ORDER BY cd.leads_totais DESC;
