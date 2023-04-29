from django.shortcuts import render, redirect
from .forms import ReserveForm

# Create your views here.
def reservefood(request):
    r = ReserveForm()
    if request.method == 'POST':
        r = ReserveForm(request.POST)
        if r.is_valid():
            r.save()
            return redirect('home')
    else:
        r = ReserveForm()
    context = {
        'form': r
    }
    return render(request, 'reserve/reserve.html', context)