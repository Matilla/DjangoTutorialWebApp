from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.http import Http404

""" Se definen las vistas que se corresponden a las URLS descritas en polls/urls """


"""def index(request):"""
""" Code before applying HTML template
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    """
""" Code after using Django HTML template
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    """
""" Improved used of Django render templates """
'''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
'''
def detail(request, question_id):
'''
""" Original Code
    return HttpResponse("You're looking at question %s." % question_id)
    """
""" Introduce HTTP 404 exceptions
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    """
""" Improved code using helper function get_object_or_404 """
'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''
'''
def results(request, question_id):
'''
""" Original code
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    """
'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
''' 
''' Se utilizan las vistas genericas para index, detail y results ''' 

def vote(request, question_id):
    """ Original code
    return HttpResponse("You're voting on question %s." % question_id) """
    """ In this code there is a race condition, two user voting at the same time might get the same value for the vote count, so instead of a plus 2 we could end up with a plus 1"""
    """ To solve this issue take a look at https://docs.djangoproject.com/en/2.0/ref/models/expressions/#avoiding-race-conditions-using-f """ 
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' """ Se necesita pasar el context_object_name porque por defecto, no se porque, se usaria question_id"""

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

""" No se necesita pasar el context_object_name porque por defecto coge el question_id ya que el modelo es question."""
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'