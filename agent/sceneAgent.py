from roleAgent import Act
from Agent import Agent
from type import AgentType, ActRecord, processType
from tool import processInfo

class SceneAgent:
    def __init__(self, sceneName):
        self.agent = Agent(sceneName, AgentType.SCENE)  # Agent类的实例
        self.records = []   # 按时间步骤记录的人物行为列表，每个元素都是ActRecord的列表(不同人物的actrecored在同一个时间步的顺序记录)
        self.history = []   # 场景设定的历史记录
        self.current_time = 0
    def init_scene(self, scene_info):
        message = processInfo(scene_info, [], processType.sceneInit)
        self.agent.initialize_agent(message)
        self.history.append(message)
        self.records.append([])
        
    def add_record(self, time_step, character_name, action):
        # 确保记录列表与时间步长同步
        while len(self.records) <= time_step:
            self.records.append([])
        self.records[time_step].append(ActRecord(character_name, action))
        self.current_time = time_step

    def set_scene(self, time_step): 
        # 确保历史记录与时间步长同步
        while len(self.history) <= time_step:
            self.history.append(None)
        self.history[time_step] = self.history[self.current_time]
        self.current_time = time_step

    def interact_scene(self, time_step, character_name, actions): 
        self.add_record(time_step, character_name, actions) # 记录人物在场景中的行为
        message = processInfo(self.history[self.current_time],(character_name, actions),processType.sceneAct)
        response = self.agent.get_response(message) # 获取场景智能体的响应，可能会根据人物行为改变场景设定
        # 假设智能体的回复包含场景的改变
        self.set_scene(time_step, response)
        return response
