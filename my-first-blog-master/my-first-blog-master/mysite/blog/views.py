from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
data = {
    'f': [
        {'id': 1, 'text': 'ololo'},
        {'id': 2, 'text': 'ololo2'},
        {'id': 3, 'text': 'cheeeekii breeki'},
    ]
}
def books(request):

    return render(request, 'blog/bookexmp.html', data,{})
def gov(request):
    return render(request, 'blog/govorit.html', data,{})