from openai import OpenAI
import json
from src.utils import openai_key, scene_info_example
from src.Role import Role

class Scene:
    def __init__(self, id, client, init_info=None) -> None:
        self.id = id
        self.init_info = init_info
        self.info = None
        self.client = client
        self.story = []
        self.timestep = None
        self.related_roles = []
        self.title = None

        """
        type: [
        {
            "sender": string,
            "sender_id": int,
            "info": {
                "BEHAVIOR": list[string],
                "SPEECH": list[string],
                "EXPRESSION": list[string],
                "PSYCHOLOGICAL_ACTIVITY": list[string]
            }
        }
        ]
        """
        self.interactions = []

    def init_scene(self) -> None:
        if self.init_info is not None:
            # 有一些初始化信息
            instructions_1 = "请你构建一个场景的信息。场景信息使用json格式描述，包含地点、时间、氛围、听觉、视觉和嗅觉这6项内容。参考示例json"
            instructions_2 = "请模仿示例的格式，在不违反已有设定的情况下补全下面这个json的内容或者根据下面文本要求生成符合格式的场景设定json数据，注意不要修改原本已有的内容，示例中所有的键都要出现，不要新添加其他键。"
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": f'{instructions_1}\n示例：{scene_info_example}\n{instructions_2}\n{self.init_info}'},
                ],
                response_format={"type": "json_object"}
            )
        else:
            # 没有初始化信息，系统随机初始化
            instructions_1 = "请你构建一个场景的信息。场景信息使用json格式描述，包含地点、时间、氛围、听觉、视觉和嗅觉这6项内容。参考示例json"
            instructions_2 = "请模仿示例的格式，自由生成场景设定信息，注意示例中所有的键都要出现，不要新添加其他键。"
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": f'{instructions_1}\n示例：{scene_info_example}\n{instructions_2}\n'},
                ],
                response_format={"type": "json_object"}
            )
        
        self.info = json.loads(response.choices[0].message.content)
        print(self.info)

    def generate_story(self, roles: list[Role]) -> None:
        context = []
        role_info = [role.info for role in roles]

        context.append({"role": "system", "content": f'你需要扮演一位故事作者，在如下##中描述的场景中发生故事，场景描述：\n#{self.info}#\n'})
        context.append({"role": "system", "content": f'在这个故事中有如下角色，他们的性格在下面的##中描述：\n#{role_info}#'})
        context.append({"role": "system", "content": f'在这个故事中的角色进行了下面这些行为：#{self.interactions}#'})
        context.append({"role": "user", "content": f'请你按照上述场景描述和发生的人物行为内容，完成这部分的故事文本撰写'})
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=context,
            response_format={"type": "text"}
        )
        gene_story = response.choices[0].message.content
        self.story.append(gene_story)
        print(self.story)

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "place": self.info["place"],
            "time": self.info["time"],
            "atmosphere": self.info["atmosphere"],
            "feeling": self.info["feeling"],
            "otherInformation": self.info["otherInformation"]
        }

    def show_info(self) -> None:
        print(self.info)