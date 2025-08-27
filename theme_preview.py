#!/usr/bin/env python
"""
Theme Preview Script for Dojo
This script shows the new theme colors and opens the application.
"""

import webbrowser
import time

def main():
    """Show theme preview and open the application."""
    print("🎨 Dojo Theme Preview")
    print("=" * 30)
    print()
    
    print("🌈 New Theme Colors:")
    print()
    print("🎯 Primary Colors:")
    print("  • Primary Purple: #B7B1F2")
    print("  • Secondary Blue: #BFECFF")
    print("  • Accent Pink: #FFE0EF")
    print("  • Success Green: #C1CFA1")
    print("  • Warning Orange: #F0A04B")
    print("  • Background Cream: #FBF3D5")
    print()
    
    print("📝 Text Colors:")
    print("  • Primary Text: #000000 (Black)")
    print("  • Secondary Text: #333333 (Dark Gray)")
    print("  • Muted Text: #666666 (Medium Gray)")
    print()
    
    print("🎨 Design Features:")
    print("  • Beautiful gradients using theme colors")
    print("  • Consistent color scheme throughout")
    print("  • Hover effects with accent colors")
    print("  • Card headers with primary gradient")
    print("  • Buttons with theme-appropriate colors")
    print("  • All text in black for maximum readability")
    print()
    
    print("🚀 Opening the application to see the new theme...")
    print("URL: http://127.0.0.1:8000/")
    print()
    
    # Wait a moment for the server to be ready
    time.sleep(2)
    
    # Open the welcome page
    try:
        webbrowser.open('http://127.0.0.1:8000/')
        print("✅ Application opened successfully!")
        print()
        print("📱 Pages to check:")
        print("  • Welcome page: http://127.0.0.1:8000/")
        print("  • Dashboard: http://127.0.0.1:8000/dashboard/")
        print("  • Login: http://127.0.0.1:8000/accounts/login/")
        print("  • Sign Up: http://127.0.0.1:8000/accounts/signup/")
        print()
        print("🎉 Enjoy your beautiful new theme!")
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print("Please manually open: http://127.0.0.1:8000/")

if __name__ == '__main__':
    main()
