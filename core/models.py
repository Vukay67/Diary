from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=50, verbose_name="Дисциплины")
    
    def __str__(self):
        return f"{self.name}"

class Day(models.Model):
    WEEK_DAYS = [
    ['Понедельник', 'Понедельник'],
    ['Вторник', 'Вторник'],
    ['Среда', 'Среда'],
    ['Четверг', 'Четверг'],
    ['Пятница', 'Пятница'],
    ['Суббота', 'Суббота'],
    ['Воскресенье', 'Воскресенье'],
]
    name = models.CharField(max_length=11, choices=WEEK_DAYS,  verbose_name="Называние")
    sub = models.ManyToManyField(Subjects, max_length=50, verbose_name="Дисциплины", null=True, blank=True)
    
    def __str__(self):
        return f"Добавлен день недели: {self.name}"
   
class Time(models.Model):
    start = models.TimeField(verbose_name="Начало")
    end = models.TimeField(verbose_name="Конец")
    sub = models.ManyToManyField(Subjects, max_length=50, verbose_name="Дисциплины", blank=True, null=True)
    
    def __str__(self):
        return f"{self.start}, {self.end}"