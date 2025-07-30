# reset_db.py

from app import create_app, db
from app.models import User, Resume

def reset_database():
    app = create_app()
    
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("All tables dropped successfully!")
        
        # Create all tables with current schema
        db.create_all()
        print("Database tables recreated successfully!")
        
        print("Database has been reset and is ready to use!")

if __name__ == '__main__':
    reset_database() 