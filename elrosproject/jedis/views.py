from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Count

from .models import Planet, Jedi, Candidate, Tests,  Questions
from .forms import CandidateForm, JediForm


def SendMail(title='Jedi Academy',text='Вас успешно записали в падаваны', recepient = 'test@test.com'):
    ''' Отправка сообщений на почту о поступлении кандидатам'''
    send_mail(
            title,
            text,
            settings.EMAIL_HOST_USER,
            [recepient],
            fail_silently=False,
            )
    return None


# Create your views here.
def index(request):
    '''This HomePage'''
    request.session.clear()
    return render(request, 'jedis/index.html')


def get_jedi(request):
    if request.GET.get('jedi'):
        if request.GET.get('jedi') == 'All':
            jedi_list = Jedi.objects.all()
            return render(request, 'jedis/jedi_list_all.html', {'jedi_list': jedi_list})
        elif request.GET.get('jedi') == 'Dj':
            jedis = Jedi.objects.annotate(candidate_count=Count('candidate')).filter(candidate_count__gt=1)
            return render(request, 'jedis/jedi_list_all.html', {'jedi_list': jedis})
        else:
            jedi = get_object_or_404(Jedi, pk=request.GET['jedi'])
            request.session['jedi_id'] = jedi.pk
            candidate_list = Candidate.objects.filter(planet=jedi.planet, jedi=None)
            num = False if len(jedi.candidate_set.values_list()) >= 3 else True
            return render(request, 'jedis/jedi_candidate_list.html', {'candidate_list':candidate_list, 'num':num})
    else:
        jedi_list = Jedi.objects.all()
        return render(request, 'jedis/jedi_list.html', {'jedi_list':jedi_list})


def candidate_view(request, candidat_id=0):
    if candidat_id > 0:
        if request.method == "GET":
            candidat = get_object_or_404(Candidate, pk=candidat_id)
            candidat.answers = candidat.get_answers()
            return render(request, 'jedis/candidate_view.html', {'candidat': candidat})

        if request.method == "POST" and request.session.get('jedi_id'):
            candidat = get_object_or_404(Candidate, pk=candidat_id)
            jedi = get_object_or_404(Jedi, pk=request.session.get('jedi_id'))
            candidat.jedi = jedi
            candidat.save()
            mailstat = SendMail(
                'Jedi Academy',
                'Вас успешно записали в падаваны к джедаю {}'.format(jedi.name),
                candidat.email,
                )
            return redirect(get_jedi)

    else:
        return redirect(get_jedi)


def get_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save()
            request.session['usr_id'] = candidate.pk
            return redirect(test_candidate)
        else:
            return render(request, 'jedis/candidate_form.html', {'form': form})

    else:
        form = CandidateForm()
        return render(request, 'jedis/candidate_form.html', {'form': form} )


def test_candidate(request):
    user_id = request.session.get('usr_id')
    if request.method == "POST" and user_id:
        post = request.POST
        answers_list = list()
        for x in post.items():
            if x[0].startswith('checkbox.'):
                test_id = x[0][9:]
                question = get_object_or_404(Questions, pk=test_id)
                answer = {'answer':question.text, 'checkbox':x[1]}
                answers_list.append(answer)

        candidat = get_object_or_404(Candidate, pk=post['user_id'])
        candidat.set_answers(answers_list)
        candidat.save()
        return render(request, 'jedis/candidate_test_complit.html', {'candidat':candidat})

    elif request.method == "GET" and user_id:
        tests = Tests.objects.prefetch_related().all()
        testList = []
        for test in tests:
            values = test.questions_set.values_list()
            testList.append([test.ordercode, values])
        return render(request, 'jedis/candidate_test.html', {'tests': testList, 'user_id':user_id})

    else:
        return redirect(index)

