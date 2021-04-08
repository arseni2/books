from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import uuid

class Book(models.Model):
    cover = models.ImageField(upload_to='covers/', blank=True)
    id = models.UUIDField( # new
        primary_key=True,
        db_index=True,
        unique=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200, db_index=True,)
    author = models.CharField(max_length=200, db_index=True,)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True,)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('book_detail', args=[str(self.id)])

    class Meta:  # new
        permissions = [
            ("special_status", "Can read all tests"),
        ]


class Review(models.Model): # new
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
        db_index=True,
    )
    review = models.CharField(max_length=255, db_index=True,)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        db_index=True,
    )

    def __str__(self):
        return self.review



