import re


def verify_url(url, ver):
    """
    校验url的格式是否是有效的URL
    """
    rule = re.compile(f"{ver}")
    try:
        rule.match(url)
        exist = True if rule.search(url) else False
    except Exception as e:
        return {"exist": False, "msg": {e}, "error": "error url"}
    return {"exist": exist, "msg": "write vaild url", "error": "error url"}
