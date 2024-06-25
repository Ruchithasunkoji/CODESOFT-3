import random
import string


def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length for the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
