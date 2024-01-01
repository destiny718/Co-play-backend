from typing import Any
from openai import OpenAI
import json
import threading
from src.utils import openai_key, role_info_example, scene_info_example
from src.Scene import Scene
from src.Role import Role

class WritingCopilot:
    def __init__(self, id, title, big_background, roles: list[Role], scenes: list[Scene], client) -> None:
        self.id = id
        self.title = title
        self.big_background = big_background
        self.roles = roles
        self.scenes = scenes
        self.total_timestep = 0

        self.story = []
        self.client = client

    def add_role(self, role: Role) -> None:
        self.roles.append(role)

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)

    def create_timestep(self) -> int:
        self.total_timestep += 1
        return self.total_timestep - 1
    
    def serialize(self) -> dict:
        timesteps = []
        for scene in self.scenes:
            if scene.timestep is not None:
                item = {
                    "id": scene.timestep,
                    "title": scene.title,
                    "relate_scene": scene.id,
                    "relate_roles": scene.related_roles,
                    "interactions": scene.interactions
                }
                timesteps.append(item)
        return {
            "title": self.title,
            "roles": [role.serialize() for role in self.roles],
            "scenes": [scene.serialize() for scene in self.scenes],
            "timesteps": timesteps
        }

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
            ],
            response_format={"type": "text"}
        )
        return json.loads(response.choices[0].message.content)
    
    

class WritingProcess:
    def __init__(self) -> None:
        self.copilots: list[WritingCopilot] = []
        self.client = OpenAI(api_key=openai_key)

    def add_copilot(self, copilot: WritingCopilot) -> None:
        self.copilots.append(copilot)

    def init_story(self, info) -> int:
        init0 = "你是一名出色的小说分析师，对各种小说的结构都很有了解，你非常善于分析小说中的故事和人物"
        init1 = f'请分析下面这段小说的内容，并给出小说的标题、大背景、主要角色和主要的发生场景。请以json格式返回内容，具体需要有如下的键：title，big_background，roles，scene，其中roles需要返回一个列表，列表中的每一项都与下面这个示例类似，注意示例中所有的键都要出现，不要新添加其他键。\n{role_info_example}\nscene与下面这个示例类似，注意示例中所有的键都要出现，不要新添加其他键。\n{scene_info_example}\n'
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": f'{init0}\n'},
                {"role": "user", "content": f'{init1}{info}\n'}
            ],
            response_format={"type": "json_object"}
        )
        story_info = json.loads(response.choices[0].message.content)
        print(story_info)

        new_client = OpenAI(api_key=openai_key) 
        copilot = WritingCopilot(id=len(self.copilots), title=story_info["title"], big_background=story_info["big_background"], roles=[], scenes=[], client=new_client)
        for role in story_info["roles"]:
            role_agent = Role(len(copilot.roles), OpenAI(api_key=openai_key), role)
            role_agent.info = role_agent.init_info
            copilot.add_role(role_agent)
        scene_agent = Scene(len(copilot.scenes), OpenAI(api_key=openai_key), story_info["scene"])
        scene_agent.info = scene_agent.init_info
        copilot.add_scene(scene_agent)
        self.copilots.append(copilot)
        return copilot.id
    
    def __len__(self) -> int:
        return len(self.copilots)
    
    def iter(self) -> list:
        return [{"id": story.id, "title": story.title} for story in self.copilots]
    

if __name__ == "__main__":
    # for test
    text = "在遥远的山区，隐藏着一个古老的村庄，那里住着三个性格截然不同的朋友：小华、小明和小丽。小华是个无忧无虑、总是充满活力的女孩，她对世界充满好奇，喜欢冒险和探索。小明则是个谨慎而内敛的男孩，他总是深思熟虑，是三人中的理性之声。小丽，一个机智而又幽默的女孩，总能用她的聪明才智化解紧张的气氛。一天，他们决定去探索村庄边缘的一座神秘废弃屋。小华兴奋不已，她一直梦想着能在那座老屋里发现未知的秘密。小明则显得有些担心，他担心这座老屋可能隐藏着未知的危险。小丽则带着她的笔记本和相机，准备记录下这次冒险的点点滴滴。当他们走进那座废弃屋时，阳光透过破碎的窗户洒在布满灰尘的地板上。这里的一切都显得古旧而神秘。小华立即开始在房间里四处寻找，好像一位寻宝者。小明则小心翼翼地检查着每个角落，以确保安全。小丽则在用她的相机捕捉这些珍贵的瞬间。他们在屋内发现了一个密室，里面堆满了各种古老的物品和书籍。小华在一堆破旧书本中发现了一本非常古老的日记，那是一位多年前的探险家的日记。小明则注意到墙上悬挂着的一幅地图，它看起来非常的古老和神秘。小丽则被一副古画吸引，画中描绘着一个未知的地点，似乎与地图上标记的位置有关。小华提议根据这些线索去寻找可能隐藏的宝藏。小明则建议他们应该更加谨慎，需要更多的准备和调查。而小丽则在想，这一切是否只是一个巧合，还是真的有什么大秘密等着他们。这时，他们听到了楼上的异响，似乎有什么东西在移动。小华勇敢地提议上楼去看看是什么，小明则坚持要他们一起行动，并提醒大家要小心。小丽则快速地记录下这些发现，并准备随时拍摄即将发生的事情。这个故事到这里暂停，留给你去续写这个充满未知和冒险的故事。"
    w = WritingProcess()
    w.init_story(text)