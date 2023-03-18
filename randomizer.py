import random


def randy():
    characters_defence = ["solis", "azami", "thorn", "thunderbird", "aruni", "melusi", "oryx", "wamai", "goyo", "warden", "mozzie", "kaid", "clash", "maestro", "alibi", "vigil", "ela", "lesion", "mira", "echo", "caviera", "valkyrie", "frost", "mute", "smoke", "castle", "pulse", "doc", "rook", "jäger", "bandit", "tachanka", "kapkan"]
    characters_attack = ["brava", "grim", "sens", "osa", "flores", "zero", "ace", "iana", "kali", "amaru", "nokk", "gridlock", "nomad", "maverick", "lion", "finka", "dokkaebi", "zofia", "ying", "jackal", "hibana", "capitao", "blackbeard", "buck", "sledge", "thatcher", "ash", "thermite", "montagne", "twitch", "blitz", "iq", "fuze", "glaz"]
    rand_def = random.choice(characters_defence)
    rand_att = random.choice(characters_attack)
    side = input("Which side would you like to choose? 'def' or 'att':  ").lower()
    while True:
        if side == "def":
            print(f"The randomizer picked: {rand_def}")
            break
        elif side == "att":
            print(f"The randomizer picked: {rand_att}")
            break
        else:
            print("You typed something wrong!")
        
        
    reroll = input("Would you like to re-roll? 'yes' or 'no' :").lower()
    if reroll == "yes":
        rerolling()


def rerolling():
    characters_defence = ["solis", "azami", "thorn", "thunderbird", "aruni", "melusi", "oryx", "wamai", "goyo", "warden", "mozzie", "kaid", "clash", "maestro", "alibi", "vigil", "ela", "lesion", "mira", "echo", "caviera", "valkyrie", "frost", "mute", "smoke", "castle", "pulse", "doc", "rook", "jäger", "bandit", "tachanka", "kapkan"]
    characters_attack = ["brava", "grim", "sens", "osa", "flores", "zero", "ace", "iana", "kali", "amaru", "nokk", "gridlock", "nomad", "maverick", "lion", "finka", "dokkaebi", "zofia", "ying", "jackal", "hibana", "capitao", "blackbeard", "buck", "sledge", "thatcher", "ash", "thermite", "montagne", "twitch", "blitz", "iq", "fuze", "glaz"]
    rand_def = random.choice(characters_defence)
    rand_att = random.choice(characters_attack)
    who = input("Which side would you like to reroll?: 'def' or 'att' :").lower()
    while True:
        if who == "def":
            print(f"your one and only re-roll picked: {rand_def}")
            break
        elif who == "att":
            print(f"your one and only re-roll picked: {rand_att}")
            break
        else:
            print("You typed something wrong!")

randy()