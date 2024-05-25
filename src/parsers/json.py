import json

def parse_list(s):
    target = s
    idx = target.find('[')
    if idx != -1:
        target = target[idx:]
    decoder = json.JSONDecoder()
    python_obj, ended_at = decoder.raw_decode(target)
    return python_obj
