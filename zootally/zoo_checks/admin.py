from django.contrib import admin

from zoo_checks.models import Animal, AnimalCount, Exhibit, Species, SpeciesCount

admin.site.register(Exhibit)
admin.site.register(Species)
admin.site.register(Animal)
admin.site.register(AnimalCount)
admin.site.register(SpeciesCount)
