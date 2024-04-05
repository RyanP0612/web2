from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import *

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    date_joined = models.DateField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email" #substitui o login username por e-mail
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email

BLOCKS = [
    ('A', 'Bloco A'),
    ('B', "Bloco B"),
    ('C', "Bloco C"),
]

TYPE = [
    ("MAN",'Manutenção'),
    ("ME",'Melhoria'),
    ("RE",'Reunião')
]

TASKS_STATUS = [
    ('AB', "Aberta"),
    ("EA","Em andamento"),
    ("CA", "CANCELADA"),
    ("CO", "Concluída"),
    ("EN","Encerrada")

]


class Environments(models.Model):
    name = models.CharField(max_length=80)
    block = models.CharField(max_length=50, choices = BLOCKS)
    def __str__(self):
       return self.name
    
class Tasks(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name="local", on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name="reportador", on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    diagnostic = models.CharField(max_length=250,  null=True, blank=True)
    type = models.CharField(max_length=50, choices= TYPE)
    status = models.CharField(max_length=60, choices=TASKS_STATUS)
    # environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name="ambiente", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

FILE_TYPE=[
    ('D','Document'),
    ("P","Photo")
]
class TaskStatus(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name="tarefa", on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=TASKS_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=350)

    def __str__(self):
        return self.taskFK.title

class FileTasksStatus(models.Model):
    taskStatusFK = models.ForeignKey(TaskStatus, related_name="tarefaFile", on_delete=models.CASCADE)
    link = models.CharField(max_length=2200)
    fileType = models.CharField(max_length=60, choices=FILE_TYPE)

    def __str__(self):
        return self.fileType
    


class TaskAssignees(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name="tarefaAssig", on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name="usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.taskFK.title


class Equipments(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=100)
    assigneeFK = models.ForeignKey(CustomUser, related_name="usuarioEquipment", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    


class TaskEquipments(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name="tarefaEquipment", on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name="equipmentTask", on_delete=models.CASCADE)
    def __str__(self):
        return self.taskFK.title
    
  
class EnviromentsAssignees(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='enviromentsAssigneesEnvironment', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='enviromentsAssigneesCustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.environmentFK.name
    
class Theme(models.Model):
    name = models.CharField(max_length=50)
    timeLoad = models.IntegerField()

    def __str__(self):
        return self.name
    

CATEGORY = [
    ("CAI","Aprendizagem industrial"),
    ("FIC","Formação continuada"),
    ("CST","Curso superior tecnológico"),
    ("CT","Curso Técnico"),

]

DURATION_TYPE = [
    ("H","Horas"),
    ("S","Semestre"),
    
]

AREA = [
    ("T","TI"),
    ("M","MECATRÔNICA"),
    ("E","ELÉTRICA"),
   
]

MODALITY = [
    ("E","EAD"),
    ("P","Presencial"),
    ("H","Híbrido"),
    
]

class Courses(models.Model):
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length=60, choices=CATEGORY)
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=60, choices=DURATION_TYPE)
    area = models.CharField(max_length=60, choices=AREA)
    modality = models.CharField(max_length=60, choices=MODALITY)

    def __str__(self):
        return self.name
    
class CoursesThemes(models.Model):
    courseFK = models.ForeignKey(Courses, related_name='courses', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Theme, related_name='themes', on_delete=models.CASCADE)

    def __str__(self):
        return self.courseFK.name
    
class Class(models.Model):
    courseFK = models.ForeignKey(Courses, related_name='coursesClass', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    startDate = models.DateField()
    endDate = models.DateField()
    def __str__(self):
        return self.name
    
class ClassDivision(models.Model):
    classFK = models.ForeignKey(Class, related_name='classDiv', on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    
class TeacherAlocation(models.Model):
    classFK = models.ForeignKey(Class, related_name='classTeacher', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Theme, related_name='theme', on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name="reporAlocation", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.classFK.name

ALOCATION_STATUS = [
    ("1","Rascunho"),
    ("2","Assinalado"),
    ("3","Concluído")
]


class TeacherAlocationDetail(models.Model):
    customUserFK = models.ForeignKey(CustomUser, related_name="UserTeacher", on_delete=models.CASCADE)
    classDivisionFK = models.ForeignKey(Class, related_name="classTeacherDetail", on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    alocationStatus = models.CharField(max_length=60, choices=ALOCATION_STATUS, default='1')
    def __str__(self):
        return self.customUserFK.email
WEEK_DAY = [
    ("S","Segunda"),
    ("T","Terça"),
    ("Q","Quarta"),
    ("QUI","Quinta"),
    ("SEX","Sexta"),
    ("S","Sábado"),
    ("D","Domingo ")
]

class TeacherAlocationDetailEnv(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name="TeacherEnvironments", on_delete=models.CASCADE)
    teacherAlocationDetail = models.ForeignKey(TeacherAlocationDetail, related_name="TeacherAlocationDetail_env", on_delete=models.CASCADE)
    weekDay = models.CharField(max_length=60, choices=WEEK_DAY)
    hourStart = models.TimeField(auto_now_add=True)
    hourEnd = models.TimeField(auto_now=True)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.environmentFK.name
    


class DeadLine(models.Model):
    targetDate = models.DateField()
    category = models.CharField(max_length=60, choices=CATEGORY)
    def __str__(self):
        return self.category
    


class Signatures(models.Model):
    customUserFK = models.ForeignKey(CustomUser, related_name="UserSignature", on_delete=models.CASCADE)
    signature = models.CharField(max_length=1000)
    creationDate = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.signature
    

STATUS = [
    ("1","Pendente"),
    ("2","Em Aprovamento"),
    ("3","Aprovamento"),
    ("4","Em Revis"),
    ("5","Cancelado"),
    
]


class Plan(models.Model):
    customUserFK = models.ForeignKey(CustomUser, related_name="UserPlan", on_delete=models.CASCADE)
    courseThemeFK = models.ForeignKey(CoursesThemes, related_name="CourseSignature", on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS, default='1')
    signatureFK = models.ForeignKey(Signatures, related_name="PlanSignature", on_delete=models.CASCADE, blank=True, null=True)
    aproverFK = models.ForeignKey(CustomUser, related_name="UserPlanAprov", on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.customUserFK.email
    
class PlanStatus(models.Model):
    planFK = models.ForeignKey(Plan, related_name="PlanFK", on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS)
    createdDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    file = models.CharField(max_length=3000)
    def __str__(self):
        return self.planFK.customUserFK.email
    