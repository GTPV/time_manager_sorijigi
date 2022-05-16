from django import forms
from .models import *

class CreateNewTime(forms.ModelForm):

    class Meta:
        model = TimeInfo
        fields = '__all__'
        widgets ={
            'time_date' : forms.DateInput(attrs={'type': 'date'}),
            'time_start' : forms.TimeInput(attrs={'type' : 'time'}),
            'time_end' : forms.TimeInput(attrs={'type' : 'time'}),
        }
        labels = {
            'time_date' : "타임 일자",
            'time_start' : "타임 시작시간",
            'time_end' : "타임 종료시간",
            'time_manager' : "타임 운영자",
        }

class AddMusic(forms.ModelForm):

    class Meta:
        model = Music
        exclude = ('time_info',)
        #fields = '__all__'
        widgets = {
            'music_request' : forms.CheckboxInput(attrs={'type' : 'checkbox'}),
        }
        labels = {
            'music_request' : "신청곡",
            'music_source' : "음원 종류",
            'music_label_id' : "음반 번호",
            'music_composer' : "작곡가",
            'music_title' : "제목",
            'music_conductor' : "지휘자",
            'music_orchestra' : "오케스트라",
        }

class AddPlayer(forms.Form):
    _player_list = forms.CharField(max_length=500, required=False, label="연주자 리스트")

class FilterTime(forms.Form):
    _time_date = forms.DateField()

class UpdateBreaktime(forms.Form):
    _time_start = forms.CharField()
    _time_end = forms.CharField()