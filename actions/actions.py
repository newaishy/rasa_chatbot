from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractDrinkEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        drink_entity = next(tracker.get_latest_entity_values('drink'), None)

        if drink_entity:
            dispatcher.utter_message(text=f"You have selected {drink_entity} as your drink choice")
        else:
            dispatcher.utter_message(text="Sorry, i could not detect the drink choice")

        return []

class OrderDrinkAction(Action):
    def name(self) -> Text:
        return "action_order_food"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(text="What kind of drink would you like to order?")

        return[]
    
class ConfirmOrderAction(Action):
    def name(delf) -> Text:
        return "action_confirm_order"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        drink_entity = next(tracker.get_latest_entity_values('drink'), None)

        if drink_entity:
            dispatcher.utter_message(text=f"I have ordered you a {drink_entity} as you requested.")
        else:
            dispatcher.utter_message(text="Sorry, i could not detect the drink choice")

        return []