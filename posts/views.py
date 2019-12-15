from django.http import HttpResponse

def list_posts(request):
  posts = [1,2,34,54]
  return HttpResponse(str(posts))
