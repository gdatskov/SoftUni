class Storage:
    def __init__(self):
        self.__categories = []
        self.__topics = []
        self.__documents = []

    @property
    def categories(self):
        return self.__categories

    @property
    def topics(self):
        return self.__topics

    @property
    def documents(self):
        return self.__documents

    def add_category(self, category):
        if category not in self.__categories:
            self.__categories.append(category)

    def add_topic(self, topic):
        if topic not in self.__topics:
            self.__topics.append(topic)

    def add_document(self, document):
        if document not in self.__documents:
            self.__documents.append(document)

    def __get_category_by_id(self, category_id):
        for cat in self.__categories:
            if cat.id == category_id:
                return cat

    def __get_topic_by_id(self, topic_id):
        for topic in self.__topics:
            if topic.id == topic_id:
                return topic

    def get_document(self, doc_id):
        for doc in self.__documents:
            if doc.id == doc_id:
                return doc

    def edit_category(self, category_id, new_name):
        category = self.__get_category_by_id(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__get_topic_by_id(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__get_category_by_id(category_id)
        if category is not None:
            self.__categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_topic_by_id(topic_id)
        if topic is not None:
            self.__topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_document(document_id)
        if document is not None:
            self.__documents.remove(document)

    def __repr__(self):
        return "\n".join(str(doc) for doc in self.__documents)