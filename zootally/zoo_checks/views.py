from datetime import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import AnimalCountForm, SpeciesExhibitCountForm
from .models import Animal, AnimalCount, Exhibit, Species, SpeciesExhibitCount


@login_required
# TODO: logins may not be sufficient - they need to be a part of a group
def home(request):
    exhibits = Exhibit.objects.filter(user=request.user)

    return render(request, "home.html", {"exhibits": exhibits})


@login_required
def count(request, exhibit_id):
    # TODO: counts should default to maximum (across users) for the day
    # TODO: condition should default to median? condition (across users) for the day

    exhibit = get_object_or_404(Exhibit, pk=exhibit_id)
    exhibit_species = exhibit.species.all()
    exhibit_animals = exhibit.animals.all()

    SpeciesCountFormset = inlineformset_factory(
        Exhibit,
        SpeciesExhibitCount,
        form=SpeciesExhibitCountForm,
        can_delete=False,
        can_order=False,
        extra=len(exhibit_species),  # exhibit.species.count(),
    )
    AnimalCountFormset = inlineformset_factory(
        Exhibit,
        AnimalCount,
        form=AnimalCountForm,
        can_delete=False,
        can_order=False,
        extra=len(exhibit_animals),  # exhibit.animals.count(),
    )

    # to set the order in JS
    species_animals_dict = {}
    for spec in exhibit_species:
        spec_anim_list = []
        for animal in exhibit_animals.filter(species=spec):
            spec_anim_list.append(animal.name)
        species_animals_dict[spec.common_name] = spec_anim_list

    init_sp_vals = [{"species": sp} for sp in exhibit_species]
    init_anim_vals = [{"animal": anim} for anim in exhibit_animals]

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        species_formset = SpeciesCountFormset(
            request.POST, request.FILES, instance=exhibit, initial=init_sp_vals
        )
        animal_formset = AnimalCountFormset(
            request.POST, request.FILES, instance=exhibit, initial=init_anim_vals
        )
        # check whether it's valid:
        if species_formset.is_valid() and animal_formset.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        species_formset = SpeciesCountFormset(instance=exhibit, initial=init_sp_vals)
        animal_formset = AnimalCountFormset(instance=exhibit, initial=init_anim_vals)

    return render(
        request,
        "tally.html",
        {
            "exhibit": exhibit,
            "species_formset": species_formset,
            "animal_formset": animal_formset,
            "exhibit_animals": list(exhibit_animals),
            "exhibit_species": list(exhibit_species),
            "species_animals_dict": species_animals_dict,
        },
    )
