# Images Directory

This directory contains static images for the Dojo application.

## 📁 Folder Structure

```
static/img/
├── icons/           # Small icons and UI elements
├── backgrounds/     # Background images and patterns
├── logos/          # Logo variations and branding
└── README.md       # This file
```

## 🖼️ How to Use Images

### 1. In Templates (HTML)
```html
{% load static %}
<img src="{% static 'img/logo.png' %}" alt="Dojo Logo">
<img src="{% static 'img/backgrounds/welcome-bg.jpg' %}" alt="Welcome Background">
```

### 2. In CSS
```css
.hero-section {
    background-image: url('../img/backgrounds/hero-bg.jpg');
}
```

### 3. In JavaScript
```javascript
const logoPath = '/static/img/logos/dojo-logo.png';
```

## 📋 Image Guidelines

- **Formats**: Use PNG for logos/icons, JPG for photos, SVG for scalable graphics
- **Sizes**: Optimize images for web (compress when possible)
- **Naming**: Use descriptive names with hyphens (e.g., `welcome-hero.jpg`)
- **Alt Text**: Always provide meaningful alt text for accessibility

## 🎯 Common Use Cases

- **Logos**: `logos/dojo-logo.png`
- **Backgrounds**: `backgrounds/welcome-bg.jpg`
- **Icons**: `icons/feature-todo.png`
- **Hero Images**: `backgrounds/hero-student.jpg`
