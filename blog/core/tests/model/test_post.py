"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from core.models import Post, Tag

from datetime import datetime

class PostTest(TestCase):

    def test_can_create_simple_post(self):
        post = Post()
        post.title = "should be title"
        post.subtitle = "should be subtitle"
        post.created = datetime.now()
        post.body = "should be body"
        
        post.save()
        
        post_find = Post.objects.get(title=post.title)
        self.assertEquals(post_find.title, post.title)
        self.assertEquals(post_find.id, post.id)
        self.assertEquals(post_find.subtitle, post.subtitle)
        self.assertEquals(post_find.body, post.body)
        self.assertEquals(post_find.created, post.created)

        post.delete()

    def test_can_add_tags_to_post(self):
        tag1 = Tag(name='my first tag', slug='my-first-tag')
        tag1.save()
        tag2 = Tag(name='my second tag', slug='my-second-tag')
        tag2.save()

        post = Post()
        post.title = "should be title"
        post.subtitle = 'should be subtitle'
        post.created = datetime.now()
        post.body =  "should be body"
        post.save()

        post.tags = [tag1, tag2]

        post_found = Post.objects.get(title=post.title)
        self.assertIn(tag1, post_found.tags.all())
        self.assertIn(tag2, post_found.tags.all())
        self.assertEquals(len(post_found.tags.all()), 2)
        
    def test_can_auto_set_created(self):
        post = Post.objects.create(title="shoudBeTitle", subtitle="should be subtitle", body="shoudBeBody")
        
        self.assertIsNotNone(post.created)