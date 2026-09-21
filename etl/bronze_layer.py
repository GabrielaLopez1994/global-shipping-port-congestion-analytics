"""
Bronze Layer

Global Shipping & Port Congestion Analytics

Source:
World Bank API

Indicator:
IS.SHP.GOOD.TU
"""

import requests
import pandas as pd

def extract_world_bank_data():

  indicator = "IS.SHP.GOOD.TU"

  base_url = (
      f"https://api.worldbank.org/v2/"
      f"country/all/indicator/{indicator}"
)

  params = {
      "format": "json",
      "per_page": 1000,
      "page": 1
}
 
all_records = []

total_pages = 1

  while params["page"] <= total_pages:

    response = requests.get(
        base_url,
        params=params,
        timeout=60
    )
 
    response.raise_for_status()

    page_data = response.json()

    metadata = page_data[0]

    total_pages = int(
        metadata["pages"]
    )

    records_page = page_data[1]

    all_records.extend(
        records_page
    )

    params["page"] += 1

  return all_records

def build_bronze_dataframe(
    spark
):
    records = (
        extract_world_bank_data()
    )
  
    pdf = pd.DataFrame(records)
 
    df_bronze = (
        spark
        .createDataFrame(pdf)
    )

    return df_bronze

def save_bronze_table(
    spark
):
  
    df_bronze = (
        build_bronze_dataframe(
            spark
        )
    )

    (
        df_bronze.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(
            "workspace.bronze.world_bank_container_traffic"
        )
    )


if __name__ == "__main__":

  save_bronze_table(
      spark
  )
