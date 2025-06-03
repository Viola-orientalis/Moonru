from sanic import Sanic
from sanic.response import text

def create_app(config):
    app = Sanic("App")

    # 예시 라우터
    @app.route("/")
    async def hello(request):
        return text("Hello from Sanic")

    # 변경: app.ext_config → app.ctx.ext_config
    app.ctx.ext_config = config  # 커스텀 설정을 context에 저장

    return app
