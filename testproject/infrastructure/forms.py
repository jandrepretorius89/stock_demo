'''
Forms for infrastructure. 
'''

from django import forms
from infrastructure.models import Facility
from general.models import District
#==============================================================================
class FacilityForm(forms.ModelForm):
    """
    Basic form to create/edit an facility object
    """
    def __init__(self, *args, **kwargs):
        # Determine if we're editing or creating
        self.existing_flag = kwargs.pop('existing_flag') if 'existing_flag' in kwargs else None

        super(FacilityForm, self).__init__(*args, **kwargs)


    #--------------------------------------------------------------------------
    class Meta:
        model = Facility
        fields = ('name', 'abbreviation', 'type', 'postal_address', 'district',)
    #--------------------------------------------------------------------------
    def clean_name(self):
        # Don't want facilities with duplicate names
        existing = Facility.objects.filter(name=self.cleaned_data['name'])
        if not self.existing_flag:
            if self.cleaned_data['name'] == '':
                raise forms.ValidationError('Please add a unique name')

            if existing:
                raise forms.ValidationError('%s is an existing  facility.' % str(existing[0].name))

    #--------------------------------------------------------------------------
    def clean_abbreviation(self):
        if self.cleaned_data['abbreviation'] == '':
            raise forms.ValidationError('Please add an abbreviation')

    #--------------------------------------------------------------------------
    def clean_type(self):
        if self.cleaned_data['type'] == '':
            raise forms.ValidationError('No type selected')

    #--------------------------------------------------------------------------
    def clean_district(self):
        existing = District.objects.filter(name=self.cleaned_data['district'])
        if self.cleaned_data['district'] == '':
            raise forms.ValidationError('No district selected')

        if not existing:
            raise forms.ValidationError('Invalid district selected')

    #--------------------------------------------------------------------------
    def clean_postal_address(self):
        if self.cleaned_data['postal_address'] == '':
            raise forms.ValidationError('Please enter an address')

    #--------------------------------------------------------------------------
    def save(self, existing_facility):
        """
        Create a facility of update an existing one
        """

        existing = District.objects.filter(pk=int(self.data['district']))

        if existing_facility:

            if existing_facility.name != self.data['name'].strip():
                existing_facility.name = self.data['name'].strip()

            existing_facility.abbreviation = self.data['abbreviation'].strip()
            existing_facility.postal_address = self.data['postal_address'].strip()
            existing_facility.type = self.data['type'].strip()
            existing_facility.district = existing[0]
            try:
                existing_facility.save()
            except:
                raise forms.ValidationError('This is an existing facility')
        else:
            Facility.objects.create(
                name=self.data['name'].strip(),
                abbreviation=self.data['abbreviation'].strip(),
                postal_address=self.data['postal_address'].strip(),
                type=self.data['type'],
                district=existing[0],
            )

