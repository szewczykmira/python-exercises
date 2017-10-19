class Widget:
    def __init__(self, name):
        self.name = name
        self.dependencies = []

    def add_dependency(self, *args):
        self.dependencies.extend(args)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def build(self):
        return ', '.join([str(dep) for dep in self.dependencies])
