# Bronze Data Profiling

## Findings

### Schema Analysis

The `value` column was inferred by Spark as `VOID`.

### Validation
A profiling analysis identified 2,793 valid records with non-null values.

### Conclusion
The issue corresponds to a schema inference problem during ingestion.
 
17
The correction will be applied during the Silver Layer transformations.
