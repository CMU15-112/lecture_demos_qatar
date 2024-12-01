from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from io import StringIO   

from .models import Question

def index(request):
    question_list = Question.objects.order_by("-pub_date")
    context = {
        "question_list": question_list
    }
    return render(request, "polls/index.html", context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    voted_choice = request.POST["choice"]
    choice = question.choice_set.get(pk=voted_choice)
    
    choice.votes += 1
    choice.save()
    return HttpResponse("Thanks for voting")

def results_graph(question):
    choices = question.choice_set.all()
    labels = []
    sizes = [] 
    for choice in choices:
        labels.append(choice.choice_text)
        sizes.append(choice.votes)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    imgdata = StringIO()
    fig.savefig(imgdata, format="svg")
    imgdata.seek(0)
    return imgdata.getvalue()

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    pic = results_graph(question)
    return render(request, "polls/results.html", {"question": question, "pic": pic})

