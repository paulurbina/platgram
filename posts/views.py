from django.shortcuts import render
from datetime import datetime

posts = [
  {
    'name': 'paul urbina',
    'user': 'tony',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/300'
  },
  {
    'name': 'tatiana urbina',
    'user': 'tati',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/300'
  },
  {
    'name': 'kevin urbin',
    'user': 'kev',
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'picture': 'https://picsum.photos/200/300'
  }
]

def list_posts(request):
  return render(request, 'feed.html', { 'posts': posts })
