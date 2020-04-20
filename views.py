# FIRST METHOD FOR VIEWS FILE

# from django.shortcuts import render

# # Create your views here.
# from .models import Book
# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
# from django.http import Http404

# def index(request):
#     all_books = Book.objects.all()
#     #template = loader.get_template('books/index.html')
#     context = {
#         'all_books': all_books
#     }
    
#     #return HttpResponse(template.render(context, request))
#     return render(request,'books/index.html',context)

# def detail(request, book_id):
#     #return HttpResponse("<h2> Details for Book ID:"+ str(book_id)+"</h2>")
#     # now for 404 error
#     try:
#         book = Book.objects.get(id=book_id)
#     except Book.DoesNotExist:
#         raise Http404('This book does not exist')
#     return render(request,'books/detail.html',{'book':book})

# SECOND METHOD

from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView
class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'