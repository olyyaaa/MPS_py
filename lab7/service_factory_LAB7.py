from DAL.user_api_connector_LAB7 import UserAPIConnector
from BLL.user_repository_LAB7 import UserRepository
from UI.user_interface_LAB7 import UserInterface

class ServiceFactory:
    @staticmethod
    def create_user_interface():
        api_connector = UserAPIConnector()  # Залежність для UserRepository
        user_repository = UserRepository(api_connector)  # Залежність для UserInterface
        return UserInterface(user_repository)  # Ін’єкція залежності у UserInterface
