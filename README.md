# ✈️ flight-search

[![PyPI](https://img.shields.io/pypi/v/flight-search)](https://pypi.org/project/flight-search/)
[![Python](https://img.shields.io/pypi/pyversions/flight-search)](https://pypi.org/project/flight-search/)
[![License](https://img.shields.io/pypi/l/flight-search)](https://github.com/Olafs-World/flight-search/blob/main/LICENSE)

CLI tool to search Google Flights. Get prices, times, and airlines from the command line.

Built on top of [fast-flights](https://github.com/AWeirdDev/flights) - no API key required.

## Installation

```bash
# using uv (recommended)
uv tool install flight-search

# or pip
pip install flight-search

# or run directly without installing
uvx flight-search DEN LAX --date 2025-03-01
```

## Usage

```bash
# One-way flight
flight-search DEN LAX --date 2025-03-01

# Round trip
flight-search JFK LHR --date 2025-06-15 --return 2025-06-22

# Multiple passengers, business class
flight-search SFO NRT --date 2025-04-01 --class business --adults 2

# JSON output
flight-search ORD CDG --date 2025-05-01 --output json
```

## Options

```
positional arguments:
  origin                Origin airport code (e.g., DEN, LAX, JFK)
  destination           Destination airport code

options:
  --date, -d            Departure date (YYYY-MM-DD) [required]
  --return, -r          Return date for round trips (YYYY-MM-DD)
  --adults, -a          Number of adults (default: 1)
  --children, -c        Number of children (default: 0)
  --class, -C           Seat class: economy, premium-economy, business, first
  --limit, -l           Max results (default: 10)
  --output, -o          Output format: text or json (default: text)
```

## Example Output

```
✈️  DEN → LAX
   One way · 2025-03-01
   Prices are currently: typical

──────────────────────────────────────────────────
   Frontier ⭐ BEST
   🕐 10:43 PM → 12:30 AM +1
   ⏱️  2 hr 47 min
   ✅ Nonstop
   💰 $84

──────────────────────────────────────────────────
   United ⭐ BEST
   🕐 5:33 PM → 7:13 PM
   ⏱️  2 hr 40 min
   ✅ Nonstop
   💰 $139
```

## JSON Output

```bash
flight-search DEN LAX --date 2025-03-01 --output json
```

```json
{
  "origin": "DEN",
  "destination": "LAX",
  "date": "2025-03-01",
  "return_date": null,
  "current_price": "typical",
  "flights": [
    {
      "airline": "Frontier",
      "departure_time": "10:43 PM",
      "arrival_time": "12:30 AM",
      "duration": "2 hr 47 min",
      "stops": 0,
      "price": 84,
      "is_best": true
    }
  ]
}
```

## Python API

```python
from flight_search import search_flights

result = search_flights(
    origin="DEN",
    destination="LAX", 
    date="2025-03-01",
    adults=2,
    seat_class="economy",
)

for flight in result.flights:
    print(f"{flight.airline}: ${flight.price}")
```

## Links

- [GitHub](https://github.com/Olafs-World/flight-search)
- [PyPI](https://pypi.org/project/flight-search/)
- [ClawHub Skill](https://clawhub.com/skills/flight-search)
- [fast-flights](https://github.com/AWeirdDev/flights) (underlying library)
