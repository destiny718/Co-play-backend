import openai
from copy import deepcopy
from type import AgentType
openai.api_key = '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'
    
class Agent():
    def __init__(self, name, type, model='gpt-4-1106-preview'):
        self.name = name
        self.model = model
        if isinstance(type, AgentType):
            self.type = type
        else:
            raise ValueError("type must be an instance of AgentType enum")
        self.context = []  # 用于保存上下文的列表，其中包含role和content键

    def initialize_agent(self, prompt, initial_context=None): # 使用prompt和可选的初始上下文来初始化智能体
        self.context = [{"role": "system", "content": prompt}]
        if initial_context:
                self.context.extend(initial_context)
        
        print(self.get_response(""))

    def add_to_context(self, role, message): # 将新消息以role和content的形式添加到上下文
        self.context.append({'role': role, 'content': message})

    def revert_context(self, steps=1): # 移除上下文中的最后几条消息
        if steps < len(self.context):
            self.context = self.context[:-steps]
        else:
            self.context = []

    def modify_context(self, index, role, new_message): # 修改指定索引处的上下文消息
        if 0 <= index < len(self.context):
            self.context[index] = {'role': role, 'content': new_message}

    def delete_from_context(self, index): # 删除指定索引处的上下文消息
        if 0 <= index < len(self.context):
            del self.context[index]

    def get_response(self, message, temperature=1): # 将用户消息添加到上下文
        self.add_to_context('user', message)
        
        # 构建聊天输入
        if self.type == (AgentType.ROLE or AgentType.SCENE):
            chat = openai.ChatCompletion.create(
                model=self.model,
                messages=self.context,
                temperature=temperature,
                response_format={"type": "json_object"}
            )
        else:
            chat = openai.ChatCompletion.create(
                model=self.model,
                messages=self.context,
                temperature=temperature,
            )
        # 从OpenAI获得回复
        response = chat.choices[0].message.content
        
        # 将智能体的回复也添加到上下文
        self.add_to_context('assistant', response)
        
        return response
    
    def show_context(self):
        print(self.context)
    def export_context(self): # 导出当前的全部上下文深拷贝
        return deepcopy(self.context)

# agent1 = Agent("writer",AgentType.ROLE)
# agent1.initialize_agent("假设你是一名数据处理专家，请你按照给定格式回答问题，所有回答需要json格式，格式为：{question：'问题', answer:'答案'}")
# print(agent1.get_response("CSR寄存器是什么"))
# agent1.show_context()