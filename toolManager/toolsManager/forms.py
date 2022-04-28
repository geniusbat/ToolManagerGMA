from django import forms
from .models import *

class MaterialLabels(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return '%s' % obj.name

class MachinesForm(forms.ModelForm):
    materials = MaterialLabels(queryset=Materials.objects.all(), widget=forms.SelectMultiple)
    class Meta:
        model = Machine
        fields = Machine.getFieldNames()
    def __init__(self, *args, **kwargs):
        super(MachinesForm, self).__init__(*args, **kwargs)
        for key in Machine.notRequiredFields():
            self.fields[key].required = False

class ToolsForm(forms.ModelForm):
    materials = MaterialLabels(queryset=Materials.objects.all(), widget=forms.SelectMultiple)
    class Meta:
        model = Tool
        fields = Tool.getFieldNames()
        fields.remove("relations")
    def __init__(self, *args, **kwargs):
        super(ToolsForm, self).__init__(*args, **kwargs)
        for key in Tool.notRequiredFields():
            self.fields[key].required = False

class MaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = Materials.getFieldNames()
    def __init__(self, *args, **kwargs):
        super(MaterialsForm, self).__init__(*args, **kwargs)
        for key in Materials.notRequiredFields():
            self.fields[key].required = False
            