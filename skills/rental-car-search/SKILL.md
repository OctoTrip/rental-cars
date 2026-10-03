---
name: octotrip-rental-car-search
description: Search and compare rental cars with real-time pricing. Use when the user wants to find rental cars, compare car hire options, or rent a vehicle at an airport, city, or station.
license: MIT
metadata:
  author: octotrip
  version: "1.0.0"
---

# OctoTrip Rental Car Search

Search and compare rental cars with real-time pricing from multiple providers worldwide. Free, no API key required.

## Connect

Add the OctoTrip Rental Cars MCP server to your configuration:

```json
{
  "mcpServers": {
    "octotrip-rental-cars": {
      "url": "https://mcp.octotrip.app/rental-cars/mcp"
    }
  }
}
```

Transport: Streamable HTTP. No authentication, no API key, no login.

## Search Parameters

Call the `search` tool with:

| Parameter | Required | Default | Description |
|---|---|---|---|
| `location` | yes | -- | Pickup location: city, airport, station, address, or landmark |
| `pickup_date` | yes | -- | YYYY-MM-DD or natural-language date |
| `dropoff_date` | yes | -- | Must be after pickup date |
| `dropoff_location` | no | same as pickup | Different dropoff for one-way rentals |
| `pickup_time` | no | "12:00" | 24-hour HH:MM format |
| `dropoff_time` | no | "12:00" | 24-hour HH:MM format |
| `currency` | no | "EUR" | ISO 4217 code (EUR, USD, GBP, etc.) |
| `language` | no | "en" | Language code (en, de, etc.) |
| `age` | no | 30 | Driver age, minimum 18 |

## Handling Results

Results are grouped by SIPP car category (economy, compact, SUV, etc.) with the cheapest options per group.

Each result includes:
- **name**, **vendor**, **category** (e.g. "Compact", "SUV")
- **price**, **price_per_day**, **currency**
- **transmission** (automatic/manual), **passengers**, **bags**, **doors**
- **fuel_policy**, **mileage** (usually "Unlimited")
- **free_cancellation**, **free_amendment**
- **deposit** and **excess** amounts
- **included_protections** -- list of insurance coverages
- **booking_url** -- a link the user can open to book

Present results by category. Highlight the cheapest option overall and mention the deposit/excess amounts since they vary significantly between vendors.

When comparing options, note:
- **Pay now vs. pay later**: some vendors split payment
- **Fuel policy**: "Full to full" means return with a full tank
- **Free cancellation**: important for flexible travel plans

## Handling Errors

- **`location_not_found`**: Try a more specific name or airport (e.g. "Munich Airport" instead of "MUC").
- **`no_results`**: The server resolved the location but found no cars. Suggest different dates, a longer rental period, or a nearby location.

## Tips

- Airports typically have the widest selection. Use "Airport" in the location for best results.
- The server resolves location names automatically. "Barcelona" will resolve to the best matching pickup point.
- One-way rentals (different pickup and dropoff) often cost more and have fewer options.
- Younger drivers (under 25) may see surcharges reflected in the price. Set the `age` parameter when relevant.
- Minimum rental period is typically 1 day. Short rentals (1-2 days) have higher per-day rates.

## Affiliate Disclosure

Booking links contain affiliate attribution. OctoTrip may earn a commission at no extra cost to the user. Results are ranked by price within each category, not by affiliate payout.
