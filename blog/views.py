from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Post
from .models import Todo
from .forms import PostForm, TaskForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST) # jezeli juz wypelnisz to nie znika tylko widok jest z wypelnoiny
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def robokop(request,dk):

    post = get_object_or_404(Post, pk=dk)
    return render(request, 'blog/testy.html',{'post': post})



def checkLIST2(request):

    return render(request,'blog/checkLIST.html')

@login_required
def Task_new2(request):

    tasks = Todo.objects.order_by('id').filter(usr= request.user)
    if request.method == "POST":

        tForm = TaskForm(request.POST)
        tForm = tForm.save(commit=False) # dodac jakies dane przy wysylaniu formularza
        tForm.usr = request.user
        tForm.save()
        return redirect('checkLIST2')
    else:
        tForm = TaskForm()

    return render(request, 'blog/checkLIST2.html', {'tForm': tForm,'tasks': tasks})

def change_status2(request,i):
    task = get_object_or_404(Todo, pk=i, usr=request.user)
    if task.status==True:
        task.status=False
        task.save()
    else:
        task.status=True
        task.save()
    return redirect('checkLIST2')

def delete_all2(request):

    tasks = Todo.objects.filter(usr=request.user)
    tasks.delete()

    return redirect('checkLIST2')

def delete_done2(request):
    tasks_D = Todo.objects.filter(usr=request.user).filter(status="True")
    tasks_D.delete()
    return redirect('checkLIST2')

def mark_all_as_done2(request):
    tasks_D = Todo.objects.filter(usr=request.user)
    for ttt in tasks_D:
        if ttt.status == False:
            ttt.status = True
            ttt.save()
    return redirect('checkLIST2')