#Pydantic はデータ検証を行うためのPythonライブラリです。
#データの「形」を属性付きのクラスとして宣言します。
#いくつかの値を持つクラスのインスタンスを作成すると、その
# 値を検証し、適切な型に変換して（もしそうであれば）全ての
# データを持つオブジェクトを提供してくれます。

from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str =  "Joe Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id" : "123",
    "string_ts" : "2017-06-01 12:22",
    "friends" : [1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.id)