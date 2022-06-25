from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='owner_id',)
    to_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,)
    content = models.TextField(
        max_length=1000,
        name='content')
    good_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.to_user.username) + ')'

class Good(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='good_owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.post) + '" (by ' + str(self.owner) + ')'