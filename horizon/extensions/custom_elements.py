from ..components import Component

# Example of a custom UI component:
class CustomCard(Component):
    """
    A custom component that developers can build, defining its own schema
    and serialize to JSON dict representation.
    """
    def __init__(self, id, title, description, icon=None):
        super().__init__(id=id)
        self.title = title
        self.description = description
        self.icon = icon

    def to_dict(self):
        return {
            "type": "custom_card",
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "icon": self.icon
        }
