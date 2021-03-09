
from django.views.generic import *
from catriges.models import *


class CatrigeListView(ListView):
    model = Catrige
    queryset = Catrige.objects.all()
    context_object_name = 'cl'
    template_name = 'catrige/catrigeList.html'



class CatrigeCreateView(CreateView):
    pass
