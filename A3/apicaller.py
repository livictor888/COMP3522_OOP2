"""This module represent an ApiCaller"""
import aiohttp


class ApiCaller:
    """
    This class represents an ApiCaller that makes
    requests to the Pokemon API with an endpoint
    specified by the Request's stored mode.
    """

    @staticmethod
    async def call_api(request):
        """
        Calls the Pokemon API with an endpoint
        created from the mode and name/id stored
        in Request and creates a dictionary of JSON
        objects returned from the API.
        :param request: a Request
        :return: a dictionary of JSON objects, else None if the API returns
        a status code that is not 200
        """
        objects = dict()
        objects["mode"] = None
        objects["stats"] = []
        objects["abilities"] = []
        objects["moves"] = []
        async with aiohttp.ClientSession() as session:
            async with session.get('https://pokeapi.co/api/v2/' + request.mode.value + "/" + request.current_item) \
                    as response:
                if response.status == 200:
                    response_object = await response.json()
                    objects["mode"] = response_object
                else:
                    print(f"Error: The name or id {request.current_item} was not able to be retrieved")
        if request.expanded and request.mode.value == "pokemon" and response.status == 200:
            await ApiCaller.call_expanded(response_object, "stats", "stat", objects)
            await ApiCaller.call_expanded(response_object, "moves", "move", objects)
            await ApiCaller.call_expanded(response_object, "abilities", "ability", objects)
        return objects

    @staticmethod
    async def call_expanded(json_object, parent, child, objects_dict):
        """
        Calls API for nested fields in expanded mode and returns the JSON objects.
        :param json_object: a JSON object of a nested field
        :param parent: the parent nested field key
        :param child: the child nested field key
        :param objects_dict: a dictionary of JSON objects
        """
        for field in json_object[parent]:
            url = field[child]['url']
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        response_object = await response.json()
                        objects_dict[parent].append(response_object)
                    else:
                        objects_dict[parent].append(None)
                        print(f"Error: There was a problem while fetching expanded fields from {json_object['name']}")
                        print(f"{url}")
