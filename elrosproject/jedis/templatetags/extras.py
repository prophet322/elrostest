from django import template
from django.db.models import Count
from ..models import Jedi, Candidate
register = template.Library()

@register.filter(name='candidate_len')
def candidate_len(value):
    return len([x for x in Jedi.objects.filter(pk=value).values('candidate__name') if x['candidate__name']])
# coun = Jedi.objects.filter(pk=1).annotate(jedi_count=Count('candidate'))

@register.filter(name='candidate_planet')
def candidate_planet(value):
    return len(Candidate.objects.filter(planet=value, jedi=None))