from django.http import HttpResponseRedirect
from django.shortcuts import render
from school.models import Student
from auto.models import Car, Foto
from kurs.models import User, Site, Top, Menu
import random

def auto(request):
    if request.method=="GET":
        n=request.GET.get("n")
    else:
        n=1
    if n==None:
        n=1
    menu=Car.objects.all()
    foto=Foto.objects.filter(id_cars=n)
    return render(request, "auto.html", {'menu':menu, "foto":foto,
    "logo":"Кращі автомобілі світу", "n":n})


def studentsView(request):
    all = Student.objects.all()
    return render(request, "students.html", {"stud": all,"text":"Список працівників та учнів школи:"})
def pupilsView(request):
    all = Student.objects.filter(post="учень")
    return render(request, "pupils.html", {"stud": all,"text":"Список учнів школи:"})
def uch_revView(request):
    all = Student.objects.filter(post="учень")
    return render(request, "uch_rev.html", {"stud": all,"text":"Список учнів школи:"})
def uch_ostView(request):
    all = Student.objects.all()[:10]
    return render(request, "uch_ost.html", {"stud": all,"text":"Список працівників школи:"})
def uchView_find(request):
    if request.method == "POST":
        post_lastname = request.POST.get("fam")
        all = Student.objects.filter(lastname=post_lastname)
        n=all.count()
        if n>0:
            powid="Знайдено"
        else:
            powid="Не знайдено"
    else:
        n=0
        all = Student.objects.filter(post="учень")
        powid="Всі учні класу!"
    return render(request, "uch_find.html", {"stud": all,"text":"Список учнів школи:","p":powid})
def uchView_add(request):
    if request.method=="POST":
        pers = Student()
        pers.lastname = request.POST.get("fam")
        pers.name = request.POST.get("name")
        pers.post = request.POST.get("pos")
        pers.save()
        powid=str(pers.lastname)+" "+str(pers.name)+" "+str(pers.post)+" - додано!"
    else:
         powid="Всі учні класу"
    all =  Student.objects.all()
    return render(request, "uch_add.html",{"stud": all,"text":"Список учнів школи:","p":powid})
def indexView(request):
    all = Site.objects.filter(name="index.html")
    m_all = Menu.objects.filter()
    t_all = Top.objects.filter()
    return render(request, "index.html", {"index": all, "menu": m_all, "top": t_all, "text":"Головна"})
def registView(request):
    if request.method=="POST":
        pers = User()
        pers.nik = request.POST.get("nik")
        pers.email = request.POST.get("ema")
        pers.password = request.POST.get("pass")
        s=""
        for i in range(10):
            l=random.randint(0,9)
            k=str(l)
            s+=k
        pers.kod=int(s)
        pers.save()
        powid=str(pers.nik)+" - додано!"
    else:
         powid="Всі користувачі сайту"
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    u_all = User.objects.filter()
    return render(request, "regist.html", {"index": all, "menu": m_all, "user": u_all, "text":"Реєстрація","p": powid})
def hudView(request):
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "hud.html", {"index": all, "menu": m_all, "text":"Художня література"})
def naukView(request):
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "nauk.html", {"index": all, "menu": m_all, "text":"Наукова література"})
def mangaView(request):
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "manga.html", {"index": all, "menu": m_all, "text":"Манґа"})
def partView(request):
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "part.html", {"index": all, "menu": m_all, "text":"Сайти-партнери"})
def speedtestView(request):
    lis=["перший", "другий"]
    s=str(random.choice(lis))
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "speedtest.html", {"index": all, "menu": m_all, "text":"Швидкість читання", "s":s})
def calkView(request):
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "calk.html", {"index": all, "menu": m_all, "text":"Калькулятор"})
def randomView(request):
    advice=Top.objects.all()
    s=str(random.choice(advice))
    if s=="Назва книжки":
        s=str(random.choice(advice))
    all = Site.objects.filter()
    m_all = Menu.objects.filter()
    return render(request, "random.html", {"index": all, "menu": m_all, "text":"Рандомайзер", "s":s})
