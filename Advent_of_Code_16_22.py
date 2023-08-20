import re
import functools
g, f = {}, {}

with open("16_22_input.txt") as file:
    input = file.read().strip()
    for line in input.split("\n"):
        valve = line[6:8]
        flow_rate = int(re.search(r'\d+',line).group())
        _, r = line.split(";")
        r = r.replace("valves","valve")[len(" tunnels lead to valve "):]
        g[valve] = r.split(", ")
        f[valve] = flow_rate

@functools.lru_cache(maxsize=None)
def best_flow (start, open_valve, minutes):
    if minutes <= 0:
        return 0 
    best = 0
    if start not in open_valve:
        val = (minutes - 1) * f[start]
        start_openend = tuple(sorted(open_valve + (start,)))
        for a in g[start]:
            if val != 0:
                best = max(best, val + best_flow(a, start_openend, minutes - 2))
            best = max(best, best_flow(a, open_valve, minutes - 1))
    return best

print("Part 1: ",best_flow("AA", (), 30))
