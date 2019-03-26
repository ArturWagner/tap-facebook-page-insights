import requests
import json


def get_page_insights(config, metrics):
    parameters = {
        'since': config['start_date'],
        'until': config['end_date'],
        'metric': metrics,
        'period': 'days_28',
        'access_token': config['access_token']
    }
    insights = requests.get(
        'https://graph.facebook.com/v3.2/{page_id}/insights?'.format(
            page_id=config['page_id']),
        params=parameters)

    return json.loads(insights.content)
