from .models import Supplier
import django_filters


class SupplierFilter(django_filters.FilterSet):

    class Meta:
        model = Supplier
        fields = ["SName"]