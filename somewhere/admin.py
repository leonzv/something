from django.contrib import admin
from django.db import models
from .models import  Aluno, Professor, Curso, Matricula, Turma, Disciplina, Nota

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Nota)

    

    
    

