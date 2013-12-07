import sys
from datetime import datetime, date
from lxml import html
from debugged.contacts.models import Location, Contact
from debugged.calendar.models import Event

BAND_CONTACT_TYPE = 'band'
CLUB_LOCATION_TYPE = 'club'
GIG_EVENT_TYPE = 'gig'
TOUR_EVENT_TYPE = 'tour'


def parse_slug(event):
    return event.get('id')[len('event-'):]

def parse_venue(venue):
    venue_tag = venue.find_class('venue')[0]
    name = venue_tag.text_content()
    city, region = venue.find_class('city')[0].text_content().split(', ')
    
    try:
        return Location.objects.get(name=name, city=city, region=region)
    except:
        location = Location(name=name, city=city, region=region)
        location.object_type = CLUB_LOCATION_TYPE
        
        if region == 'QC' or region == 'ON':
            location.country = 'CA'
            
        if venue_tag.tag == 'a':
            location.website = venue_tag.get('href')
            
        location.save()
        
        print "Venue: " + str(location)
        return location
    
def parse_gig(gig, tour=None):
    slug = parse_slug(gig)
    
    try:
        return Event.objects.get(slug=slug)
    except:
        event = Event()
        event.slug = slug
        event.object_type = GIG_EVENT_TYPE
        event.location = parse_venue(gig.find_class('location')[0])
        event.start_date = datetime.strptime(gig.find_class('dtstart')[0].get('title'), '%Y-%m-%d').date()
        event.parent = tour
        event.save()
    
        print "Gig: " + str(event)

        """
        for note_class, note_type in NOTE_MAP.items():
            try:
                note_content = gig.find_class(note_class)[0].text_content()
            except:
                continue
            
            if not note_content:
                continue
        
            note = Note(content=note_content)
            note.object_type = note_type
            note.parent = event
            note.save()
        """
    
        return event
    
def parse_tour(tour):
    slug = parse_slug(tour)
    
    try:
        event = Event.objects.get(slug=slug)
    except:
        event = Event()
        event.slug = slug
        event.object_type = TOUR_EVENT_TYPE
        event.start_date = datetime.strptime(tour.find_class('dtstart')[-1].get('title'), '%Y-%m-%d').date()
        event.name = tour.cssselect('h3')[0].text_content()
        event.save()
        
        print "Tour: " + str(event)
    
    for gig in tour.find_class('gig'):
        parse_gig(gig, event)

    return event
    
if __name__ == "__main__":
    cal_string = open(sys.argv[1]).read()
    cal = html.fragment_fromstring(cal_string)

    for event in cal:
        event_class = event.get('class')
        if event_class.startswith('gig'):
            parse_gig(event)
        if event_class.startswith('tour'):
            parse_tour(event)
