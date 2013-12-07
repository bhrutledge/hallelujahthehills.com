import sys
import os.path

from lxml import html
from django.core.files.base import ContentFile
from debugged.calendar.models import Event
from debugged.attachments.models import ImageType, ImageSize, Image

FLYER_IMAGE_TYPE = ImageType.objects.get_or_create(name='Flyer', slug='flyer')[0]

def create_sizes():
    thumbnail = ImageSize.objects.get_or_create(name='Thumbnail', slug='thumbnail')[0]
    thumbnail.width = 150
    thumbnail.height = 150
    thumbnail.crop = True
    thumbnail.save()
    
    medium = ImageSize.objects.get_or_create(name='Medium', slug='medium')[0]
    medium.width = 300
    medium.height = 0
    medium.crop = False
    medium.save()

def parse_flyer(flyer, root_dir='.'):
    event_slug = flyer.get('id')[len('flyer-'):]
    try:
        event = Event.objects.get(slug=event_slug)
        print event_slug
    except:
        print "Not found: " + event_slug
        return

    flyer_link = flyer[0].get('href')
    flyer_path = os.path.join(root_dir, os.path.splitext(flyer_link)[0] + '.jpg')
    flyer_name = os.path.join('images', os.path.basename(flyer_path))
        
    image = Image(object_type=FLYER_IMAGE_TYPE, parent=event)
    image.title = unicode(event) + ' flyer'
    image.featured = True
    image.image.save(flyer_name, ContentFile(open(flyer_path, 'rb').read()))
    image.save()

if __name__ == "__main__":
    create_sizes()
    
    root_dir = os.path.dirname(sys.argv[1])
    flyers_string = open(sys.argv[1]).read()
    flyers = html.fragment_fromstring(flyers_string)
    
    for flyer in flyers:
        parse_flyer(flyer, root_dir)