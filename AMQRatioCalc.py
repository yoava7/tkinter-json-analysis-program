"""
The Ratio calculator functionality.
Fully implemented in AMQGUITry2.py.
"""
import AMQFolderReader


def total_ratio_return(AMQDict, user_input=None, input_type=None, min_entries=0, max_ratio=1):
    """
    :param AMQDict: Valid Dictionary from AMQFolderReader.py
    :param user_input: The user's inputted anime name or song ID if they provided one.
    :param input_type: Either none for all shows, id for song ID, or anime_name for an anime's name
    :param min_entries: The wanted minimum entries for an ID to be returned
    :param max_ratio: The max correct guess ratio for an ID to be returned
    :return: A list of every ID

    Commented out is for printing out the results.
    """
    if min_entries == "":
        min_entries = 1
    if max_ratio == "":
        max_ratio = 1
    min_entries = int(min_entries)
    max_ratio = float(max_ratio)
    dict_key_list = AMQFolderReader.get_dict_keys(AMQDict)
    ratio_dict = {}
    for song in dict_key_list:
        ratio_dict[song] = {
            "id": song,
            "total": (AMQDict[song]["correct"] + AMQDict[song]["incorrect"]),
            "ratio": (AMQDict[song]["correct"] / (AMQDict[song]["correct"] + AMQDict[song]["incorrect"])),
            "correct": AMQDict[song]["correct"],
            "incorrect": AMQDict[song]["incorrect"]}
    if input_type is None:
        returned_list = []
        for song in dict_key_list:
            # print(f"Song ID {song}:", end="")
            # print(" Ratio = " + str(ratio_dict[song]["ratio"]), end="")
            # print("  Total = " + str(ratio_dict[song]["correct"] + ratio_dict[song]["incorrect"]), end="")
            # print("  Correct = " + str(ratio_dict[song]["correct"]), end="")
            # print("  Incorrect = " + str(ratio_dict[song]["incorrect"]))
            if (len(AMQDict[song]["total_entries"]) >= min_entries) and (ratio_dict[song]["ratio"] <= max_ratio):
                returned_list.append(ratio_dict[song])
        return returned_list
    else:
        if input_type == "id":
            # print(f"Song ID {user_input}:", end="")
            # print(" Ratio = " + str(ratio_dict[user_input]["ratio"]), end="")
            # print("  Total = " + str(ratio_dict[user_input]["correct"] + ratio_dict[user_input]["incorrect"]), end="")
            # print("  Correct = " + str(ratio_dict[user_input]["correct"]), end="")
            # print("  Incorrect = " + str(ratio_dict[user_input]["incorrect"]))
            return [ratio_dict[user_input]]
        elif input_type == "anime_name":
            returned_list = []
            id_list = AMQFolderReader.name_to_ids(AMQDict, user_input)
            # print(f"For anime {user_input}: ")
            for song in id_list:
                # print(f"Song ID {song}:", end="")
                # print(" Ratio = " + str(ratio_dict[song]["ratio"]), end="")
                # print("  Total = " + str(ratio_dict[song]["correct"] + ratio_dict[song]["incorrect"]),
                #       end="")
                # print("  Correct = " + str(ratio_dict[song]["correct"]), end="")
                # print("  Incorrect = " + str(ratio_dict[song]["incorrect"]))
                if (len(AMQDict[song]["total_entries"]) >= min_entries) and (ratio_dict[song]["ratio"] <= max_ratio):
                    returned_list.append(ratio_dict[song])
            return returned_list
        else:
            print("SOMETHING DIDN'T HAPPEN IN TOTAL_RATIO_RETURN")


def main():
    print(total_ratio_return(AMQFolderReader.make_master_dict(), min_entries=3))


if __name__ == '__main__':
    main()
