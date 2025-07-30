# init_db_sqlalchemy.py

from app import create_app, db
from app.models import User, Resume

def init_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables using SQLAlchemy
        db.create_all()
        print("Database tables created successfully using SQLAlchemy!")
        print("All tables have been created with the correct structure.")

if __name__ == '__main__':
    init_database() 