"""This module represents a PokeFacade"""
import re

from pokeretriever.apicaller import ApiCaller
from pokeretriever.pokedexobject import PokedexObject
from pokeretriever.stats import Stats
from pokeretriever.pokemon import Pokemon
from pokeretriever.move import Move
from pokeretriever.ability import Ability
import asyncio


class PokeFacade:
    """
    Represents a facade that provides a simplified interface
    to the pokeretriever package.
    """

    @staticmethod
    def execute_request(request) -> PokedexObject:
        """
        Drives processing the request passed by calling the ApiHandler class
        to grab the data to create and return a PokedexObject
        :param request: a Request
        :return: a PokedexObject
        """
        try:
            loop = asyncio.get_event_loop()
            api_result = loop.run_until_complete(ApiCaller.call_api(request))
            return PokeFacade.create_pokedexobject(api_result, request)
        except Exception:
            print(f"Error: There was a problem while retrieving data from the Pokemon API")

    @staticmethod
    def create_pokedexobject(object_dict, request):
        """
        Creates a PokedexObject
        :param object_dict: a dictionary of JSON objects
        :param request: a Request
        :return: a PokedexObject
        """
        mode_json = object_dict["mode"]
        if mode_json is None:
            print(f"The {request.mode.value} requested could not be retrieved.")
            return None
        name = mode_json["name"]
        item_id = mode_json["id"]
        if request.mode.value == "pokemon":
            height = mode_json["height"]
            weight = mode_json["weight"]
            poke_types = []
            for field_type in mode_json["types"]:
                name_type = field_type["type"]["name"]
                poke_types.append(name_type)
            pokemon = Pokemon(name=name, id=item_id, height=height, weight=weight, types=poke_types)
            PokeFacade.create_stat(object_dict, pokemon, request)
            PokeFacade.create_ability(object_dict, request, pokemon)
            PokeFacade.create_move(object_dict, request, pokemon)
            return pokemon

        elif request.mode.value == "move":
            return PokeFacade.create_move(object_dict, request)

        elif request.mode.value == "ability":
            return PokeFacade.create_ability(object_dict, request)

    @staticmethod
    def create_stat(object_dict, pokemon, request):
        """
        Creates a Stat object
        :param object_dict: a dictionary of JSON objects
        :param pokemon: a Pokemon
        :param request: a Request
        :return: a PokedexObject, else None if modifying passed Pokemon object
        """
        mode_object = object_dict["mode"]
        index = 0
        for stat in mode_object["stats"]:
            base_stat = stat["base_stat"]
            name = stat["stat"]["name"]
            unprocessed_id = stat["stat"]["url"]
            processed_id = re.search(r'/(\d+)/', unprocessed_id).group(1)
            stat = Stats(name=name, base_stat=base_stat, id=processed_id)
            if request.expanded:
                is_battle_only = object_dict["stats"][index]["is_battle_only"]
                stat.set_is_battle_only(is_battle_only)
            index += 1
            pokemon.add_stat(stat)

    @staticmethod
    def create_move(object_dict, request, pokemon=None):
        """
        Creates a Move object
        :param object_dict: a dictionary of JSON objects
        :param pokemon: a Pokemon
        :param request: a Request
        :return: a PokedexObject, else None if modifying passed Pokemon object
        """
        mode_json = object_dict["mode"]
        index = 0
        if request.mode.value == "pokemon":
            for move in mode_json["moves"]:
                name = move["move"]["name"]
                unprocessed_id = move["move"]["url"]
                processed_id = re.search(r'/(\d+)/', unprocessed_id).group(1)
                level = move["version_group_details"][0]["level_learned_at"]
                move = Move(name=name, id=processed_id)
                move.set_level_learned_at(level)
                if request.expanded and len(object_dict["moves"]) != 0 and object_dict["moves"][index] is not None:
                    move.set_generation(object_dict["moves"][index]["generation"]["name"])
                    move.set_accuracy(object_dict["moves"][index]["accuracy"])
                    move.set_pp(object_dict["moves"][index]["pp"])
                    move.set_power(object_dict["moves"][index]["power"])
                    move.set_type(object_dict["moves"][index]["type"]["name"])
                    move.set_damage_class(object_dict["moves"][index]["damage_class"]["name"])
                    move.set_level_learned_at_to_none()
                    for effect in object_dict["moves"][index]["effect_entries"]:
                        if effect["language"]["name"] != "en":
                            continue
                        else:
                            move.set_short_effect(effect["short_effect"])
                index += 1
                pokemon.add_move(move)
        if request.mode.value == "move":
            name = mode_json["name"]
            move_id = mode_json["id"]
            move = Move(name=name, id=move_id)
            move.set_generation(mode_json["generation"]["name"])
            move.set_accuracy(mode_json["accuracy"])
            move.set_pp(mode_json["pp"])
            move.set_power(mode_json["power"])
            move.set_type(mode_json["type"]["name"])
            move.set_damage_class(mode_json["damage_class"]["name"])
            move.set_level_learned_at_to_none()
            for effect in mode_json["effect_entries"]:
                if effect["language"]["name"] != "en":
                    continue
                else:
                    move.set_short_effect(effect["short_effect"])
            return move

    @staticmethod
    def create_ability(object_dict, request, pokemon=None):
        """
        Creates an Ability object
        :param object_dict: a dictionary of JSON objects
        :param pokemon: a Pokemon
        :param request: a Request
        :return: a PokedexObject, else None if modifying passed Pokemon object
        """
        mode_json = object_dict["mode"]
        index = 0
        if request.mode.value == "pokemon":
            for ability in mode_json["abilities"]:
                name = ability["ability"]["name"]
                unprocessed_id = ability["ability"]["url"]
                processed_id = re.search(r'/(\d+)/', unprocessed_id).group(1)
                ability = Ability(name=name, id=processed_id)
                if request.expanded and len(object_dict["abilities"]) != 0 and object_dict["abilities"][index] \
                        is not None:
                    ability.set_generation(object_dict["abilities"][index]["generation"]["name"])
                    for effect in object_dict["abilities"][index]["effect_entries"]:
                        if effect["language"]["name"] != "en":
                            continue
                        else:
                            ability.set_effect(effect["effect"])
                            ability.set_short_effect(effect["short_effect"])
                    pokemon_list = []
                    for pokemon_field in object_dict["abilities"][index]["pokemon"]:
                        pokemon_list.append(pokemon_field["pokemon"]["name"])
                    ability.set_pokemon(pokemon_list)
                index += 1
                pokemon.add_ability(ability)
        if request.mode.value == "ability":
            name = mode_json["name"]
            ability_id = mode_json["id"]
            ability = Ability(name=name, id=ability_id)
            ability.set_generation(mode_json["generation"]["name"])
            for effect in mode_json["effect_entries"]:
                if effect["language"]["name"] != "en":
                    continue
                else:
                    ability.set_effect(effect["effect"])
                    ability.set_short_effect(effect["short_effect"])
            pokemon_list = []
            for pokemon_field in mode_json["pokemon"]:
                pokemon_list.append(pokemon_field["pokemon"]["name"])
            ability.set_pokemon(pokemon_list)
            return ability
