from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def projects(request):
    project_list = [
    {
        "title" : "Rasoi Connect ",
        "image" : "images/rasoi_connect.png",
        "URL" : "#"
    },
    {
        "title" : "Ecommerce",
        "image" : "images/ecommerce.png",
        "URL" : "#"
    },
    {
        "title" : "Timetable Scheduler",
        "image" : "images/timtable.PNG",
        "URL" : "#"
    },
    {
        "title" : "CRUD",
        "image" : "images/CRUD.png",
        "URL" : "#"
    },
    {
        "title" : "Portfolio",
        "image" : "images/portfolio.png",
        "URL" : "#"
    },
    {
        "title" : "Labor Hiring",
        "image" : "images/labour_hiring.png",
        "URL" : "#"
    },

]
    return render (request, "projects.html", { "projects" : project_list })

def experiences(request):
    experiences_list = [
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/labour_hiring.png"
        },
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/portfolio.png"
        },
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/CRUD.png"
        },
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/timtable.PNG"
        },
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/ecommerce.png",
        },
        {
            "company" : "Expressmartke",
            "role" : "Graphic Designer & Full-Stack Developer",
            "Achievements" : "Designed engaging social media posts and developed the ecommerce website",
            "image" : "images/rasoi_connect.png",
        },
    ]
    return render (request, "experiences.html" , {"experiences" : experiences_list})

def certs(request):
    certificate_list = [
        {
            "Cert" : "Graphic Design | UI/UX design Course",
            "Achievements" : "5 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/labour_hiring.png"
        },
        {
            "Cert" : "Front-End Development | Zero to Mastery",
            "Achievements" : "12 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/portfolio.png"
        },
        {
            "Cert" : "Back-End Development | Zero to Mastery",
            "Achievements" : "12 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/CRUD.png"
        },
        {
            "Cert" : "Graphic Design | UI/UX design Course",
            "Achievements" : "5 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/labour_hiring.png"
        },
        {
            "Cert" : "Front-End Development | Zero to Mastery",
            "Achievements" : "12 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/portfolio.png"
        },
        {
            "Cert" : "Back-End Development | Zero to Mastery",
            "Achievements" : "12 months course with real world projects and a certificate recognized by big companies",
            "image" : "images/CRUD.png"
        }
    ]
    return render(request, "certificates.html", {"Certificates" : certificate_list})

def contact(request):
    return render(request, "contact.html")

def resume(request):
    pdf_path = 'pdf/Dummy_Portfolio.pdf'
    pdf_path = staticfiles_storage.path(pdf_path) 