# main.py
from app import create_app
import os
import sys

# Redirect stderr to suppress GTK/GLib warnings
#sys.stderr = open(os.devnull, 'w')

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
