from rest_framework.fields import BooleanField, FloatField, IntegerField, CharField
from rest_framework.serializers import ModelSerializer

from crm.models import Client, Contract, Event


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ContractSerializer(ModelSerializer):
    status = BooleanField(required=True)
    amount = FloatField(required=True)

    class Meta:
        model = Contract
        fields = '__all__'


class EventSerializer(ModelSerializer):
    attendees = IntegerField(required=True)
    notes = CharField(required=True)

    class Meta:
        model = Event
        fields = '__all__'
        # extra_kwargs = {'support_contact': {'required': False}}
