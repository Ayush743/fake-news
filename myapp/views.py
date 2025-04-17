from django.shortcuts import render
from django.http import HttpResponse
from newspaper import Article
from urllib.parse import urlparse

# Create your views here.
def index(request):
      return render(request,'index.html')
   
def result(request):
    url_label=request.GET.get("url_label")
   
    article = Article(url_label)

    article.download()
    article.parse()
    context={
    "title": article.title,
    "source": urlparse(url_label).netloc,
    "text": article.text[:500]
    
    }
    # print("Title:", article.title)
    # print("Author(s):", article.authors)
    # print("Publish Date:", article.publish_date)
    # print("Main Text:\n", article.text[:100])
   
    return render(request,'result.html',context)


      