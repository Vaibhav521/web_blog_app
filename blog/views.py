from django.shortcuts import render , get_object_or_404
from django.shortcuts import redirect


from django.http import HttpResponse
from blog.models import Post , Category , Comment , Contact

from django.contrib.auth.models import User
from django.contrib import messages 

from django.contrib.auth  import authenticate,  login, logout , get_user_model

from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def home(request):
    #fetch data
    posts = Post.objects.all()[:9]
    cats = Category.objects.all()
    data={
        'post':posts,
        'cat':cats
      
    }
    return render(request,'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    comments= Comment.objects.filter(post=post)
    return render(request,'posts.html',{'post':post , 'comments':comments})

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})


def aboutus(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')



def create_account(request):
    if request.method == 'POST':
        #data form users
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
      
       
        #check "kekw"

        if get_user_model().objects.filter(username=username):
            messages.error(request,'user name is taken try with another username')
            return redirect('/home')

        if get_user_model().objects.filter(email=email):
            messages.error(request,'email is taken try with another username')
            return redirect('/home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/home')
        if (password!= confirmpassword):
             messages.error(request, " Passwords do not match")
             return redirect('/home')

        #creat the user
        
        myuser = User.objects.create_user(username,email,password)
      
            

        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()
        
        #messages are not working / wana show profile made message 
        messages.success(request, 'Your Profile has been made  successfully.')

        return redirect('/home') #wihtout slash it wont work


    else :
        return HttpResponse('404 not allowed')


def user_login (request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)

    if user and user.is_superuser:
        return redirect("/home")

    if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/home")
    else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/home")

    return HttpResponse("404- Not found")

def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/home')


def postComment(request):
    if request.method == "POST":
        post_url = request.POST.get("post_url")
        content = request.POST.get('comment')
        author = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(post_id=post_id)
        comment = Comment(content=content, author=author, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        comment.created_at = timezone.now()
        comment.save()

    return redirect(f"/blog/{post_url}")



def contact_us_form(request):
    if request.method== "POST":
        email = request.POST.get("email")
        name =request.POST.get("name")
        user_message = request.POST.get("message")
        user_form_message = Contact(name=name,email=email,message=user_message)
        user_form_message.save()
        messages.success(request, "Your message has been sent successfully")
        user_form_message.created_at = timezone.now()
        user_form_message.save()

    return redirect("contact/")