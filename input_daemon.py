import asyncio
import json
import time
import random
import websockets
from pynput.keyboard import Controller

keyboard = Controller()

# 默认延迟，会被前端的设置覆盖
BASE_DELAY = 0.04
RANDOM_DELAY = 0.03

async def type_text(text: str):
    """模拟输入文本"""
    for ch in text:
        keyboard.type(ch)
        time.sleep(BASE_DELAY + random.random() * RANDOM_DELAY)

async def handler(ws):
    """WebSocket处理器"""
    async for msg in ws:
        try:
            data = json.loads(msg)
            if data.get("type") == "TYPE":
                text = data.get("text", "")
                if text:
                    await type_text(text)
        except Exception as e:
            print(f"处理消息时出错: {e}")

async def main():
    """主函数"""
    async with websockets.serve(handler, "127.0.0.1", 8765):
        print("OS键盘服务已启动: ws://127.0.0.1:8765")
        print("等待前端连接...")
        await asyncio.Future()  # 永久运行

if __name__ == "__main__":
    asyncio.run(main())