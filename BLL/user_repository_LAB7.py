class UserRepository:
    def __init__(self, api_connector):
        self.api_connector = api_connector

    def get_all_users(self):
        """Отримує всіх користувачів через API-запит"""
        return self.api_connector.get_users()

    def get_user_posts(self, user_id):
        """Отримує пости конкретного користувача"""
        return self.api_connector.get_user_posts(user_id)

    def get_user_by_name(self, name):
        """Пошук користувача за ім'ям"""
        users = self.api_connector.get_users()
        for user in users:
            if user['name'].lower() == name.lower():
                return user
        return None  # Повертаємо None, якщо користувача з таким ім'ям не знайдено

