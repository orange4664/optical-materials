# Type Safety

## Status

There is no frontend TypeScript code in this project.

## Applicable Type Practices

- For Python scripts, prefer clear function signatures and simple typed containers where useful.
- Use descriptive CSV column names with units, such as `wavelength_nm`.
- Avoid untyped, undocumented output columns.

## Forbidden Patterns

- Do not introduce TypeScript config or frontend type systems for non-frontend tasks.
- Do not rename generated CSV columns without updating paper references and validation checks.
