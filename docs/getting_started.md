# Getting Started with horizonUI-kit

`horizonUI-kit` is the official Python SDK for building native application interfaces on Horizon OS. It allows Python developers to easily write user interfaces using simple, declarative components and handle client-side events.

## Installation

You can install the package in development mode using `pip`:

```bash
pip install -e .
```

## Basic Concepts

An application in Horizon OS using `horizonUI-kit` follows a declarative structure:
1. **The App Object**: The entry point and event manager of your application.
2. **Components**: UI blocks (buttons, text fields, layouts) added to the application.
3. **Events**: Handlers that listen to stdin (JSON formatted inputs from Horizon OS) and perform operations or updates.
4. **Render Loop**: Emitting JSON payloads of the layout updates back to stdout for Horizon OS to render.

## Hello World Example

Here is a simple example showing how to build a basic application:

```python
import horizon as hz

# Initialize the application with its unique package ID
app = hz.App(id="com.example.hello")

# Create a column layout with text and a button
with app.add(hz.Column(id="main_container")) as col:
    col.add(hz.Text("Welcome to Horizon OS", id="title"))
    col.add(hz.Button("Click Me", id="click_btn"))

# Register an event handler for the button click
@app.event("click_btn_click")
def on_button_click(data):
    # Update the title text
    app.update_element("title", text="Hello from Python!")
    # Render the patch (only sends updates to the layout)
    app.render_patch()

# Initial render of the entire layout
app.render()

# Start the main event loop to listen for events
app.run()
```

## App Lifecycle

- **`app.add(component)`**: Adds a root component to the application layout.
- **`app.render()`**: Generates and prints the complete JSON layout structure to stdout.
- **`app.update_element(id, **kwargs)`**: Modifies properties of a component locally and queues the changes.
- **`app.render_patch()`**: Outputs only the modified properties to stdout, which is highly efficient.
- **`app.run()`**: Starts blocking execution, reading incoming event JSON messages from standard input line-by-line.
