from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg,Max,Min

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")   # title : asecending order , -title : decending order
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    return render(request,'book_outlet/index.html',{'books':books,'total_books':total_books,'avg_rating':avg_rating})  #There are multiple agg function thats why we have to used (rating__avg)



def book_detail(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
        raise Http404()
    return render(request,'book_outlet/book_detail.html',{"title":book.title,"author":book.author,"rating":book.rating,"is_bestselling":book.is_bestselling})