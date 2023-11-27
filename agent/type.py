from enum import Enum

# 枚举类型，用于描述人物行为的不同方面
class ActionType(Enum):
    SPEECH = 1
    BEHAVIOR = 2
    EXPRESSION = 3
    PSYCHOLOGICAL_ACTIVITY = 4
class Act:
    def __init__(self, act_type, content):
        self.acttype = act_type
        self.content = content
class History:
    def __init__(self, traits={}, acts=[]):
        self.traits = traits  # 人物信息，json
        self.acts = acts      # 人物行为，Act结构体列表
        
class AgentType(Enum):
    ROLE = 1
    SCENE = 2
    WRITER = 3
    
class ActRecord:
    def __init__(self, character_name, actions):
        self.character_name = character_name
        self.actions = actions # 列表
        
class processType(Enum):
    roleAct = 1
    sceneAct = 2
    writerAct = 3
    roleInit = 4
    sceneInit = 5
    writerInit = 6
    writerSum = 7
