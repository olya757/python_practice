from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.


class Teacher(AbstractUser):
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    name = models.CharField(verbose_name='Имя', max_length=20)
    second_name = models.CharField(verbose_name='Отчество', max_length=20, blank=True)

    def __str__(self):
        return str(self.surname)+' '+str(self.name)+' '+str(self.second_name)


class Subject(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=50)

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    COURSE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '1 маг.'),
        (6, '2 маг.')
    )

    course = models.IntegerField(verbose_name='Курс', choices=COURSE, default=1)
    number = models.PositiveIntegerField(verbose_name='Номер группы', default=1)

    def __str__(self):
        return str(self.course)+' курс '+str(self.number)+' гр.'


class Student(models.Model):
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    name = models.CharField(verbose_name='Имя', max_length=20)
    second_name = models.CharField(verbose_name='Отчество', max_length=20, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='Группа')

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.second_name)+' '+str(self.group)


# курс лекций
class Curriculum(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Преподаватель')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name='Предмет')

    def __str__(self):
        return 'Преподаватель: ' + str(self.teacher)+'\n' + \
               'Предмет: ' + str(self.subject)


class GroupCurriculum(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True,verbose_name='Группа')
    curriculum = models.ForeignKey(Curriculum, on_delete=models.SET_NULL, null=True,verbose_name='Учебный курс')
    semester = models.PositiveIntegerField(verbose_name='Семестр')

    TYPE_OF_CLASS = (
        (1, 'Семинар'),
        (2, 'Лекция'),
        (3, 'Практика')
    )
    type = models.IntegerField(choices=TYPE_OF_CLASS,default=2,verbose_name='Тип занятия')



    def __str__(self):
        return str(self.curriculum)+'\n '+str(self.group)+'\n '+str(self.semester) + ' семестр\n' + self.TYPE_OF_CLASS[int(str(self.type))-1][1]

    def get_group(self):
        return self.group


class Visit(models.Model):
    group_curriculum = models.ForeignKey(GroupCurriculum, verbose_name='Учебный курс', on_delete=models.SET_NULL,null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name='Студент')
    date = models.DateField(verbose_name='Дата')
    visit = models.BooleanField(verbose_name="Посетил")

    def __str__(self):
        return str(self.group_curriculum)+'\n '+str(self.student)+'\n'+str(self.date)+'\n'+str(self.visit)