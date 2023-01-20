from django.db import models

import uuid
# Create your models here.

class Artwork(models.Model):
    # owner = models.ForeignKey(
    #     Profile, null=True, blank=True, on_delete=models.SET_NULL
    # )
    title = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default_image.jpg"
    )
    year_created = models.IntegerField(default=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    topic = models.TextField(default="Write your goals for the work here", null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    # owner =
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    VOTE_TYPE = (
        ("one_star", 1),
        ("two_stars", 2),
        ("three_stars", 3),
        ("four_stars", 4),
        ("five_stars", 5),
    )
    rating = models.CharField(max_length=200, choices=VOTE_TYPE, default="None")
    Sum_it_up = models.CharField(max_length=400, null=True, blank=True)
    What_works = models.TextField(null=True, blank=True)
    What_needs_work = models.TextField(null=True, blank=True)
    What_might_work = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.rating


# Use Tag to create a Many to Many relationship. It connects the Artworks with the votes they receive.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name