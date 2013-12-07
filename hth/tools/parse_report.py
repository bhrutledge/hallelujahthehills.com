import sys
import csv

from debugged.calendar.models import Event
from debugged.management.models import EventReport

if __name__ == "__main__":
    for row in csv.reader(open(sys.argv[1], 'rb')):
        date = row[0]
        try:
            door = round(float(row[15]))
            merch = round(float(row[14]))
            event = Event.objects.get(slug=date)
        except:
            print "Skipping " + date
            continue
        
        print "Creating report for " + date
        EventReport.objects.create(event=event, door_income=door, merch_income=merch)
        

