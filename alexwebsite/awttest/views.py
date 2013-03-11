import urllib2
import json
from datetime import *
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

def done(request):
    request.session['question_number'] = -1
    return render_to_response('done.html')

def question(request):
    question_number = request.session['question_number']
    curr_form = 'question' + str(question_number) + '.html'
    if question_number == 5:
        next_form = 'instructions2.html'
    elif question_number == 8:
        next_form = 'instructions3.html'
    elif question_number == 13:
        next_form = 'done.html'
    elif question_number == -1:
        return render_to_response('error_finished_quiz.html')
    else:
        next_form = 'question' + str(question_number + 1) + '.html'
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
                if question <= 8:
                    correct = check_answer(question, answer)
                else:
                    correct = None
                time = (datetime.now() - request.session['start_time']).seconds
                new = Response(name=name, question=question, answer=answer, correct=correct, time=time)
                new.save()
                request.session['start_time'] = datetime.now()
                if next_form == 'done.html':
                    done(request)
                return render_to_response(next_form)
    else:
        request.session['start_time'] = datetime.now()
        return render_to_response(curr_form)

def view_scores(request):
    responses = Response.objects.all()
    return render_to_response('view_scores.html', {'responses': responses})

def check_answer(question_number, answer):
    if question_number == 1:
        if answer == -5:
            return True
    elif question_number == 2:
        if answer == -3:
            return True
    elif question_number == 3:
        if answer == 17:
            return True
    elif question_number == 4:
        if answer == 16:
            return True
    elif question_number == 5:
        if answer == 22:
            return True
    elif question_number == 6:
        if answer == 16:
            return True
    elif question_number == 7:
        if answer == 4:
            return True
    elif question_number == 8:
        if answer == 29:
            return True
    else:
        return False
    return False