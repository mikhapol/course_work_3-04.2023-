class Currency:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        if self.name is not None:
            return self.name
        return ""
