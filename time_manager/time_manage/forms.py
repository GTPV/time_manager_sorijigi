from django import forms

class CreateNewTime(forms.Form):
    _time_manager = forms.CharField(label='manager', max_length=100)
    _time_date = forms.DateField(label='date')
    _time_start = forms.TimeField(label='start time')
    _time_end = forms.TimeField(label='end time')

class AddMusic(forms.Form):
    _music_request = forms.BooleanField(required=False)
    _music_source = forms.CharField(max_length=100)
    _music_label_id = forms.CharField(max_length=50, required=False, initial="해당 없음")
    _music_composer = forms.CharField(max_length=100)
    _music_title = forms.CharField(max_length=200)
    _music_conductor = forms.CharField(max_length=100, required=False, initial="해당 없음")
    _music_orchestra = forms.CharField(max_length=200, required=False, initial="해당 없음")

class FilterTime(forms.Form):
    _time_date = forms.DateField()