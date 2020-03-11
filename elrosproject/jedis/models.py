from django.db import models
import json


# My models here.
class Planet(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название", blank=False, db_index=True)

    class Meta:
        verbose_name_plural = "Список планет"

    def __str__(self):
        return self.name


class Jedi(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Имя")
    planet = models.ForeignKey(Planet, verbose_name=u"Планета", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Список Джидаев"

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.IntegerField(blank=False)
    email = models.EmailField(unique=True, blank=False)
    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE)
    answers = models.TextField(blank=True)

    def set_answers(self, x):
        self.answers = json.dumps(x)

    def get_answers(self):
        return json.loads(self.answers)

    def __str__(self):
        return self.name

class Tests(models.Model):
    ordercode = models.CharField(max_length=100, verbose_name=u"Код ордена", unique=True, blank=False)

    class Meta:
        verbose_name_plural = "Тестовое испытание падавана"

    def __str__(self):
        return 'Код ордена: {}'.format(self.ordercode)


class Questions(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u"Суть вопроса", blank=False)

    class Meta:
        verbose_name_plural = "Cписок вопросов"

    def __str__(self):
        return 'Cписок вопросов {}'.format(self.test.ordercode)
