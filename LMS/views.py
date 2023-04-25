from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import studentdetails
from .models import Courses
from .models import Assignment
from .models import Marks

def index(request):
    return render(request, 'index.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')

def parent(request):
    return render(request, 'parent.html')

def Coursesviews(request):
    if request.method == "POST":
        course1 = request.POST.get('course1')
        course2 = request.POST.get('course2')
        course3 = request.POST.get('course3')
        course4 = request.POST.get('course4')
        course5 = request.POST.get('course5')
        course6 = request.POST.get('course6')
        semester = request.POST.get('semester')
        Coursesobj = Courses(course1=course1, course2=course2, course3=course3, course4=course4, course5=course5, course6=course6, semester=semester, date=datetime.today())
        Coursesobj.save()
    return render(request, 'Courses.html')

def Assignmentviews(request):
    if request.method == "POST":
        semester = request.POST.get('semester')
        course = request.POST.get('course')
        assignment = request.POST.get('assignment')
        Assignmentobj = Assignment(semester=semester, course=course, assignment=assignment, date=datetime.today())
        Assignmentobj.save()
    return render(request, 'Assignment.html')

def Marksview(request):
    if request.method == "POST":
        name = request.POST.get('name')
        semester = request.POST.get('semester')
        course1 = request.POST.get('course1')
        mark1 = request.POST.get('mark1')
        course2 = request.POST.get('course1')
        mark2 = request.POST.get('mark1')
        course3 = request.POST.get('course1')
        mark3 = request.POST.get('mark1')
        course4 = request.POST.get('course1')
        mark4 = request.POST.get('mark1')
        course5 = request.POST.get('course1')
        mark5 = request.POST.get('mark1')
        course6 = request.POST.get('course1')
        mark6 = request.POST.get('mark1')       
        Marksobj = Marks(name=name, semester=semester, course1=course1, mark1=mark1, course2=course2, mark2=mark2, course3=course3, mark3=mark3, course4=course4, mark4=mark4, course5=course5, mark5=mark5, course6=course6, mark6=mark6, date=datetime.today()) 
        Marksobj.save()
    return render(request, 'Marks.html')

def studentdetailsview(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Father_Name = request.POST.get('father_name')
        Mother_Name = request.POST.get('mother_name')
        Seat_Number = request.POST.get('seat_number')
        Phone = request.POST.get('phone')
        email = request.POST.get('email')
        semester = request.POST.get('semester')
        studentdetailsobj = studentdetails.objects.create(name=name, Father_Name=Father_Name, Mother_Name=Mother_Name, Seat_Number=Seat_Number, phone=Phone, email=email,semester=semester, date=datetime.today())
        # studentdetailsobj.save()
        return render(request, 'studentdetails.html')
    else:
        return render(request, 'studentdetails.html')