from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime

posts = [
  {
    'name': 'paul urbina',
    'user': {
      'name': 'Tony Urbina',
      'picture': 'https://i.picsum.photos/id/21/70/70.jpg'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/19/400/300.jpg'
  },
  {
    'name': 'Tatiana urbina',
    'user': {
      'name': 'Tatiana Urbina',
      'picture': 'https://i.picsum.photos/id/31/70/70.jpg'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/20/400/300.jpg'
  },
  {
    'name': 'kevin urbin',
    'user': {
      'name': 'Kev Urbina',
      'picture': 'https://i.picsum.photos/id/32/70/70.jpg'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://i.picsum.photos/id/22/400/300.jpg'
  }
]

@login_required
def list_posts(request):
  return render(request, 'posts/feed.html', { 'posts': posts })
