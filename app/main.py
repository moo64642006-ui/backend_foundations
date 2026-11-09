from app.utils import create_user


def main() -> None:

    print("=== User Registration ===")

    try:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))

        user = create_user(name, email, age)

        print("\nUser Created Successfully!")
        print("-------------------------")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Age: {user.age}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()