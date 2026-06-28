# Changelog

## [1.0.0] - 2026-06-28

Initial stable release.

- Hosted streamable HTTP + SSE MCP server
- `search` tool with location, pickup/dropoff dates, one-way support, currency, language, and driver age
- No auth, no API key required

## 0.4.0 - 2026-06-25

### Added
- Response schema (response_schema.json) with full JSON Schema for success and error payloads
- Wire-level protocol example (curl) in README
- Server log samples in PRIVACY.md for full transparency

### Changed
- Removed IP address logging entirely — access logs no longer contain any user-identifiable data
- Updated privacy documentation to reflect actual logging behavior

## 0.3.0 - 2026-06-24

### Changed
- Improved tool description with usage guidance and behavioral transparency
- Added MCP tool annotations (readOnlyHint, destructiveHint, idempotentHint, openWorldHint)
- Richer parameter descriptions in input schema
- Added minimum age validation (18+)

## 0.2.0 - 2026-06-22

### Changed
- Live DiscoverCars.com integration with real-time pricing
- Results grouped by SIPP car category (cheapest 2 per group)
- Deployed at mcp.octotrip.app/rental-cars

## 0.1.0 - 2026-06-22

### Added
- Initial release with `search` tool
- Streamable HTTP MCP transport
