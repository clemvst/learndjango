from django.db import models

# # Create your models here.
# ARTISTS = {
#   'francis-cabrel': {'name': 'Francis Cabrel'},
#   'lej': {'name': 'Elijay'},
#   'rosana': {'name': 'Rosana'},
#   'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
# }
#
#
# ALBUMS = [
#   {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
#   {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
#   {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
# ]
class Contact(models.model):
    email = models.EmailField(max_length = 100)
    name = models.CharField(max_length = 200)

class Artist(models.model):
    name = models.CharField(max_length = 200, unique = True)

class Album(models.model):
    reference = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    available = models.BooleanField(default = True)
    title = models.CharField(max_length = 200)
    picture = models.URLField()

class Booking(models.model):
    created_at = models.DateTimeField(auto_now_add = True)
    contacted = models.BooleanField(default = False)

class AlbumArtist(models.model):
    id_Artist = Artist.name
