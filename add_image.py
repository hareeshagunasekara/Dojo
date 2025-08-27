#!/usr/bin/env python
"""
Helper script to add images to the Dojo project.
This script helps you organize and add images to the correct folders.
"""

import os
import shutil
import sys

def main():
    """Help user add images to the project."""
    print("🖼️  Dojo Image Helper")
    print("=" * 30)
    print()
    
    # Show current image structure
    print("📁 Current image folders:")
    print("  static/img/")
    print("  ├── icons/          # Small icons and UI elements")
    print("  ├── backgrounds/    # Background images and patterns")
    print("  ├── logos/          # Logo variations and branding")
    print("  └── README.md       # Image usage guide")
    print()
    
    # Show usage examples
    print("📋 How to use images in your templates:")
    print()
    print("1. In HTML templates:")
    print("   {% load static %}")
    print("   <img src=\"{% static 'img/logos/dojo-logo.png' %}\" alt=\"Dojo Logo\">")
    print()
    print("2. In CSS:")
    print("   .hero-section {")
    print("       background-image: url('../img/backgrounds/hero-bg.jpg');")
    print("   }")
    print()
    print("3. In JavaScript:")
    print("   const logoPath = '/static/img/logos/dojo-logo.png';")
    print()
    
    # Show recommended image types
    print("🎯 Recommended image types:")
    print("  • PNG: For logos, icons, and graphics with transparency")
    print("  • JPG: For photographs and complex images")
    print("  • SVG: For scalable graphics and icons")
    print()
    
    # Show naming conventions
    print("📝 Naming conventions:")
    print("  • Use descriptive names: 'welcome-hero.jpg'")
    print("  • Use hyphens instead of spaces: 'feature-todo.png'")
    print("  • Include size in name if needed: 'logo-large.png'")
    print()
    
    print("✅ Ready to add your images!")
    print("Just copy your image files to the appropriate folders in static/img/")

if __name__ == '__main__':
    main()
