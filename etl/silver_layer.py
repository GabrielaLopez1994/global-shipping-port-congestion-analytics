"""
Silver Layer

Global Shipping & Port Congestion Analytics

"""

# Read Bronze (Extract)

df_bronze = spark.table(
"workspace.bronze.world_bank_container_traffic"
)

# Transformation: Flatten country and indicator, casts

from pyspark.sql.functions import col

df_silver = (

    df_bronze
    .filter(
        col("value").isNotNull()
    )
    .select(
        col("country.id")
            .alias("country_id"),
        col("country.value")
            .alias("country_name"),
        col("countryiso3code")
            .alias("country_iso3"),
        col("indicator.id")
            .alias("indicator_id"),
        col("indicator.value")
            .alias("indicator_name"),
        col("date")
            .cast("int")
            .alias("year"),
        col("value")
            .cast("double")
            .alias("port_traffic_teu")
    )
)

# Data quality rules

df_silver.count()
from pyspark.sql.functions import *

df_silver.select(
    [
       count(
            when(col(c).isNull(), c)
        ).alias(c)
        for c in df_silver.columns
    ]
).show()

total_records = df_silver.count()
unique_records = df_silver.dropDuplicates().count()
duplicates = total_records - unique_records

print(f"Duplicados encontrados: {duplicates}")

# MD5 Hash

from pyspark.sql.functions import (
    md5,
    concat_ws
)

df_silver = (
    df_silver
    .withColumn(
        "record_hash",
        md5(
            concat_ws(
                "|",    
            col("country_iso3"),
            col("year"),
            col("port_traffic_teu")
            )
        )
    )
)

# Metadata

from pyspark.sql.functions import (
    current_timestamp
)

df_silver = (
    df_silver
    .withColumn(
        "silver_load_timestamp",
        current_timestamp()
    )
)

# Persist to Silver

spark.sql(
"""
CREATE SCHEMA IF NOT EXISTS workspace.silver
"""
)

(
    df_silver.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(
        "workspace.silver.port_traffic_clean"
    )
)

