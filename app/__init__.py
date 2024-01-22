from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path=r'')

    # 注册蓝图和其他扩展
    from app.apis.agent import agent_bp

    app.register_blueprint(agent_bp)
    
    # 服务端测试
    @app.route('/test', methods=['GET'])
    def test():
        return '你好啊！ Hello!'
    
    return app
