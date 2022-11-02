
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


# class BlogList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog.html'
#     context_object_name = 'blog_list'
#     paginate_by = 6

def BlogList (request):
    template_name = 'blog.html'
    blog_list = Post.objects.all()
    page = request.GET.get('page', 1)
    x = blog_list.count()
    y = x/2
    paginator = Paginator(blog_list,y) # Show 25 contacts per page.]
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, template_name, {"blog_list":blog_list, 'posts': posts})

# class BlogDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog-single.html'
#     context_object_name = 'blog_detail'

def post_detail(request, slug):
    template_name = 'blog-single.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})




