import urllib2
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from alexwebsite.awttest.models import *

# Create your views here.

def login(request):
    errors = []
    if 'name' in request.GET:
        name = request.GET['name']
        if not name:
            errors.append('Enter a username')
            return render_to_response('start.html', {'errors': errors})
        else:
            request.session['username'] = name
            request.session['question_number'] = 1
            return render_to_response('instructions1.html')
    return render_to_response('start.html')

def question(request):
    question_number = request.session['question_number']
    print question_number
    curr_form = 'question' + str(question_number) + '.html'
    if question_number == 5:
        next_form = 'instructions2.html'
    elif question_number == 8:
        next_form = 'instructions3.html'
    elif question_number == 13:
        next_form = 'done.html'
    else:
        next_form = 'question' + str(question_number + 1) + '.html'
    print 'curr_form: ' + curr_form
    print 'next_form: ' + next_form
    errors = []
    if 'answer' in request.GET:
        a = request.GET['answer']
        if not a:
            errors.append('Enter an answer.')
            return render_to_response(curr_form, {'errors': errors})
        else:
            try:
                val = float(a)
            except ValueError:
                errors.append('Enter an integer answer.')
            if not len(errors) == 0:
                return render_to_response(curr_form, {'errors': errors})
            else:
                name = request.session['username']
                request.session['question_number'] += 1
                question = int(question_number)
                answer = int(a)
                new = Response(name=name, question=question, answer=answer)
                new.save()
                question_number
                return render_to_response(next_form)
    else:
        return render_to_response(curr_form)