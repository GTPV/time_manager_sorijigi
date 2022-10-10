import uuid
from django.db import models

# Create your models here.
class TimeInfo(models.Model):
    time_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    time_manager = models.CharField(max_length=100)
    time_manager_time = models.CharField(max_length=100)
    time_unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'일시 : {self.time_date:%y/%m/%d} {self.time_start:%H:%M}~{self.time_end:%H:%M}, 타임 운영자 : {self.time_manager}, 출근 시간 : {self.time_manager_time}'

    class Meta:
        verbose_name = '타임 정보'
        verbose_name_plural = '타임 정보'
        ordering = ['-time_date', '-time_start']

class Music(models.Model):
    time_info = models.ForeignKey(TimeInfo, on_delete=models.CASCADE)

    
    music_request = models.BooleanField(default=False)
    music_source = models.CharField(max_length=100, default='ROON')
    music_label_id = models.CharField(max_length=50, blank=True, default='해당 없음')
    music_composer = models.CharField(max_length=100)
    music_title = models.CharField(max_length=200)
    music_conductor = models.CharField(max_length=100, blank=True, default='해당 없음')
    music_orchestra = models.CharField(max_length=200, blank=True, default='해당 없음')

    def __str__(self):
        return f'{self.music_composer}, {self.music_title}'

    class Meta:
        verbose_name='곡 정보'
        verbose_name_plural='곡 정보'
        ordering=['id', 'music_composer', 'music_title']

class Player(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    player_name = models.CharField(max_length=100, default='연주자이름')
    player_instrument = models.CharField(max_length=100, blank=True, default='악기')

    class Meta:
        verbose_name='연주자'
        verbose_name_plural='연주자'
        ordering=['id', 'player_name']