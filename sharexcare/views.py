from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import user, post
from django.core.paginator import Paginator, EmptyPage
from django.views.generic.list import ListView
import re

# Create your views here.

def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,"signin.html")

def explorePage(request):
    return redirect('/explore')

def login_user(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pwsrd = request.POST['userpass']

        check_user = user.objects.filter(username=usr,password=pwsrd)
        
        if check_user:
            request.session['username'] = usr
            all_posts = post.objects.all().order_by('-created_on')
            test = request.session['username']


            page_num = request.GET.get('page',1)

            p = Paginator(all_posts, 5)

            try:
                Page = p.page(page_num)
            except EmptyPage:
                Page = p.page(1)

            
            


            return render(request,"base.html",{'Posts': Page,'tests':test})
        else:
            messages.error(request, "Invalid Username or Password.")
            return render(request,"signin.html")
    else:
        #return HttpResponse('wrong.')
        all_posts = post.objects.all().order_by('-created_on')
        test = request.session['username']


        page_num = request.GET.get('page',1)

        p = Paginator(all_posts, 5)

        try:
            Page = p.page(page_num)
        except EmptyPage:
            Page = p.page(1)
        return render(request,"base.html",{'Posts': Page,'tests':test})
    #   return profile_view(request,id)

# def logoutUser(request):
    
#     #del request.session['username']
#     return render(request,"index.html")

     #logout(request)
    
    
    
       

def signup(request):
    
    return render(request,"signup.html")
   


def saved(request):
    if request.method == "POST":
        name = request.POST['name']
        usr = request.POST['username']
        eml = request.POST['useremail']
        pswrd = request.POST['userpass']
        github = request.POST['github']
        youtube = request.POST['youtube']
        linkedin = request.POST['linkedin']
        #data = {'usr':usr,'eml':eml,'pswrd':pswrd}
        
        if not name or not usr or not eml or not pswrd or not github or not youtube or not linkedin:
            messages.error(request,"Please fill the form correctly")
        elif user.objects.filter(username=usr).exists():
            messages.error(request,"Sorry this Username already exists.")
        elif not re.fullmatch(r'[A-Za-z0-9@#$%^&+=_*!]{8,}', pswrd):
            messages.error(request,"Password should contain at least 8 Characters and can contain Special Symbols, 0-9 Numbers !")
        else:
            user_save = user(name=name ,username=usr, email= eml, password= pswrd,github=github,youtube=youtube,linkedin=linkedin)
            user_save.save()
        #all_posts = post.objects.all().order_by('-created_on')
            request.session['username'] = usr
        #return render(request,"base.html",{'Posts': all_posts})
            return redirect('/explore')
    return render(request,"signup.html")


def create_post(request):
    return render(request,"create_post.html")  



def post_save(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        user_name = request.session['username']

        if len(body.split()) < 50:
            messages.error(request,"Please add Description upto 50 words !")
            return render(request,"create_post.html")
        else:
            author = user.objects.get(username=user_name)
            post_save = post(title=title,body=body,author=author)
            post_save.save()

        #all_posts = post.objects.all().order_by('-created_on')
            return redirect('/explore')
      
    return render(request,"create_post.html")

def profile_view(request,id):
    

    datacontext = {}
    

    user_info = user.objects.filter(username=id).values('name','username','email','github','youtube','linkedin')
    user_info = list(user_info)
    datacontext['name'] = user_info[0]['name']
    datacontext['username'] = user_info[0]['username']
    datacontext['email'] = user_info[0]['email']
    datacontext['github'] = user_info[0]['github']
    datacontext['youtube'] = user_info[0]['youtube']
    datacontext['linkedin'] = user_info[0]['linkedin']

    #for post count
    post_info = user.objects.filter(username=id).values('post').count()

    #fetching all post id of specific user
    fetch_id = user.objects.filter(username=id).values('post')
    fetch_id = list(fetch_id)
    
    post_id = [i['post'] for i in fetch_id]

    #fetching all posts 
    user_post = post.objects.filter(id__in=post_id).values('title','created_on','body')
    user_post = list(user_post)
    
    datacontext['post_count'] = post_info
    datacontext['posts'] = fetch_id

    #making a list which contains 'titles' of that user
    post_title = [ i['title'] for i in user_post ]

    post_created_on = [ i['created_on'] for i in user_post ]

    post_body = [ i['body'][:90] for i in user_post ]

    datacontext['POSTS'] = zip(post_title,post_created_on,post_body)
    
    #print(data)
    return render(request,"viewprofile.html",datacontext)


def loggedin_users_profile_view(request):
    

    datacontext = {}
    
    usr = request.session['username']
    user_info = user.objects.filter(username=usr).values('name','username','email','github','youtube','linkedin')
    user_info = list(user_info)
    datacontext['name'] = user_info[0]['name']
    datacontext['username'] = user_info[0]['username']
    datacontext['email'] = user_info[0]['email']
    datacontext['github'] = user_info[0]['github']
    datacontext['youtube'] = user_info[0]['youtube']
    datacontext['linkedin'] = user_info[0]['linkedin']

    #for post count
    post_info = user.objects.filter(username=usr).values('post').count()

    #fetching all post id of specific user
    fetch_id = user.objects.filter(username=usr).values('post')
    fetch_id = list(fetch_id)
    
    post_id = [i['post'] for i in fetch_id]

    #fetching all posts 
    user_post = post.objects.filter(id__in=post_id).values('title','created_on','body')
    user_post = list(user_post)
    
    datacontext['post_count'] = post_info
    datacontext['posts'] = fetch_id

    #making a list which contains 'titles' of that user
    post_title = [ i['title'] for i in user_post ]

    post_created_on = [ i['created_on'] for i in user_post ]

    post_body = [ i['body'][:90] for i in user_post ]

    datacontext['POSTS'] = zip(post_title,post_created_on,post_body)
    
    #print(data)
    return render(request,"viewprofile.html",datacontext)


def feedRead(request,title):
    
    feeds = {}
    

    share_detail = post.objects.filter(title=title).values('title','created_on','body')
    share_detail = list(share_detail)

    feeds['title_'] = share_detail[0]['title']
    feeds['created_on_'] = share_detail[0]['created_on']
    feeds['body_'] = share_detail[0]['body']

    return render(request,"feedread.html",feeds)
