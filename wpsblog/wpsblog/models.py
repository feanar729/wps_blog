from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

# Posts list( /posts/ ) -> 이 주소로 들어갔을 때 <h1>Posts list</h1>으로 나오게 해보기...
# Posts Detail ( /posts/:id )
