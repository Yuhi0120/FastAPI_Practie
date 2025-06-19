from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: datetime = Body(),
    end_datetime: datetime = Body(),
    process_after: timedelta = Body(),
    repeat_at: Union[time, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }

#UUID:
# 多くのデータベースやシステムで共通のIDとして使用される、標準的な「ユニバーサルにユニークな識別子」です。
# リクエストとレスポンスではstrとして表現されます。

# datetime.datetime:
# Pythonのdatetime.datetimeです。
# リクエストとレスポンスはISO 8601形式のstrで表現されます: 2008-09-15T15:53:00+05:00

# datetime.date:
# Pythonのdatetime.dateです。
# リクエストとレスポンスはISO 8601形式のstrで表現されます: 2008-09-15

# datetime.time:
# Pythonのdatetime.time.
# リクエストとレスポンスはISO 8601形式のstrで表現されます: 14:23:55.003

# datetime.timedelta:
# Pythonのdatetime.timedeltaです。
# リクエストとレスポンスでは合計秒数のfloatで表現されます。
# Pydanticでは「ISO 8601 time diff encoding」として表現することも可能です。詳細はドキュメントを参照してください。

# frozenset:
# リクエストとレスポンスではsetと同じように扱われます:
# リクエストでは、リストが読み込まれ、重複を排除してsetに変換されます。
# レスポンスではsetがlistに変換されます。
# 生成されたスキーマはsetの値が一意であることを指定します（JSON SchemaのuniqueItemsを使用します）。

# bytes:
# Pythonの標準的なbytesです。
# リクエストとレスポンスではstrとして扱われます。
# 生成されたスキーマはstrでbinaryの「フォーマット」持つことを指定します。

# Decimal:
# Pythonの標準的なDecimalです。
# リクエストやレスポンスではfloatと同じように扱います。