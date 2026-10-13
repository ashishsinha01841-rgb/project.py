# Cab/Taxi Route Finder

A command-line tool that finds the shortest route and total distance between a
pickup location and a destination. Locations are graph vertices, roads are
weighted edges, and the route is computed with Dijkstra's algorithm.

## Requirements
- Python 3.8 or newer (no third-party packages needed)

## Setup
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python --version        # confirm 3.8+
```
There are no dependencies to install.

## Run
```bash
# list valid locations
python main.py --list

# find a route
python main.py --from "Railway Station" --to "Airport"
```
Example output:
```
Route   : Railway Station -> Market -> Mall -> Airport
Distance: 12.5 km
Est. fare: 200.00
```
Optional flags: `--map <file.csv>`, `--base-fare <n>`, `--rate <n>`.

## Map file format
CSV with one road per line: `location_a,location_b,distance_km`. Roads are
two-way. Lines starting with `#` and a `from,to,distance_km` header are ignored.
To use your own map, pass `--map path/to/file.csv`.

## Run the tests
```bash
python -m unittest discover tests
```
(Run from the repository root.)

## Project structure
- `graph.py` – graph class, CSV loader, Dijkstra search
- `main.py` – command-line interface
- `data/city.csv` – sample road network
- `tests/test_graph.py` – unit tests
