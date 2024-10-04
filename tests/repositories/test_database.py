import pytest
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from src.repositories.database import SessionLocal


def test_database_connection():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1"))
        assert result.fetchone()[0] == 1
    except OperationalError as e:
        pytest.fail(f"Connection failed. Error: {e}")
    finally:
        db.close()
