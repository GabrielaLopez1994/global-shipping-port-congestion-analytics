# Silver Data Quality

Rules Applied

1. Remove rows where value is NULL.
   2793 valid rows

3. Flatten nested JSON structures.

4. Convert year to INTEGER.

5. Convert port traffic to DOUBLE.

6. Validate duplicate records
   0 duplicate values

7. Generate MD5 hash.

## Additional Finding

The World Bank API contains:

- Countries
- Regional aggregates
- Economic groups

Examples:

- Argentina
- Australia
- Belgium

and

- OECD Members
- European Union
- World

Decision:

All entities were retained in Silver.
Filtering will be applied during Gold according to analytical requirements.
