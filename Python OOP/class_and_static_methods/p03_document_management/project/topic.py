class Topic:
    def __init__(self, id, topic, storage_folder):
        self.__id = id
        self.__topic = topic
        self.__storage_folder = storage_folder

    @property
    def id(self):
        return self.__id

    @property
    def topic(self):
        return self.__topic

    @property
    def storage_folder(self):
        return self.__storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.__topic = new_topic
        self.__storage_folder = new_storage_folder

    def __repr__(self):
        return f"Topic {self.__id}: {self.__topic} in {self.__storage_folder}"
