from django.shortcuts import render,redirect
from .models import Higher,Inter,School,Portfolio,Language,Projects,Skills
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_signup(request):
    msg=''
    if request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        p1=request.POST.get('p1')
        p2=request.POST.get('p2')
        if p1==p2:
            if not User.objects.filter(username=name).exists():
                User.objects.create_user(username=name,email=email,password=p2)
                return redirect('login')
            else:
                msg=" username already exists " 
        else:
            msg=" incorrect password "
    return render(request,'signup.html')
def user_login(request):
    msg=''
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        name=request.POST.get('name')
        p1=request.POST.get('p1')
        user=authenticate(request,username=name,password=p1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg="username not found "
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('login')
def create_portfolio(request):
    if  not request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        name=request.POST.get('name')
        image=request.POST.get('image')
        age=request.POST.get('age')
        email=request.POST.get('email')
        address=request.POST.get('add')
        resume = request.FILES.get('resume')

        # college
        cname=request.POST.get('cname')
        cstart=request.POST.get('cstart')
        cend=request.POST.get('cend')
        caddress=request.POST.get('cadd')
        cdesc=request.POST.get('cdesc')
        cmarks=request.POST.get('cmarks')

        # Intermediate
        iiname=request.POST.get('iname')
        istart=request.POST.get('istart')
        iend=request.POST.get('iend')
        iaddress=request.POST.get('iadd')
        idesc=request.POST.get('idesc')
        imarks=request.POST.get('imarks')

        # school
        ssname=request.POST.get('sname')
        sstart=request.POST.get('sstart')
        send=request.POST.get('send')
        saddress=request.POST.get('sadd')
        sdesc=request.POST.get('sdesc')
        smarks=request.POST.get('smarks')

        # language
        lname=request.POST.get('lname')

        # skills 
        ssname=request.POST.get('ssname')

        # projects 
        pname=request.POST.get('pname')
        piv=request.FILES.get('piv')
        pdesc=request.POST.get('desc')

        # Hobbies
        h=request.POST.get('hobbies')
        github=request.POST.get('github')
        linkidin=request.POST.get('linkidin')
       

        
        language=Language.objects.create(lname=lname)
        skills=Skills.objects.create(ssname=ssname)
        projects=Projects.objects.create(pname=pname,pimage_or_video=piv,pdesc=pdesc)
        higher=Higher.objects.create(college_name=cname,start=cstart,end=cend,desc=cdesc,address=caddress,marks=cmarks)
        inter=Inter.objects.create(inter_name=iiname,start=istart,end=iend,desc=idesc,address=iaddress,marks=imarks)
        school=School.objects.create(school=ssname,start=sstart,end=send,desc=sdesc,address=saddress,marks=smarks)
        portfolio=Portfolio.objects.create(name=name,image=image,age=age,email=email,address=address,higher_education=higher,
                                           inter=inter,school=school,hobbies=h,project=projects,github=github,linkidin=linkidin,
                                         user=request.user)
        portfolio.language.set([language])
        portfolio.skills.set([skills])
        return redirect('home')
    return render(request,'create.html')
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={
        'portfolio':Portfolio.objects.all(),
        'page_url': request.build_absolute_uri()
    }
    return render(request,'home.html',context)
def portfolio_view(request,ids):
    port=Portfolio.objects.get(id=ids,user=request.user)
    context={
        'port':port
    }
    return render(request,'portview.html',context)
def port_delete(request,ids):
    port=Portfolio.objects.get(id=ids)
    port.delete()
    return redirect('home')
def port_edit(request, ids):
    port = Portfolio.objects.get(id=ids,user=request.user)

    if request.method == "POST":
        port.name = request.POST.get('name')
        port.age = request.POST.get('age')
        port.email = request.POST.get('email')
        port.address = request.POST.get('add')
        port.hobbies = request.POST.get('hobbies')
        port.github = request.POST.get('github')
        port.linkidin = request.POST.get('linkidin')

        image = request.FILES.get('image')
        if image:
            port.image = image

        port.higher_education.college_name = request.POST.get('cname')
        port.higher_education.start = request.POST.get('cstart')
        port.higher_education.end = request.POST.get('cend')
        port.higher_education.address = request.POST.get('cadd')
        port.higher_education.desc = request.POST.get('cdesc')
        port.higher_education.marks = request.POST.get('cmarks')
        port.higher_education.save()

        port.inter.inter_name = request.POST.get('iname')
        port.inter.start = request.POST.get('istart')
        port.inter.end = request.POST.get('iend')
        port.inter.address = request.POST.get('iadd')
        port.inter.desc = request.POST.get('idesc')
        port.inter.marks = request.POST.get('imarks')
        port.inter.save()

        port.school.school = request.POST.get('sname')
        port.school.start = request.POST.get('sstart')
        port.school.end = request.POST.get('send')
        port.school.address = request.POST.get('sadd')
        port.school.desc = request.POST.get('sdesc')
        port.school.marks = request.POST.get('smarks')
        port.school.save()

 
        project = port.project
        project.pname = request.POST.get('pname')
        new_piv = request.FILES.get('piv')
        if new_piv:
            project.pimage_or_video = new_piv
        project.pdesc = request.POST.get('desc')
        project.save()

      
        lname = request.POST.get('lname')
        if lname:
            new_lang = Language.objects.create(lname=lname)
            port.language.add(new_lang)

       
        ssname = request.POST.get('ssname')
        if ssname:
            new_skill = Skills.objects.create(ssname=ssname)
            port.skills.add(new_skill)

   
        port.save()

        return redirect('view',ids=port.id)

    context = {
        'port': port
    }
    return render(request, 'edit.html', context)
