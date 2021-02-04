from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login,logout
from .models import Question_model,Question_model2,Question_model3,User


def create_user(request):
    if request.method == 'POST':
        username = request.POST['username_data']
        password = request.POST['password_data']
        email = request.POST['email_data']
        try:
            User.objects.create_user(username,email,password)
        except IntegrityError:
            return render(request,'create_user.html',{'error':'このユーザーは既に登録されています。'})    

    else:
        return render(request,'create_user.html',{})
    return render(request,'complete.html',{})

def loginview(request):
    
    if request.method == 'POST':
        username_data = request.POST['username_data']    
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return render(request,'start.html',{})
        else:
            return render(request,'login.html',{'error':'ユーザー名もしくはパスワードが間違っています'})
    return render(request,'login.html')   

def question1(request):

#countは問題数、numberは正解数

    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
        
    record=Question_model.objects.get(pk=request.session['count'])
    if not 'number' in request.session:
        request.session['number']=0
    number=request.session['number']

    request.session['level']=1
    

    return render(request,'question.html',{'model':record,'number':number})

def question2(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
        
    record=Question_model2.objects.get(pk=request.session['count'])
    if not 'number' in request.session:
        request.session['number']=0
    number=request.session['number']

    request.session['level']=2

    return render(request,'question2.html',{'model':record,'number':number})   

def question3(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1
        
    record=Question_model3.objects.get(pk=request.session['count'])
    if not 'number' in request.session:
        request.session['number']=0
    number=request.session['number']

    request.session['level']=3

    return render(request,'question3.html',{'model':record,'number':number})

def answer(request,correct):
    record=Question_model.objects.get(pk=request.session['count'])

    if record.answer == correct:
        print(record.answer)
        print(correct)
        request.session['number']+=1
        plg=1
        

    else:
        print(record.answer)
        print(correct)
        plg=0

    
    flg=0    

    
    if Question_model.objects.all().count() == request.session['count']:
        request.session['count'] = 0
        flg=1

    
    number=request.session['number']
    
    
    return render(request,'answer.html',{'model':record,'number':number,'flg':flg,'plg':plg})

def answer2(request,correct):
    record=Question_model2.objects.get(pk=request.session['count'])

    if record.answer == correct:
        print(record.answer)
        print(correct)
        request.session['number']+=1
        plg=1
        

    else:
        print(record.answer)
        print(correct)
        plg=0

    
    flg=0    

    
    if Question_model2.objects.all().count() == request.session['count']:
        request.session['count'] = 0
        flg=1

    
    number=request.session['number']
    
    
    return render(request,'answer2.html',{'model':record,'number':number,'flg':flg,'plg':plg})    

def answer3(request,correct):
    record=Question_model3.objects.get(pk=request.session['count'])

    if record.answer == correct:
        print(record.answer)
        print(correct)
        request.session['number']+=1
        plg=1
        

    else:
        print(record.answer)
        print(correct)
        plg=0

    
    flg=0    

    
    if Question_model3.objects.all().count() == request.session['count']:
        request.session['count'] = 0
        flg=1

    
    number=request.session['number']
    
    
    return render(request,'answer3.html',{'model':record,'number':number,'flg':flg,'plg':plg})      

def result(request):
    result=request.session['number'] 
    if result >= 15:
        blg=1
    else:
        blg=0

    score=User.objects.get(username=request.user)
    
    

     
    
    request.session['number'] =0 
    request.session['count'] = 0  
    return render(request,'result.html',{'result':result,'blg':blg,})

def start(request):
    #request.session['count']=1
    return render(request,'start.html')

def top(request):
    return render(request,'top.html')

def complete(request):
    return render(request,'complete.html')

def logoutview(request):
    logout(request)
    return redirect('top')   







    


# Create your views here.
