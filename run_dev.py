#!/usr/bin/env python
"""
Development runner script for Dojo.
This script sets up the environment and runs the development server.
"""

import os
import sys
import subprocess

def main():
    """Run the development server with proper settings."""
    # Set development settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dojo.settings.dev')
    
    # Run the development server
    subprocess.run([sys.executable, 'manage.py', 'runserver'])

if __name__ == '__main__':
    main()
