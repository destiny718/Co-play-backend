from typing import Any
from openai import OpenAI
import json
import threading
from utils import openai_key
from Scene import Scene
from Role import Role

class WritingCopilot:
    def __init__(self, id, title, big_background, roles: list[Role], scenes: list[Scene], client) -> None:
        self.id = id
        self.title = title
        self.big_background = big_background
        self.roles = roles
        self.scenes = scenes
        self.story = []
        self.current_env = []
        self.client = client

    def add_role(self, role: Role) -> None:
        self.roles.append(role)

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)
    
    def generate_part(self, roles: list[Role], scene: Scene, step_range:tuple[int, int]):
        self.story.append[scene.generate_story(roles, step_range)]

    def generate_stories(self, generate_prompt):
        # prompt reference: https://askexperts.ai/
        init = "你是一名出色的小说家。你将创作出引人入胜的创意故事，能够吸引读者长时间阅读。你可以选择任何类型的小说，如奇幻、浪漫、历史虚构等，但目标是写出具有出色情节、吸引人物和意外高潮的作品。"
        if generate_prompt:
            instruction = f'需要你根据##中的提示信息中的写作要求，提示信息:#{generate_prompt}#,将下述数组提供的一个故事的几部分内容整合为一个完整的故事，数组下标顺序即故事的发展顺序:'
        else:
            instruction = "需要你将下述数组提供的一个故事的几部分内容整合为一个完整的故事，数组下标顺序即故事的发展顺序:"
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": f'{init}\n'},
                {"role": "user", "content": f'{instruction}{self.story}\n'}
            ]
        )
        return json.loads(response.choices[0].message.content)
    
    def clear_env(self):
        self.current_env = []
        
    def interact(self, role: Role, scene: Scene, init_interact = None):
        self.current_env.append((role.info, role.create_actions(scene, self.current_env, init_interact)))       

class WritingProcess:
    def __init__(self) -> None:
        self.copilots: list[WritingCopilot] = []

    def add_copilot(self, copilot: WritingCopilot) -> None:
        self.copilots.append(copilot)

    def __len__(self) -> int:
        return len(self.copilots)
    
    def iter(self) -> list:
        return [{"id": story.id, "title": story.title} for story in self.copilots]
    
        
client1 = OpenAI(api_key=openai_key)
client2 = OpenAI(api_key=openai_key)
client3 = OpenAI(api_key=openai_key)
client4 = OpenAI(api_key=openai_key)   
client5 = OpenAI(api_key=openai_key) 
info1 = {
    "基本信息": {
        "名字": "李凯尔",
        "年龄": 30,
        "性别": "男",
        "职业": "篮球运动员，司职前锋",
    },
    "性格特征": ["随遇而安"],
    "外貌描述": [],
    "背景故事": [],
    "当前状态": []
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
    "氛围": "篮球场内气氛紧张",
    "听觉": ["球场内非常喧闹"],
    "视觉": [],
    "嗅觉": []          
}
role1 = Role(client1, info1)
role2 = Role(client2, info2)
scene = Scene(client3, info3)
roles = [role1,role2]
scenes = [scene]
writer = WritingCopilot(roles, scenes, client4)
timestep: int = 0
story_flag1 = 0
story_flag2 = 0
count = 0
while True:
    command = input("请输入交互命令: ")
    if command.lower() == 'exit': 
        print("退出")
        break
    elif command == "show":
        show_type = input("查看类型：")
        if show_type == "role":
            for r in writer.roles:
                print(r.info) 
        elif show_type == "scene":
            for s in writer.scenes:
                print(s.info)
    elif command == "init":
        init_type = input("请输入需要初始化的内容类型: ")
        if init_type == "role":
            init_info = input("初始化人物提示：") # json or str
            role_clients.append(OpenAI(api_key=openai_key))
            roles.append(Role(role_clients[-1], init_info))
            roles[-1].init_role()
        elif init_type == "scene":
            init_info = input("初始化场景提示：")
            scene_clients.append(OpenAI(api_key=openai_key))
            scenes.append(Scene(scene_clients[-1], init_info))
            scenes[-1].init_scene()
    elif command == "gen":
        prompt = input("请输入编写故事的要求提示信息:(如文学体裁或者风格) ")
        res = writer.generate_stories(prompt)
        print(res)
    elif command == "round":
        scene = input("请输入需要调用的场景: ")
        inscene_roles = []
        cur_scene = None
        while count < len(writer.roles):
            role = input("请输入需要调用的角色: ")
            for s in writer.scenes:
                if s.info["地点"] == scene:
                    cur_scene = s
                    for r in writer.roles:
                        if r.info["基本信息"]["名字"] == role:
                            inscene_roles.append(r)
                            prompt = input("请输入人物行为提示信息: ")
                            writer.interact(r, s, prompt)
                            count+=1
        count = 0
        if input("是否需要生成当前时间步故事文本") == "y":
            writer.generate_part(inscene_roles, cur_scene, (timestep,timestep+1))
        
# thread1 = threading.Thread(target=role1.init_role)
# thread2 = threading.Thread(target=role2.init_role)
# thread3 = threading.Thread(target=scene.init_scene)
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()

# # role1.create_actions(scene, ["鲁迪·戈贝尔因为上一个回合你们在防守中沟通不当而十分愤怒，对你挥拳相向"])
# # role2.create_actions(scene, [{"李凯尔": f'{role1.actions}'}])
# role1.actions.append([{'BEHAVIOR': ['在鲁迪·戈贝尔挥拳的瞬间，迅速后退一步，做好防守姿态，防止被出其不意地袭击'], 'SPEECH': ["高声对鲁迪·戈贝尔说：'你这是在场上求败吗？来吧，看我如何在比赛中教训你！'"], 'EXPRESSION': ['脸上流露出不屑和挑衅的神情，眼神紧盯着鲁迪·戈贝尔'], 'PSYCHOLOGICAL_ACTIVITY': ['感到愤怒和不满，同时也认为需要在场上展示出自己的领袖气质和竞争力']}])
# role2.actions.append([{'BEHAVIOR': ['显得异常激动，急速冲向李凯尔，准备开始一次强有力的身体对抗'], 'SPEECH': ["咆哮道：'你这种挑衅对我没用，看我在场上如何用实力压制你！'"], 'EXPRESSION': ['面容扭曲，眼中闪烁着怒火和挑战的光芒'], 'PSYCHOLOGICAL_ACTIVITY': ['内心燃烧着战斗的渴望，对手的态度更是激起了他想要证明自己的决心']}])
# scene.generate_story([role1, role2])