def converts_temperature(suhu, satuan):
    if satuan == "C":
        return suhu * 9/5 + 32, "Fahrenheit"
    elif satuan == "F":
        return (suhu - 32) * 5/9, "Celsius"

print(converts_temperature(30, "C"))
print(converts_temperature(86, "F"))