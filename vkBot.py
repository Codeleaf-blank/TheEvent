import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

def get_random_id():
    return int(random.getrandbits(31)) * int(random.choice([-1, 1]))

vk=vk_api.VkApi(token='90aa67fb7b2b00be222fdef31be70a96a3e284b42f997f398273e4ba7329d772d4ed5ff73e8c0b6013233')
#Rtest = vk.method('messages.getConversations')
#print(Rtest)
mtest = vk.method('messages.send',{'user_id':240188108,'message': 'я слышу тебя','random_id':get_random_id()})