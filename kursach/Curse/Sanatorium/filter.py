

from django_filters import  FilterSet, DateFilter, CharFilter, NumberFilter, ModelChoiceFilter,ChoiceFilter


from .models import *

class UserFilter(FilterSet):
    last_name = CharFilter(field_name='last_name', lookup_expr='contains', label='Фамилия')
    first_name = CharFilter(field_name='first_name', lookup_expr='contains', label='Имя')
    birth_date = DateFilter(field_name='birth_date', lookup_expr='contains', label='Дата рождения')
    class Meta:
        model = Users
        fields =['last_name','first_name','birth_date']


class ProgramFilter(FilterSet):
    program_name = CharFilter(field_name='name', lookup_expr='contains',label="Название программы")
    price =NumberFilter(field_name='price',lookup_expr='exact',label='Цена')
    class Meta:
        model = Program
        fields = ['price']

class RoomFilter(FilterSet):
    pk = NumberFilter(field_name='pk',lookup_expr='lte',label="Номер")
    type = ModelChoiceFilter(queryset=Type.objects.all(),label="Тип")
    class Meta:
        model = Room
        fields = ['pk','type']


class TypeFilter(FilterSet):
    type_name = CharFilter(field_name="name",lookup_expr='contains',label="Название типа" )
    price = NumberFilter(field_name="price",lookup_expr="exact",label="Цена")
    class Meta:
        model = Type
        fields = ['price']