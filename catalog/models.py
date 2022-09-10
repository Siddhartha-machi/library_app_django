from re import L
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date
import uuid

# Create your models here.
class Lang(models.Model):
    """Model representing the language"""

    lang = models.CharField(
        "Language" ,
        max_length = 5,
        default = 'Eng' 
        )

    def __str__(self):
        return self.lang


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Genre(models.Model):
    """The genre class"""
    genre = models.CharField(
        max_length = 10 ,
        help_text = 'Genere of the Book.' ,
        
        )

    
    def __str__(self):
        return self.genre


class Book(models.Model):
    """The book class"""

    title = models.CharField(max_length = 50 , help_text = 'Title of the book.' ,)
    isbn = models.CharField('ISBN',max_length = 13 , unique = True , help_text = 'A 13 characters length unique id.<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ForeignKey(Author , on_delete = models.CASCADE , help_text = 'Author of the book.' )
    summary = models.TextField(max_length = 100 ,help_text = 'A brief summary of the book.')
    genre = models.ManyToManyField(Genre  , help_text = 'Genere of the book.' )
    copies  = models.IntegerField(default = 0 , help_text = 'No of copies Available.')
    lang = models.ForeignKey(Lang , help_text = 'Language of the book.' ,on_delete = models.SET_NULL , null = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    class Meta:
        ordering = ['title' ]


class BookInstance(models.Model):

    """BookInstances class"""

    id = models.UUIDField(
        primary_key = True , 
        default = uuid.uuid4,
        help_text='Unique ID for this particular book across whole library'
        )

    book = models.ForeignKey(
        Book , 
        on_delete = models.RESTRICT
        )

    imprint = models.CharField(
        max_length=200
        )

    due_back = models.DateField(
        null=True, 
        blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
            max_length = 1 ,
            choices = LOAN_STATUS ,
            help_text = 'Status of the Instance.' ,
            
            )
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ['due_back']

    def is_overdue(self):

        return bool(self.due_back and date.today() > self.due_back )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'