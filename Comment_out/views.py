from django.shortcuts import render,redirect
from . models import Comment
from . forms import CommentForm
# Create your views here.
def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments' : comments}
    return render(request,'Comment_out/index.html',context)

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = Comment(name=request.POST['name'],comment=request.POST['comment'])
            new_form.save()
            return redirect('index')
    else:
        form = CommentForm()
        
    context = {'form' : form }
    return render(request,'Comment_out/comment.html',context)
