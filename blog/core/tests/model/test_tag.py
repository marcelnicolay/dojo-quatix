from django.test import TestCase
from core.models import Tag

class TagTest(TestCase):
    
    def test_can_create_simple_tag(self):
        
        tag = Tag()
        tag.name = 'shouldBeName'
        tag.slug = 'shouldBeSlug'
        tag.save()
        
        tag_find = Tag.objects.get(name=tag.name)
        self.assertEquals(tag_find.name, tag.name)
        self.assertEquals(tag_find.slug, tag.slug)
        self.assertEquals(tag_find.id, tag.id)
        
        tag.delete()
