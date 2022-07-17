from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, id, category_id, topic_id, file_name):
        self.__id = id
        self.__category_id = category_id
        self.__topic_id = topic_id
        self.__file_name = file_name
        self.__tags = []

    @property
    def id(self):
        return self.__id

    @property
    def category_id(self):
        return self.__category_id

    @property
    def topic_id(self):
        return self.__topic_id

    @property
    def file_name(self):
        return self.__file_name

    @property
    def tags(self):
        return self.__tags

    @classmethod
    def from_instances(cls, id, category, topic, file_name):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content not in self.__tags:
            self.__tags.append(tag_content)

    def remove_tag(self, tag_content):
        if tag_content in self.__tags:
            self.__tags.remove(tag_content)

    def edit(self, file_name):
        self.__file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"
