from django.shortcuts import render, redirect
from . models import Course, Description
# Create your views here.
def index(request):
    # print "*"*42
    # Course.objects.all().delete()
    try:
        context = {
            "courses" : Course.objects.all(),
        }
    except:
        context = {}
        Course.objects.all().delete()
    return render(request,'courses_app/index.html', context)

def add_course(request):
    if request.method == 'POST':
        print "*"*42
        print request.POST
        # Course.objects.create(course_name=request.POST['course_name'])
        course = Course(course_name=request.POST['course_name'])
        course.save()
        # print Course.objects.all()
        course_id = Course.objects.get(course_name=request.POST['course_name']).id
        description = Description(description=request.POST['description'])
        # this command is strange but it assigns the foreignkey correctly
        description.course_id = course
        description.save()
        # print Description.objects.all()
        # course_id = Course.objects.get(course_name=request.POST['course_name']).id
        # print course_id, "*"*19
        # Description.objects.create(description=request.POST['description'],
        #     course_id=course_id)
        # print Description.objects.all()
    return redirect('/')

def delete_page(request, id):
    # if request.method == 'POST':
    print "*"*42
    print id
    course = Course.objects.get(id=id)
    print course
    print "*"*21
    context = {
        'course_to_delete' : course
    }

    return render(request,'courses_app/delete_course.html', context)

def delete_course(request):
    if request.method == 'POST':
        if 'yes' in request.POST:
            # print request.POST
            # print request.POST.get('yes')
            id = request.POST['id']
            # print id
            course = Course.objects.get(id=id)
            print course
            # print context['course_to_delete']
            print "*"*42
            course.delete()

    return redirect('/')
