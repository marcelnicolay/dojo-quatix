from django.test import TestCase
from core.models import Post

class HomeViewTestCase(TestCase):
    
    def test_can_view_home(self):
        
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_view_last_10_posts(self):
        posts = []
        for i in xrange(0, 11):
            post = Post.objects.create(title="shouldBeTitle %s" % i)
            posts.append(post)

        response = self.client.get('/')
        
        posts_found = response.context['posts']
        posts.reverse()
    
        for i in xrange(0, 10):
            self.assertEquals(posts_found[i].title, posts[i].title)
            self.assertIn(posts_found[i].title, response.content)
            self.assertIn(posts_found[i].created.strftime("%d/%m/%Y"), response.content)
