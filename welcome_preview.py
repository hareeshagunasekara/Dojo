#!/usr/bin/env python
"""
Welcome Page Preview
Shows the updated welcome page with SVG background and concise content.
"""

import webbrowser
import time

def main():
    """Show welcome page preview."""
    print("Welcome to Dojo - Updated")
    print("=" * 30)
    print()
    
    print("✨ New Features:")
    print("  • SVG background image centered")
    print("  • Concise, inviting content")
    print("  • No emojis - clean design")
    print("  • Short feature descriptions")
    print()
    
    print("🎨 Background Details:")
    print("  • Custom SVG with theme colors")
    print("  • Subtle gradients and shapes")
    print("  • Fixed positioning for stability")
    print("  • Responsive design")
    print()
    
    print("📝 Content Updates:")
    print("  • Shorter, more inviting text")
    print("  • Clean feature descriptions")
    print("  • Professional tone")
    print("  • Focused call-to-action")
    print()
    
    print("🚀 Opening welcome page...")
    print("URL: http://127.0.0.1:8000/")
    print()
    
    time.sleep(2)
    
    try:
        webbrowser.open('http://127.0.0.1:8000/')
        print("✅ Welcome page opened!")
        print()
        print("The page now features:")
        print("  • Beautiful SVG background")
        print("  • Clean, professional design")
        print("  • Inviting, concise content")
        print("  • Your custom theme colors")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please manually visit: http://127.0.0.1:8000/")

if __name__ == '__main__':
    main()
