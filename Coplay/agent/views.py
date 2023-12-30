from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from openai import OpenAI
import json

from src.utils import openai_key
from src.WritingCopilot import WritingCopilot
from src.Role import Role
from src.Scene import Scene
from models import run_process_model

# Create your views here.
def post_create_story(req: HttpRequest):
    body = json.loads(req.body.decode("utf-8"))
    title = require(body, "title", "string", err_msg="title缺失或者类型错误")
    big_background = require(body, "big_background", "string", err_msg="big_background缺失或者类型错误")
    client = OpenAI(api_key=openai_key) 
    copilot = WritingCopilot(len(run_process_model), title, big_background, [], [], client)
    run_process_model.add_copilot(copilot)
    return request_success()

def get_story(req: HttpRequest):
    param = req.GET
    story_id = None
    try:
        story_id = param["id"]
    except Exception as e:
        pass

    if story_id:
        # 返回特定的故事
        # TODO:
        pass
    else:
        # 返回故事的title列表
        title_list = run_process_model.iter()
        return request_success({"stories": title_list})

def post_create_role(req: HttpRequest):
    body = json.loads(req.body.decode("utf-8"))
    story_id = require(body, "story_id", "int", err_msg="story_id缺失或者类型错误")
    story_copilot = run_process_model.copilots[story_id]
    client = OpenAI(api_key=openai_key)
    del body["story_id"]
    need_completion = require(body, "need_completion", "bool", err_msg="need_completion缺失或者类型错误")
    del body["need_completion"]

    if need_completion:
        role = Role(len(story_copilot.roles), client, body)
        role.init_role()
    else:
        role = Role(len(story_copilot.roles), client, body)
        role.info = role.init_info

    story_copilot.add_role(role)
    return request_success({"id": role.id})

def post_update_role(req: HttpRequest):
    body = json.loads(req.body.decode("utf-8"))
    role_id = require(body, "id", "int", err_msg="id缺失或者类型错误")
    story_id = require(body, "story_id", "int", err_msg="story_id缺失或者类型错误")
    del body["id"]
    del body["story_id"]
    story_copilot = run_process_model.copilots[story_id]
    story_copilot.roles[role_id].info = body
    return request_success()


def post_create_scene(req: HttpRequest):
    body = json.loads(req.body.decode("utf-8"))
    story_id = require(body, "story_id", "int", err_msg="story_id缺失或者类型错误")
    story_copilot = run_process_model.copilots[story_id]
    client = OpenAI(api_key=openai_key)
    del body["story_id"]
    need_completion = require(body, "need_completion", "bool", err_msg="need_completion缺失或者类型错误")
    del body["need_completion"]

    if need_completion:
        scene = Scene(len(story_copilot.scenes), client, body)
        scene.init_scene()
    else:
        scene = Role(len(story_copilot.scenes), client, body)
        scene.info = scene.init_info

    story_copilot.add_scene(scene)
    return request_success({"id": scene.id})

def post_update_scene(req: HttpRequest):
    body = json.loads(req.body.decode("utf-8"))
    scene_id = require(body, "id", "int", err_msg="id缺失或者类型错误")
    story_id = require(body, "story_id", "int", err_msg="story_id缺失或者类型错误")
    del body["id"]
    del body["story_id"]
    story_copilot = run_process_model.copilots[story_id]
    story_copilot.scenes[scene_id].info = body
    return request_success()


def post_create_timestep(req: HttpRequest):
    pass

def post_create_interaction(req: HttpRequest):
    pass

def request_success(data={}):
    return JsonResponse({
        "code": 0,
        "message": "Succeed",
        **data
    })

def require(body, key, type="string", err_msg=None, err_code=-2):
    
    if key not in body.keys():
        raise KeyError(err_msg if err_msg is not None else f"参数错误。参数 `{key}` 缺失。", err_code)
    
    val = body[key]
    
    err_msg = f"参数错误。参数 `{key}` 需要是 `{type}` 类型。" if err_msg is None else err_msg
    
    if type == "int":
        try:
            val = int(val)
            return val
        except:
            raise KeyError(err_msg, err_code)
        
    elif type == "bool":
        try:
            val = bool(val)
            return val
        except:
            raise KeyError(err_msg, err_code)
    
    elif type == "float":
        try:
            val = float(val)
            return val
        except:
            raise KeyError(err_msg, err_code)
    
    elif type == "string":
        try:
            val = str(val)
            return val
        except:
            raise KeyError(err_msg, err_code)
    
    elif type == "list":
        try:
            assert isinstance(val, list)
            return val
        except:
            raise KeyError(err_msg, err_code)

    else:
        raise NotImplementedError(f"类型 `{type}` 错误。", err_code)