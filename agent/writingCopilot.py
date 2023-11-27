from Agent import Agent, AgentType
from roleAgent import RoleAgent
from sceneAgent import SceneAgent
from tool import processInfo

# agent0 = SceneAgent("某高中学校教室")
# agent0.init_scene("一所普通的高中学校教室，中午，午休时间，发挥你的创造性补全场景")
agent1 = RoleAgent("路人甲")
agent1.initialize_role("请你发挥自己的创造性，给出一个校园生活中可能出现的青少年的人物形象设计")