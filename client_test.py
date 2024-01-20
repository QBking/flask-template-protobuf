import requests
from app.pb2s.Agent_pb2 import AgentQuery, AgentReply, EventStatus, EventType


def test_demo():
    """
    测试 protobuf
    """
    
    # 创建一个Protobuf对象，并设置其属性，模拟请求数据
    request_data = AgentQuery()
    
    world = request_data.world
    world.id = 1
    world.key = 'world test'
    
    position = request_data.position
    position.name = 'position test'
    
    source_npc = request_data.sourceNPC
    source_npc.id = 1
    source_npc.key = 'npc1 test'
    
    event = request_data.event
    event.text = 'event test'
    event.status = EventStatus.DOING
    event.type = EventType.EVENT
    
    interact_npc = request_data.interactNPC
    interact_npc.id = 2
    interact_npc.key = 'npc2 test'
    
    for i in range(3):
        item = request_data.interactItems.add()
        item.id = i + 1
        item.key = f'item{i} test'
    
    req_data = request_data.SerializeToString()  # 序列化
    
    # 发送请求
    url = 'http://localhost:8888/agent/test'
    response = requests.post(url, data=req_data)
    data = response.content
    
    # 反序列化
    agent_reply = AgentReply()
    agent_reply.ParseFromString(data)
    
    print('reply', agent_reply)

if __name__ == '__main__':
    test_demo()
