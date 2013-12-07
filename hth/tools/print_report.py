import sys

from debugged.calendar.models import Event
from debugged.management.models import EventReport

if __name__ == "__main__":
    tour_slug = sys.argv[1]
    
    print "-------\n"
    
    reports = EventReport.objects.filter(event__parent__slug=tour_slug)
    for report in reports:
        event = report.event
        location = event.location

        print "%d/%d/%d: %s, %s, %s " % (event.start_date.month, event.start_date.day, event.start_date.year,
                                           location.name, location.city, location.region)
                                           
        try:
            bands = event.notes.filter(object_type__slug='bands')[0].content.strip()
            if bands:
                print "    %s" % bands
        except:
            pass
        
        try:
            print "Take: $%d" % report.door_income
        except:
            pass
            
        try:
            print "Merch: $%d" %  report.merch_income
        except:
            pass
            
        
        notes = report.notes.strip()
        if notes:
            print "\n%s" % notes

        print "\n-------"
