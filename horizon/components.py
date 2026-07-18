class Component:
    def __init__(self, id=None):
        self.id = id

    def to_dict(self):
        raise NotImplementedError()

# --- Container Components ---

class Container(Component):
    def __init__(self, id=None):
        super().__init__(id=id)
        self.children = []

    def add(self, child):
        self.children.append(child)
        return child

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class Row(Container):
    def to_dict(self):
        d = {"type": "row", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class Column(Container):
    def to_dict(self):
        d = {"type": "column", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class Grid(Container):
    def __init__(self, id=None, columns=3, gap="10px"):
        super().__init__(id=id)
        self.columns = columns
        self.gap = gap

    def to_dict(self):
        d = {
            "type": "grid",
            "columns": self.columns,
            "gap": self.gap,
            "children": [c.to_dict() for c in self.children]
        }
        if self.id: d["id"] = self.id
        return d

class GridItem(Container):
    def __init__(self, id=None, colspan=1):
        super().__init__(id=id)
        self.colspan = colspan

    def to_dict(self):
        d = {
            "type": "grid_item",
            "colspan": self.colspan,
            "children": [c.to_dict() for c in self.children]
        }
        if self.id: d["id"] = self.id
        return d

class Stack(Container):
    def to_dict(self):
        d = {"type": "stack", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class Card(Container):
    def __init__(self, id=None, title=None):
        super().__init__(id=id)
        self.title = title

    def to_dict(self):
        d = {
            "type": "card",
            "children": [c.to_dict() for c in self.children]
        }
        if self.title: d["title"] = self.title
        if self.id: d["id"] = self.id
        return d

class Section(Container):
    def __init__(self, id=None, title=None, subtitle=None):
        super().__init__(id=id)
        self.title = title
        self.subtitle = subtitle

    def to_dict(self):
        d = {
            "type": "section",
            "children": [c.to_dict() for c in self.children]
        }
        if self.title: d["title"] = self.title
        if self.subtitle: d["subtitle"] = self.subtitle
        if self.id: d["id"] = self.id
        return d

class ScrollArea(Container):
    def __init__(self, id=None, max_height=None):
        super().__init__(id=id)
        self.max_height = max_height

    def to_dict(self):
        d = {
            "type": "scroll_area",
            "children": [c.to_dict() for c in self.children]
        }
        if self.max_height: d["max_height"] = self.max_height
        if self.id: d["id"] = self.id
        return d

class Tabs(Container):
    def to_dict(self):
        d = {"type": "tabs", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class TabItem(Container):
    def __init__(self, id=None, label="Tab"):
        super().__init__(id=id)
        self.label = label

    def to_dict(self):
        d = {
            "type": "tab_item",
            "label": self.label,
            "children": [c.to_dict() for c in self.children]
        }
        if self.id: d["id"] = self.id
        return d

class Accordion(Container):
    def __init__(self, id=None, title="Expand"):
        super().__init__(id=id)
        self.title = title

    def to_dict(self):
        d = {
            "type": "accordion",
            "title": self.title,
            "children": [c.to_dict() for c in self.children]
        }
        if self.id: d["id"] = self.id
        return d

class Sidebar(Container):
    def to_dict(self):
        d = {"type": "sidebar", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

# --- Basic Controls & Content ---

class Text(Component):
    def __init__(self, value, id=None, style=None):
        super().__init__(id=id)
        self.value = value
        self.style = style

    def to_dict(self):
        d = {"type": "text", "value": self.value}
        if self.style: d["class"] = f"hz-{self.style}"
        if self.id: d["id"] = self.id
        return d

class Spacer(Component):
    def __init__(self, id=None, height=None, width=None):
        super().__init__(id=id)
        self.height = height
        self.width = width

    def to_dict(self):
        d = {"type": "spacer"}
        if self.height: d["height"] = self.height
        if self.width: d["width"] = self.width
        if self.id: d["id"] = self.id
        return d

class Divider(Component):
    def __init__(self, id=None, orientation="horizontal"):
        super().__init__(id=id)
        self.orientation = orientation

    def to_dict(self):
        d = {"type": "divider", "orientation": self.orientation}
        if self.id: d["id"] = self.id
        return d

class Button(Component):
    def __init__(self, id, text, action, disabled=False):
        super().__init__(id=id)
        self.text = text
        self.action = action
        self.disabled = disabled

    def to_dict(self):
        d = {
            "type": "button",
            "id": self.id,
            "text": self.text,
            "event": self.action,
            "disabled": self.disabled
        }
        return d

class IconButton(Component):
    def __init__(self, id, icon, action, disabled=False):
        super().__init__(id=id)
        self.icon = icon
        self.action = action
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "icon_button",
            "id": self.id,
            "icon": self.icon,
            "event": self.action,
            "disabled": self.disabled
        }

class Link(Component):
    def __init__(self, id=None, text="", url=""):
        super().__init__(id=id)
        self.text = text
        self.url = url

    def to_dict(self):
        d = {"type": "link", "text": self.text, "url": self.url}
        if self.id: d["id"] = self.id
        return d

class Badge(Component):
    def __init__(self, id=None, text="", color="primary"):
        super().__init__(id=id)
        self.text = text
        self.color = color

    def to_dict(self):
        d = {"type": "badge", "text": self.text, "color": self.color}
        if self.id: d["id"] = self.id
        return d

class Tag(Component):
    def __init__(self, id=None, text=""):
        super().__init__(id=id)
        self.text = text

    def to_dict(self):
        d = {"type": "tag", "text": self.text}
        if self.id: d["id"] = self.id
        return d

class Icon(Component):
    def __init__(self, name, id=None):
        super().__init__(id=id)
        self.name = name

    def to_dict(self):
        d = {"type": "icon", "name": self.name}
        if self.id: d["id"] = self.id
        return d

class Image(Component):
    def __init__(self, src, id=None, alt=""):
        super().__init__(id=id)
        self.src = src
        self.alt = alt

    def to_dict(self):
        d = {"type": "image", "src": self.src, "alt": self.alt}
        if self.id: d["id"] = self.id
        return d

class Video(Component):
    def __init__(self, src, id=None, controls=True):
        super().__init__(id=id)
        self.src = src
        self.controls = controls

    def to_dict(self):
        d = {"type": "video", "src": self.src, "controls": self.controls}
        if self.id: d["id"] = self.id
        return d

class Audio(Component):
    def __init__(self, src, id=None, controls=True):
        super().__init__(id=id)
        self.src = src
        self.controls = controls

    def to_dict(self):
        d = {"type": "audio", "src": self.src, "controls": self.controls}
        if self.id: d["id"] = self.id
        return d

# --- Input Controls ---

class Input(Component):
    def __init__(self, id, placeholder="", focus=False, disabled=False):
        super().__init__(id=id)
        self.placeholder = placeholder
        self.focus = focus
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "input",
            "id": self.id,
            "placeholder": self.placeholder,
            "focus": self.focus,
            "disabled": self.disabled
        }

class TextArea(Component):
    def __init__(self, id, placeholder="", disabled=False):
        super().__init__(id=id)
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "textarea",
            "id": self.id,
            "placeholder": self.placeholder,
            "disabled": self.disabled
        }

class PasswordInput(Component):
    def __init__(self, id, placeholder="", disabled=False):
        super().__init__(id=id)
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "password_input",
            "id": self.id,
            "placeholder": self.placeholder,
            "disabled": self.disabled
        }

class NumberInput(Component):
    def __init__(self, id, min_val=0, max_val=100, val=0, disabled=False):
        super().__init__(id=id)
        self.min_val = min_val
        self.max_val = max_val
        self.val = val
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "number_input",
            "id": self.id,
            "min": self.min_val,
            "max": self.max_val,
            "value": self.val,
            "disabled": self.disabled
        }

class Checkbox(Component):
    def __init__(self, id, label="", checked=False, disabled=False):
        super().__init__(id=id)
        self.label = label
        self.checked = checked
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "checkbox",
            "id": self.id,
            "label": self.label,
            "checked": self.checked,
            "disabled": self.disabled
        }

class CheckboxGroup(Component):
    def __init__(self, id, options=None, disabled=False):
        super().__init__(id=id)
        self.options = options or []
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "checkbox_group",
            "id": self.id,
            "options": self.options,
            "disabled": self.disabled
        }

class Radio(Component):
    def __init__(self, id, label="", checked=False, disabled=False):
        super().__init__(id=id)
        self.label = label
        self.checked = checked
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "radio",
            "id": self.id,
            "label": self.label,
            "checked": self.checked,
            "disabled": self.disabled
        }

class RadioGroup(Component):
    def __init__(self, id, options=None, disabled=False):
        super().__init__(id=id)
        self.options = options or []
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "radio_group",
            "id": self.id,
            "options": self.options,
            "disabled": self.disabled
        }

class Select(Component):
    def __init__(self, id, options=None, selected=None, disabled=False):
        super().__init__(id=id)
        self.options = options or []
        self.selected = selected
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "select",
            "id": self.id,
            "options": self.options,
            "selected": self.selected,
            "disabled": self.disabled
        }

class MultiSelect(Component):
    def __init__(self, id, options=None, selected=None, disabled=False):
        super().__init__(id=id)
        self.options = options or []
        self.selected = selected or []
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "multiselect",
            "id": self.id,
            "options": self.options,
            "selected": self.selected,
            "disabled": self.disabled
        }

class Slider(Component):
    def __init__(self, id, min_val=0, max_val=100, val=50, disabled=False):
        super().__init__(id=id)
        self.min_val = min_val
        self.max_val = max_val
        self.val = val
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "slider",
            "id": self.id,
            "min": self.min_val,
            "max": self.max_val,
            "value": self.val,
            "disabled": self.disabled
        }

class Switch(Component):
    def __init__(self, id, label="", active=False, disabled=False):
        super().__init__(id=id)
        self.label = label
        self.active = active
        self.disabled = disabled

    def to_dict(self):
        return {
            "type": "switch",
            "id": self.id,
            "label": self.label,
            "active": self.active,
            "disabled": self.disabled
        }

class DatePicker(Component):
    def __init__(self, id, disabled=False):
        super().__init__(id=id)
        self.disabled = disabled

    def to_dict(self):
        return {"type": "datepicker", "id": self.id, "disabled": self.disabled}

class TimePicker(Component):
    def __init__(self, id, disabled=False):
        super().__init__(id=id)
        self.disabled = disabled

    def to_dict(self):
        return {"type": "timepicker", "id": self.id, "disabled": self.disabled}

# --- Feedback & Status ---

class ProgressBar(Component):
    def __init__(self, id, visible=True, value=0):
        super().__init__(id=id)
        self.visible = visible
        self.value = value

    def to_dict(self):
        return {
            "type": "progress_bar",
            "id": self.id,
            "visible": self.visible,
            "value": self.value
        }

class Spinner(Component):
    def __init__(self, id=None, size="medium"):
        super().__init__(id=id)
        self.size = size

    def to_dict(self):
        d = {"type": "spinner", "size": self.size}
        if self.id: d["id"] = self.id
        return d

class Alert(Component):
    def __init__(self, text, id=None, level="info"):
        super().__init__(id=id)
        self.text = text
        self.level = level

    def to_dict(self):
        d = {"type": "alert", "text": self.text, "level": self.level}
        if self.id: d["id"] = self.id
        return d

class Toast(Component):
    def __init__(self, text, id=None, duration=3000):
        super().__init__(id=id)
        self.text = text
        self.duration = duration

    def to_dict(self):
        d = {"type": "toast", "text": self.text, "duration": self.duration}
        if self.id: d["id"] = self.id
        return d

class Tooltip(Component):
    def __init__(self, text, id=None):
        super().__init__(id=id)
        self.text = text

    def to_dict(self):
        d = {"type": "tooltip", "text": self.text}
        if self.id: d["id"] = self.id
        return d

class Avatar(Component):
    def __init__(self, src, id=None, size="medium"):
        super().__init__(id=id)
        self.src = src
        self.size = size

    def to_dict(self):
        d = {"type": "avatar", "src": self.src, "size": self.size}
        if self.id: d["id"] = self.id
        return d

class Skeleton(Component):
    def __init__(self, id=None, shape="row"):
        super().__init__(id=id)
        self.shape = shape

    def to_dict(self):
        d = {"type": "skeleton", "shape": self.shape}
        if self.id: d["id"] = self.id
        return d

class Metric(Component):
    def __init__(self, label, value, id=None, trend=None):
        super().__init__(id=id)
        self.label = label
        self.value = value
        self.trend = trend

    def to_dict(self):
        d = {"type": "metric", "label": self.label, "value": self.value}
        if self.trend: d["trend"] = self.trend
        if self.id: d["id"] = self.id
        return d

# --- Advanced Data Display ---

class Table(Container):
    def to_dict(self):
        d = {"type": "table", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class TableHeader(Container):
    def to_dict(self):
        d = {"type": "table_header", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class TableRow(Container):
    def to_dict(self):
        d = {"type": "table_row", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class TableCell(Container):
    def to_dict(self):
        d = {"type": "table_cell", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class List(Container):
    def to_dict(self):
        d = {"type": "list", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class ListItem(Container):
    def to_dict(self):
        d = {"type": "list_item", "children": [c.to_dict() for c in self.children]}
        if self.id: d["id"] = self.id
        return d

class ImageGrid(Component):
    def __init__(self, id, images=None, action_event="select_wallpaper"):
        super().__init__(id=id)
        self.images = images or []
        self.action_event = action_event

    def to_dict(self):
        return {
            "type": "image_grid",
            "id": self.id,
            "images": self.images,
            "action_event": self.action_event
        }

class LineChart(Component):
    def __init__(self, id, data=None):
        super().__init__(id=id)
        self.data = data or []

    def to_dict(self):
        return {"type": "line_chart", "id": self.id, "data": self.data}
