"""Command-line interface for the Cab/Taxi Route Finder."""
import argparse
import sys

from graph import Graph


def main():
    p = argparse.ArgumentParser(description="Find the shortest cab route between two locations.")
    p.add_argument("--map", default="data/city.csv", help="road map CSV (default: data/city.csv)")
    p.add_argument("--from", dest="src", help="pickup location")
    p.add_argument("--to", dest="dst", help="destination")
    p.add_argument("--list", action="store_true", help="list all known locations and exit")
    p.add_argument("--base-fare", type=float, default=50.0, help="base fare (default 50)")
    p.add_argument("--rate", type=float, default=12.0, help="rate per km (default 12)")
    args = p.parse_args()

    try:
        graph = Graph.from_csv(args.map)
    except (OSError, ValueError) as e:
        sys.exit(f"Error loading map: {e}")

    if args.list:
        print("\n".join(graph.locations()))
        return
    if not args.src or not args.dst:
        p.error("--from and --to are required (or use --list)")

    try:
        path, km = graph.shortest_path(args.src, args.dst)
    except KeyError as e:
        sys.exit(f"Unknown location: {e.args[0]}. Use --list to see valid names.")

    if path is None:
        sys.exit(f"No route found between {args.src} and {args.dst}.")

    print("Route   :", " -> ".join(path))
    print(f"Distance: {km:.1f} km")
    print(f"Est. fare: {args.base_fare + args.rate * km:.2f}")


if __name__ == "__main__":
    main()
