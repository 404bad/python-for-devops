try:
    x = int("abc")

except (ValueError, TypeError):
    print("INput problem")
