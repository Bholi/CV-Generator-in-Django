from django.shortcuts import render
from .models import Profile
import pdfkit
import io
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        exp = request.POST.get('exp')
        skills = request.POST.get('skills')

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,experience=exp,skills=skills)
        profile.save()


    return render(request,'index.html')

def resume(request,id):
    cv_data = Profile.objects.get(id=id)
    template = loader.get_template('resume.html')
    html = template.render()
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    cv = pdfkit.from_string(html,False,options)
    response = HttpResponse(cv,content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume.pdf"'
    # import time
    # time.sleep(5)
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request,'list.html',{'profile':profile})
