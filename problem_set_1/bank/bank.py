def main():
    greating = input("Greating: ").strip().lower()

    if greating.startswith("hello"):
        print("$0")

    elif greating.startswith("h"):
        print("$20")

    else:
        print("$100")


if __name__ == "__main__":
    main()
