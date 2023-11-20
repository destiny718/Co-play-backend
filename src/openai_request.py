import requests
import json
from config.chatgpt_config import config_dict 

class OpenAI_Request(object):

    def __init__(self,key,model_name,request_address,generate_config=None):
        super().__init__()
        self.headers = {"Authorization":f"Bearer {key}","Content-Type": "application/json"}
        self.model__name = model_name
        self.request_address = request_address
        self.generate_config = generate_config

    def post_request(self,message):

        data = {
            "model": self.model__name,
            "messages":  message
        }

        # add generate parameter of api
        if self.generate_config:
            for k,v in self.generate_config.param_dict.__dict__.items():
                data[k] = v

        data = json.dumps(data)

        response = requests.post(self.request_address, headers=self.headers, data=data)

        return response


if __name__ == '__main__':
    keys = config_dict['Acess_config']['authorization']
    model_name = config_dict["Model_config"]['model_name']
    request_address = config_dict["Model_config"]['request_address']
    requestor = OpenAI_Request(keys,model_name,request_address)

    while 1:
        input_s = input('user input: ')
        res = requestor.post_request(input_s)

        response = res.json()['choices'][0]['message']['content']

        if  response:
            requestor.context_handler.append_cur_to_context(response,tag=1)

        print(f"chatGPT: {response}")

