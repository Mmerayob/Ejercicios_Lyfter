#Cree una clase de User que:
# -Tenga un atributo de date_of_birth.
# -Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro que se 
#encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.


from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):

        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def age_validation(func):
    def wrapper(user):

        if user.age < 18:
            raise ValueError(f"El usuario tiene {user.age} años, no es mayor de edad")            

        return func(user)

    return wrapper


@age_validation
def age_validated(user):
    print(f"La edad {user.age} fue validada correctamente")


my_user1 = User(date(1990, 1, 1))
my_user2 = User(date(2010, 1, 1))

try:
    age_validated(my_user1)
    age_validated(my_user2)
    

except ValueError as error:
    print(f"Error: {error}")

