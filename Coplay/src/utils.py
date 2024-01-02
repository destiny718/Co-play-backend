openai_key = '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'

role_info_example = {
    "name": "科怀·伦纳德",
    "age": "31",
    "characteristics": ["谦逊"],
    "preferences": ["篮球", "高尔夫"],
    "otherInformation": [
        "一位打小前锋的篮球运动员",
        "曾两次获得总决赛最有价值球员（FMVP）和最佳防守球员（DPOY）奖项",
        "目前效力于洛杉矶快船队"
    ]
}

scene_info_example = {
    "place": "一家古老的图书馆",
    "time": "一个阴雨天的下午",
    "atmosphere": ["寂静而神秘，充满陈旧的书香味"],
    "feeling": [
        "雨滴打在窗户上",
        "远处雷声",
        "楼上隐约的脚步声",
        "雨滴打在窗户上",
        "远处雷声",
        "楼上隐约的脚步声",
        "高耸的书架上铺满尘封的书籍",
        "地上铺着历史感十足的红色地毯",
        "角落的大火炉旁摇曳着火苗",
        "半开的窗户透进雨声",
        "大木桌旁黄色台灯下的古老地图",
        "墙上挂着似乎各有故事的古旧画作",
        "老式吊灯微晃，散发着微弱的光线",
        "旧木楼梯旁似有秘密通道",
        "空气中弥漫着木头和陈旧书页的味道",
        "新鲜泥土的气息从窗户中飘入",
    ],
    "otherInformation": []
}

action_info_example = {
    "CHARACTER": ['李芊'],
    "BEHAVIOR": ["打开一本陈旧的书籍，仔细翻阅"],
    "SPEECH": ["对着房间里的其他人说：'这里藏着不为人知的秘密。'"],
    "EXPRESSION": ["脸上露出惊讶的表情，随着发现的深入而眼睛逐渐放大"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理活动复杂，对于可能的发现感到既兴奋又紧张"]
}


# ========================axis: more example==============================


# 我
girl_A_info = {
    "name": "李芊",
    "age": "高中生",
    "characteristics": ["文静", "好奇心强"],
    "preferences": ["解谜", "冒险"],
    "otherInformation": [
        "对校园中的奇怪事件充满好奇",
        "在探险中展现坚定和果断的一面"
    ]
}

# 男生A
boy_A_info = {
    "name": "张翔",
    "age": "高中生",
    "characteristics": ["热情", "大胆"],
    "preferences": ["冒险", "解谜"],
    "otherInformation": [
        "一直向往冒险，听说废弃老楼有玄机",
        "在关键时刻表现出一些不安"
    ]
}

# 女生B
girl_B_info = {
    "name": "刘婷",
    "age": "高中生",
    "characteristics": ["幽默", "好奇"],
    "preferences": ["八卦", "冒险"],
    "otherInformation": [
        "喜欢津津乐道校园中的八卦",
        "对废弃老楼充满好奇"
    ]
}

# 校园保安
security_info = {
    "name": "张保安",
    "age": "中年",
    "characteristics": ["平实", "关爱"],
    "preferences": ["校园安全"],
    "otherInformation": [
        "一直默默守护校园的老保安",
        "对废弃老楼有深厚的经验"
    ]
}

scene_info = {
    "place": "废弃的老楼内部",
    "time": "深夜",
    "atmosphere": ["昏暗而神秘，弥漫着陈旧的尘埃"],
    "feeling": [
        "墙上的涂鸦在微弱的光线下显得诡异",
        "古老的门散发着一股潮湿的气息",
        "楼梯上的脚步声回荡在空荡的走廊中",
        "打开通往楼顶的门，古老的风扑面而来",
        "解开密码时，字符间的神秘感渐渐浮现",
        "发现通往地下的楼梯，阶梯间弥漫着古老的木头味",
        "地下空间中古老文献的气息让人感到诡异",
        "发现了神秘仪式用品，空气中弥漫着神秘的仪式感",
        "四人在地下空间展开深入的调查，气氛越发紧张",
        "古老的文献透露着一场神秘聚会的影子",
    ],
    "otherInformation": ["解开密码，发现通往地下的楼梯", "地下空间中发现了古老的文献和仪式用品"]
}

action_info_1 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["抬头看着陈旧的楼梯，心生一丝好奇。"],
    "SPEECH": ["这里好像很久没人来过了。"],
    "EXPRESSION": ["眉头微蹙，仿佛能感受到岁月的沉淀。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知的好奇和期待。"]
}

action_info_2 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["走上前，轻轻推开通往楼顶的门。"],
    "SPEECH": ["看起来很古老，但应该还能用。"],
    "EXPRESSION": ["眼中闪烁着冒险的光芒。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对新奇事物的好奇心。"]
}

action_info_3 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["靠近墙壁，观察上面的涂鸦。"],
    "SPEECH": ["这些涂鸦好像在诉说着什么故事。"],
    "EXPRESSION": ["眼中闪过一丝好奇和不安。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知故事的渴望，但也带着一些紧张。"]
}

action_info_4 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["走到一旁，默默注视着四人的一举一动。"],
    "SPEECH": ["小心点，年轻人，有些事情不是那么好解开的。"],
    "EXPRESSION": ["脸上露出沉稳的表情。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对校园安全的责任感，对年轻人的好奇心保持理解。"]
}

action_info_5 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["握着那封古老的信，仔细阅读着上面的内容。"],
    "SPEECH": ["这封信里提到了当晚的神秘聚会，我们或许能找到线索。"],
    "EXPRESSION": ["眉头微皱，思考着信中的可能线索。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对过去事件的好奇和解谜的愿望。"]
}

action_info_6 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["在字符间来回比对，试图找出可能的规律。"],
    "SPEECH": ["也许这些字符之间隐藏着某种密码。"],
    "EXPRESSION": ["眼中闪烁着解谜时的兴奋。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对密码破解的兴奋和好奇。"]
}

action_info_7 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["查阅历史资料，试图寻找那个时代可能用的密码方式。"],
    "SPEECH": ["也许当时有些秘密社团会用特殊密码沟通。"],
    "EXPRESSION": ["眼中有了些许发现的光芒。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对历史线索的好奇和期待。"]
}

action_info_8 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["走到四人身边，帮忙分析密码。"],
    "SPEECH": ["或许当年确实有些特殊的密码，你们试试这样。"],
    "EXPRESSION": ["面带微笑，展现出对年轻人的关心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对年轻人安全的关切，同时也对解谜过程保持耐心。"]
}

action_info_9 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["打开通往地下的楼梯门，露出一丝期待。"],
    "SPEECH": ["也许下面有更多的线索，我们一起去看看吧。"],
    "EXPRESSION": ["眼中透露出对未知的好奇和决心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对地下空间的好奇和探索欲望。"]
}

action_info_10 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["迈开大步，领先地走向楼梯。"],
    "SPEECH": ["让我们一探究竟，看看这里到底藏着什么。"],
    "EXPRESSION": ["表情中带着冒险的坚定。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知冒险的兴奋和期待。"]
}

action_info_11 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["在地下空间中仔细搜查文献和仪式用品。"],
    "SPEECH": ["这些东西真是古老而神秘，我们得小心查看。"],
    "EXPRESSION": ["眼中透露出对古老文献的好奇和不安。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对文献背后故事的好奇和紧张。"]
}

action_info_12 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["默默注视四人的一举一动，保持警惕。"],
    "SPEECH": ["小心行事，年轻人，这里可能有些无法预知的事情。"],
    "EXPRESSION": ["表情凝重，透露出对地下空间的警觉。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生安全的责任感和对未知的谨慎。"]
}

scene_info_2 = {
    "place": "地下空间深处",
    "time": "半夜",
    "atmosphere": ["黑暗笼罩，只有微弱的光线透过古老的仪式用品洒下"],
    "feeling": [
        "空气中弥漫着神秘的氛围，似乎有一些无形的力量在游走",
        "地下空间的古老文献显得更为神秘，透露着古老的仪式感",
        "四人的脚步声在地下空间中回响，显得格外深沉",
        "仪式用品的影子在微弱的灯光下显得扭曲而怪异",
        "四人心中的紧张感在地下空间逐渐升温",
        "蜡烛的微弱光芒照亮了地下空间的一角，但也让阴影显得更加深沉",
    ],
    "otherInformation": ["四人在地下空间中深入探索，逐渐发现更多神秘的事物"]
}

action_info_13 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["继续仔细查看古老文献，寻找可能的线索。"],
    "SPEECH": ["这些文献里好像有一些古老的仪式记录，我们得找到相关的信息。"],
    "EXPRESSION": ["眼中透露出对文献中信息的渴望和紧张。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对解开谜团的渴望，但也感到了一些紧张。"]
}

action_info_14 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["绕过一堆古老的仪式用品，突然感觉到一阵寒意。"],
    "SPEECH": ["这里感觉...好像有什么不对劲。"],
    "EXPRESSION": ["表情中带着一丝紧张和不安。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对周围环境的紧张感和戒备。"]
}

action_info_15 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["靠近一个装满古老符咒的角落，突然间感觉到一股奇怪的能量。"],
    "SPEECH": ["这些符咒好像散发出一种古老的力量，我们得小心。"],
    "EXPRESSION": ["眼中透露出一丝惊讶和紧张。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对符咒能量的好奇和戒备。"]
}

action_info_16 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["继续保持对四人的警戒，注意四周的动静。"],
    "SPEECH": ["这个地方确实有些不同寻常，大家小心。"],
    "EXPRESSION": ["脸上露出一丝严肃，保持对周围环境的关注。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生安全的责任感和对地下空间的警觉。"]
}

action_info_17 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["突然听到远处传来一阵低沉的声音，让人毛骨悚然。"],
    "SPEECH": ["你们听到了吗？那是什么声音？"],
    "EXPRESSION": ["眼中闪过一丝惊恐，全身紧绷。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知声音的恐惧和紧张。"]
}

action_info_18 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["环顾四周，突然发现有一些阴影在墙上晃动。"],
    "SPEECH": ["那是什么？有什么东西在这里。"],
    "EXPRESSION": ["表情中带着明显的恐慌，身体略微后退。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对突发情况的恐慌和不安。"]
}

action_info_19 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["突然感觉到一些无形的力量，让她难以站稳。"],
    "SPEECH": ["这里好像充满了一些无法言说的力量，我们得赶紧离开。"],
    "EXPRESSION": ["眼中透露出一丝无助和惊慌。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对神秘力量的惊慌和渴望逃离。"]
}

action_info_20 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["迅速拉起四人，试图带领大家远离那些阴影。"],
    "SPEECH": ["快，我们得赶紧离开这个地方，有些事情我也难以解释。"],
    "EXPRESSION": ["脸上露出紧张和焦虑的表情。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对突发状况的紧张和责任感，试图保护年轻人。"]
}

scene_info_3 = {
    "place": "地下空间深处",
    "time": "凌晨",
    "atmosphere": ["黑暗笼罩，神秘的氛围更为浓郁，四处弥漫着古老仪式的味道"],
    "feeling": [
        "地下空间显得更加安静，只有四人的呼吸声和微弱的蜡烛光芒",
        "古老的仪式用品在黑暗中闪烁出诡异的光芒",
        "四人的神情变得更加紧张，随时准备应对可能发生的危险",
        "墙上的符咒在微弱的灯光下显得更为神秘",
        "空气中弥漫着一种无法言喻的压抑感，让人感到窒息",
    ],
    "otherInformation": ["四人在黑暗中寻找着前行的方向"]
}

action_info_21 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["仔细观察四周，试图找到通往外面的出口。"],
    "SPEECH": ["我们必须找到出口，不能再待在这里。"],
    "EXPRESSION": ["眼中透露出对找到安全通道的渴望和紧张。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对现状的不安和寻找出路的渴望。"]
}

action_info_22 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["试图移开一些仪式用品，为大家打开前行的道路。"],
    "SPEECH": ["让我们快点，我们不能在这里待太久。"],
    "EXPRESSION": ["表情中带有焦急和坚定。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对危险的警觉和保护同伴的责任感。"]
}

action_info_23 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["突然感觉到周围的空气变得沉重，好像有一些无形的阻力。"],
    "SPEECH": ["这里的能量越来越奇怪了，我们要小心应对。"],
    "EXPRESSION": ["眼中透露出对周围环境异常的惊愕和不安。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知力量的惊愕和对应对方式的思考。"]
}

action_info_24 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["拉起女生B，试图帮助她走出那些无形的阻力。"],
    "SPEECH": ["我们要紧密相连，一起克服这些困难。"],
    "EXPRESSION": ["表情中充满了对学生安全的关切和对突发状况的决心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生的责任感和对困境的决心。"]
}

action_info_25 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["突然听到一阵低沉的声音，仿佛有什么在黑暗中悄悄靠近。"],
    "SPEECH": ["大家小心，有什么东西在我们周围。"],
    "EXPRESSION": ["眼中闪烁着对未知的恐惧。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对突发状况的紧张和对周围动静的关注。"]
}

action_info_26 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["转头向声音的方向看去，试图辨别出是什么。"],
    "SPEECH": ["别怕，我们一定能解决的。"],
    "EXPRESSION": ["表情中透露出对同伴的安抚和对未知的挑战。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对安抚同伴的责任感和对未知的勇气。"]
}

action_info_27 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["突然感觉到有什么在身后移动，不禁加快脚步。"],
    "SPEECH": ["我们得尽快离开这里，有些东西在追着我们。"],
    "EXPRESSION": ["眼中透露出对身后威胁的惊慌。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对逃离的渴望和对未知威胁的惊恐。"]
}

action_info_28 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["带头朝着可能的出口方向迅速前行，试图引导大家。"],
    "SPEECH": ["跟紧我，我们快点离开这里。"],
    "EXPRESSION": ["表情中充满了对学生的保护欲望和对危险的应对决心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生安全的紧张和对应对困境的决心。"]
}

girl_C_info = {
    "name": "林婉",
    "age": "高中生",
    "characteristics": ["神秘", "聪明"],
    "preferences": ["掌握秘密", "操控局势"],
    "otherInformation": [
        "在校园中总是保持低调，很少参与学生活动",
        "对于古老仪式和神秘力量有深刻的了解",
        "喜欢操控他人，掌握局势"
    ]
}

scene_info_4 = {
    "place": "地下空间深处",
    "time": "凌晨",
    "atmosphere": ["黑暗笼罩，神秘的氛围更为浓郁，四处弥漫着古老仪式的味道"],
    "feeling": [
        "地下空间显得更加安静，只有四人的呼吸声和微弱的蜡烛光芒",
        "古老的仪式用品在黑暗中闪烁出诡异的光芒",
        "四人的神情变得更加紧张，随时准备应对可能发生的危险",
        "墙上的符咒在微弱的灯光下显得更为神秘",
        "空气中弥漫着一种无法言喻的压抑感，让人感到窒息",
    ],
    "otherInformation": ["四人在黑暗中寻找着前行的方向"]
}

action_info_29 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["仔细观察四周，试图找到通往外面的出口。"],
    "SPEECH": ["我们必须找到出口，不能再待在这里。"],
    "EXPRESSION": ["眼中透露出对找到安全通道的渴望和紧张。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对现状的不安和寻找出路的渴望。"]
}

action_info_30 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["试图移开一些仪式用品，为大家打开前行的道路。"],
    "SPEECH": ["让我们快点，我们不能在这里待太久。"],
    "EXPRESSION": ["表情中带有焦急和坚定。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对危险的警觉和保护同伴的责任感。"]
}

action_info_31 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["突然感觉到周围的空气变得沉重，好像有一些无形的阻力。"],
    "SPEECH": ["这里的能量越来越奇怪了，我们要小心应对。"],
    "EXPRESSION": ["眼中透露出对周围环境异常的惊愕和不安。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知力量的惊愕和对应对方式的思考。"]
}

action_info_32 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["拉起女生B，试图帮助她走出那些无形的阻力。"],
    "SPEECH": ["我们要紧密相连，一起克服这些困难。"],
    "EXPRESSION": ["表情中充满了对学生安全的关切和对突发状况的决心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生的责任感和对困境的决心。"]
}

action_info_33 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["突然听到一阵低沉的声音，仿佛有什么在黑暗中悄悄靠近。"],
    "SPEECH": ["大家小心，有什么东西在我们周围。"],
    "EXPRESSION": ["眼中闪烁着对未知的恐惧。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对突发状况的紧张和对周围动静的关注。"]
}

action_info_34 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["转头向声音的方向看去，试图辨别出是什么。"],
    "SPEECH": ["别怕，我们一定能解决的。"],
    "EXPRESSION": ["表情中透露出对同伴的安抚和对未知的挑战。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对安抚同伴的责任感和对未知的勇气。"]
}

action_info_35 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["突然感觉到有什么在身后移动，不禁加快脚步。"],
    "SPEECH": ["我们得尽快离开这里，有些东西在追着我们。"],
    "EXPRESSION": ["眼中透露出一丝无助和惊慌。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对逃离的渴望和对未知威胁的惊恐。"]
}

action_info_36 = {
    "CHARACTER": ["校园保安"],
    "BEHAVIOR": ["带头朝着可能的出口方向迅速前行，试图引导大家。"],
    "SPEECH": ["跟紧我，我们快点离开这里。"],
    "EXPRESSION": ["表情中充满了对学生的保护欲望和对危险的应对决心。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对学生安全的紧张和对应对困境的决心。"]
}

# 危险的来源 - 林婉的计谋
action_info_37 = {
    "CHARACTER": ["林婉"],
    "BEHAVIOR": ["悄悄地从阴影中走出，微笑着看着四人的惊慌。"],
    "SPEECH": ["你们终于发现了我的存在，可惜太迟了。"],
    "EXPRESSION": ["脸上带着得逞的笑容，眼中闪烁着邪恶的光芒。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对操控局势的满足和对四人绝望的期待。"]
}

action_info_38 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["惊讶地看着林婉，意识到自己中了对方的计谋。"],
    "SPEECH": ["你...你是故意引导我们来到这里的吗？"],
    "EXPRESSION": ["表情中带着无法接受的震惊。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对自己轻信的自责和对敌人的愤怒。"]
}

action_info_39 = {
    "CHARACTER": ["林婉"],
    "BEHAVIOR": ["冷笑着点头，慢慢走近女生A。"],
    "SPEECH": ["没错，你们就是我的游戏棋子，而这是我的领域。"],
    "EXPRESSION": ["眼中透露出对自己计谋得逞的得意。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对掌握局势的满足和对四人绝望的期待。"]
}

scene_info_5 = {
    "place": "地下空间深处",
    "time": "凌晨",
    "atmosphere": ["紧张而激烈，四处弥漫着古老仪式的味道"],
    "feeling": [
        "空气中弥漫着激烈的战斗氛围，蜡烛的火焰摇曳不定",
        "四人与林婉展开激烈的对抗，各自施展着自己的力量",
        "墙上的符咒在战斗中闪烁出神秘的光芒",
        "地下空间的回音回荡着战斗的声音，显得格外恐怖",
        "女生A勉强逃离，但一个人却在混乱中走散，下落未知"
    ],
    "otherInformation": ["女生A和其他同伴展开与林婉的绝望对抗"]
}

# 战斗环节
action_info_40 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["运用一些掌握的仪式技巧，试图制造一些干扰。"],
    "SPEECH": ["我们不能让她得逞，得赶紧离开这里。"],
    "EXPRESSION": ["表情中透露出对战斗的焦虑和坚定。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对同伴安危的担忧和对战胜林婉的决心。"]
}

action_info_41 = {
    "CHARACTER": ["男生A"],
    "BEHAVIOR": ["奋力挡住林婉的攻击，试图给女生A争取时间。"],
    "SPEECH": ["别担心，我们会保护好你的。"],
    "EXPRESSION": ["表情中充满了对同伴的保护欲望和对林婉的愤怒。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对同伴安危的担忧和对战胜林婉的决心。"]
}

action_info_42 = {
    "CHARACTER": ["女生B"],
    "BEHAVIOR": ["利用自己的能力，试图寻找林婉的弱点。"],
    "SPEECH": ["我们得找到她的弱点，否则我们逃不出去。"],
    "EXPRESSION": ["眼中透露出对战斗的冷静和对林婉的仇恨。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对同伴安危的担忧和对战胜林婉的决心。"]
}

action_info_43 = {
    "CHARACTER": ["林婉"],
    "BEHAVIOR": ["反击女生A的干扰，试图击败她们中的每一个。"],
    "SPEECH": ["你们太天真了，这里是我掌控的领域。"],
    "EXPRESSION": ["眼中闪烁着邪恶的光芒，面对战局毫不畏惧。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对掌握局势的得意和对四人绝望的期待。"]
}

action_info_44 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["在战斗中不小心中了林婉的陷阱，被击败。"],
    "SPEECH": ["啊！小心，有什么东西..."],
    "EXPRESSION": ["表情中充满了痛苦和无助，随着力量的消失倒在地上。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对自己失误的懊悔和对未知命运的恐惧。"]
}

# 主人公勉强逃离，女生C走散
action_info_45 = {
    "CHARACTER": ["女生A"],
    "BEHAVIOR": ["拉着其他同伴，奋力突围，试图逃离战斗。"],
    "SPEECH": ["我们没办法战胜她，得先逃出去，再想办法。"],
    "EXPRESSION": ["表情中透露出对逃生的渴望和对同伴的牵引。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对女生C下落的担忧和对逃生的紧张。"]
}

action_info_46 = {
    "CHARACTER": ["林婉"],
    "BEHAVIOR": ["眼中闪烁着冷酷的光芒，看着女生A逃离。"],
    "SPEECH": ["逃吧，但你们无法逃脱我的掌控。"],
    "EXPRESSION": ["脸上带着得逞的笑容，对女生A逃离毫不阻拦。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对战胜的得意和对四人绝望的期待。"]
}

# 女生C走散
action_info_47 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["在混乱中迷失了方向，孤身一人走散在地下空间。"],
    "SPEECH": ["大家在哪里？！"],
    "EXPRESSION": ["表情中透露出对失散的恐惧和对同伴的呼唤。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知命运的恐惧和对寻找同伴的渴望。"]
}

# 女生C的迷失与新发现
action_info_48 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["在黑暗中四处寻找同伴的踪迹，试图找到出口。"],
    "SPEECH": ["大家在哪里？！"],
    "EXPRESSION": ["眼中透露出迷失和害怕，不知所措。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知命运的恐惧和对寻找同伴的渴望。"]
}

action_info_49 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["突然听到一阵诡异的声音，好像有什么在黑暗中靠近。"],
    "SPEECH": ["是谁？有人吗？"],
    "EXPRESSION": ["表情中透露出对陌生声音的警觉和恐惧。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知威胁的担忧和对自身安危的紧张。"]
}

action_info_50 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["勇敢地面对黑暗，试图辨别出周围的环境。"],
    "SPEECH": ["别躲藏了，出来吧！"],
    "EXPRESSION": ["眼中闪烁着对未知挑战的勇气。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对陌生声音的挑战和对寻找同伴的决心。"]
}

# 揭开黑暗中的真相
action_info_51 = {
    "CHARACTER": ["神秘声音"],
    "BEHAVIOR": ["从黑暗中走出，露出一抹微光，面露微笑。"],
    "SPEECH": ["别害怕，我不会伤害你。"],
    "EXPRESSION": ["脸上带着友好的笑容，眼中透露出关切。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对女生C的关切和对黑暗中的孤独感的理解。"]
}

action_info_52 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["看着神秘声音，试图辨认对方的身份。"],
    "SPEECH": ["你是谁？为什么会在这里？"],
    "EXPRESSION": ["表情中带有对陌生人的疑惑和警觉。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对未知真相的好奇和对自身安危的担忧。"]
}

action_info_53 = {
    "CHARACTER": ["神秘声音"],
    "BEHAVIOR": ["慢慢透露身份，解释自己是古老仪式的守护者。"],
    "SPEECH": ["我是这个地方的守护者，你们不应该在这里。"],
    "EXPRESSION": ["神秘声音透露出对仪式的责任感和对四人的警告。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对仪式安宁的关切和对四人安危的担忧。"]
}

action_info_54 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["逐渐相信神秘声音，表现出一些放松。"],
    "SPEECH": ["我们是被诱导到这里的，能帮帮我们吗？"],
    "EXPRESSION": ["眼中透露出对守护者的信任和对救援的期望。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对陌生帮助的感激和对未知前路的期待。"]
}

# 新场景，守护者的助力
scene_info_6 = {
    "place": "地下空间深处",
    "time": "凌晨",
    "atmosphere": ["神秘而宁静，四处弥漫着守护者的力量"],
    "feeling": [
        "神秘声音引导女生C走向安全通道，避开危险",
        "四周的符咒在守护者的干预下释放出宁静的光芒",
        "地下空间显得更加宁静，守护者的存在使得一切变得有序"
    ],
    "otherInformation": ["女生C在守护者的帮助下寻找安全通道"]
}

# 守护者的助力
action_info_55 = {
    "CHARACTER": ["神秘声音"],
    "BEHAVIOR": ["引导女生C走向通往安全通道的方向。"],
    "SPEECH": ["跟紧我，我会带你走出这片迷雾。"],
    "EXPRESSION": ["神秘声音表情中透露出对安全通道的信心和对四人的关切。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对守护使命的责任感和对四人的期望。"]
}

# 女生C获救
action_info_56 = {
    "CHARACTER": ["女生C"],
    "BEHAVIOR": ["跟随神秘声音的引导，逐渐远离战斗的区域。"],
    "SPEECH": ["谢谢你，如果没有你，我们可能真的无法逃脱。"],
    "EXPRESSION": ["表情中透露出对守护者的感激和对未知前路的期待。"],
    "PSYCHOLOGICAL_ACTIVITY": ["心理上充满了对陌生帮助的感激和对未来的期许。"]
}
