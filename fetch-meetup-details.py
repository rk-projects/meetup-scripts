"""
Fetch Meetup Details like upcoming events and comments from those events.abs
"""
import meetup.api

CLIENT = meetup.api.Client(overlimit_wait=True)

GROUP = CLIENT.GetGroup({'urlname': 'fosscafe'})

all_upcoming_events = CLIENT.GetEvents(group_id = GROUP.id , status = "upcoming")
for upcoming_event in all_upcoming_events.results:
    print ("Event Name : " + upcoming_event['name'] + " \t Event ID : "+ upcoming_event['id'])
    upcoming_event_comments = CLIENT.GetEventComments(event_id = upcoming_event['id'])
    for comments in upcoming_event_comments.results:
        print(comments['member_name'] + "\t\t" +comments['comment'])
        
    print("---------------------------")
