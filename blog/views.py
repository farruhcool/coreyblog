from django.shortcuts import render

posts = [
    {
        'author': 'FX',
        'title': 'First Post 1',
        'content': 'First post content 1',
        'date_posted': 'August 8, 2019'
    },

    {
        'author': 'MX',
        'title': 'Second Post 2',
        'content': 'Second post content 2',
        'date_posted': 'August 8, 2019'
    }
]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
