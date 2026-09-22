spark.sql("""

CREATE OR REPLACE VIEW
workspace.gold.vw_top_countries_by_year

AS

SELECT

    c.country_name,

    f.year,

    f.port_traffic_teu

FROM workspace.gold.fact_port_traffic f

INNER JOIN workspace.gold.dim_country c

ON f.country_id = c.country_id

""")
