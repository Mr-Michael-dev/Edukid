from models import storage
from models.base_model import Base


def reset_database():
    """Drops all tables and recreates them."""
    # Drop all tables
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=storage._DBStorage__engine)

    # Create all tables
    print("Creating all tables...")
    Base.metadata.create_all(bind=storage._DBStorage__engine)

    print("Database reset complete.")


if __name__ == "__main__":
    reset_database()
