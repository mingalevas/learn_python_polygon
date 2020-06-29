from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests

from .forms import NameForm


def get_total(term_one: int, term_two: int):
    try:
        payload = {'term_one': term_one, 'term_two': term_two}
        host = 'subproject_calculator'
        port = 5000
        r = requests.get('http://{}:{}/'.format(host, port), params=payload)
        if r.status_code == 200:
            return r.json()['result']
        else:
            return 'error'
    except Exception as exc:
        return 'internal error'


def get_name(request):
    if request.method == "POST":
        # Get the posted form

        form = NameForm(request.POST)
        if form.is_valid():
            term_one = form.cleaned_data['term_one']
            term_two = form.cleaned_data['term_two']
            total = get_total(term_one, term_two)
            return render(request, 'output.html', {'term_one': term_one,
                                                   'term_two': term_two,
                                                   'total': total})

    else:
        form = NameForm()

    return render(request, 'input.html', {'form': form})
