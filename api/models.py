import uuid

from django.db import models
from django.contrib.auth.models import User



class Teacher(models.Model):

    user        = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Teacher: {user.get_full_name()}>"



class Class_Template(models.Model):

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session     = models.CharField(max_length=10)
    name        = models.CharField(max_length=150)
    teacher     = models.ManyToManyField(Teacher)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Class_Template: {name} | {session}>"
    



class Subject(models.Model):

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_template  = models.ForeignKey(Class_Template, on_delete=models.SET_NULL, 
                                        blank=False, null=True)
    name            = models.CharField(max_length=100)
    description     = models.CharField(max_length=400)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Subject: {class_template.name} - {name}>"


class Term(models.Model):
    
    FIRST, SECOND, THIRD, ERROR = 'F', 'S', 'T', 'E'
    TERM_CHOICES = [(FIRST, 'FIRST'), (SECOND, 'SECOND'), 
                    (THIRD, 'THIRD'), (ERROR, 'ERROR')]

    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    term            = models.CharField(max_length=1, choices=TERM_CHOICES, default=ERROR)
    class_template  = models.ForeignKey(Class_Template, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Term: {term} | {class_template.name} | {class_template.session}>"



class Result(models.Model):


    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    subject     = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=False, null=True)
    test        = models.IntegerField(null=True, blank=True, default="N")
    exam        = models.IntegerField(null=True, blank=True, default="N")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __repr__(self):
        val = " | ".join([subject.name, user.get_full_name, f"Test:{test}", f"Exam:{exam}"])
        return f"<Result: {val} \n"
    


class Comment(models.Model):


    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User        = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    comment     = models.CharField(max_length=500, editable=False, blank=False, null=False, default="No Comment")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Comment: {id} >"


class Ticket(models.Model):


    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    used_by     = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)
    ticket      = models.CharField(max_length=5)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True) 
    


    def __repr__(self):
        return f"<Ticket: {ticket} | User: {used_by.get_full_name()}>"



class Communication_Book(models.Model):

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student     = models.ManyToManyField(User, blank=False, null=False)
    comment     = models.ManyToManyField(Comment, blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Communication Book>: {student.get_full_name()}>"



class Profile(models.Model):

        
    GENDER = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('N', 'NEITHER'),
    )

    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user                = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    dob                 = models.DateField(null=True, blank=False)
    image               = models.URLField(max_length=500)
    gender              = models.CharField(choices=GENDER, max_length=1, null=True, blank=False)
    class_template      = models.ForeignKey(Class_Template, on_delete=models.SET_NULL, null=True, blank=False)
    guardian_name       = models.CharField(max_length=150, null=True, blank=False)
    guardian_phone      = models.CharField(max_length=15, null=True, blank=False)
    guardian_address    = models.CharField(max_length=250, null=True, blank=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


    def __repr__(self):
        return f"<Profile: user.get_full_name()>"
