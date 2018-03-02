class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return self.title
