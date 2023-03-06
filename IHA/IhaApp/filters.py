import django_filters
from django_filters import CharFilter

from .models import iha_property


class IhaPropertyFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs.update({'class': 'form-control'})

    ad_contain = CharFilter(field_name='ad', lookup_expr='icontains')
    marka_contain = CharFilter(field_name='marka', lookup_expr='icontains')

    class Meta:
        model = iha_property
        fields = '__all__'
        exclude = 'image'  # image filter yok
