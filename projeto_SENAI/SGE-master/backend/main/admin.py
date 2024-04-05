from django.contrib import admin
from .models import *

class AdminCustomUser(admin.ModelAdmin):
    list_display  = ('id','email','registrationNumber','is_active',)
    list_display_links = ('id','email','registrationNumber','is_active',)
    search_fields = ('email','registrationNumber',)
    list_per_page = 10

admin.site.register(CustomUser, AdminCustomUser)

class AdminEnvironments(admin.ModelAdmin):
    list_display  = ('id','name','block',)
    list_display_links = ('id','name','block',)
    search_fields = ('name','block',)
    list_per_page = 10

admin.site.register(Environments, AdminEnvironments)

class AdminTasks(admin.ModelAdmin):
    list_display  = ('id','title','environmentFK','creationDate',)
    list_display_links = ('id','title','environmentFK','creationDate',)
    search_fields = ('title',)
    list_per_page = 10

admin.site.register(Tasks, AdminTasks)

class AdminTasksAssignes(admin.ModelAdmin):
    list_display  = ('id','taskFK','assigneeFK',)
    list_display_links = ('id','taskFK','assigneeFK',)
    search_fields = ('taskFK',)
    list_per_page = 10

admin.site.register(TaskAssignees, AdminTasksAssignes)

class AdminEquipments(admin.ModelAdmin):
    list_display  = ('id','name','code',)
    list_display_links = ('id','name','code',)
    search_fields = ('name','code',)
    list_per_page = 10

admin.site.register(Equipments, AdminEquipments)

class AdminTasksStatus(admin.ModelAdmin):
    list_display  = ('id','taskFK','status',)
    list_display_links = ('id','taskFK','status',)
    search_fields = ('taskFK',)
    list_per_page = 10

admin.site.register(TaskStatus, AdminTasksStatus)

class AdminFileTasksStatus(admin.ModelAdmin):
    list_display  = ('id','taskStatusFK','fileType',)
    list_display_links = ('id','taskStatusFK','fileType',)
    search_fields = ('taskStatusFK',)
    list_per_page = 10

admin.site.register(FileTasksStatus, AdminFileTasksStatus)



class AdminTasksEquipments(admin.ModelAdmin):
    list_display  = ('id','taskFK','equipmentFK',)
    list_display_links = ('id','taskFK','equipmentFK',)
    search_fields = ('equipmentFK',)
    list_per_page = 10

admin.site.register(TaskEquipments, AdminTasksEquipments)


class AdminEnviromentsAssignees(admin.ModelAdmin):
    list_display  = ('id','environmentFK','assigneeFK',)
    list_display_links = ('id','environmentFK','assigneeFK',)
    search_fields = ('environmentFK',)
    list_per_page = 10

admin.site.register(EnviromentsAssignees, AdminEnviromentsAssignees)


class AdminThemes(admin.ModelAdmin):
    list_display  = ('id','name','timeLoad',)
    list_display_links = ('id','name','timeLoad',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Theme, AdminThemes)


class AdminCourses(admin.ModelAdmin):
    list_display  = ('id','name','category','duration_type','area',)
    list_display_links = ('id','name','category','duration_type','area',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Courses, AdminCourses)

class AdminCoursesTheme(admin.ModelAdmin):
    list_display  = ('id','courseFK','themeFK',)
    list_display_links = ('id','courseFK','themeFK',)
    search_fields = ('courseFK','themeFK',)
    list_per_page = 10

admin.site.register(CoursesThemes, AdminCoursesTheme)

class AdminClass(admin.ModelAdmin):
    list_display  = ('id','name','courseFK',)
    list_display_links = ('id','name','courseFK',)
    search_fields = ('name','courseFK',)
    list_per_page = 10

admin.site.register(Class, AdminClass)


class AdminClassDivision(admin.ModelAdmin):
    list_display  = ('id','classFK','name',)
    list_display_links = ('id','classFK','name',)
    search_fields = ('classFK','name',)
    list_per_page = 10

admin.site.register(ClassDivision, AdminClassDivision)

class AdminTeacherAlocation(admin.ModelAdmin):
    list_display  = ('id','classFK','themeFK','reporterFK',)
    list_display_links = ('id','classFK','themeFK','reporterFK',)
    search_fields = ('reporterFK','classFK',)
    list_per_page = 10

admin.site.register(TeacherAlocation, AdminTeacherAlocation)


class AdminTeacherAlocationDetail(admin.ModelAdmin):
    list_display  = ('id','customUserFK','classDivisionFK','creationDate','updateDate','alocationStatus',)
    list_display_links = ('id','customUserFK','classDivisionFK','creationDate','updateDate','alocationStatus',)
    search_fields = ('customUserFK','classDivisionFK','alocationStatus',)
    list_per_page = 10

admin.site.register(TeacherAlocationDetail, AdminTeacherAlocationDetail)

class AdminTeacherAlocationDetailEnv(admin.ModelAdmin):
    list_display  = ('id','environmentFK','teacherAlocationDetail','weekDay','hourStart','hourEnd','startDate','endDate',)
    list_display_links = ('id','environmentFK','teacherAlocationDetail','weekDay','hourStart','hourEnd','startDate','endDate',)
    search_fields = ('environmentFK','teacherAlocationDetail',)
    list_per_page = 10

admin.site.register(TeacherAlocationDetailEnv, AdminTeacherAlocationDetailEnv)

class AdminDeadLine(admin.ModelAdmin):
    list_display  = ('id','targetDate','category',)
    list_display_links = ('id','targetDate','category',)
    search_fields = ('targetDate','category',)
    list_per_page = 10

admin.site.register(DeadLine, AdminDeadLine)


class AdminSignatures(admin.ModelAdmin):
    list_display  = ('id','customUserFK','signature','creationDate',)
    list_display_links = ('id','customUserFK','signature','creationDate',)
    search_fields = ('customUserFK','signature',)
    list_per_page = 10

admin.site.register(Signatures, AdminSignatures)




class AdminPlan(admin.ModelAdmin):
    list_display  = ('id','customUserFK','courseThemeFK','status', 'signatureFK','aproverFK',)
    list_display_links = ('id','customUserFK','courseThemeFK','status', 'signatureFK','aproverFK',)
    search_fields = ('customUserFK','courseThemeFK','status','aproverFK',)
    list_per_page = 10

admin.site.register(Plan, AdminPlan)

class AdminPlanStatus(admin.ModelAdmin):
    list_display  = ('id','planFK','status','createdDate', 'comment','file',)
    list_display_links = ('id','planFK','status','createdDate', 'comment','file',)
    search_fields = ('planFK','status',)
    list_per_page = 10

admin.site.register(PlanStatus, AdminPlanStatus)






















