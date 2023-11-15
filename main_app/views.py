from django.shortcuts import render, redirect
from .models import Finch, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# finches = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#   {'name': 'Ama', 'breed': 'void', 'description': 'silently judges you', 'age': 2},
#   {'name': 'Bobo', 'breed': 'tabby', 'description': 'good boy, eats too much', 'age': 1},
#   {'name': 'Boots', 'breed': 'tabby', 'description': 'cuddly, but stinky', 'age': 1},

# ]

def home(request):
    return render(request, 'home.html',)

def about(request):
    return render(request, 'about.html')

def finches_index(request):
   finches = Finch.objects.all() # Retrieve all finches
   return render(request, 'finches/index.html', 
    { 
        'finches': finches 
    }
)

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'
   sucess_url = '/finches'

class FinchUpdate(UpdateView):
   model = Finch
   fields = ['name', 'description', 'age']

class FinchDelete(DeleteView):
   model = Finch
   success_url = '/finches'

def assoc_toy(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=cat_id).toys.remove(toy_id)
  return redirect('detail', cat_id=cat_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'
