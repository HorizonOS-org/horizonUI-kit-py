# 🌌 horizonUI-kit

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Horizon%20OS-purple.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)

The official Python SDK for building native, lightweight, and modern application user interfaces on **Horizon OS**.

`horizonUI-kit` allows you to design applications in pure Python with simple, declarative components. It handles communication over standard streams automatically, so you can focus on building beautiful user experiences.

---

## ✨ Features

* 📦 **Declarative UI**: Construct layouts instantly using Python `with` contexts and components (`Row`, `Column`, `Grid`, `Card`, etc.).
* ⚡ **High Performance Patches**: Update specific elements dynamically with `app.render_patch()` instead of redrawing the full screen.
* 🎙️ **Event Loop**: Clean event listener decorators (`@app.event("id_click")`) that capture inputs automatically.
* 🏝️ **Dynamic Actions**: Interact directly with Horizon OS features like the dynamic island via built-in hooks.

---

## 🚀 Installation

Install the library in development/editable mode:

```bash
pip install -e .
```

---

## 🛠️ Quick Start

Below is a complete hello world program featuring dynamic interaction and updates:

```python
import horizon as hz

# Initialize the App container
app = hz.App(id="com.horizon.quickstart")

# Build layout declaratively
with app.add(hz.Card(title="Settings Panel")) as card:
    card.add(hz.Text("Toggle Dark Mode status", id="status_text"))
    card.add(hz.Switch(id="theme_switch", label="Dark Mode", checked=True))
    card.add(hz.Button("Apply Configuration", id="apply_btn"))

# Define event handler for the toggle switch
@app.event("theme_switch_change")
def on_theme_change(data):
    checked = data.get("checked", False)
    status = "Enabled" if checked else "Disabled"
    app.update_element("status_text", text=f"Dark Mode: {status}")
    app.render_patch()

# Define event handler for the button click
@app.event("apply_btn_click")
def on_apply(data):
    # Trigger native dynamic island notification
    app.trigger_dynamic_action("showNotification", message="Settings applied successfully!")

# Start the application
if __name__ == "__main__":
    app.render()
    app.run()
```

---

## 📚 Documentation Reference

For more detailed guides and API references, check out:

* 📖 **[Getting Started Guide](docs/getting_started.md)** - Installation, lifecycle details, and setup.
* 🧩 **[UI Components Reference](docs/components.md)** - Lists all containers, inputs, media, and layout blocks.
* 🛰️ **[Events and Actions Guide](docs/events_and_actions.md)** - Handling user clicks, input changes, and triggering global actions.

---

## 📄 License

This project is licensed under the MIT License.
