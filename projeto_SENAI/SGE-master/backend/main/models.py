from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

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
    environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name="ambiente", on_delete=models.CASCADE)

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

class FileTasksStatus(models.model):
    taskStatusFK = models.ForeignKey(TaskStatus, related_name="tarefaFile", on_delete=models.CASCADE)
    link = models.CharField(max_length=2200)
    fileType = models.CharField(max_length=60, choices=FILE_TYPE)

    def __str__(self):
        return self.fileType
    


class TaskAssignees(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name="tarefa", on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name="usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.taskFK.title


class Equipments(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=100)
    assigneeFK = models.ForeignKey(CustomUser, related_name="usuarioEquipment", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    


class TaskEquipments(models.model):
    taskFK = models.ForeignKey(Tasks, related_name="tarefaEquipment", on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name="equipmentTask", on_delete=models.CASCADE)
    def __str__(self):
        return self.taskFK.title
    
