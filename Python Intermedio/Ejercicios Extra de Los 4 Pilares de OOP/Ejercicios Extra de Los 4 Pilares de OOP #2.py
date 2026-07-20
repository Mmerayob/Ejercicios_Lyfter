# Cree una clase abstracta User con los siguientes métodos abstractos:
# get_role()
# has_permission(permission)
# Luego cree dos clases que hereden de ella:
# AdminUser
# RegularUser
# Cada una debe implementar los métodos
# Por ejemplo:
# AdminUser siempre tiene permisos
# RegularUser solo tiene permisos limitados

from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self,permission):
        pass


class AdminUser(User):
    def get_role(self):
        return "Admin"

    def has_permission(self,permission):
        return True

class RegularUser(User):
    def get_role(self):
        return "Regular"

    def has_permission(self,permission):
        return False
    

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))
print(user2.has_permission("delete"))


