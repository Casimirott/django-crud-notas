from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from notas.models import Nota

# Muestre mis notas 
class HomePageView(ListView):
    template_name = 'notas/home.html'
    model = Nota
    
# crear mis notas 
class CreateNotaView(CreateView):
    template_name = 'notas/nuevo.html'
    model = Nota
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('home')

# actualizar notas 
class UpdateNotaView(UpdateView):
    template_name = 'notas/actualizar.html'
    model = Nota
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('home')

# eliminar notas 
class DeleteNotaView(DeleteView):
    template_name = 'notas/eliminar.html'
    model = Nota
    success_url = reverse_lazy('home')