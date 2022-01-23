"""
データの宣言:username
    属性:
        実際のユーザー名
    ルール:
        ユーザー名は4文字以上20文字以内である。
    できること:
        ユーザー名を大文字の変換する

"""


class UserName:
    def __init__(self, name):
        # nameのチェック
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}はルール違反です")
        self.name = name

    def upper_name(self):
        return self.name.upper()


bob = UserName(name="Bob Smith")
# tom = UserName(name="Tom Ford")

print(bob.name)
print(bob.upper_name())
# print(tom.name)
