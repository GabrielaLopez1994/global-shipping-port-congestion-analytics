CREATE OR REPLACE VIEW
workspace.gold.vw_country_ranking
AS

SELECT
    c.country_name,
    SUM(f.port_traffic_teu) AS total_teu
FROM workspace.gold.fact_port_traffic f
INNER JOIN workspace.gold.dim_country c
ON f.country_id = c.country_id
GROUP BY c.country_name;
