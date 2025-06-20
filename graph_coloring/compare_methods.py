import subprocess
import time
import tracemalloc
import csv
import matplotlib.pyplot as plt

# Parametry eksperymentu
graph_file = "data/sample_graph.txt"
colors = 3
repeats = 5
tabu_sizes = [3, 5, 7]
methods = ["brute", "hill", "tabu"]

results = []

# Eksperymenty
for method in methods:
    for param in (tabu_sizes if method == "tabu" else [None]):
        times = []
        costs = []
        memories = []

        for i in range(repeats):
            cmd = ["python", "main.py",
                   "--file", graph_file,
                   "--colors", str(colors),
                   "--method", method]

            if param is not None:
                cmd += ["--tabu_size", str(param)]

            # Start pomiarów
            tracemalloc.start()
            start_time = time.time()

            process = subprocess.run(cmd, capture_output=True, text=True)

            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            duration = end_time - start_time
            output = process.stdout
            lines = output.splitlines()

            # Parsowanie kosztu
            cost_line = next((l for l in lines if "Koszt" in l), None)
            cost = int(cost_line.split(":")[1].strip()) if cost_line else None

            costs.append(cost)
            times.append(duration)
            memories.append(peak / 1024)  # KB

        results.append({
            "method": method,
            "param": param,
            "avg_cost": sum(costs) / len(costs),
            "avg_time": sum(times) / len(times),
            "avg_memory_kb": sum(memories) / len(memories)
        })

# Zapis do CSV
with open("results.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["method", "param", "avg_cost", "avg_time", "avg_memory_kb"])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("Wyniki zapisane do pliku: results.csv")

# Wykresy
labels = []
costs = []
times = []
memories = []

for res in results:
    label = f"{res['method']}({res['param']})" if res['param'] else res['method']
    labels.append(label)
    costs.append(res["avg_cost"])
    times.append(res["avg_time"])
    memories.append(res["avg_memory_kb"])

plt.figure(figsize=(14, 4))

plt.subplot(1, 3, 1)
plt.bar(labels, costs, color='skyblue')
plt.title("Średni koszt rozwiązania")
plt.ylabel("Koszt")
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
plt.bar(labels, times, color='salmon')
plt.title("Średni czas wykonania")
plt.ylabel("Czas [s]")
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
plt.bar(labels, memories, color='lightgreen')
plt.title("Średnie zużycie pamięci")
plt.ylabel("Pamięć [KB]")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
