from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    teams = Team.objects.all()
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    if request.method == 'POST':
        # POST isteği geldiğinde formdan gelen verileri alın
        fullname = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Veritabanına kaydetmek için Contact modelini kullanın
        contact = Contact(
            fullname=fullname,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()  # Veriyi kaydedin
    context = {
        'teams' : teams,
        'testimonials' : testimonials,
        'projects' : projects
    }
    return render(request, "uluocak/index.html", context)

def about(request):
    
    return render(request, 'uluocak/about.html')