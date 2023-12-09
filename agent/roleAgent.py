from copy import deepcopy
from Agent import Agent
from tool import processInfo, get_json
from type import ActionType, Act, History, AgentType, processType

class RoleAgent:
    def __init__(self, name):
        self.agent = Agent(name, AgentType.ROLE)    # Agent类的实例
        self.historys = []    # 历史记录数组

    def initialize_role(self, prompt, initial_context=None):
        self.agent.initialize_agent(processInfo(sceneInfo=[], roleInfo=prompt, infoType=processType.roleInit), initial_context)
        
    def get_act_response(self, scene, acts):
        message = processInfo(scene, acts, processType.roleAct)
        self.agent.get_response(message)
        
    def add_history(self, traits, acts):
        # 确保acts中的元素是Act实例
        if not all(isinstance(act, Act) for act in acts):
            raise ValueError("All acts must be instances of Act")
        self.historys.append(History(traits, acts))

    def modify_history(self, time_step, traits=None, acts=None):
        # 检查索引是否在范围内
        if not (0 <= time_step < len(self.historys)):
            raise IndexError("Time step out of range")
        if traits is not None:
            self.historys[time_step].traits = traits
        if acts is not None:
            if all(isinstance(act, Act) for act in acts):
                self.historys[time_step].acts = acts
            else:
                raise ValueError("All acts must be instances of Act")

    def delete_history(self, time_step=None):
        # 如果提供了time_step，删除指定的历史记录
        if time_step is not None:
            if not (0 <= time_step < len(self.historys)):
                raise IndexError("Time step out of range")
            del self.historys[time_step]
        # 否则，默认删除最后一条历史记录
        else:
            self.historys.pop()

    def get_all_histories(self):
        # 返回所有历史记录的深拷贝
        return [deepcopy(history) for history in self.historys]
