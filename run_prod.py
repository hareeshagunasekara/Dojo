#!/usr/bin/env python
"""
Production runner script for Dojo.
This script sets up the environment and runs the production server.
"""

import os
import sys
import subprocess

def main():
    """Run the production server with proper settings."""
    # Set production settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dojo.settings.prod')
    
    # Run the production server (using gunicorn if available)
    try:
        subprocess.run([sys.executable, '-m', 'gunicorn', 'dojo.wsgi:application', '--bind', '0.0.0.0:8000'])
    except FileNotFoundError:
        print("Gunicorn not found. Install with: pip install gunicorn")
        print("Running with Django's development server instead...")
        subprocess.run([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])

if __name__ == '__main__':
    main()
