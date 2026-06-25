# Privacy Policy

## Data Flow

```
User query --> MCP client --> OctoTrip MCP server --> Provider API(s) --> Response to user
```

## What We Do NOT Collect

- No user accounts or logins
- No personal information
- No IP addresses
- No search queries or search history
- No cookies or tracking pixels
- No analytics or telemetry

## Server Logs

We maintain minimal access logs for operational monitoring. Here is exactly what a log entry looks like:

```json
{"ts": "2026-06-25T13:21:00.706176+00:00", "method": "POST", "path": "/mcp", "status": 200, "ms": 7, "ua": "python-httpx/0.28.1"}
```

**What is logged:** timestamp, HTTP method, path, status code, response time, user-agent.

**What is NOT logged:** IP addresses, search queries, locations, dates, results, or any user-identifiable data.

Log files are rotated automatically (10 MB cap, 5 backups) and contain only the fields shown above.

## What Happens to Your Query

1. Your MCP client sends a search query to our server
2. Our server forwards the relevant parameters to third-party provider APIs
3. Provider APIs return results
4. Our server formats the results and returns them to your MCP client
5. Nothing is stored -- the query and results exist only for the duration of the request

## Third-Party Provider APIs

This server queries external provider APIs to retrieve pricing and availability data. Those providers have their own privacy policies. We send only the search parameters necessary to fulfill your query (e.g., location, dates, preferences) -- never any personal or identifying information.

## Booking Links

Search results include booking URLs that contain affiliate attribution parameters. Clicking these links takes you to the provider's website, which is governed by the provider's own privacy policy. The affiliate parameter identifies OctoTrip as the referral source -- it does not contain or transmit any information about you.

## Changes

If this policy changes, the updated version will be published in this repository.

## Contact

Questions about privacy: xltnapps@gmail.com
