#!/usr/bin/env python
"""
Demo script to showcase the Dojo welcome page.
This script opens the welcome page in the default browser.
"""

import webbrowser
import time
import subprocess
import sys
import os

def main():
    """Open the welcome page in the browser."""
    print("🎓 Welcome to Dojo - Your Student Space, Simplified!")
    print("=" * 50)
    print()
    print("Opening the welcome page in your browser...")
    print("URL: http://127.0.0.1:8000/")
    print()
    print("Features you'll see:")
    print("✅ Beautiful welcome page with background color #FBF3D5")
    print("✅ Animated elements and smooth transitions")
    print("✅ Feature highlights with icons")
    print("✅ Call-to-action buttons for Sign Up and Sign In")
    print("✅ Responsive design for all devices")
    print("✅ Automatic redirect to dashboard for authenticated users")
    print()
    
    # Wait a moment for the server to be ready
    time.sleep(2)
    
    # Open the welcome page in the default browser
    try:
        webbrowser.open('http://127.0.0.1:8000/')
        print("✅ Welcome page opened successfully!")
        print()
        print("To stop the server, press Ctrl+C in the terminal where it's running.")
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print("Please manually open: http://127.0.0.1:8000/")

if __name__ == '__main__':
    main()
