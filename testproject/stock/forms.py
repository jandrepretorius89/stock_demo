'''
Forms for stock and stock levels
'''

from django import forms
from stock.models import StockItem, StockLevel
#==============================================================================
class StockForm(forms.ModelForm):
    """
    Form for creating/editing stock items 
    """
    def __init__(self, *args, **kwargs):

        self.existing_flag = kwargs.pop('existing_flag') if 'existing_flag' in kwargs else None
        super(StockForm, self).__init__(*args, **kwargs)

    #--------------------------------------------------------------------------
    class Meta:
        model = StockItem
        fields = ('name', 'abbreviation', 'trade_name', 'description', 'class_name', 'cas_number', 'va_class')
    #--------------------------------------------------------------------------
    def clean_name(self):
        existing = StockItem.objects.filter(name=self.cleaned_data['name'])
        if not self.existing_flag:
            if self.cleaned_data['name'] == '':
                raise forms.ValidationError('Please add a unique name')

            if existing:
                raise forms.ValidationError('%s is an existing stock item.' % str(existing[0].name))

    #--------------------------------------------------------------------------
    def clean_abbreviation(self):
        if self.cleaned_data['abbreviation'] == '':
            raise forms.ValidationError('Please add an abbreviation')

    #--------------------------------------------------------------------------
    def clean_trade_name(self):
        if self.cleaned_data['trade_name'] == '':
            raise forms.ValidationError('No trade_name entered')

    #--------------------------------------------------------------------------
    def clean_class_name(self):
        if self.cleaned_data['class_name'] == '':
            raise forms.ValidationError('No class name entered')

    #--------------------------------------------------------------------------
    def clean_cas_number(self):
        existing = StockItem.objects.filter(name=self.cleaned_data['cas_number'])
        if self.cleaned_data['cas_number'] == '':
            raise forms.ValidationError('Please enter a CAS number')

        if existing:
            raise forms.ValidationError('The CAS number selected has already been used.')
    #--------------------------------------------------------------------------
    def clean_va_class(self):
        if self.cleaned_data['va_class'] == '':
            raise forms.ValidationError('Please enter a VA class')

    #--------------------------------------------------------------------------
    def save(self, existing_item):

        if existing_item:

            if existing_item.name != self.data['name'].strip():
                existing_item.name = self.data['name'].strip()

            existing_item.abbreviation = self.data['abbreviation'].strip()
            existing_item.trade_name = self.data['trade_name'].strip()
            existing_item.description = self.data['description'].strip()
            existing_item.class_name = self.data['class_name'].strip()
            existing_item.cas_number = self.data['cas_number'].strip()
            existing_item.va_class = self.data['va_class'].strip()
            try:
                existing_item.save()
            except:
                raise forms.ValidationError('This is an existing stock item')
        else:
            StockItem.objects.create(
                name=self.data['name'].strip(),
                trade_name=self.data['trade_name'].strip(),
                abbreviation=self.data['abbreviation'].strip(),
                description=self.data['description'].strip(),
                class_name=self.data['class_name'],
                cas_number=self.data['cas_number'],
                va_class=self.data['va_class'],
            )


#==============================================================================
class StockLevelForm(forms.ModelForm):
    """
    Form for creating stock levels
    """
    def __init__(self, *args, **kwargs):

        super(StockLevelForm, self).__init__(*args, **kwargs)
        self.fields['stock_item'].queryset = StockItem.objects.exclude(active=False)
    #--------------------------------------------------------------------------
    class Meta:
        model = StockLevel
        fields = ('stock_item', 'minimum_level')
    #--------------------------------------------------------------------------
    def clean_minimum_level(self):
        if self.cleaned_data['minimum_level'] == '':
            raise forms.ValidationError('Please enter a minimum level')

        try:
            int(self.cleaned_data['minimum_level'])
        except:
            raise forms.ValidationError('Please enter a positive, whole integer')

    #--------------------------------------------------------------------------
    def clean_stock_item(self):
        if not self.cleaned_data['stock_item']:
            raise forms.ValidationError('Please select a stock item')
    #--------------------------------------------------------------------------
    def save(self, stock_item, facility):

        StockLevel.objects.create(
            stock_item=stock_item,
            facility=facility,
            current_level=0,
            minimum_level=self.data['minimum_level'],
        )


