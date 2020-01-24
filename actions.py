from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_sdk import Action

logger = logging.getLogger(__name__)


class ActionPassword(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_password"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        message = {
            "attachments": [
                {
                    "text": "Hi, How can I assist you?",
                    "attachment_type": "default",
                    "actions": [
                        {
                            "name": "Password",
                            "text": "Password Reset",
                            "type": "button",
                            "value": "Password Reset"
                        }
                    ]
                }
            ]
        }
        dispatcher.utter_custom_json(message)
        return []
