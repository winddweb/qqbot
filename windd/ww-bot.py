# -*- coding: utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot
import random
import jieba
import windd.reply as rp

my_name = "小熊"

def will_reply():
    seed = random.randint(0,6)
    print(seed)
    return seed % 2 == 1

def get_keyword(msg):
    lmsg = jieba.lcut(msg)
    lmsg = [x.encode('utf8') for x in lmsg]
    le = max(len(x) for x in lmsg)
    longest = [x for x in lmsg if len(x) == le]
    random.sample(set(longest), 1)
    keyword = max(lmsg, key=len)
    return keyword

@qqbotslot
def onQQMessage(bot, contact, member, content):
    m_contact = contact
    msg = content
    nickname = rp.get_nickname(member.name)
    keyword = get_keyword(msg)
    print(m_contact.ctype, m_contact.name, m_contact.qq, member.name, nickname)

    if '@ME' in content:
        bot.SendTo(contact, '%s， 想我了吧？' % member.name)
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
