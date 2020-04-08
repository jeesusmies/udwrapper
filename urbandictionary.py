import requests
import json

UD_URL = 'https://api.urbandictionary.com/v0/define?term='
UD_RANDOM_URL = 'https://api.urbandictionary.com/v0/random'

class UrbanDictionary:
    def __init__(self):
        pass

    def _return_dict(parsed_json)
        result = {"word": parse_json[0],
                "def": parse_json[1],
                "date": parse_json[2],
                "eg": parse_json[3],
                "t_up": parse_json[4],
                "t_down": parse_json[5],
                "p_link": parse_json[6],
                "str": f"{result["word"]}: {result["def"][:50]}{'...' if len(result["def"]) > 50 else ''} ({result["date"]})"}
        
        return result
        
    def _parse_json(url, page: int = None):
        if page == None:
            page = 0
        result = []
        response = requests.get(url)
        # lol variable names because i am stupid
        json_thing = response.json()
        data = json_thing["list"][page]
        try:
            result.extend((data["word"],
                        data["definition"],
                        data["written_on"],
                        data["example"],
                        data["thumbs_up"],
                        data["thumbs_down"],
                        data["permalink"]))
        except:
            return 0 # means not found or something is broken
        
        return result
        
    def define(word, page: int = None):
        url = UD_URL + word
        return self._return_dict(_parse_json(url, page))
        
    def random():
        return self._return_dict(_parse_json(UD_RANDOM_URL))
        
