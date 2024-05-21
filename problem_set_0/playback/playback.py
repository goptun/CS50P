def main():
    user_input = input("Please, enter your phrase: ")

    slowed_down_input = user_input.replace(" ", "...")

    print(slowed_down_input)


if __name__ == "__main__":
    main()
