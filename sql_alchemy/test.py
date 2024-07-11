from conftest import db
from models import User

def test_something(db):
    # Use the db fixture to create a session
    session = db()
    u = User(username="Julian")
    db.add(u)
    db.commit()
    
    session.close()

if __name__ == "__main__":
    test_something(db)