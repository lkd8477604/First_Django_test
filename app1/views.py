from django.shortcuts import render
from django.shortcuts import HttpResponse
from app1 import models
# Create your views here.
def home(request):
    return HttpResponse('app01.home')
def new(request, page,num):
    nid = page + num
    return HttpResponse(nid)
def db_handle(request):
    # models.modue1.objects.create(username='john',password='545804',age='22')
    # dict = {'username':'yao', 'password': '545804', 'age': 22}
    # models.modue1.objects.create(**dict)
    # models.modue1.objects.filter(age=22).delete()
    # models.modue1.objects.all().update(age=22)
    models.modue1.objects.filter(username='john')
    if request.method == 'POST':
        # print (request.POST)
        # request.POST['age'] = int(request.POST['age'])
        models.modue1.objects.create(username=request.POST['username'], password=request.POST['password'], age=request.POST['age'])
    data = models.modue1.objects.all()
    for i in data:
        name = i.username
        password = i.password
        age = i.age
        print ('name {0} passwd {1} age {2}'.format(name,password,age))
        # return HttpResponse('name:{} passwd:{} age:{}'.format(name,password,age))
    return render(request, 't1.html', {'i':data})
def host_page(request):
    return render(request, 'app1/pag1.html')
def page2(request):
    return render(request, 'app1/pag2.html')