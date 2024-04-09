from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    CHOICES = (
        ('Blind', 'Blind'),
        ('Deaf', 'Deaf'),
    )
    user =models.CharField(max_length=25)
    age =models.IntegerField()
    choice_field = models.CharField(choices=CHOICES, max_length=10) 
    def __str__(self):
        return self.user

class Computer(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    

class Computer12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class NComputer(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    

class NComputer12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class Maths(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class Maths12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class NMaths(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class NMaths12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class English(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class English12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class NEnglish(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
class NEnglish12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class Tamil(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class Tamil12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class NTamil(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class NTamil12(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class QuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
class QuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
class NQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
class NQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class EQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class EQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class NEQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class NEQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class MQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
    
class MQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
class NMQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
    
class NMQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name

class CQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    

class CQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name


class NCQuizResult(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name
    
class NCQuizResult12(models.Model):
    user_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_name