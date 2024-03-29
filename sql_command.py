import mysql.connector

# Note: Please use string as all arguments' type

mydb = mysql.connector.connect(
    # host="140.113.68.114",
    host="localhost",
    user="manager",
    password="toServer111550009",
    database="db_final"
)
mycursor = mydb.cursor()

# all possible tags
genresList = ['Action', 'Free to Play', 'Strategy', 'Adventure', 'Indie', 'RPG', 'Animation & Modeling', 'Video Production', 'Casual', 'Simulation', 'Racing', 'Violent', 'Massively Multiplayer', 'Nudity', 'Sports', 'Early Access', 'Gore', 'Utilities', 'Design & Illustration', 'Web Publishing', 'Education', 'Software Training', 'Sexual Content', 'Audio Production', 'Game Development', 'Photo Editing', 'Accounting', 'Documentary', 'Tutorial']
categoriesList = ['Multi-player', 'Online Multi-Player', 'Local Multi-Player', 'Valve Anti-Cheat enabled', 'Single-player', 'Steam Cloud', 'Steam Achievements', 'Steam Trading Cards', 'Captions available', 'Partial Controller Support', 'Includes Source SDK', 'Cross-Platform Multiplayer', 'Stats', 'Commentary available', 'Includes level editor', 'Steam Workshop', 'In-App Purchases', 'Co-op', 'Full controller support', 'Steam Leaderboards', 'SteamVR Collectibles', 'Online Co-op', 'Shared/Split Screen', 'Local Co-op', 'MMO', 'VR Support', 'Mods', 'Mods (require HL2)', 'Steam Turn Notifications']
spytagsList = ['1980s', '1990s', '2.5d', '2d', '2d_fighter', '360_video', '3d', '3d_platformer', '3d_vision', '4_player_local', '4x', '6dof', 'atv', 'abstract', 'action', 'action_rpg', 'action_adventure', 'addictive', 'adventure', 'agriculture', 'aliens', 'alternate_history', 'america', 'animation_&_modeling', 'anime', 'arcade', 'arena_shooter', 'artificial_intelligence', 'assassin', 'asynchronous_multiplayer', 'atmospheric', 'audio_production', 'bmx', 'base_building', 'baseball', 'based_on_a_novel', 'basketball', 'batman', 'battle_royale', 'beat_em_up', 'beautiful', 'benchmark', 'bikes', 'blood', 'board_game', 'bowling', 'building', 'bullet_hell', 'bullet_time', 'crpg', 'capitalism', 'card_game', 'cartoon', 'cartoony', 'casual', 'cats', 'character_action_game', 'character_customization', 'chess', 'choices_matter', 'choose_your_own_adventure', 'cinematic', 'city_builder', 'class_based', 'classic', 'clicker', 'co_op', 'co_op_campaign', 'cold_war', 'colorful', 'comedy', 'comic_book', 'competitive', 'conspiracy', 'controller', 'conversation', 'crafting', 'crime', 'crowdfunded', 'cult_classic', 'cute', 'cyberpunk', 'cycling', 'dark', 'dark_comedy', 'dark_fantasy', 'dark_humor', 'dating_sim', 'demons', 'design_&_illustration', 'destruction', 'detective', 'difficult', 'dinosaurs', 'diplomacy', 'documentary', 'dog', 'dragons', 'drama', 'driving', 'dungeon_crawler', 'dungeons_&_dragons', 'dynamic_narration', 'dystopian_', 'early_access', 'economy', 'education', 'emotional', 'epic', 'episodic', 'experience', 'experimental', 'exploration', 'fmv', 'fps', 'faith', 'family_friendly', 'fantasy', 'fast_paced', 'feature_film', 'female_protagonist', 'fighting', 'first_person', 'fishing', 'flight', 'football', 'foreign', 'free_to_play', 'funny', 'futuristic', 'gambling', 'game_development', 'gamemaker', 'games_workshop', 'gaming', 'god_game', 'golf', 'gore', 'gothic', 'grand_strategy', 'great_soundtrack', 'grid_based_movement', 'gun_customization', 'hack_and_slash', 'hacking', 'hand_drawn', 'hardware', 'heist', 'hex_grid', 'hidden_object', 'historical', 'hockey', 'horror', 'horses', 'hunting', 'illuminati', 'indie', 'intentionally_awkward_controls', 'interactive_fiction', 'inventory_management', 'investigation', 'isometric', 'jrpg', 'jet', 'kickstarter', 'lego', 'lara_croft', 'lemmings', 'level_editor', 'linear', 'local_co_op', 'local_multiplayer', 'logic', 'loot', 'lore_rich', 'lovecraftian', 'mmorpg', 'moba', 'magic', 'management', 'mars', 'martial_arts', 'massively_multiplayer', 'masterpiece', 'match_3', 'mature', 'mechs', 'medieval', 'memes', 'metroidvania', 'military', 'mini_golf', 'minigames', 'minimalist', 'mining', 'mod', 'moddable', 'modern', 'motocross', 'motorbike', 'mouse_only', 'movie', 'multiplayer', 'multiple_endings', 'music', 'music_based_procedural_generation', 'mystery', 'mystery_dungeon', 'mythology', 'nsfw', 'narration', 'naval', 'ninja', 'noir', 'nonlinear', 'nudity', 'offroad', 'old_school', 'on_rails_shooter', 'online_co_op', 'open_world', 'otome', 'parkour', 'parody_', 'party_based_rpg', 'perma_death', 'philisophical', 'photo_editing', 'physics', 'pinball', 'pirates', 'pixel_graphics', 'platformer', 'point_&_click', 'political', 'politics', 'pool', 'post_apocalyptic', 'procedural_generation', 'programming', 'psychedelic', 'psychological', 'psychological_horror', 'puzzle', 'puzzle_platformer', 'pve', 'pvp', 'quick_time_events', 'rpg', 'rpgmaker', 'rts', 'racing', 'real_time_tactics', 'real_time', 'real_time_with_pause', 'realistic', 'relaxing', 'remake', 'replay_value', 'resource_management', 'retro', 'rhythm', 'robots', 'rogue_like', 'rogue_lite', 'romance', 'rome', 'runner', 'sailing', 'sandbox', 'satire', 'sci_fi', 'science', 'score_attack', 'sequel', 'sexual_content', 'shoot_em_up', 'shooter', 'short', 'side_scroller', 'silent_protagonist', 'simulation', 'singleplayer', 'skateboarding', 'skating', 'skiing', 'sniper', 'snow', 'snowboarding', 'soccer', 'software', 'software_training', 'sokoban', 'souls_like', 'soundtrack', 'space', 'space_sim', 'spectacle_fighter', 'spelling', 'split_screen', 'sports', 'star_wars', 'stealth', 'steam_machine', 'steampunk', 'story_rich', 'strategy', 'strategy_rpg', 'stylized', 'submarine', 'superhero', 'supernatural', 'surreal', 'survival', 'survival_horror', 'swordplay', 'tactical', 'tactical_rpg', 'tanks', 'team_based', 'tennis', 'text_based', 'third_person', 'third_person_shooter', 'thriller', 'time_attack', 'time_management', 'time_manipulation', 'time_travel', 'top_down', 'top_down_shooter', 'touch_friendly', 'tower_defense', 'trackir', 'trading', 'trading_card_game', 'trains', 'transhumanism', 'turn_based', 'turn_based_combat', 'turn_based_strategy', 'turn_based_tactics', 'tutorial', 'twin_stick_shooter', 'typing', 'underground', 'underwater', 'unforgiving', 'utilities', 'vr', 'vr_only', 'vampire', 'video_production', 'villain_protagonist', 'violent', 'visual_novel', 'voice_control', 'voxel', 'walking_simulator', 'war', 'wargame', 'warhammer_40k', 'web_publishing', 'werewolves', 'western', 'word_game', 'world_war_i', 'world_war_ii', 'wrestling', 'zombies', 'e_sports']

# dict used in "searchByRnage", format: "condiction":[[use, lowerbound, upperbound],[possible ranges]], use(bool): 0 if not use, lower/upper(int): close interval of range index
# not used
rangedict = {
    # for the owner column, range[i] means from range[i] to range[i+1], ex: range[0] = 0 means from 0 to 20000
    "owners":[[0, 0, 11],[0, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]],
    # for following column, use between function as a condiction
    "date":[[0, 0, 22],[1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]],
    "pratio":[[0, 0, 10],[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]],
    "prating":[[0, 0, 11],[0, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]],
    "price":[[0, 0, 9],[0, 1, 2, 5, 10, 20, 50, 100, 200, 500]],
    # for below condiction, 0: not use, 1: use
    "platform":[[1, 1, 1],["windows", "mac", "linux"]]
}

# sorted: first value means the priority (0 if not use), second value means ASC(0) / DESC(1)
# note: the priority should be 0, 1, 2
sortingdict = {"release_date": [0, 0], "positive_ratings":[0, 0], "pratio":[0, 0], "owners":[0, 0], "price":[0, 0], "name": [0, 0]}

"""
def funList():
    global mydb, mycursor
    taglist = list()
    sql_command = "SELECT count(*) FROM steam_basic_data WHERE price <5"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        taglist.append(col[0])
    return taglist
"""
# reset auto increment of table: should not called in app
def resetAI(tablename: str) -> None:
    global mydb, mycursor
    sql_command = "ALTER TABLE "+tablename+" AUTO_INCREMENT = 1"
    mycursor.execute(sql_command)
    mydb.commit()
    mycursor.reset()

def getUserName(uid: str) -> str:
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    mytup = (uid, )
    sql_command = "SELECT username FROM user_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    return results[0][0]

def appDetailInfo(appid: str) -> dict:
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    infodict=dict()
    mytup = (appid, )
    sql_command = "SELECT * FROM steam_basic_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    # infodict["id"] = results[0]
    infodict["name"] = results[1]
    infodict["date"] = results[2]
    infodict["developer"] = results[4]
    infodict["publisher"] = results[5]
    infodict["platforms"] = results[6].replace(";", ", ")
    infodict["age"] = results[7]
    infodict["categories"] = results[8].replace(";",", ")
    infodict["genres"] = results[9].replace(";",", ")
    infodict["tags"] = results[10].replace(";",", ")
    infodict["pratings"] = results[12]
    infodict["nratings"] = results[13]
    # pratio: float, pratiopct: str(percentage)
    if results[12] + results[13] == 0:
        infodict["pratio"] = 0
    else:
        infodict["pratio"] = results[12] / (results[12]+results[13])
    infodict["pratiopct"] = str(round(infodict["pratio"]*100,1))+"%"
    infodict["avetime"] = results[14]
    infodict["medtime"] = results[15]
    infodict["owners"] = results[16]
    infodict["price"] = results[17]
    sql_command = "SELECT * FROM steam_requirements_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    if "windows" in infodict["platforms"]:
        infodict["pcreq"] = results[1]
    if "mac" in infodict['platforms']:
        infodict["macreq"] = results[2]
    if 'linux' in infodict['platforms']:
        infodict["linuxreq"] = results[3]
    sql_command = "SELECT * FROM steam_desc_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    infodict["desc"] = textAdjust(results[1])
    sql_command = "SELECT * FROM steam_media_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    infodict["headimg"] = results[1]
    return infodict

def appShortInfo(appidlist: list) -> dict:
    global mycursor, mydb
    appdict = dict()
    infodict=dict()
    for appid in appidlist:
        infodict.clear()
        id = str(appid)
        mytup = (id, )
        sql_command = "SELECT * FROM steam_basic_data WHERE appid = %s"
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        results = results[0]
        mycursor.reset()
        # infodict["id"] = results[0]
        infodict["name"] = results[1]
        infodict["date"] = results[2]
        # infodict["age"] = results[7]
        infodict["pratings"] = results[12]
        # pratio: float, pratiopct: str(percentage)
        if results[12] + results[13] == 0:
            infodict["pratio"] = 0
        else:
            infodict["pratio"] = results[12] / (results[12]+results[13])
        infodict["pratiopct"] = str(round(infodict["pratio"]*100, 2))+"%"
        infodict["owners"] = results[16]
        infodict["price"] = results[17]
        appdict[appid] = infodict.copy()
    return appdict

def createFList(uid: str, listname: str) -> int:
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    mytup = (listname, uid)
    sql_command = "SELECT COUNT(*) FROM flist_conn_data WHERE listname = %s AND userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    if results[0][0] != 0:
        return 0
    sql_command = "INSERT INTO flist_conn_data (listname, userid) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = results[0][0]
    return id

# list[name, id]: list of flist
# ord: 0:ASC, 1:DESC
# not used
def showFList(uid: str, ord: bool) -> list:
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    flistlist = list()
    mytup = (uid, )
    sql_command = "SELECT listname, listid FROM flist_conn_data WHERE userid = %s ORDER BY listname "
    if ord == 0:
        sql_command += "ASC"
    else:
        sql_command += "DESC"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    for col in results:
        flistlist.append([col[0], col[1]])
    return flistlist

# 0: newname exist, 1: success
# not used
def renameFList(uid: str, listid: str, newname:str) -> bool:
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    sql_command = "SELECT count(*) FROM flist_conn_data WHERE listname = %s AND userid = %s"
    mytup = (newname, uid)
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    if results[0][0] > 0:
        return 0
    sql_command = "UPDATE flist_conn_data SET listname = %s WHERE listid = %s"
    mytup = (newname, listid)
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# not used
def mergeFList(uid: str, mainlistid: str, mergedlistid: str) -> None:
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    if type(mainlistid) != str:
        mainlistid = str(mainlistid)
    if type(mergedlistid) != str:
        mergedlistid = str(mergedlistid)
    mytup = (mainlistid, mainlistid, mergedlistid)
    sql_command = "UPDATE flist_data AS t1\
        LEFT JOIN (SELECT * FROM flist_data WHERE listid = %s) AS t2 ON t1.appid = t2.appid \
        SET t1.listid = %s WHERE t1.listid = %s AND t2.listid IS NULL"
    mycursor.execute(sql_command, mytup)
    mycursor.reset()
    mydb.commit()
    deleteFList(mergedlistid)

# not used
def deleteFList(listid: str) -> None:
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, )
    sql_command = "DELETE FROM flist_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "DELETE FROM flist_conn_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

def deleteUserFLists(uid: str) -> None:
    global mydb, mycursor
    mytup = (uid, )
    sql_command = "SELECT listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        try:
            lid = col[0]
            mytup = (lid, )
            sql_command = "DELETE FROM flist_data WHERE listid = %s"
            mycursor.execute(sql_command, mytup)
            mydb.commit()
            mycursor.reset()
        except:
            break
    mytup = (uid, )
    sql_command = "DELETE FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

# 0: already in this flist, 1: success
def insertAppIntoFList(uid: str, appid: str) -> bool:
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(uid) != str:
        uid = str(uid)
    mytup = (uid, )
    sql_command = "SELECT listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    listid = str(results[0][0])
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = results[0][0]
    if cnt != 0:
        return 0
    sql_command = "INSERT INTO flist_data VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# list[id]: list of app
def showAppFromFList(uid: str) -> list:
    global mydb, mycursor, sortingdict
    if type(uid) != str:
        uid = str(uid)
    flistlist = list()
    srt = "ORDER BY "
    cnt = 0
    for key in sortingdict.keys():
        if key == "name":
            continue
        if sortingdict[key][0] == 1:
            cnt = 1
            nxt = True
            if key == "pratio":
                srt += "CASE sb.positive_ratings + sb.negative_ratings\
                    WHEN 0 THEN 0 ELSE sb.positive_ratings/(sb.positive_ratings + sb.negative_ratings) END "
            elif key == "owners":
                srt += 'CAST(SUBSTRING_INDEX(owners, "-", 1) AS UNSIGNED) '
            else:
                srt += ("sb."+key+" ")
            if sortingdict[key][1] == 0:
                srt += "ASC "
            else:
                srt += "DESC "
            break
    if cnt == 1:
        srt += ", "
    srt += "sb.name "
    if sortingdict["name"][1] == 1:
        srt += "DESC "
    else:
        srt += "ASC "
    mytup = (uid, )
    sql_command = "SELECT f.appid FROM flist_data AS f\
        INNER JOIN steam_basic_data AS sb ON sb.appid = f.appid\
        INNER JOIN flist_conn_data AS fc ON fc.listid = f.listid\
        WHERE fc.userid = %s "
    sql_command += srt
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        flistlist.append(col[0])
    return flistlist

# 0: not in flist, 1: success
def deleteAppFromFList(uid: str, appid: str) -> bool:
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(uid) != str:
        uid = str(uid)
    mytup = (uid, )
    sql_command = "SELECT listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    listid = str(results[0][0])
    mycursor.reset()
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = results[0][0]
    if cnt == 0:
        return 0
    sql_command = "DELETE FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# 0: account has been used, id: new account id
def createUserAccount(userName: str, userPass: str) -> int:
    global mydb, mycursor
    if ' ' in userName or ' ' in userPass:
        return 0
    sql_command = "SELECT COUNT(username) FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = results[0][0]
    if cnt != 0:
        return 0
    mytup = (userName, userPass)
    sql_command = "INSERT INTO user_data (username, userpassword) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = results[0][0]
    createFList(id, "MyWishList")
    return id

# 0: fail, 1: success
def deleteUserAccount(uid: str, userPass: str) -> int:
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    sql_command = "SELECT * FROM user_data WHERE userid = %s"
    mytup = (uid, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    password = results[0][2]
    if userPass != password:
        return 0
    deleteUserFLists(uid)
    mytup = (uid, )
    sql_command = "DELETE FROM user_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# 0: fail, id: login
def login(userName: str, userPass: str) -> int:
    global mydb, mycursor
    sql_command = "SELECT * FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        id = results[0][0]
        password = results[0][2]
    except:
        return -1
    if userPass != password:
        return 0
    return id

# 0: account has been exist, 1: success
def renameUserAccount(uid: str, newname: str) -> int:
    global mycursor, mydb
    if type(uid) != str:
        uid = str(uid)
    if ' ' in newname:
        return 0
    mytup = (newname, uid)
    sql_command = "SELECT count(*) FROM user_data WHERE username = %s and userid <> %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    if results[0][0] > 0:
        return 0
    mytup = (newname, uid)
    sql_command = "UPDATE user_data SET username = %s WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# 0: password fail, 1: success
def resetUserPassword(uid: str, newPass: str) -> int:
    global mycursor, mydb
    if type(uid) != str:
        uid = str(uid)
    if ' ' in newPass:
        return 0
    mytup = (newPass, uid)
    sql_command = "UPDATE user_data SET userpassword = %s WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# ord: ASC(0) / DESC(1)
# key: "release_date", "positive_ratings", "pratio", "owners", "price", "name"
def modifySorting(key: str, ord: bool) -> None:
    global sortingdict
    for k in sortingdict.keys():
        sortingdict[k] = [0, 0]
    sortingdict[key] = [1, 0]
    if ord == 1:
        sortingdict[key] = [1, 1]

# list[id] sorted by match tags
def searchByTag(taglist: list) -> list:
    global mydb, mycursor, sortingdict
    if type(taglist) != list:
        return []
    sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE genres LIKE %s OR categories like %s OR steamspy_tags like %s "
    appdict = dict()
    for tag in taglist:
        mytup = ("%"+tag+"%", "%"+tag+"%", "%"+tag+"%")
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            if id not in appdict:
                appdict[id] = 1
            else:
                appdict[id] += 1
    applist = sorted(appdict.items(), key = lambda x:(x[1],x[0]), reverse=True)
    finallist = []
    srt = "ORDER BY "
    cnt = 0
    for key in sortingdict.keys():
        if key == "name":
            continue
        if sortingdict[key][0] == 1:
            cnt = 1
            nxt = True
            if key == "pratio":
                srt += "CASE positive_ratings + negative_ratings\
                    WHEN 0 THEN 0 ELSE positive_ratings/(positive_ratings + negative_ratings) END "
            elif key == "owners":
                srt += 'CAST(SUBSTRING_INDEX(owners, "-", 1) AS UNSIGNED) '
            else:
                srt += (key+" ")
            if sortingdict[key][1] == 0:
                srt += "ASC "
            else:
                srt += "DESC "
            break
    if cnt == 1:
        srt += ", "
    srt += "name "
    if sortingdict["name"][1] == 1:
        srt += "DESC "
    else:
        srt += "ASC "
    i = 0
    while i < len(applist):
        scorelist = []
        nowscore = applist[i][1]
        scorelist.append(applist[i][0])
        i += 1
        while i < len(applist) and applist[i][1] == nowscore:
            scorelist.append(applist[i][0])
            i += 1
        if len(scorelist) == 1:
            s = "("+str(scorelist[0])+")"
        else:
            s = str(tuple(scorelist))
        sql_command = "SELECT appid FROM steam_basic_data WHERE appid IN "+s+" "+ srt
        mycursor.execute(sql_command)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            finallist.append(col[0])
        i += 1
    return finallist

# []: no condiction, list[id] sorted by match tags
# not used
def searchByRange() -> list:
    global mydb, mycursor, rangedict, sortingdict
    sql_command = "SELECT appid FROM steam_basic_data WHERE "
    condiction = '('
    keys = rangedict["platform"][0]
    cnt = 0
    use = 0
    for i in range(0,3):
        if keys[i] == 1:
            if cnt > 0:
                condiction += 'OR '
            condiction += 'platforms like "%'+rangedict["platform"][1][i]+'%" '
            cnt += 1
    if cnt > 0:
        use += 1
        condiction += ')'
    else:
        condiction = ''
    cnt = 0
    if rangedict["owners"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('substring_index(owners, "-", 1) between '+str(rangedict["owners"][1][rangedict["owners"][0][1]])\
                       +' AND '+str(rangedict["owners"][1][rangedict["owners"][0][2]])+' ')
    if rangedict["date"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('left(release_date, 4) between '+str(rangedict["date"][1][rangedict["date"][0][1]])\
                       +' AND '+str(rangedict["date"][1][rangedict["date"][0][2]])+' ')
    if rangedict["pratio"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('if(positive_ratings+negative_ratings=0, 0, positive_ratings/(positive_ratings+negative_ratings)) between '\
                       +str(rangedict["pratio"][1][rangedict["pratio"][0][1]])\
                       +' AND '+str(rangedict["pratio"][1][rangedict["pratio"][0][2]])+' ')
    if rangedict["prating"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('positive_ratings between '+str(rangedict["prating"][1][rangedict["prating"][0][1]])\
                       +' AND '+str(rangedict["prating"][1][rangedict["prating"][0][2]])+' ')
    if rangedict["price"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('price between '+str(rangedict["price"][1][rangedict["price"][0][1]])\
                       +' AND '+str(rangedict["price"][1][rangedict["price"][0][2]])+' ')
    if use == 0:
        return []
    srt = "ORDER BY "
    cnt2 = 0
    for key in sortingdict.keys():
        if key == "name":
            continue
        if sortingdict[key][0] == 1:
            cnt2 = 1
            nxt = True
            if key == "pratio":
                srt += "CASE positive_ratings + negative_ratings\
                    WHEN 0 THEN 0 ELSE positive_ratings/(positive_ratings + negative_ratings) END "
            elif key == "owners":
                srt += 'SUBSTRING_INDEX(owners, "-", 1) '
            else:
                srt += (key+" ")
            if sortingdict[key][1] == 0:
                srt += "ASC "
            else:
                srt += "DESC "
            break
    if cnt2 == 1:
        srt += ", "
    srt += "name "
    if sortingdict["name"][1] == 1:
        srt += "DESC "
    else:
        srt += "ASC "
    sql_command += condiction
    sql_command += srt
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    applist = []
    for col in results:
        applist.append(col[0])
    return applist

# 0: input type not list, list[id] sorted by match words and accuracy
def searchByName(wordlist: list) -> list:
    global mydb, mycursor, sortingdict
    if type(wordlist) != list:
        return 0
    appdict = dict()
    for word in wordlist:
        sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE sb.name LIKE %s"
        mytup = ("%"+word+"%",)
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            if id not in appdict:
                appdict[id] = 1
            else:
                appdict[id] += 1
        sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE sb.name LIKE %s OR sb.name LIKE %s OR sb.name LIKE %s OR sb.name LIKE %s "
        mytup = ("% "+word+" %", word+" %", "% "+word, word)
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            appdict[id] += 100
    applist = sorted(appdict.items(), key = lambda x:(x[1],x[0]), reverse=True)
    finallist = []
    srt = "ORDER BY "
    cnt = 0
    for key in sortingdict.keys():
        if key == "name":
            continue
        if sortingdict[key][0] == 1:
            cnt = 1
            if key == "pratio":
                srt += "CASE positive_ratings + negative_ratings\
                    WHEN 0 THEN 0 ELSE positive_ratings/(positive_ratings + negative_ratings) END "
            elif key == "owners":
                srt += 'CAST(SUBSTRING_INDEX(owners, "-", 1) AS UNSIGNED) '
            else:
                srt += (key+" ")
            if sortingdict[key][1] == 0:
                srt += "ASC "
            else:
                srt += "DESC "
            break
    if cnt == 1:
        srt += ", "
    srt += "name "
    if sortingdict["name"][1] == 1:
        srt += "DESC "
    else:
        srt += "ASC "
    i = 0
    while i < len(applist):
        scorelist = []
        nowscore = applist[i][1]
        scorelist.append(applist[i][0])
        i += 1
        while i < len(applist) and applist[i][1] == nowscore:
            scorelist.append(applist[i][0])
            i += 1
        if len(scorelist) == 1:
            s = "("+str(scorelist[0])+")"
        else:
            s = str(tuple(scorelist))
        sql_command = "SELECT appid FROM steam_basic_data WHERE appid IN "+s+" "+ srt
        mycursor.execute(sql_command)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            finallist.append(col[0])
        i += 1
    return finallist

def takePage(p: int, mylist: list) -> list:
    limitpage = int((len(mylist)+9) / 10)
    if p > limitpage:
        p = limitpage
    elif p < 1:
        p = 1
    return mylist[10*(p-1):10*p-1]

def textAdjust(s: str) -> str:
    newstring = ''
    c = 0
    while c < len(s):
        lft = s.find('<', c)
        if lft == -1:
            newstring += s[c:len(s)]
            break
        cnt = 1
        if lft > c:
            newstring += s[c:lft]
        while cnt > 0:
            nl = s.find('<', lft+1)
            nr = s.find('>', lft+1)
            if nl > nr or nl == -1:
                cnt -= 1
                lft = nr
            else:
                cnt += 1
                lft = nl
        newstring += " "
        c = lft+1
    newstring = newstring.replace("\t", " ")
    newstring = newstring.replace("\n", " ")
    newstring = ' '.join(newstring.split())
    return newstring

"""
#testing code

uid = createUserAccount("A","0800000123")
renameUserAccount(uid, "B")
resetUserPassword(uid, "1911111234")
insertAppIntoFList(uid, 1610)
insertAppIntoFList(uid, 1670)
flist = takePage(1, showAppFromFList(uid))
print(flist)
deleteUserAccount(uid,"1911111234")
resetAI("user_data")
resetAI("flist_conn_data")

#testing code 2

searchResult = searchByName(["neko"])
for info in appShortInfo(takePage(1, searchResult)).values():
    print(info)
"""