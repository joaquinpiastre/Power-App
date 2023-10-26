from app.services.command import TareaCommand

class UserBalance(TareaCommand):
    
    def __init__(self, country):
        self.country = country
        pass

    def execute(self, model):
        self.model = model 
    
    def send_bill(self):
        print("Envio facturación de {model.name} suscripcion VIP")
    
#TODO: Buscar como validar el pais por la IP