import os
import sys
import json
from .app import App
from .components import *
from .extensions import *

# Backward compatibility implementation
class HorizonApp(App):
    def __init__(self):
        # We assign a default app id for backward compatibility
        super().__init__(id="com.user.horizon_app")
        self._current_layout = None
        self.app_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def load_layout_from_ui(self, filename="layout.json"):
        """Loads default layout from the ui/ folder."""
        ui_path = os.path.join(self.app_dir, "ui", filename)
        if os.path.exists(ui_path):
            try:
                with open(ui_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                sys.stderr.write(f"Failed to read layout: {e}\n")
        return None

    def send_layout(self, layout):
        """Emits layout to stdout."""
        print(json.dumps(layout), flush=True)

    def update_component(self, component_id, **kwargs):
        """Sends updates for a specific UI component by its id."""
        payload = {"id": component_id}
        payload.update(kwargs)
        print(json.dumps(payload), flush=True)

    def trigger_action(self, action_name, **kwargs):
        """Sends a custom global action like applying wallpaper."""
        payload = {"action": action_name}
        payload.update(kwargs)
        print(json.dumps(payload), flush=True)

    def on(self, event_name):
        """Decorator to register event handler functions."""
        return self.event(event_name)

class InputField(Input):
    def __init__(self, id, placeholder="", focus=False):
        super().__init__(id=id, placeholder=placeholder, focus=focus)
    def to_dict(self):
        return {
            "type": "input_fields",
            "id": self.id,
            "placeholder": self.placeholder,
            "focus": self.focus
        }

class ImageGrid(Component):
    def __init__(self, id, images=None, action_event="select_wallpaper"):
        self.id = id
        self.images = images or []
        self.action_event = action_event
        
    def to_dict(self):
        return {
            "type": "image_grid",
            "id": self.id,
            "images": self.images,
            "action_event": self.action_event
        }
