from app.models import User

def create_user(name: str, email: str, age: int) -> User:

    if not name:
        raise ValueError("Name cannot be empty")

    if not email:
        raise ValueError("Email cannot be empty")

    if age <= 0:
        raise ValueError("Age must be positive")

    user = User(
        name=name,
        email=email,
        age=age
    )

    return user