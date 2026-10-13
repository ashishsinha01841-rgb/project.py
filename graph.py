"""Graph model and Dijkstra shortest-path search for the route finder."""
import csv
import heapq


class Graph:
    """Undirected weighted graph: locations are vertices, roads are edges."""

    def __init__(self):
        self.adj = {}  # location -> list of (neighbor, distance_km)

    def add_road(self, a, b, km):
        if km < 0:
            raise ValueError(f"Negative distance on road {a}-{b}")
        self.adj.setdefault(a, []).append((b, km))
        self.adj.setdefault(b, []).append((a, km))

    @classmethod
    def from_csv(cls, path):
        """Load roads from a CSV with rows: location_a,location_b,distance_km."""
        g = cls()
        with open(path, newline="", encoding="utf-8") as f:
            for line_no, row in enumerate(csv.reader(f), start=1):
                if not row or row[0].strip().startswith("#"):
                    continue
                if len(row) != 3:
                    raise ValueError(f"Line {line_no}: expected 3 columns")
                a, b, km = row[0].strip(), row[1].strip(), row[2].strip()
                if a.lower() == "from":  # skip header
                    continue
                g.add_road(a, b, float(km))
        return g

    def locations(self):
        return sorted(self.adj)

    def shortest_path(self, source, target):
        """Return (path, total_km), or (None, inf) if target is unreachable."""
        for name in (source, target):
            if name not in self.adj:
                raise KeyError(name)
        dist = {source: 0.0}
        prev = {}
        heap = [(0.0, source)]
        done = set()
        while heap:
            d, u = heapq.heappop(heap)
            if u in done:
                continue
            done.add(u)
            if u == target:
                break
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))
        if target not in dist:
            return None, float("inf")
        path = [target]
        while path[-1] != source:
            path.append(prev[path[-1]])
        return path[::-1], dist[target]
