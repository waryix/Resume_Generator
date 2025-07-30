# init_db.py

from app import create_app, db
from app.models import User, Resume

def init_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Optionally add some sample data
        # You can uncomment the following lines if you want to add sample data
        
        # # Check if we already have users
        # if User.query.first() is None:
        #     print("Adding sample user...")
        #     sample_user = User(
        #         username='testuser',
        #         email='test@example.com',
        #         password='hashed_password_here'
        #     )
        #     db.session.add(sample_user)
        #     db.session.commit()
        #     print("Sample user added!")

if __name__ == '__main__':
    init_database() 