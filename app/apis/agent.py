from flask import Blueprint, request
from app.pb2s.Agent_pb2 import AgentQuery, AgentReply


agent_bp = Blueprint('agent', __name__, url_prefix='/agent')


@agent_bp.route('/test', methods=['POST'])
def test():
    # 解析请求数据
    agent_query = AgentQuery()
    agent_query.ParseFromString(request.get_data())
    
    world_req = agent_query.world
    position_req = agent_query.position
    
    # 打印数据
    print('===打印数据===')
    print('world:', world_req)
    print('position_name:', position_req.name)
    print('event:', agent_query.event)
    for item in agent_query.interactItems:
        print('item:', item)
    print('======')
    
    # 返回数据
    agent_reply = AgentReply()
    
    order = agent_reply.order
    order.text = 'sleep'
    order.duration = 10
    
    world = agent_reply.world
    world.id = 1
    world.key = 'world 1'
    
    position = agent_reply.position
    position.name = 'position 1'
    
    for i in range(5):
        item = agent_reply.interactItems.add()
        item.id = i
        item.key = 'reply item ' + str(i)
    
    return agent_reply.SerializeToString()
