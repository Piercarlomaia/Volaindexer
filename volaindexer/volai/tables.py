import django_tables2 as tables
from .models import Rooms

class RoomsTable(tables.Table):
    class Meta:
        model = Rooms
