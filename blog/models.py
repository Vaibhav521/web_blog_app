from django.db import models
from django.utils.html import format_html
from froala_editor.fields import FroalaField



from django.contrib.auth.models import User
from django.utils.timezone import now

# Categorys  

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description = models.TextField()
    url=models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/")
    add_date = models.DateField(auto_now=True,null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="height:40px;width:40px;border-radius:50%;" />'.format(self.image)  )

    def __str__(self) :
        return  self.title

# post 

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title =models.CharField(max_length=200)
    content = FroalaField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

 

    def __str__(self) :
        return  self.title


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.author.username} on {self.post.title}"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=now)

    def  __str__(self):
        return self.name