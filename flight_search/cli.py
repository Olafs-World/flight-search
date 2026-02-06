"""CLI for searching Google Flights."""

import argparse
import json
import sys
from typing import Optional

from .search import search_flights, SearchResult


def format_text_output(result: SearchResult) -> str:
    """Format search results as human-readable text."""
    lines = []

    # Header
    trip_type = "Round trip" if result.return_date else "One way"
    lines.append(f"✈️  {result.origin} → {result.destination}")
    lines.append(f"   {trip_type} · {result.date}" + (f" - {result.return_date}" if result.return_date else ""))

    if result.current_price:
        lines.append(f"   Prices are currently: {result.current_price}")

    lines.append("")

    if not result.flights:
        lines.append("   No flights found.")
        return "\n".join(lines)

    # Flights
    for flight in result.flights:
        best_tag = " ⭐ BEST" if flight.is_best else ""
        price_str = f"${flight.price}" if flight.price else "Price N/A"

        lines.append(f"{'─' * 50}")
        lines.append(f"   {flight.airline}{best_tag}")
        lines.append(f"   🕐 {flight.departure_time} → {flight.arrival_time}" +
                    (f" {flight.arrival_ahead}" if flight.arrival_ahead else ""))
        lines.append(f"   ⏱️  {flight.duration}")

        if flight.stops == 0:
            lines.append("   ✅ Nonstop")
        else:
            stop_text = f"{flight.stops} stop" + ("s" if flight.stops > 1 else "")
            if flight.stop_info:
                stop_text += f" ({flight.stop_info})"
            lines.append(f"   🔄 {stop_text}")

        lines.append(f"   💰 {price_str}")
        lines.append("")

    return "\n".join(lines)


def main(args: Optional[list[str]] = None) -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Search Google Flights for prices and schedules",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  flight-search DEN LAX --date 2025-03-01
  flight-search JFK LHR --date 2025-06-15 --return 2025-06-22
  flight-search SFO NRT --date 2025-04-01 --class business --adults 2
  flight-search ORD CDG --date 2025-05-01 --output json
        """,
    )

    parser.add_argument("origin", help="Origin airport code (e.g., DEN, LAX, JFK)")
    parser.add_argument("destination", help="Destination airport code")
    parser.add_argument("--date", "-d", required=True, help="Departure date (YYYY-MM-DD)")
    parser.add_argument("--return", "-r", dest="return_date", help="Return date for round trips (YYYY-MM-DD)")
    parser.add_argument("--adults", "-a", type=int, default=1, help="Number of adults (default: 1)")
    parser.add_argument("--children", "-c", type=int, default=0, help="Number of children (default: 0)")
    parser.add_argument(
        "--class", "-C",
        dest="seat_class",
        choices=["economy", "premium-economy", "business", "first"],
        default="economy",
        help="Seat class (default: economy)",
    )
    parser.add_argument("--limit", "-l", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument(
        "--output", "-o",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    parsed = parser.parse_args(args)

    try:
        result = search_flights(
            origin=parsed.origin.upper(),
            destination=parsed.destination.upper(),
            date=parsed.date,
            return_date=parsed.return_date,
            adults=parsed.adults,
            children=parsed.children,
            seat_class=parsed.seat_class,
            max_results=parsed.limit,
        )

        if parsed.output == "json":
            print(json.dumps(result.to_dict(), indent=2))
        else:
            print(format_text_output(result))

        return 0

    except Exception as err:
        if parsed.output == "json":
            print(json.dumps({"error": str(err)}), file=sys.stderr)
        else:
            print(f"Error: {err}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
