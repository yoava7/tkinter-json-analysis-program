# Yoav's Personal AMQ Ranked Match Data Parsing Program
## Description
This program is meant for studying your own (or any other player in the provided training data's) performance in the ranked game mode of AnimeMusicQuiz.com
## Features
**Song Ratios Functionality**
- Ability to see your guess rate and your total number of guesses on a specific song by using its AMQ song ID.
- Ability to see your guess rate and your total number of guesses on every song in a specific anime using either the roumaji or English (if one exists) naming  of an anime.

**Database Functionality**
  - Ability to access every song alongside its type (Opening, Ending, or Insert), and the information of the anime it comes from (or the first anime in records if it appears in more than one).
     - The library of songs that appear can be filtered by the minimum entries of a song or by the song's maximum correct guess ratio.

**Entries Functionality (PTUI ONLY)**
- Ability to see every entry of a song. Alongside the typical song info shown, a list of the players who correctly guessed the song is also present for each entry.
  - Like in Song Ratios, you may specify to either include a single song using its AMQ song ID, or include an Anime name- which will return all entries for every song present in the Anime.

  **Player Lookup Functionality (PTUI ONLY)**
  - Ability to see the score of a specific player over the entire period provided by the user.
  - Ability to compare the scores of two users and see which one has the higher score.

  ## Important Note
  Due to the nature of the game, you must provide the program with your own JSON files of ranked matches. To do this, simply put all your JSON files in a folder **with nothing else in it**, and either select it in the GUI or pass its path in the make_master_dict() method in AMQFOLDERREADER.py as the argument (the latter is only needed if you intend to use PTUI only features).
