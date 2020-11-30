import math


def create_rsvty_list(r, l):
    radius = 0.00035
    rsvty_list = []

    for i in range(0, 6):
        rsvty_list.append((r[i] * math.pi * (radius ** 2)) / l[i])

    return rsvty_list


def create_conductivity_list(c):
    conductivity_list = []

    for i in c:
        conductivity_list.append(1 / i)

    return conductivity_list


def average(l):
    return sum(l) / len(l)


def variance(l):
    avrg = average(l)
    return sum([((i - avrg) ** 2) for i in l]) / len(l)


def standart_deviation(l):
    return variance(l) ** 0.5


radius = 0.0035
Resistance_list = [2.6, 2.8, 3, 3.2, 3.4, 3.6]
length_list = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
resistivity_l = create_rsvty_list(Resistance_list, length_list)
conductivity_l = create_conductivity_list(resistivity_l)
average_c = average(conductivity_l)
variance_c = variance(conductivity_l)
standart_deviation_c = standart_deviation(conductivity_l)

print("Resistance list")
print(Resistance_list)
print("Length of the leads")
print(length_list)
print("Resistivity list")
print(resistivity_l)
print("Conductivity list")
print(conductivity_l)
print("Average Conductivity")
print(average_c)
print("Variance")
print(variance_c)
print("Standart Deviation")
print(standart_deviation_c)
print("Estimated Conductivity Range")
print("[", str(average_c - 3 * standart_deviation_c), ",", str(average_c + 3 * standart_deviation_c), "]")
print("Estimated Conductivity")
print(average_c + 3 * standart_deviation_c)
print(math.pi * (radius ** 2))

print("\n\n\n")

# coming soon
