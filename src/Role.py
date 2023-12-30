from openai import OpenAI
import json
from utils import openai_key, role_info_example, action_info_example

class Role:
    def __init__(self, id, client, init_info=None) -> None:
        self.id = id
        self.init_info = init_info
        self.info = None
        self.client = client
        self.actions = []

    def init_role(self) -> None:
        if self.init_info is not None:
            # 有一些初始化信息
            instructions_1 = "你需要扮演一位故事角色，角色设定信息使用json格式描述，包含name、age、characteristics、preference、otherInformation这5项内容。参考示例json"
            instructions_2 = "请模仿示例的格式，在不违反已有设定的情况下补全下面这个json的内容，注意不要修改原本已有的内容，示例中所有的键都要出现，不要新添加其他键。"
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": f'{instructions_1}\n示例：{role_info_example}\n{instructions_2}\n{self.init_info}'},
                ],
                response_format={"type": "json_object"}
            )
        else:
            # 没有初始化信息，系统随机初始化
            instructions_1 = "你需要扮演一位故事角色，角色设定信息使用json格式描述，包含name、age、characteristics、preference、otherInformation这5项内容。参考示例json"
            instructions_2 = "请模仿示例的格式，自由生成人物的角色设定信息，注意示例中所有的键都要出现，不要新添加其他键。"
            response = self.client.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {"role": "system", "content": f'{instructions_1}\n示例：{role_info_example}\n{instructions_2}\n'},
                ],
                response_format={"type": "json_object"}
            )
        
        self.info = json.loads(response.choices[0].message.content)
        print(self.info)

    def create_actions(self, scene, envir: list, create_prompt = None):
        context = []
        context.append({"role": "system", "content": f'你需要扮演一位故事角色，角色设定信息由下面的json文件给出\n{self.info}\n你之前的行为由下面的list给出，这个list中每项表示一个时间步下你的行为\n{self.actions}'})
        context.append({"role": "system", "content": f'这是你当前所处的环境：{scene.info}'})
        # FIXME: 删掉“注意PSYCHOLOGICAL_ACTIVITY你是观察不到的” 直接在list中把PSYCHOLOGICAL_ACTIVITY的键去掉
        context.append({"role": "system", "content": f'这是当前场景中其他角色及其行为表现，注意PSYCHOLOGICAL_ACTIVITY你是观察不到的：{envir}'})
        if create_prompt:
            context.append({"role": "user", "content": f'你需要在不明显违反人物设定的前提下，根据下述##中的提示信息做出更倾向于提示的行为：#{create_prompt}#'})
        context.append({"role": "user", "content": f'请根据以上信息，模拟你所扮演的角色的行为。行为具体有如下四种：BEHAVIOR、SPEECH、EXPRESSION、PSYCHOLOGICAL_ACTIVITY。请按照下面提供的样例json文件格式，结合你所处的场景和周围人的行为，做出你的行为。注意，你做出的行为类型应当只包括上面四种。因为我想要创作一个富有冲突性的情节，请你表现得更有攻击性和戏剧性一些。\n{action_info_example}'})
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=context,
            response_format={"type": "json_object"}
        )
        self.actions.append(json.loads(response.choices[0].message.content))
        print(self.actions)
        return json.loads(response.choices[0].message.content)

    def print_info(self) -> None:
        print(self.info)
    