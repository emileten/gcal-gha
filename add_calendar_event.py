from __future__ import print_function

import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def main():
    
    try:
        service = build('calendar', 'v3')

        event = {
        'summary': 'Test event with service account',
        'location': 'Seoul, Korea',
        'description': 'Testing inserting event with service account running python code.',
        'start': {
        'dateTime': '2023-05-16T11:30:00+09:00',
        'timeZone': 'Asia/Seoul',
        },
        'end': {
        'dateTime': '2023-05-16T11:40:00+09:00',
        'timeZone': 'Asia/Seoul',
        }
        }

        event_result = service.events().insert(calendarId=os.environ['calendar_id'], body=event).execute()
        print('Event created: %s' % (event_result.get('htmlLink')))

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()