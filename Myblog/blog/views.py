from django.shortcuts import redirect, render, HttpResponse
from blog.models import Post, blogComment
from django.contrib import messages

# Create your views here.
def blogpage(request):
    allpost=Post.objects.all()
    context = {'allposts': allpost}
    return render(request, 'blog/blogpage.html',context)


def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments= blogComment.objects.filter(post=post)
    print("Hello")
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method =="POST":
        comment=request.POST.get('comment')
        user=request.user
        sno =request.POST.get('postSno')
        post= Post.objects.get(sno=sno)
        comment=blogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")       
    return redirect(f"/blog/{post.slug}")