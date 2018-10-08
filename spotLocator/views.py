from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Spot
from django.views.generic.edit import UpdateView, CreateView


def index(request):
    spot_list = Spot.objects.all()

    spot_activity_type = Spot.ACTIVITY_CHOICES
    context = {
        'spot_list': spot_list,
        'spot_activity_type' : spot_activity_type,
    }
    return render(request, 'spotLocator/index.html', context)


def detail(request, spot_id):
    spot = get_object_or_404(Spot, pk=spot_id)
    activity_type = spot.activity
    if request.method == 'POST':
        spot.delete()
        return HttpResponseRedirect(reverse('spotLocator:index'))
    return render(request, 'spotLocator/detail.html', {'spot': spot, 'activity_type' : activity_type})


class AddSpot(CreateView):
    model = Spot
    fields = ['name', 'description', 'notes', 'activity']
    def get_success_url(self):
        return reverse('spotLocator:index')
    def get_context_data(self, **kwargs):
        context = super(AddSpot, self).get_context_data(**kwargs)
        context['action'] = 'Add'
        context['title'] = 'Add A New Favorite Spot'
        
        if self.kwargs:
            context['activity'] = self.kwargs
        return context


def activity(request, activity_type):
    spot_activity_type = Spot.objects.all().filter(activity = activity_type)
    return render(request, 'spotLocator/activity.html', {'spot_activity_type' : spot_activity_type, 'activity_type' : activity_type})



class EditSpot(UpdateView):
    model = Spot
    
    fields = ['name', 'description', 'notes', 'activity']
    def get_success_url(self):
        return reverse('spotLocator:detail', kwargs={
            'spot_id': self.object.pk,
        })
    def get_context_data(self, **kwargs):
        context = super(EditSpot, self).get_context_data(**kwargs)
        context['action'] = 'Save'
        context['title'] = 'Edit ' + self.object.name
        return context