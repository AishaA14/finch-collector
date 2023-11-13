from django.shortcuts import render

finches = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
  {'name': 'Ama', 'breed': 'void', 'description': 'silently judges you', 'age': 2},
  {'name': 'Bobo', 'breed': 'tabby', 'description': 'good boy, eats too much', 'age': 1},
  {'name': 'Boots', 'breed': 'tabby', 'description': 'cuddly, but stinky', 'age': 1},

]

def home(request):
    return render(request, 'home.html',)

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })