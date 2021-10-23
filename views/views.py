from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.template import loader
from .models import Question


# Create your views here.
def funky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)


def danger(request):
    response = """<html><body>
    <p>Your guess was """+request.GET['guess']+"""</p>
    </body></html>"""
    return HttpResponse(response)


def game(request):
    response = """<html><body>
    <p>Your guess was """+escape(request.GET['guess'])+"""</p>
    </body></html>"""
    return HttpResponse(response)


def rest(request, guess):
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

# This is a command to the browser


def bounce(request):
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')

# https://docs.djangoproject.com/en/3.0/topics/class-based-views/


class MainView(View):
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)


class RestMainView(View):
    def get(self, request, guess):
        print("We got a slug from the URL", guess)
        response = """<html><body>
        <p>Your guess was """+escape(guess)+"""</p>
        </body></html>"""
        return HttpResponse(response)


# Added by IOAN

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('/polls/index.html')
    print(template)
    context = {'latest_question_list': latest_question_list, }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
