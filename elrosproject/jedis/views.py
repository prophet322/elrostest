from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Planet, Jedi, Candidate, Tests,  Questions
from .forms import CandidateForm, JediForm


# Create your views here.
def index(request):
    return render(request, 'jedis/index.html')


def get_jedi(request):
    if request.GET.get('jedi'):
        jedi = get_object_or_404(Jedi, pk=request.GET['jedi'])
        request.session['jedi_id'] = jedi.pk
        candidate_list = Candidate.objects.filter(planet=jedi.planet).exclude(jedi=jedi.pk)

        return render(request, 'jedis/jedi_candidate_list.html', {'candidate_list': candidate_list})
    else:
        jedi_list = Jedi.objects.all()
        # form = JediForm()
        return render(request, 'jedis/jedi_list.html', {'jedi_list': jedi_list})



def candidate_list(request):
    tests = Candidate.objects.filter(planet=request.session['jedi_planet'])
    if request.method == "POST":
        return render(request, 'jedis/index.html')
    else:
        form = CandidateForm()


def get_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save()
            request.session['usr_id'] = candidate.pk
            # candidate = form.save(commit=False)
            # candidate.published_date = candidate.now()
            return redirect(test_candidate)
        else:
            return render(request, 'jedis/candidate_form.html', {'form': form})
    else:
        form = CandidateForm()
        return render(request, 'jedis/candidate_form.html', {'form': form} )


def test_candidate(request):
    if request.method == "POST":
        post = request.POST
        if post['user_id']:
            answers_list = list()
            for x in post.items():
                if x[0].startswith('checkbox.'):
                    test_id = x[0][9:]
                    question = get_object_or_404(Questions, pk=test_id)
                    answer = '{}-{}'.format(question.text, x[1])
                    answers_list.append(answer)
            answers = '|'.join(answers_list)

            candidat = get_object_or_404(Candidate, pk=post['user_id'])
            candidat.answers = answers
            candidat.save()
            return render(request, 'jedis/candidate_test_complit.html', {'candidat':candidat})
    else:
        user_id = request.session.get('usr_id')
        tests = Tests.objects.prefetch_related().all()
        testList = []
        for test in tests:
            values = test.questions_set.values_list()
            testList.append([test.ordercode,values])
        return render(request, 'jedis/candidate_test.html', {'tests': testList, 'user_id':user_id})


def results(request, question_id):
    planet = get_object_or_404(Planet, pk=question_id)
    return render(request, 'jedis/index.html')