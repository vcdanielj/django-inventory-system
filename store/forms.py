import calculation
from core.layout import CancelButton, DeleteButton, Formset
from core.widgets import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Button, ButtonHolder, Column, Div, Fieldset,
                                 Layout, Row, Submit, Field)
from django import forms
from django.db.models import fields

from .models import Order, OrderDetail


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['type', 'date', 'supplier', 'buyer', 'observation']
        widgets = { 'date':DateInput }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(Column("type"), Column("date")),
            "supplier",
            "buyer",
            "observation",
            Fieldset(
                u'Artículos',
                Formset(
                    "OrderDetailInline"
                )
            ),
            Row(
                Div(Submit("submit", "Guardar"), HTML("""<a class="btn btn-secondary" href="{% url 'order_list' %}"> Cancelar</a>""" ))
            )
           
        )

class OrderDetForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['product']

