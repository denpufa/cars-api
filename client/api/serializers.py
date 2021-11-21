from rest_framework.serializers import ModelSerializer
from client.models import Client

class ClientSerializer(ModelSerializer) :
    class Meta :
        model = Client
        fields = [
            'username','phone','email','password'
        ]
    
    def	save(self):

        account = Client(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    phone=self.validated_data['phone']                   
                )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account 