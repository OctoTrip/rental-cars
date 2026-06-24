# OctoTrip Rental Cars MCP Server

Free, no-login MCP server for discovering and comparing rental cars with real-time pricing from multiple providers worldwide.

**Endpoint:** `https://mcp.octotrip.app/rental-cars/mcp`

## Affiliate Disclosure

OctoTrip is free to use. Booking links contain affiliate attribution -- OctoTrip may earn a commission at no extra cost to you. Search results are ranked by price within each car category, not by affiliate payout.

## Quick Start

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "octotrip-rental-cars": {
      "url": "https://mcp.octotrip.app/rental-cars/mcp"
    }
  }
}
```

No API key or login required.

## Tool: `search`

Searches live rental-car offers for a pickup location and rental period. Returns available cars from multiple vendors grouped by category (economy, compact, SUV, etc.), showing the cheapest options in each. The tool queries external provider APIs in real time and may include affiliate booking links. It does not book cars, modify reservations, charge users, or store user data.

### Parameters

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `location` | string | yes | -- | Pickup location: city, airport, station, address, or landmark |
| `pickup_date` | string | yes | -- | Pickup date (YYYY-MM-DD, DD.MM.YYYY, or natural-language) |
| `dropoff_date` | string | yes | -- | Dropoff date, must be after pickup date |
| `dropoff_location` | string | no | same as pickup | Different dropoff location for one-way rentals |
| `pickup_time` | string | no | `"12:00"` | Pickup time in 24-hour HH:MM format |
| `dropoff_time` | string | no | `"12:00"` | Dropoff time in 24-hour HH:MM format |
| `currency` | string | no | `"EUR"` | ISO 4217 currency code (EUR, USD, GBP, etc.) |
| `language` | string | no | `"en"` | Response language code (en, de, etc.) |
| `age` | integer | no | `30` | Driver age, minimum 18 (younger drivers may incur surcharges) |

### Response Format

Results are grouped by SIPP car category with the cheapest 2 options per group:

```json
{
  "results": [
    {
      "name": "Volkswagen Golf",
      "vendor": "Europcar",
      "sipp": "CDMR",
      "category": "Compact",
      "price": 181.03,
      "price_per_day": 45.26,
      "pay_now": 181.03,
      "pay_later": 0,
      "currency": "EUR",
      "transmission": "manual",
      "passengers": 5,
      "bags": 1,
      "doors": 4,
      "air_con": true,
      "fuel_policy": "Full to Full",
      "mileage": "Unlimited",
      "free_cancellation": true,
      "free_amendment": true,
      "deposit": 800,
      "excess": 950,
      "included_protections": ["Collision Damage Waiver", "Theft Protection"],
      "image_url": "https://...",
      "booking_url": "https://...",
      "link_type": "affiliate",
      "affiliate_disclosure": "This link contains affiliate attribution. OctoTrip may earn a commission at no extra cost to you."
    }
  ],
  "total": 23,
  "total_available": 379,
  "rental_days": 4,
  "pickup_location_resolved": "Munich International Airport",
  "dropoff_location_resolved": "Munich International Airport",
  "query": { ... }
}
```

### Error Responses

The server returns structured errors with suggestions:

- **`location_not_found`** -- location could not be resolved. Try a more specific name or airport.
- **`invalid_date`** -- date format not recognized. Use YYYY-MM-DD, DD.MM.YYYY, or similar.
- **`no_results`** -- no cars available for the given criteria. Try different dates or a nearby location.

## Example Prompts

- Find me a cheap rental car at Amsterdam Schiphol for next weekend
- Compare automatic SUVs available in Munich Airport for July 10-15
- I need a car in Barcelona from August 1-14, budget around 30 EUR/day
- One-way rental from Berlin to Hamburg, picking up Friday, returning Monday
- What's the cheapest economy car at London Heathrow for a week in September?

## Use with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "octotrip-rental-cars": {
      "url": "https://mcp.octotrip.app/rental-cars/mcp"
    }
  }
}
```

## Use with Cursor / Windsurf

Add to your MCP settings:

```json
{
  "mcpServers": {
    "octotrip-rental-cars": {
      "url": "https://mcp.octotrip.app/rental-cars/mcp"
    }
  }
}
```

## Use with Cline

Add to your Cline MCP settings:

```json
{
  "mcpServers": {
    "octotrip-rental-cars": {
      "url": "https://mcp.octotrip.app/rental-cars/mcp"
    }
  }
}
```

## Use with LobeHub

[![MCP Badge](https://lobehub.com/badge/mcp/octotrip-rental-cars)](https://lobehub.com/mcp/octotrip-rental-cars)

## Use with OpenClaw

```bash
openclaw plugins install clawhub:@xltnapps/octotrip-rental-cars
```

## Use with Smithery

Install via [Smithery](https://smithery.ai/servers/xltnapps/octotrip-rental-cars):

```bash
npx -y @smithery/cli install xltnapps/octotrip-rental-cars --client claude
```

## Use with Hermes Agent

```bash
hermes mcp add octotrip-rental-cars --url https://mcp.octotrip.app/rental-cars/mcp
hermes mcp test octotrip-rental-cars
```

Or add to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  octotrip_rental_cars:
    url: "https://mcp.octotrip.app/rental-cars/mcp"
```

## Privacy

This server does not store, log, or track any user data. Queries are forwarded to provider APIs and results are returned directly. See [PRIVACY.md](PRIVACY.md) for details.

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md).

## License

MIT
