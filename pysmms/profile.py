import requests

from .utils import auth, table, profile_url


class Profile(object):

    def __init__(self):
        self.auth_list = auth() if auth() else None
        self.profile_url = profile_url

    @staticmethod
    def format_profile(item):
        """
        格式化 profile 接口返回的数据
        """

        data = item["data"]
        items = [
            ["用户名", data["username"]],
            ["电子邮箱", data["email"]],
            ["用户组", data["role"]],
            ["到期时间", data["group_expire"]],
            ["已使用", data["disk_usage"]],
            ["总容量", data["disk_limit"]]
        ]
        return table(items=items, title="用户资料")

    def get_profile(self):
        """
        /profile : 获取用户个人资料
        """

        if auth not in self.auth_list:
            sys.exit("您的输入有误！请核对 Authorization！")

        result = list()
        for _auth in self.auth_list:
            headers = {"Authorization": _auth}
            doc = requests.post(self.profile_url, headers=headers).json()
            if doc["success"]:
                item = self.format_profile(doc)
                result.append(item)
            else:
                print("Authorization: {} \n信息异常！".format(auth))
        return result
