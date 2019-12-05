from django import forms
from .models import Town

# class town_form(forms.Form):
#     date = forms.DateTimeField(label='Date')
#     name = forms.CharField(label='Name', max_length=30)
#     phone = forms.IntegerField(label='Phone Number')
#     details_of_route = forms.CharField(label='Details of Route', max_length=50)
#     time_from = forms.TimeField(label='Time From')
#     time_to = forms.TimeField(label='Time To')
#     return_date = forms.DateTimeField(label='Return Date')
#     number_of_personnel = forms.IntegerField(label='Number of Personnel Enroute')
#     directorate = forms.ChoiceField(label='Directorate', choices=[('ED','ED'), ('DFA','DFA'), ('DNF','DNF')])
#     trans_officer = forms.ChoiceField(label='Approved by', choices=[('TO','TO')])


class town_form(forms.ModelForm):
    class Meta:
        model = Town
        fields = ['date', 'name', 'phone', 'details_of_route', 'time_from', 'time_to',
        'return_date', 'number_of_personnel', 'directorate', 'trans_officer']
        labels = {'date':'Date', 'phone':'Phone Number', 'details_of_route':'Details of Route',
        'time_from':'Time From', 'time_to':'Time To', 'return_date':'Return Date',
        'number_of_personnel':'Number of Personnel', 'directorate':'Directorate',
        'trans_officer':'Transport Officer'}
