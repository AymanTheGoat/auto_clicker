from random import choice


def welcome(colors):
    welcomes = [
        "Skibidi-fishing time! Grab your rod, mog the oceans, and catch some gyatt-level loot! Let's gooo!",
        "Welcome to the autofisher grind! Baby Gronk wishes you skibidi luck—time to mog these fish!",
        "Time to edge those fish closer and closer... to your inventory. Get ready for some Ohio-tier catches!",
        "Yo, fisher, let's reel in some grimace shake-tier loot! Don't be cringe, keep it sigma!",
        "Gooning over fishing? Edging closer to being the top Minecraft pro. Let's skibidi GO!",
        "Mewing hard while you autofish? Big brain plays. Phanum tax paid, let's rizz these waters!",
        "It's not just fishing; it's sigma grindset. Mog the sea, mog the game!",
        "Welcome, Minecraft mogger! The fish don't stand a chance—this script is built diff!",
        "Ready to Ligma some treasure from the ocean? Let's Livee Dunn-level this auto-fishing sesh!",
        "You're about to rizz the waters like Kai Cenat with a fishing rod. Skibidi baaaap!",
        "Skibidi systems online—time to mog the oceans and rizz up the AFK grind, king.",
        "Ohio vibes initialized—your rod game is about to hit Sigma status, fisherman.",
        "Baby Gronk-tier grind incoming—prepare to mog the waters with max Goon energy.",
        "Grimace shake loading—your AFK journey starts now, no Phanum tax required.",
        "Level 99 Gyatt energy detected—let's mew our way to fishing dominance, gamer.",
        "Kai Cenat-coded AFK vibes online—rizz up those seas like a true Sigma.",
        "Autofish mogging protocol active—make the oceans cringe with your Beta flex.",
        "Livee Dunn herself would approve—skibidi bop and mog those waters.",
        "Ohio dominance detected—time to rizz up some enchanted loot, AFK lord.",
        "Sigma grindset locked in—let's Goon our way to AFK greatness.",
    ]
    if colors:  
        print(f"\033[95m{choice(welcomes)}\033[0m")
        return
    print(choice(welcomes))


def farewell(colors):
    farewells = [
        "Gooning complete, mogging the fish done—time to dip. Until next time, fisher legend!",
        "You've sigma-ed your way outta here. Come back soon and mog the oceans again!",
        "GG, that was a Baby Gronk-tier session. Livee Dunn says bye, and so do I!",
        "Cringe to leave, but you're leaving on a Grimace shake high note. Skibidi out!",
        "Log off like a true sigma. The fish will fear your return. Ligma later!",
        "Time to Kai Cenat your way to the exit. Keep mogging IRL, champ!",
        "Don't be cringe, come back soon to mog the oceans again. GGs, my gyatt-fisher!",
        "Phanum tax paid, grind completed. Skibidi farewell, Minecraft king!",
        "The fish are safe... for now. Goon hard in real life till your next fishing sesh!",
        "Peace out, you edgy sigma. Leave the cringe to others; you mogged today!",
        "AFK grind complete—oceans mogged, loot secured, skibidi bop signing off.",
        "Sigma fisherman out—cringe waters left trembling in your AFK wake.",
        "Shutting down with Kai Cenat-level precision—Baby Gronk-tier loot achieved.",
        "Rod down, grind over—Livee Dunn herself couldn't mog this AFK game harder.",
        "Grimace shake of victory—AFK grind done, oceans thoroughly edged.",
        "Logging off like a true Sigma—Phanum tax dodged, oceans mogged.",
        "Ohio-style sign-off—cringe fish left behind, AFK mastery secured.",
        "Skibidi bop shutdown initiated—Sigma status remains untouched.",
        "The oceans were mogged, the loot was gyatted—AFK grind complete.",
        "Beta script disengaged—Baby Gronk-level AFK vibes achieved, goodbye.",
    ]

    if colors: 
        print(f"\n\033[95m{choice(farewells)}\033[0m")
        return
    print(choice(farewells))
