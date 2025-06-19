from typing import List, Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    encoded_item = jsonable_encoder(item)
    items[item_id] = encoded_item
    return encoded_item

# To change the body partially, use patch
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item = items[item_id]
    stored_item_model = Item(**stored_item)
    update_item=item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_item)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
"""
まとめると、部分的な更新を適用するには、次のようにします:

(オプションで)PUTの代わりにPATCHを使用します。
保存されているデータを取得します。
そのデータをPydanticモデルにいれます。
入力モデルからデフォルト値を含まないdictを生成します（exclude_unsetを使用します）。
この方法では、モデル内のデフォルト値ですでに保存されている値を上書きするのではなく、ユーザーが実際に設定した値のみを更新することができます。
保存されているモデルのコピーを作成し、受け取った部分的な更新で属性を更新します（updateパラメータを使用します）。
コピーしたモデルをDBに保存できるものに変換します（例えば、jsonable_encoderを使用します）。
これはモデルの.dict()メソッドを再度利用することに匹敵しますが、値をJSONに変換できるデータ型、例えばdatetimeをstrに変換します。
データをDBに保存します。
更新されたモデルを返します。
"""

