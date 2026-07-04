import secrets
import string

def main():
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print("Minimum length is 8. Setting to 8.")
            length = 8
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
