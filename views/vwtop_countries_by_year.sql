spark.sql("""

CREATE OR REPLACE VIEW
workspace.gold.vw_global_growth

AS

SELECT

    year,

    SUM(
        port_traffic_teu
    ) AS global_teu

FROM workspace.gold.fact_port_traffic

GROUP BY year

""")
