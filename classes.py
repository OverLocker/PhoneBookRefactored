class Users:
    def __init__(self, id, name, phone, comment):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def search_by_user(self):
        pass

    def __repr__(self):
        pass

class DB:
    def __init__(self, db_file):
        self.db_file = db_file

    def load_db(self):
        pass

    def save_db(self):
        pass

class Menu:
    menu_items = []
    def __init__(self, menu_items):
        pass

