"""
The Player Stats functionality.
Loads up the total points of a specific player or loads up the points of two players and compares them.
"""
import AMQFolderReader


def player_lookup(AMQDict, player_name=None, user_input=None, input_type=None):
    """
    Performs a lookup on an individual player.
    :param AMQDict: Valid Dictionary from AMQFolderReader.py
    :param player_name: A string of the name of the player to look up
    :param user_input: The user's inputted anime name or song ID if they provided one.
    :param input_type: Either none for all shows, id for song ID, or anime_name for an anime's name
    :return: A dictionary with all correct guesses with the specified parameters.
    """
    player_dict = {}
    for song in AMQDict:
        for entry in AMQDict[song]["total_entries"]:
            if player_name in entry["correctGuessPlayers"]:
                if song in player_dict:
                    player_dict[song].append(entry)
                else:
                    player_dict[song] = []
                    player_dict[song].append(entry)
    if input_type is None:
        return player_dict
    elif input_type == "id":
        if user_input in player_dict:
            return player_dict[user_input]
        else:
            return {}
    elif input_type == "anime_name":
        id_list = AMQFolderReader.name_to_ids(AMQDict, user_input)
        anime_ids_dict = {}
        for song in id_list:
            if song in player_dict:
                anime_ids_dict[song] = player_dict[song]
        return anime_ids_dict


def player_comparison(AMQDict, player1, player2, user_input=None, input_type=None):
    """
    Prints out which player has the greater
    :param AMQDict: Valid parsed dictionary from player_lookup
    :param player1: The string of a player's name to compare
    :param player2: The string of a player's name to compare
    :param user_input: The user's inputted anime name or song ID if they provided one
    :param input_type: Either none for all shows, id for song ID, or anime_name for an anime's name
    :return: none, prints out result
    """
    player1_stats = player_lookup(AMQDict, player1, user_input, input_type)
    player2_stats = player_lookup(AMQDict, player2, user_input, input_type)
    # Following is commented out for too much clutter.
    # print(f"{player1}'s stats are: \n{player1_stats}")
    # print(f"{player2}'s stats are: \n{player2_stats}")
    if len(player1_stats) > len(player2_stats):
        print(f"{player1} wins with a total of {len(player1_stats)} over {player2}'s total of {len(player2_stats)}")
    elif len(player1_stats) < len(player2_stats):
        print(f"{player2} wins with a total of {len(player2_stats)} over {player1}'s total of {len(player1_stats)}")
    elif len(player1_stats) == len(player2_stats):
        print(f"Both {player1} and {player2} are tied with {len(player1_stats)}, that's a bit sus!")


if __name__ == '__main__':
    master_dict = AMQFolderReader.make_master_dict("TestData")
    output = player_lookup(master_dict, "Asumin")
    player_comparison(master_dict, "QMLime", "Myst")
