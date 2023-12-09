import json
from enum import Enum
from type import ActionType, processType
import openai

openai.api_key = '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'
    
action_type_to_str = {
    ActionType.SPEECH: "SPEECH",
    ActionType.BEHAVIOR: "BEHAVIOR",
    ActionType.EXPRESSION: "EXPRESSION",
    ActionType.PSYCHOLOGICAL_ACTIVITY: "PSYCHOLOGICAL_ACTIVITY"
}
    
def processInfo(sceneInfo, roleInfo, infoType, writerInfo = "default"): # 生成发送给openai的message
    if infoType == processType.roleAct: # 所在场景 该时间步中之前发生的act列表
        message = "你所扮演的角色所处场景为：" + sceneInfo + "在这个场景中按照时间顺序所有人物(可能也包括你之前的行为)的行为依次如下[]中所示："
        message += "["
        for actinfo in roleInfo:
            message += "角色：" + actinfo.character_name + "行为如下<>中所示：<" 
            for act in actinfo.actions:
                message += "行为类型：" + action_type_to_str(act.acttype) + "具体行为内容：" + act.content + "|"
            message += ">"
        message += "]"   
        message += "请基于你的人物设定信息json，结合所处场景信息以及场景中给出的之前所有人物的行为(如果是心理活动，则只参考自己角色的心理活动)，用json格式按照行为时间顺序依次给出你在这个情景下会做出的反应(行为动作，语言，神态，心理活动)，注意你的回复应只包括json"  
        message += "人物反应json格式示例在下述===分割号之间给出:"
        act_json =  [
            {
                "acttype": "BEHAVIOR",
                "content": "打开一本陈旧的书籍，仔细翻阅"
            },
            {
                "acttype": "SPEECH",
                "content": "对着房间里的其他人说：'这里藏着不为人知的秘密。'"
            },
            {
                "acttype": "EXPRESSION",
                "content": "脸上露出惊讶的表情，随着发现的深入而眼睛逐渐放大"
            },
            {
                "acttype": "PSYCHOLOGICAL_ACTIVITY",
                "content": "心理活动复杂，对于可能的发现感到既兴奋又紧张"
            }
        ]
        message += f"==={act_json}===\n"
    
    elif infoType == processType.sceneAct: # 场景信息 场景中发生的1次act (rolename,roleact)
        message = ("你管理的的场景"+ sceneInfo +"中人物" + roleInfo[0] + "做出了如下[]中的行为/神态/语言。" + "["+ roleInfo[1] + "]。"
         "请你根据上述人物行为和你做管理的场景信息判断人物行为是否改变了场景信息，按照场景信息json格式给出最新的场景信息，如果场景信息没有改变只需返还原本的场景信息json"+sceneInfo+"即可" )
        
    elif infoType == processType.writerAct: # 给出某一场景信息，场景下所有act信息，按照act顺序组织文本
        message = "场景"+ sceneInfo +"中按照时间顺序各个人物的行为言语神态心理活动如下[]中内容所示：" 
        message += "["
        for acts in roleInfo:
            message += "人物" + acts.character_name + "行为如下<>中所示：<" 
            for act in acts.actions:
                message += "行为类型：" + action_type_to_str(act.acttype) + "具体行为内容：" + act.content + "|"
            message += ">"
        message += "]"
        message += "请你基于被设定的文字风格和语言要求，合成依据上述场景和人物行为信息构成的故事片段，直接给出合成后的故事片段文本"
        
    elif infoType == processType.roleInit: # 根据用户给出的初始化建议初始化角色，sceneInfo为空
        instructions = instructions = ("你需要扮演一位故事角色，你需要首先根据用户的要求文本创建这个角色的设定信息并在后续对话中扮演这个角色，如果用户没有具体设定要求请你自由发挥补全人物设定。"
         "角色设定信息使用json格式描述，包含基本信息、性格特征、外貌描述、背景故事、当前状态这5项内容.这5项内容下还有更具体的划分，参考示例json"
         "用户给出的设定意见文本在[]中给出，示例的任务信息json在下述内容中给出。如果用户设定信息没有指定的内容你可以直接自己补充完整"
         "你需要仿照示例格式并从用户意见文本中提取对应内容创建人物信息，如果参考意见文本中信息不够全面，你可以发挥创造性在不违反用户设定的情况下补全人物信息json，并且在后续对话中你只能使用json格式回复")
        # 示例JSON格式的人物设定
        role_json = {
            "角色": {
                "基本信息": {
                    "名字": "艾丽莎·斯通",
                    "年龄": 28,
                    "性别": "女",
                    "职业": "科学记者",
                },
                "性格特征": {
                    "主要性格": ["好奇心强", "批判性思维", "独立", "固执"],
                    "优点": ["智慧", "勇敢", "诚实"],
                    "缺点": ["偏执", "冲动", "有时过于直接"],
                    "恐惧": ["失去亲人", "被遗忘", "失败"],
                    "喜好": ["阅读科学杂志", "户外运动", "钢琴演奏"],
                    "价值观": ["坚信事实和科学","反对一切形式的不实报道"],
                },
                "外貌描述": {
                    "身高": "5英尺5英寸",
                    "体重": "130磅",
                    "眼睛颜色": "绿色",
                    "头发": "长卷发，栗色"
                },
                "背景故事": {
                    "家庭环境": ["出生于科学家家庭，自幼被教育重视科学方法和探索精神"],
                    "教育背景": ["生物学学士学位", "科学传播硕士学位"],
                    "过往经历": ["在一次科学展览中获得青年科学家奖", "报道过多次重大科学事件，获得了科学界的认可"],
                    "成就": ["建立了一个科学博客，拥有大量忠实读者", "成功揭露了一起科学骗局，为公众揭露了真相"],
                    "挫折": ["曾被错误的科学理论误导，导致报道失误", "在科学道德问题上与同行发生过严重争论"]
                },
                "当前状态": {
                    "动机": ["揭露学术道德问题","普及科学知识"],
                    "目标": ["成为一个知名的科学传播者"],
                    "内在冲突": ["在追求真相的过程中，常常挑战权威，导致社会关系紧张"]
                },
            }
        }

        fin = "现在请你根据上述信息和要求，给出你创建的人物设定信息json"
        message = (
            f"{instructions}\n"
            f"[{sceneInfo}]\n"
            f"==={role_json}===\n"
            f"{fin}\n"
        )
    elif infoType == processType.sceneInit: # 根据用户给出的初始化建议初始化场景，roleInfo为空
        instructions = ("假设你是一个剧本场景管理者，你负责根据用户的场景设定意见文本创建并维护一个场景的信息。场景信息使用json格式描述，包含地点、时间、氛围、听觉、视觉和嗅觉这6项内容."
        "用户给出的设定意见文本在[]中给出，示例的场景信息json在分隔符===之间。你需要仿照示例格式并从用户意见文本中提取对应内容创建场景信息，如果意见文本中信息不够全面，你可以发挥创造性补全场景信息json，后续对话中你只能使用场景信息json作为回复内容")

        # 示例JSON格式的场景设定
        scene_json = {
            "场景": {
                "地点": "一家古老的图书馆",
                "时间": "一个阴雨天的下午",
                "氛围": "寂静而神秘，充满陈旧的书香味",
                "听觉": [
                    "雨滴打在窗户上",
                    "远处雷声",
                    "楼上隐约的脚步声"
                ],
                "视觉": [
                    "高耸的书架上铺满尘封的书籍",
                    "地上铺着历史感十足的红色地毯",
                    "角落的大火炉旁摇曳着火苗",
                    "半开的窗户透进雨声",
                    "大木桌旁黄色台灯下的古老地图",
                    "墙上挂着似乎各有故事的古旧画作",
                    "老式吊灯微晃，散发着微弱的光线",
                    "旧木楼梯旁似有秘密通道"
                ],
                "嗅觉": [
                    "空气中弥漫着木头和陈旧书页的味道",
                    "新鲜泥土的气息从窗户中飘入",
                ]          
            }
        }
        fin = "现在请你根据上述信息和要求，给出你创建的场景信息json"
        message = (
            f"{instructions}\n"
            f"[{sceneInfo}]\n"
            f"{scene_json}\n"
            f"{fin}\n"
        )
        
    elif infoType == processType.writerInit: # 根据用户给出的初始化建议初始化写作agent, 设定文学风格，主题和语言特征
        if writerInfo == "default":
            style = "现代主义"          
            theme = "人与自然的关系"     
            language_features = "象征主义和复杂的句子结构"
            message = (
                "你是一名专业的故事编写者。请根据以下[]中的创作指导完成指定内容的写作：\n"
                f"[文学风格: {style}\n"
                f"主题: {theme}\n"
                f"语言特征: {language_features}]\n\n"
                "请遵循上述指导，在下述对话中根据给出具体的场景信息和人物行为完成剧本文本的写作。确保你生成的文本体现出上述[]中文本指定的文学风格，紧扣主题，并且在故事文本中使用了指定的语言特征。"
            )
        else:
            message = (
                "作为一个专业的故事编写者，请根据以下的创作指导完成指定内容的写作：\n"
                f"[{writerInfo}]\n"
                "请遵循上述指导，在下述对话中根据用户给出具体的场景信息和人物行为完成剧本文本的写作。确保你生成的文本体现出上述[]中文本指定的文学风格，紧扣主题，并且在故事文本中使用了指定的语言特征。"
            )
            
    elif infoType == processType.writerSum: # 给出每一个时间步下的所有文本 组织为最终的剧本 writerinfo是字符串列表
        message = "根据以下[]中按照时间顺序提供的故事片段，基于你被设定的文字风格和语言要求，合成一个连贯完整的故事，叙事顺序不一定需要按照时间顺序进行，可以考虑选择更好叙事效果的组织形式，直接给出合成后的完整故事文本："
        message += "["
        for i, part in enumerate(writerInfo, 1):
            message += f"第{i}部分: {part}\n\n"
        message += "]"
        
    return message
        
def get_json(text):
    stack = []
    for i, char in enumerate(text):
        if char == '{':
            stack.append(i)
        elif char == '}' and stack:
            start = stack.pop()
            if not stack:
                # 完整的JSON对象
                end = i + 1
                try:
                    json_data = json.loads(text[start:end])
                    return json_data  # 返回找到的第一个完整的JSON对象
                except json.JSONDecodeError:
                    pass  # 如果不是有效的JSON，继续查找
    return None  # 如果没有找到有效的JSON，返回None

