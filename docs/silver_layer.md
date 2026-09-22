# Silver Layer

1. Objective

Convert Bronze raw data into analysis-ready data.

2. Read Bronze
   
Input: workspace.bronze.world_bank_container_traffic

4. Transformations

- Data type correction
- Null handling
- JSON flattening
- Hash generation
- Metadata creation

4. Data Quality Validation

- Nested JSON successfully flattened.
- Numeric measures converted to DOUBLE.
- MD5 hash generated.
- Metadata timestamp generated.
   
6. Output Table: workspace.silver.port_traffic_clean

## Additional Finding

The World Bank API includes both countries and aggregated regional/economic entities.

Examples:

- World
- European Union
- OECD Members
- Latin America & Caribbean

These entities will be retained in Silver and filtered during Gold modeling according to the analytical requirements.
