import sys
import json
import os

class App:
    def __init__(self, id):
        self.id = id
        self.children = []
        self._handlers = {}
        self._pending_updates = {}

    def add(self, component):
        self.children.append(component)
        return component

    def event(self, event_name):
        def decorator(func):
            self._handlers[event_name] = func
            return func
        return decorator

    def _find_component(self, current, element_id):
        if getattr(current, "id", None) == element_id:
            return current
        if hasattr(current, "children"):
            for child in current.children:
                found = self._find_component(child, element_id)
                if found:
                    return found
        return None

    def update_element(self, element_id, **kwargs):
        # Update internal state if found
        for root_child in self.children:
            found = self._find_component(root_child, element_id)
            if found:
                for k, v in kwargs.items():
                    setattr(found, k, v)
                break
        
        # Record patch
        if element_id not in self._pending_updates:
            self._pending_updates[element_id] = {}
        self._pending_updates[element_id].update(kwargs)

    def render(self):
        layout = {
            "app_id": self.id,
            "type": "layout_update",
            "children": [c.to_dict() for c in self.children]
        }
        print(json.dumps(layout), flush=True)

    def trigger_dynamic_action(self, action_type, **kwargs):
        """Triggers a dynamic island action (e.g. showSmartLamp, showVolume) from the app."""
        payload = {
            "action": "dynamic_action",
            "type": action_type
        }
        payload.update(kwargs)
        print(json.dumps(payload), flush=True)

    def render_patch(self):
        for element_id, updates in self._pending_updates.items():
            payload = {"id": element_id}
            payload.update(updates)
            print(json.dumps(payload), flush=True)
        self._pending_updates.clear()

    def run(self):
        """Main loop that listens to stdin and routes events."""
        for line in sys.stdin:
            try:
                line_str = line.strip()
                if not line_str:
                    continue
                event_data = json.loads(line_str)
                event = event_data.get("event")
                data = event_data.get("data", {})
                
                if event in self._handlers:
                    self._handlers[event](data)
                else:
                    sys.stderr.write(f"No handler registered for event: {event}\n")
            except Exception as e:
                sys.stderr.write(f"SDK Event loop error: {e}\n")
