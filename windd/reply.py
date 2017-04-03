def get_nickname(memberName):
    nickname_dict = {
        'Joker Water' : '水军',
        'Kry☣Music' : '哭响',
        '只有昵称可以很长windd' : 'Master',
        '水里的阿畅~' : '流畅叔叔',
        'Outsider' : '容容',
        'Tessa' : '容容',
        '十七海里' : '十七',
        '芦苇' : '手哥',
        'Miao' : '屁屁'
    }
    return nickname_dict.get(memberName, memberName)

def get_reply(number,keyword=''):
    reply_dict = {
        0 : '那你真的很棒棒哦',
        1 : '反正你又听不懂人话',
        2 : '说人话',
        3 : '哦，是吗',
        4 : '说的很有道理',
        5 : '厉害，厉害',
        6 : '少来'
    }
    reply_dict_keyword = {
        0 : '神tmXX',
        1 : 'XX好像很厉害的样子',
        2 : '我也有XX',
        3 : 'XX吗',
        4 : 'XX大法好',
        5 : '我也XX',
        6 : '你才XX，你全家都XX'
    }
    rand = random.randint(0,3)
    if keyword != '' and rand % 4 != 3:
        # rand = random.randint(0,6)
        reply = reply_dict_keyword.get(number)
        reply = reply.replace("XX", keyword)
    else:
        reply = reply_dict.get(number, '那你很屌咯')

    return reply