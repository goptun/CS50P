def convert(input_str):
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")
    return input_str


def main():
    user_input = input("Please, enter a phrase: ")
    converted_input = convert(user_input)
    print(converted_input)


if __name__ == "__main__":
    main()
