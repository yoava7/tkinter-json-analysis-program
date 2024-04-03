import os
import json


def make_master_dict(file_folder=None):
    """
    :param file_folder: A folder with AMQ ranked game exports.
    :return: A dict of every song ID played, with the song info and a list of
    total entries of said song.
    :precondition: file_folder must only have AMQ exports.
    """
    master_dict = {}
    directory = file_folder
    files_list = os.listdir(directory)

    for file in files_list:
        with open(directory + "\\" + file) as current_file:
            for line in current_file:
                loaded = json.loads(line)
                if "videoUrl" in loaded["songs"][0]:  # Checks if file has song IDs
                    for song in loaded["songs"]:
                        if song["videoUrl"][-10:-4] in master_dict:
                            pass
                        else:
                            # Creates keys for a new song's dict
                            master_dict[song["videoUrl"][-10:-4]] = {}
                            master_dict[song["videoUrl"][-10:-4]]["info"] = song["songInfo"]
                            master_dict[song["videoUrl"][-10:-4]]["correct"] = 0
                            master_dict[song["videoUrl"][-10:-4]]["incorrect"] = 0
                            master_dict[song["videoUrl"][-10:-4]]["total_entries"] = []

                        # Adding correct or incorrect count
                        if song["correctGuess"]:
                            master_dict[song["videoUrl"][-10:-4]]["correct"] += 1
                        else:
                            master_dict[song["videoUrl"][-10:-4]]["incorrect"] += 1

                        # Adding guess to entries for song:
                        song_key_list_dict_keys = song.keys()
                        song_key_list = []
                        song_entry_dict = {}

                        for thing in song_key_list_dict_keys:
                            song_key_list.append(thing)
                        song_key_list.remove("songInfo")
                        # THIS IS SUPER JANK, AMQ NEEDS TO CHANGE THEIR FILE NAMES!!!
                        split_file_name = file.split("-")
                        date_placeholder = split_file_name[1] + "-" + split_file_name[2] + "-" + split_file_name[3][:2]
                        time_placeholder = split_file_name[3][3:]+":"+split_file_name[4]+":"+split_file_name[5][:2]
                        song_entry_dict["date"] = date_placeholder
                        song_entry_dict["time"] = time_placeholder
                        for key in song_key_list:
                            song_entry_dict[key] = song[key]
                        master_dict[song["videoUrl"][-10:-4]]["total_entries"].append(song_entry_dict)
                else:
                    print(f"File: {file}  does not have song IDs, its data was not added.")
    return master_dict


def get_dict_keys(song_dict):
    """
    Technically redundant.
    :param song_dict: Valid AMQDict from make_master_dict
    :return: a list of song IDs from the given dictionary
    """
    list_of_dict_keys = song_dict.keys()
    return list_of_dict_keys


def name_to_ids(AMQDict: dict, anime_name: str = None):
    """
    Gets all IDs from a given show.
    :param AMQDict: Valid AMQDict from make_master_dict
    :param anime_name: A string of the wanted anime name
    :return: A list of IDs that appear in the show.
    """
    id_list = []
    for song in AMQDict:
        if anime_name == AMQDict[song]["info"]["animeNames"]["english"]\
                or anime_name == AMQDict[song]["info"]["animeNames"]["romaji"]\
                or anime_name in AMQDict[song]["info"]["altAnimeNames"]\
                or anime_name in AMQDict[song]["info"]["altAnimeNamesAnswers"]:
            id_list.append(song)
    return id_list


def id_to_name(AMQDict: dict, song_id: str):
    """
    Gets the name of a show from the given ID.
    :param AMQDict: Valid AMQDict from make_master_dict
    :param song_id: a string of the given song's ID
    :return: A string of the english name of the anime.
    """
    return AMQDict[song_id]["info"]["animeNames"]["english"]


def main():
    anime_dict = make_master_dict()
    print(name_to_ids(anime_dict, "Yakusoku no Neverland"))
    for entry in anime_dict["ezttt3"]["total_entries"]:
        print(entry)


if __name__ == '__main__':
    main()
