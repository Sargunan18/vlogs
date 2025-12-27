from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from games.models import Post,AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm


# Create your views here.
# posts = [
#         { "id":1, "title" : "free fire", "content":"online gun shooting game"},
#         { "id":2, "title":"COC", "content":" realty game"},
#         { "id":3, "title":"pubg", "content":" online realty gun shooting game "},
#         { "id":4, "title":"minimiltry", "content":"this is gun game this wife game"},
#         { "id":5, "title":"RC2025", "content":"this is criket game"},
#         { "id":6, "title":"Rummmy", "content":"this is card game"},
#     ]    
def index(request):
    Game_mode="latest post"
    #geeting deta from post model
    posts=Post.objects.all()

    #paginator
    paginator=Paginator(posts, 5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, "games/index.html", {"game_mode":Game_mode, "page_obj":page_obj})
           
def post(request,slug):
    #post = next((item for item in posts if item['id'] == int(post_id)), None)
    # logger=logging.getLogger("TESTING")
    # logger.debug(f"post variable is{post}")
    try:
        # getting data from model by slug
        post_obj = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post_obj.category).exclude(pk=post_obj.id)

        #paginate
      

    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")

    return render(request, "games/details.html", {'post': post_obj, "related_posts": related_posts})

def new(request):
    return HttpResponse("redirect agidchu") 

def old(request):
    return redirect(reverse("games:new"))


               
def contect(request):
    form = ContactForm(request.POST)
    name=request.POST.get("name")
    email=request.POST.get("email")
    message=request.POST.get("message")
    
    if request.method == "POST":
        
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            
            logger.debug(
                f"contact form submitted: {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}"
            )
            #send email or save in database
            success_message="your email has been sent"
            return render(request, "games/contact.html",{'success_message':success_message})
        else:
            logger.debug(f"from validation errror")
        return render(request, "games/contact.html", {'form': form ,'name':name, 'email':email, 'message':message})        
    #return render(request, "games/contact.html", {'form': form ,'name':name, 'email':email, 'message':message})
    return render(request, "games/contact.html")


def about_view(request):
    about_content=AboutUs.objects.first().content
    return render(request, "games/about.html" ,{'about_content':about_content})


