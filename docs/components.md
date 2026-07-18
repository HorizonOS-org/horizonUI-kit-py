# UI Components Reference

`horizonUI-kit` comes with a comprehensive set of layout elements, controls, form inputs, and informational displays.

## 1. Container & Layout Components

Containers are components that can hold other components.

### Column
A vertical layout container.
```python
hz.Column(id=None)
```
- **Example**:
  ```python
  with app.add(hz.Column()) as col:
      col.add(hz.Text("Item 1"))
      col.add(hz.Text("Item 2"))
  ```

### Row
A horizontal layout container.
```python
hz.Row(id=None)
```

### Grid & GridItem
A responsive multi-column layout grid.
```python
hz.Grid(id=None, columns=3, gap="10px")
hz.GridItem(id=None, colspan=1)
```
- **Example**:
  ```python
  with app.add(hz.Grid(columns=2)) as grid:
      with grid.add(hz.GridItem(colspan=2)):
          hz.Text("Header spanning 2 columns")
      grid.add(hz.Text("Column 1"))
      grid.add(hz.Text("Column 2"))
  ```

### Card
A grouped block with an optional title and border.
```python
hz.Card(id=None, title="Card Title")
```

### Section
A container for grouping related items under a title and subtitle.
```python
hz.Section(id=None, title="Section Title", subtitle="Section Subtitle")
```

### ScrollArea
A container that enables scrolling for long contents.
```python
hz.ScrollArea(id=None)
```

### Tabs & TabItem
Tabbed interface layouts.
```python
hz.Tabs(id=None)
hz.TabItem(id=None, label="Tab Name")
```

---

## 2. Basic Controls and Media

### Text
Renders text contents.
```python
hz.Text(text, id=None)
```

### Button
A standard push button. Triggers a click event matching `{id}_click`.
```python
hz.Button(label, id=None)
```

### IconButton
A button representing an icon without textual label.
```python
hz.IconButton(icon, id=None)
```

### Link
An anchor tag for navigation.
```python
hz.Link(label, url, id=None)
```

### Badge & Tag
Small status markers or tags.
```python
hz.Badge(label, type="default") # types: default, success, warning, danger
hz.Tag(label)
```

### Image & Video & Audio
Media components.
```python
hz.Image(src, alt=None, id=None)
hz.Video(src, controls=True, id=None)
hz.Audio(src, controls=True, id=None)
```

---

## 3. Form Inputs

### Input
Single line text input field.
```python
hz.Input(id, placeholder="", value="", focus=False)
```

### TextArea
Multiline text inputs.
```python
hz.TextArea(id, placeholder="", value="")
```

### Checkbox & CheckboxGroup
Selectable binary state options.
```python
hz.Checkbox(id, label, checked=False)
hz.CheckboxGroup(id, options=None)
```

### Radio & RadioGroup
Single choice selectable options.
```python
hz.Radio(id, label, checked=False)
hz.RadioGroup(id, options=None)
```

### Select & MultiSelect
Dropdown dropdowns.
```python
hz.Select(id, options=None, value=None)
hz.MultiSelect(id, options=None, values=None)
```

### Switch
Toggle switches.
```python
hz.Switch(id, label="", checked=False)
```

### Slider
Numeric range inputs.
```python
hz.Slider(id, min=0, max=100, value=50, step=1)
```

---

## 4. Status and Feedback

### ProgressBar
Visual progress indicator.
```python
hz.ProgressBar(value=0, max=100)
```

### Spinner
A loading indicator.
```python
hz.Spinner(size="medium")
```

### Alert
Notice messages.
```python
hz.Alert(message, type="info") # info, success, warning, error
```
