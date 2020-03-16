from django import template
from ..models import Jedi, Candidate
register = template.Library()

@register.filter(name='candidate_len')
def candidate_len(jedi_id):
    '''Возвращает количество падаванов у джедая'''
    try:
        return Jedi.objects.get(pk=jedi_id).candidate_set.all().count()
    except:
        return 0


@register.filter(name='candidate_planet')
def candidate_planet(planet_id):
    ''' Возвращяет количество кандидатов на данной планете
     (еще не зачисленных в падаваны) '''
    try:
        return Candidate.objects.filter(planet=planet_id, jedi=None).count()
    except:
        return 0
