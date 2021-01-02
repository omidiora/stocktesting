from django import forms
from .models import Stock



class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category', 'item_name' , 'quantity']

    # def clean_category(self):
    #     category=self.cleaned_data.get('category')
    #     if not category:
    #         raise forms.ValidationError('This field is requjired')

        # for instance in Stock.objects.all():
        #     raise forms.ValidationError('category is already created')
        # return category

    def clean_item_name(self):
        category=self.cleaned_data.get('item_name')
        if not category:
            raise forms.ValidationError('This field is requjired')



class StockSearchForm(forms.ModelForm):
    export_to_csv=forms.BooleanField(required=False)
    class Meta:
        model=Stock
        fields=['category', 'item_name' ]


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category', 'item_name'  , 'quantity']




class IssueForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['issue_quantity'  , 'issue_to']


class RecieveForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['recieve_quantity'  , 'recieve_to']


class ReOrderLevelForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['reorder_level']