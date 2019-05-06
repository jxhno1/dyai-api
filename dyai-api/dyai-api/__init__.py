import json
def gen_api_data_format(if_err, msg_content, data):
    res = {'error':if_err,
           'message':msg_content,
           'result':data}
    return json.dumps(res)