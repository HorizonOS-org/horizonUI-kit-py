# Events, State Updates, and Actions

`horizonUI-kit` applications run as processes communicating with Horizon OS through standard streams (`stdin` and `stdout`). The event loop parses input signals, triggers decorators, and formats updates.

## 1. Event Handling

### `@app.event(event_name)`
Register callback handlers for UI events. Buttons trigger `{id}_click` events by default, while form elements trigger `{id}_change` events.

```python
import horizon as hz

app = hz.App(id="com.example.app")
app.add(hz.Button("Save Settings", id="save_btn"))

@app.event("save_btn_click")
def on_save(data):
    print("Save button was clicked!", data)
```

## 2. Dynamic State Updates

When the application state changes inside an event handler, you can update the UI components dynamically using `update_element` and then rendering the patch.

### `app.update_element(element_id, **kwargs)`
Modifies parameters of a component matching the `element_id`.

### `app.render_patch()`
Sends the delta changes (patches) of updated components to Horizon OS. This is much faster and cleaner than rerendering the whole app layout.

```python
@app.event("volume_slider_change")
def on_volume_change(data):
    # data contains the new state of the slider, e.g. {"value": 75}
    new_value = data.get("value", 50)
    
    # Update text label and slider component
    app.update_element("vol_label", text=f"Volume: {new_value}%")
    app.update_element("volume_slider", value=new_value)
    
    # Send updates to the screen
    app.render_patch()
```

## 3. Horizon OS Global Actions

You can trigger special global native actions within Horizon OS.

### `app.trigger_dynamic_action(action_type, **kwargs)`
Triggers a dynamic island action (e.g., displaying interactive panels like smart lights controls, volume meters, active media notifications).

```python
# Show smart lamp controls in the native dynamic island UI
app.trigger_dynamic_action(
    "showSmartLamp",
    lamp_id="living_room_1",
    brightness=80,
    color="#FF5733"
)
```

### Backward-compatible `HorizonApp` Actions
If you are using the older `HorizonApp` class, you can use:
* `app.trigger_action(action_name, **kwargs)`: Custom actions like applying wallpaper.
* `app.update_component(component_id, **kwargs)`: Sends component updates.
* `app.send_layout(layout)`: Emits layout to stdout.
