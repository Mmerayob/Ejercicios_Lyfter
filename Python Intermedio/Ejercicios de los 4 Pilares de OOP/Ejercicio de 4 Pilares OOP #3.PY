# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class ElectronicDevice:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"El dispositivo {self.brand} se ha encendido.")

class CommunicationMedium:
    def __init__(self, network_type):
        self.network_type = network_type
        self.is_connected = False

    def connect_to_network(self):
        self.is_connected = True
        print(f"Conectándose a la red {self.network_type}...")

class Smartphone(ElectronicDevice, CommunicationMedium):
    def __init__(self, brand, network_type, model):
        
        ElectronicDevice.__init__(self, brand)
        CommunicationMedium.__init__(self, network_type)

        self.model = model

    def use_phone(self):
        print(f"Estás usando un {self.brand} {self.model}.")


my_phone = Smartphone(brand="Samsung", network_type="5G", model="Galaxy S24")
my_phone.use_phone()