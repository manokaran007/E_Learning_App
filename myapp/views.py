from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback.objects.create(name=name,email=email,message=message)
        return redirect('home')
    return render(request,'feedback.html')


def register(request):
    category = Category()
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pword = request.POST.get('password')
        age = request.POST.get('age')
        cho = request.POST.get('choice')
        print(age,cho)

        cuser=User.objects.create_user(uname,email,pword)

        Category.objects.create(user=uname,age=age,choice_field=cho)

        cuser.save()
        
        
        return redirect('user_login')
        
    return render(request,"register.html", {'category': category})

def user_login(request):
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        users = authenticate(request,username=uname,password=pword)
        print(uname,pword)
        print(users)
        if users is not None:
            login(request,users)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    a=request.user.username
    print(a)
    return render(request,'home.html')
def course(request):
    
    return render(request,'course.html')
def computer(request):
    return render(request,'computer/computer.html')

def com1(request):
    return render(request,'computer/1.html')


def com2(request):
    return render(request,'computer/2.html')

def com3(request):
    return render(request,'computer/3.html')

def com4(request):
    return render(request,'computer/4.html')

def com5(request):
    return render(request,'computer/5.html')

def com6(request):
    return render(request,'computer/6.html')

def com7(request):
    return render(request,'computer/7.html')

def com8(request):
    return render(request,'computer/8.html')

def comtest(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age
    if request.method == 'POST':
        if cat == "Blind":
            print("1")
            if num >= 7: 
                print("2")
                questions=NComputer12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    ncsave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=NComputer.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    ncsave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)
        else:
            if num >= 7: 
                print(request.POST)
                questions=Computer12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    csave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=Computer.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    csave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

        
        
    else:
        
        if cat == "Blind":
            
            if num >= 7:
                question1 =NComputer12.objects.get(question = "How do you copy a file on a computer?") 
                questions=NComputer12.objects.all()
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NComputer12.objects.get(question = "What does the C drive usually represent on a computer?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NComputer12.objects.get(question = "What is the function of a keyboard?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NComputer12.objects.get(question = "Which program do you use to browse the internet?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NComputer12.objects.get(question = "What is the purpose of a computer monitor?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    'questions':questions,
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                return render(request,'computer/nquiz12.html',context)
            else:
                question1 =NComputer.objects.get(question = "What is the main input device of a computer?") 
                
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NComputer.objects.get(question = "Which button do you press to start a computer?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NComputer.objects.get(question = "What does the www in a website address stand for?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NComputer.objects.get(question = "How do you save a file on a computer?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NComputer.objects.get(question = "What is a mouse used for?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }



            return render(request,'computer/nquiz.html',context)
        else:
            if num >= 7: 
                questions=Computer12.objects.all()
                context = {
                    'questions':questions
                }
            else:
                questions=Computer.objects.all()
                context = {
                    'questions':questions
                }
        return render(request,'computer/quiz.html',context)

    # if request.method == 'POST':
    #     print(request.POST)
    #     questions=Computer.objects.all()
    #     score=0
    #     wrong=0
    #     correct=0
    #     total=0
    #     for q in questions:
    #         total+=1
    #         print(request.POST.get(q.question))
    #         print(q.ans)
    #         print()
    #         if q.ans ==  request.POST.get(q.question):
    #             score+=10
    #             correct+=1
    #         else:
    #             wrong+=1
    #     percent = score/(total*10) *100
    #     if request.user.is_authenticated:
    #         csave_quiz_result(user_name=request.user.username, score=score)
        
    #     context = {
    #         'score':score,
    #         'time': request.POST.get('timer'),
    #         'correct':correct,
    #         'wrong':wrong,
    #         'percent':percent,
    #         'total':total
    #     }
    #     return render(request,'Quiz/result.html',context)
    # else:
    #     questions=Computer.objects.all()
    #     context = {
    #         'questions':questions
    #     }
    #     return render(request,'computer/quiz.html',context)
    

def maths(request):
    return render(request,'maths/maths.html')
def mat1(request):
    return render(request,'maths/1.html')
def mat2(request):
    return render(request,'maths/2.html')
def mat3(request):
    return render(request,'maths/3.html')
def mat4(request):
    return render(request,'maths/4.html')
def mat5(request):
    return render(request,'maths/5.html')
def mat6(request):
    return render(request,'maths/6.html')
def mat7(request):
    return render(request,'maths/7.html')
def mat8(request):
    return render(request,'maths/8.html')

def mattest(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age
    if request.method == 'POST':
        if cat == "Blind":
            print("1")
            if num >= 7: 
                print("2")
                #Try this Later
                # question1 =NMaths12.objects.get(question = "Can you count by twos up to 10?") 
                # print('Question 1',question1.ans)
                questions=NMaths12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print('Thid is Request',request.POST.get(q.question))
                    print(q.ans)
                    
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nmsave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print("3")
                
                questions=NMaths.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nmsave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)
        else:
            if num >= 7: 
                print(request.POST)
                questions=Maths12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    msave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=Maths.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    msave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

        
        
    else:
        
        if cat == "Blind":
            if num >= 7:
                question1 =NMaths12.objects.get(question = "Can you count by twos up to 10?") 
                questions=NMaths12.objects.all()
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NMaths12.objects.get(question = "What is the product of 3 and 2?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NMaths12.objects.get(question = "How many corners does a square have?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NMaths12.objects.get(question = "What is the result of dividing 8 by 2?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NMaths12.objects.get(question = "What is the next number in the sequence: 1, 2, 3, 4, __?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    'questions':questions,
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                return render(request,'maths/nquiz12.html',context)
            else:
                question1 =NMaths.objects.get(question = "What is the sum of 5 and 3?") 
                
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NMaths.objects.get(question = "Can you count backwards from 10 to 1?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NMaths.objects.get(question = "What is the result of adding 2 and 4?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NMaths.objects.get(question = "How many sides does a triangle have?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NMaths.objects.get(question = "What is the value of 10 minus 5?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                # questions=NMaths.objects.all()
                # context = {
                #     'questions':questions
                # }

            return render(request,'maths/nquiz.html',context)
        else:
            if num >= 7: 
                questions=Maths12.objects.all()
                context = {
                    'questions':questions
                }
            else:
                questions=Maths.objects.all()
                context = {
                    'questions':questions
                }
        return render(request,'maths/quiz.html',context)


def english(request):
    return render(request,'english/english.html')
def eng1(request):
    return render(request,'english/1.html')
def eng2(request):
    return render(request,'english/2.html')
def eng3(request):
    return render(request,'english/3.html')
def eng4(request):
    return render(request,'english/4.html')
def eng5(request):
    return render(request,'english/5.html')
def eng6(request):
    return render(request,'english/6.html')
def eng7(request):
    return render(request,'english/7.html')
def eng8(request):
    return render(request,'english/8.html')

def engtest(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age
    if request.method == 'POST':
        if cat == "Blind":
            print("1")
            if num >= 7: 
                print("2")
                questions=NEnglish12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nesave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=NEnglish.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nesave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)
        else:
            if num >= 7: 
                print(request.POST)
                questions=English12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    esave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=English.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    esave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

        
        
    else:
        
        if cat == "Blind":
            

            if num >= 7:
                question1 =NEnglish12.objects.get(question = "What is the correct order of the alphabet?") 
                questions=NEnglish12.objects.all()
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NEnglish12.objects.get(question = "What is a synonym for big?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NEnglish12.objects.get(question = "What is the opposite of day?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NEnglish12.objects.get(question = "What is the meaning of the word beautiful?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NEnglish12.objects.get(question = "Can you name three animals in English?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    'questions':questions,
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                return render(request,'english/nquiz12.html',context)
            else:
                question1 =NEnglish.objects.get(question = "What is the opposite of happy?") 
                
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NEnglish.objects.get(question = "Can you name three colors in English?") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NEnglish.objects.get(question = "What is the plural form of cat?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NEnglish.objects.get(question = "What is the past tense of run?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NEnglish.objects.get(question = "Fill in the blank: I ____ to the park yesterday.") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }

            return render(request,'english/nquiz.html',context)
        else:
            if num >= 7: 
                questions=English12.objects.all()
                context = {
                    'questions':questions
                }
            else:
                questions=English.objects.all()
                context = {
                    'questions':questions
                }
        return render(request,'english/quiz.html',context)
    

    
def tamil(request):
    return render(request,'tamil/tamil.html')
def tam1(request):
    return render(request,'tamil/1.html')
def tam2(request):
    return render(request,'tamil/2.html')
def tam3(request):
    return render(request,'tamil/3.html')
def tam4(request):
    return render(request,'tamil/4.html')
def tam5(request):
    return render(request,'tamil/5.html')
def tam6(request):
    return render(request,'tamil/6.html')
def tam7(request):
    return render(request,'tamil/7.html')
def tam8(request):
    return render(request,'tamil/8.html')

def tamtest(request):

    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age
    if request.method == 'POST':
        if cat == "Blind":
            print("1")
            if num >= 7: 
                print("2")
                questions=NTamil12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nsave_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=NTamil.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    nsave_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)
        else:
            if num >= 7: 
                print(request.POST)
                questions=Tamil12.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    save_quiz_result12(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

            else:
                print(request.POST)
                questions=Tamil.objects.all()
                score=0
                wrong=0
                correct=0
                total=0
                for q in questions:
                    total+=1
                    print(request.POST.get(q.question))
                    print(q.ans)
                    print()
                    if q.ans ==  request.POST.get(q.question):
                        score+=10
                        correct+=1
                    else:
                        wrong+=1
                percent = score/(total*10) *100
                if request.user.is_authenticated:
                    save_quiz_result(user_name=request.user.username, score=score)

                context = {
                    'score':score,
                    'time': request.POST.get('timer'),
                    'correct':correct,
                    'wrong':wrong,
                    'percent':percent,
                    'total':total
                }
                return render(request,'Quiz/result.html',context)

        
        
    else:
        
        if cat == "Blind":
            
            if num >= 7:
                question1 =NTamil12.objects.get(question = "பின்னணி உயிர் எழுத்தைக் குறிப்பிடுக.") 
                questions=NTamil12.objects.all()
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NTamil12.objects.get(question = "பின்னணி மெய் எழுத்தைக் குறிப்பிடுக.") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NTamil12.objects.get(question = "ஆ + (ட் + உ) = ?") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NTamil12.objects.get(question = "(ப் + அ) + ஞ் + சு = ?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NTamil12.objects.get(question = "திருக்குறளின் ஆசிரியர் யார்?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    'questions':questions,
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                return render(request,'tamil/nquiz12.html',context)
            else:
                question1 =NTamil.objects.get(question = "தமிழ் உயிர் எழுத்துக்களில் முதல் எழுத்து யாது?") 
                
                print(question1)
                print(question1.op1)
                print(question1.op2)
                print(question1.op3)
                print(question1.op4)
                
                q1op1=question1.op1               
                q1op2=question1.op2
                q1op3=question1.op3
                q1op4=question1.op4

                question2 =NTamil.objects.get(question = "விடுபட்ட எழுத்தை கண்டுபிடி. ஆ, ____ , ஈ") 
                q2op1=question2.op1               
                q2op2=question2.op2
                q2op3=question2.op3
                q2op4=question2.op4

                question3 =NTamil.objects.get(question = "உயிர் எழுத்துகள் மொத்தம் _____") 
                q3op1=question3.op1               
                q3op2=question3.op2
                q3op3=question3.op3
                q3op4=question3.op4

                question4 =NTamil.objects.get(question = "ஆயுத எழுத்துகள் மொத்தம் எத்தனை?") 
                q4op1=question4.op1               
                q4op2=question4.op2
                q4op3=question4.op3
                q4op4=question4.op4

                question5 =NTamil.objects.get(question = "தமிழ் எழுத்துகள் மொத்தம் எத்தனை?") 
                q5op1=question5.op1               
                q5op2=question5.op2
                q5op3=question5.op3
                q5op4=question5.op4
               
                context = {
                    
                    'question1':question1,
                    'q1op1':q1op1,
                    'q1op2':q1op2,
                    'q1op3':q1op3,
                    'q1op4':q1op4,
                    'question2':question2,
                    'q2op1':q2op1,
                    'q2op2':q2op2,
                    'q2op3':q2op3,
                    'q2op4':q2op4,
                    'question3':question3,
                    'q3op1':q3op1,
                    'q3op2':q3op2,
                    'q3op3':q3op3,
                    'q3op4':q3op4,
                    'question4':question4,
                    'q4op1':q4op1,
                    'q4op2':q4op2,
                    'q4op3':q4op3,
                    'q4op4':q4op4,
                    'question5':question5,
                    'q5op1':q5op1,
                    'q5op2':q5op2,
                    'q5op3':q5op3,
                    'q5op4':q5op4,
                }
                # questions=NMaths.objects.all()
                # context = {
                #     'questions':questions
                # }


            return render(request,'tamil/nquiz.html',context)
        else:
            if num >= 7: 
                questions=Tamil12.objects.all()
                context = {
                    'questions':questions
                }
            else:
                questions=Tamil.objects.all()
                context = {
                    'questions':questions
                }
        return render(request,'tamil/quiz.html',context)

    # if request.method == 'POST':
    #     print(request.POST)
    #     questions=English.objects.all()
    #     score=0
    #     wrong=0
    #     correct=0
    #     total=0
    #     for q in questions:
    #         total+=1
    #         print(request.POST.get(q.question))
    #         print(q.ans)
    #         print()
    #         if q.ans ==  request.POST.get(q.question):
    #             score+=10
    #             correct+=1
    #         else:
    #             wrong+=1
    #     percent = score/(total*10) *100
    #     if request.user.is_authenticated:
    #         save_quiz_result(user_name=request.user.username, score=score)
        
    #     context = {
    #         'score':score,
    #         'time': request.POST.get('timer'),
    #         'correct':correct,
    #         'wrong':wrong,
    #         'percent':percent,
    #         'total':total
    #     }
    #     return render(request,'Quiz/result.html',context)
    # else:
    #     questions=English.objects.all()
    #     context = {
    #         'questions':questions
    #     }
    #     return render(request,'tamil/quiz.html',context)

def save_quiz_result(user_name, score):
    try:
        quiz_result = QuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except QuizResult.DoesNotExist:
        QuizResult.objects.create(user_name=user_name, score=score)

def save_quiz_result12(user_name, score):
    try:
        quiz_result = QuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except QuizResult12.DoesNotExist:
        QuizResult12.objects.create(user_name=user_name, score=score)

def nsave_quiz_result(user_name, score):
    try:
        quiz_result = NQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NQuizResult.DoesNotExist:
        NQuizResult.objects.create(user_name=user_name, score=score)

def nsave_quiz_result12(user_name, score):
    try:
        quiz_result = NQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NQuizResult12.DoesNotExist:
        NQuizResult12.objects.create(user_name=user_name, score=score)


def esave_quiz_result(user_name, score):
    try:
        quiz_result = EQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except EQuizResult.DoesNotExist:
        EQuizResult.objects.create(user_name=user_name, score=score)
        
def esave_quiz_result12(user_name, score):
    try:
        quiz_result = EQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except EQuizResult12.DoesNotExist:
        EQuizResult12.objects.create(user_name=user_name, score=score)

def nesave_quiz_result(user_name, score):
    try:
        quiz_result = NEQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NEQuizResult.DoesNotExist:
        NEQuizResult.objects.create(user_name=user_name, score=score)
        
def nesave_quiz_result12(user_name, score):
    try:
        quiz_result = NEQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NEQuizResult12.DoesNotExist:
        NEQuizResult12.objects.create(user_name=user_name, score=score)



def msave_quiz_result(user_name, score):
    try:
        quiz_result = MQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except MQuizResult.DoesNotExist:
        MQuizResult.objects.create(user_name=user_name, score=score)
        
def msave_quiz_result12(user_name, score):
    try:
        quiz_result = MQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except MQuizResult12.DoesNotExist:
        MQuizResult12.objects.create(user_name=user_name, score=score)

def nmsave_quiz_result(user_name, score):
    try:
        quiz_result = NMQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NMQuizResult.DoesNotExist:
        NMQuizResult.objects.create(user_name=user_name, score=score)

def nmsave_quiz_result12(user_name, score):
    try:
        print("1NMQuizResult12")
        quiz_result = NMQuizResult12.objects.get(user_name=user_name)
        print("2NMQuizResult12")
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NMQuizResult12.DoesNotExist:
        print("3NMQuizResult12")
        NMQuizResult12.objects.create(user_name=user_name, score=score)



def csave_quiz_result(user_name, score):
    try:
        quiz_result = CQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except CQuizResult.DoesNotExist:
        CQuizResult.objects.create(user_name=user_name, score=score)


def csave_quiz_result12(user_name, score):
    try:
        quiz_result = CQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except CQuizResult12.DoesNotExist:
        CQuizResult.objects.create(user_name=user_name, score=score)


def ncsave_quiz_result(user_name, score):
    try:
        quiz_result = NCQuizResult.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NCQuizResult.DoesNotExist:
        NCQuizResult.objects.create(user_name=user_name, score=score)


def ncsave_quiz_result12(user_name, score):
    try:
        quiz_result = NCQuizResult12.objects.get(user_name=user_name)
        if score > quiz_result.score:
            quiz_result.score = score
            quiz_result.save()
    except NCQuizResult12.DoesNotExist:
        NCQuizResult12.objects.create(user_name=user_name, score=score)

def leaderboard(request):

    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age

    if cat == "Blind":
        if num >= 7: 
            top_results = NQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        else:
            top_results = NQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        return render(request, 'leaderboard.html', context)
    else:
        if num >= 7: 
            top_results = QuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        else:
            top_results = QuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        return render(request, 'leaderboard.html', context)
    
 
def eleaderboard(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age

    if cat == "Blind":
        if num >= 7: 
            top_results = NEQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        else:
            top_results = NEQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        return render(request, 'leaderboard.html', context)
    else:
        if num >= 7: 
            top_results = EQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        else:
            top_results = EQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        return render(request, 'leaderboard.html', context)
    

def mleaderboard(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age

    if cat == "Blind":
        if num >= 7: 
            top_results = NMQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        else:
            top_results = NMQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        return render(request, 'leaderboard.html', context)
    else:
        if num >= 7: 
            top_results = MQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        else:
            top_results = MQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        return render(request, 'leaderboard.html', context)
    
def cleaderboard(request):

    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age

    if cat == "Blind":
        if num >= 7: 
            top_results = NCQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        else:
            top_results = NCQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
            
        return render(request, 'leaderboard.html', context)
    else:
        if num >= 7: 
            top_results = CQuizResult12.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        else:
            top_results = CQuizResult.objects.order_by('-score')[:10]
            context = {
                'top_results': top_results
            }
        return render(request, 'leaderboard.html', context)


def lb(request):
    return render(request,"elb.html")
def game(request):
    name =  Category.objects.get(user=request.user.username)
    print(name,name.age,name.choice_field)
    cat = name.choice_field
    num = name.age
    if cat == "Blind":
        return render(request,'Ngame.html')
    return render(request,'game.html')
def abc(request):
    return render(request,"Games/abc/index.html")
def click(request):
    return render(request,"Games/click/index.html")
def cube(request):
    return render(request,"Games/cube/index.html")
def hangman(request):
    return render(request,"Games/hangman/index.html")
def tower(request):
    return render(request,"Games/tower/index.html")
def chess(request):
    return render(request,"Games/chess/index.html")

def blind1(request):
    return render(request,"Games/1.html")

def blind2(request):
    return render(request,"Games/2.html")

def blind3(request):
    return render(request,"Games/3.html")

def blind4(request):
    return render(request,"Games/4.html")