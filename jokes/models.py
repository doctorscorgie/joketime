from django.db import models

class JokeType(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Joke(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(JokeType, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'myentries'
 
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."

