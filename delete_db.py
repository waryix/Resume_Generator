# delete_db.py
import os

def delete_database():
    db_files = ['site.db', 'C:/projects/resume/site.db', 'instance/site.db']
    
    for db_file in db_files:
        if os.path.exists(db_file):
            try:
                os.remove(db_file)
                print(f"Deleted: {db_file}")
            except Exception as e:
                print(f"Error deleting {db_file}: {e}")
        else:
            print(f"File not found: {db_file}")
    
    print("Database files deleted. The application will recreate them with the new schema when you run it.")

if __name__ == '__main__':
    delete_database() 