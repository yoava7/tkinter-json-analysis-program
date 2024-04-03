"""
The entries calculator functionality.
"""
import AMQFolderReader


def entries_calc(AMQDict, user_input=None, input_type=None):
    """
    :param AMQDict: Valid Dictionary from AMQFolderReader.py
    :param user_input: The user's inputted anime name or song ID if they provided one
    :param input_type: Either none for all shows, id for song ID, or anime_name for an anime's name
    :return: none, prints out every guess of either the song of the given ID or every ID in the given anime
    """
    if input_type == "id":
        for entry in AMQDict[user_input]["total_entries"]:
            print(entry)
    elif input_type == "anime_name":
        id_list = AMQFolderReader.name_to_ids(AMQDict, user_input)
        for song in id_list:
            for entry in AMQDict[song]["total_entries"]:
                print(entry)


if __name__ == '__main__':
    entries_calc(AMQFolderReader.make_master_dict(), "Tensura", "anime_name")
