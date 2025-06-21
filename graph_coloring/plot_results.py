import csv
import matplotlib.pyplot as plt

# Wczytaj dane z CSV
results = {}
with open("results.csv", newline="") as csvfile:    #plik csv
    reader = csv.DictReader(csvfile)
    for row in reader:
        method = row["method"]
        param = row["param"]
        cost = float(row["avg_cost"])
        time_sec = float(row["avg_time"])
        memory_kb = float(row["avg_memory_kb"])

        if method not in results:
            results[method] = {"params": [], "costs": [], "times": [], "memories": []}

        results[method]["params"].append(param)
        results[method]["costs"].append(cost)
        results[method]["times"].append(time_sec)
        results[method]["memories"].append(memory_kb)

# Rysowanie wykresów
for metric in ["costs", "times", "memories"]:
    plt.figure()
    for method, data in results.items():
        plt.plot(data["params"], data[metric], label=method, marker="o")
    plt.title(f"Porównanie metod: {metric}")
    plt.xlabel("Parametr metody")
    plt.ylabel({
        "costs": "Średni koszt (liczba konfliktów)",
        "times": "Średni czas (s)",
        "memories": "Średnie zużycie pamięci (KB)"
    }[metric])
    plt.legend()
    plt.grid(True)

plt.show()
