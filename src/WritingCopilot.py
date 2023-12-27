from openai import OpenAI
import json
import threading
from utils import openai_key
from Scene import Scene
from Role import Role

class WritingCopilot:
    def __init__(self, roles: list[Role], scenes: list[Scene]) -> None:
        self.roles = roles
        self.scenes = scenes
        self.story = []

    def add_role(self, role: Role) -> None:
        self.roles.append(role)

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)

    def interact(self, role: Role, scene: Scene):
        pass


client1 = OpenAI(api_key=openai_key)
client2 = OpenAI(api_key=openai_key)
client3 = OpenAI(api_key=openai_key)
        
info1 = {
    "基本信息": {
        "名字": "李凯尔",
        "年龄": 30,
        "性别": "男",
        "职业": "篮球运动员，司职前锋",
    },
    "性格特征": {
        "主要性格": ["随遇而安"],
    },
    "外貌描述": {
        "身高": "2.03米",
        "体重": "100公斤",
        "眼睛颜色": "黑色",
    },
    "背景故事": {

    },
    "当前状态": {
    }
}

info2 = {
    "基本信息": {
        "名字": "鲁迪·戈贝尔",
        "年龄": 27,
        "性别": "男",
        "职业": "篮球运动员，司职中锋",
    },
    "性格特征": {
        "主要性格": ["易怒", "固执"],
    },
    "外貌描述": {
        "身高": "2.17米",
        "体重": "120公斤",
        "眼睛颜色": "黑色",
    },
    "背景故事": {

    },
    "当前状态": {
    }
}

info3 = {
    "地点": "明尼苏达森林狼的主场Target Center",
    "时间": "一个阴雨天的下午",
    "氛围": "篮球场内十分喧闹",
    "听觉": [],
    "视觉": [],
    "嗅觉": []          
}

role1 = Role(client1, info1)
role2 = Role(client2, info2)
scene = Scene(client3, info3)

thread1 = threading.Thread(target=role1.init_role)
thread2 = threading.Thread(target=role2.init_role)
thread3 = threading.Thread(target=scene.init_scene)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# role1.create_actions(scene, ["鲁迪·戈贝尔因为上一个回合你们在防守中沟通不当而十分愤怒，对你挥拳相向"])
# role2.create_actions(scene, [{"李凯尔": f'{role1.actions}'}])
role1.actions.append([{'BEHAVIOR': ['在鲁迪·戈贝尔挥拳的瞬间，迅速后退一步，做好防守姿态，防止被出其不意地袭击'], 'SPEECH': ["高声对鲁迪·戈贝尔说：'你这是在场上求败吗？来吧，看我如何在比赛中教训你！'"], 'EXPRESSION': ['脸上流露出不屑和挑衅的神情，眼神紧盯着鲁迪·戈贝尔'], 'PSYCHOLOGICAL_ACTIVITY': ['感到愤怒和不满，同时也认为需要在场上展示出自己的领袖气质和竞争力']}])
role2.actions.append([{'BEHAVIOR': ['显得异常激动，急速冲向李凯尔，准备开始一次强有力的身体对抗'], 'SPEECH': ["咆哮道：'你这种挑衅对我没用，看我在场上如何用实力压制你！'"], 'EXPRESSION': ['面容扭曲，眼中闪烁着怒火和挑战的光芒'], 'PSYCHOLOGICAL_ACTIVITY': ['内心燃烧着战斗的渴望，对手的态度更是激起了他想要证明自己的决心']}])
scene.generate_story([role1, role2])