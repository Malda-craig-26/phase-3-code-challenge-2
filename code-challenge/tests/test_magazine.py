import pytest
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_module(module):
    conn = get_connection()
    conn.execute("DELETE FROM magazines")
    conn.commit()

def test_magazine_save_and_find():
    mag = Magazine(name="Test Mag", category="Test Category")
    mag.save()
    assert mag.id is not None

    found = Magazine.find_by_id(mag.id)
    assert found.name == "Test Mag"
    assert found.category == "Test Category"
