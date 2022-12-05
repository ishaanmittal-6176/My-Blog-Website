from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import redirect,render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.warning(request,'please fill the form properly')
        else:
            messages.success(request,"Your issue has been sent")
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts=Post.objects.none()
    else:
        allposts=Post.objects.filter(title__icontains=query)
        allposts=Post.objects.filter(author__icontains=query)
        allposts=Post.objects.filter(content__icontains=query)
    
    if allposts.count()==0:
        messages.warning(request, "No search results found. Please refine your query")
    params={'allposts': allposts}
    return render(request, 'home/search.html',params)

def signin(request):
    if request.method =="POST":

        #parameters
        username = request.POST['username']
        inputfname = request.POST['inputfname']
        inputlname = request.POST['inputlname']
        inputemail = request.POST['inputemail']
        inputPass1 = request.POST['inputPass1']
        inputPass2 = request.POST['inputPass2']

        # check for error password input
        if len(username)>10:
            messages.error(request, "Your username must be below 10 characters")
            return redirect('home')

        if not username.isalnum:
            messages.error(request, "Your username should pnly contain numbers and letters")
            return redirect('home')

        if(inputPass1 != inputPass2):
            messages.error(request, "Passwords do not match, Please check the password and try again")
            return redirect('home')
        #creating user
        myuser = User.objects.create_user(username, inputemail,inputPass1)
        myuser.first_name = inputfname
        myuser.last_name = inputlname
        myuser.save()
        messages.success(request, "Your user has been created successfully")
        return redirect('home')
    
    else:
        return HttpResponse("Error - Please try again")

def blogLogin(request):
        if request.method =="POST":

            #parameters
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
        
            user=authenticate(username=loginusername, password=loginpassword)
            if user is None:
                messages.error(request, "Invalid credentials, Please check and retry")
                return redirect('home')
            
            else:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("home")
        else:
            return HttpResponse("Error 404 - Not Found")

def blogLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")




