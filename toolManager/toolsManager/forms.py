from django import forms
from .models import *

class MachinesForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = Machine.getFieldNames()
    def __init__(self, *args, **kwargs):
        super(MachinesForm, self).__init__(*args, **kwargs)
        for key in Machine.notRequiredFields():
            self.fields[key].required = False

class ArchetypesForm(forms.ModelForm):
    class Meta:
        model = ToolArchetype
        fields = ToolArchetype.getFieldNames()
        fields.remove("relation")
    def __init__(self, *args, **kwargs):
        super(ArchetypesForm, self).__init__(*args, **kwargs)
        for key in ToolArchetype.notRequiredFields():
            self.fields[key].required = False

class MaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = Materials.getFieldNames()
    def __init__(self, *args, **kwargs):
        super(MaterialsForm, self).__init__(*args, **kwargs)
        for key in Materials.notRequiredFields():
            self.fields[key].required = False
            