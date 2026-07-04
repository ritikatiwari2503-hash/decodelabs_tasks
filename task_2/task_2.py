def main():
    total = 0  # OUTSIDE the loop — important!

    while True:
        entry = input("Enter expense amount (or 'quit' to stop): ")

        if entry.lower() == "quit":
            break

        try:
            expense = float(entry)
            total += expense
            print(f"Added! Running total: ₹{total:.2f}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"\nTotal Spent: ₹{total:.2f}")

if __name__ == "__main__":
    main()
