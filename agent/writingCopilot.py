from Agent import Agent, AgentType
from roleAgent import RoleAgent
from sceneAgent import SceneAgent
from tool import processInfo
import openai


class PlayGround:
    def __init__(self, scenes: list[SceneAgent], roles: list[RoleAgent]) -> None:
        self.scenes = scenes
        self.roles = roles
        self.story = []
        self.time_step = 0

    def add_scene(self, scene: SceneAgent) -> None:
        self.scenes.append(scene)

    def add_role(self, role: RoleAgent) -> None:
        self.roles.append(role)

    def interact(self) -> None:
        # test
        scene = self.scenes[0]
        role0 = self.roles[0]
        role1 = self.roles[1]
        print()

        content = f'请扮演一个小说创作者，在{scene.agent.context}场景中，写出两个角色{role0.agent.context}, {role1.agent.context}之间发生的故事。'
        chat = openai.ChatCompletion.create(
                model='gpt-4-1106-preview',
                messages=[{'role': 'user', 'content': content}],
                temperature=0.3,
            )
        # 从OpenAI获得回复
        response = chat.choices[0].message.content
        print(response)

agent0 = SceneAgent("某高中学校教室")
agent0.init_scene("一所普通的高中学校教室，中午，午休时间，发挥你的创造性补全场景")
agent1 = RoleAgent("路人甲")
agent1.initialize_role("请你发挥自己的创造性，给出一个校园生活中可能出现的青少年的人物形象设计")
agent2 = RoleAgent("路人乙")
agent2.initialize_role("请你发挥自己的创造性，给出一个校园生活中可能出现的青少年的人物形象设计")
play = PlayGround([agent0], [agent1, agent2])
play.interact()
