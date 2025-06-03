class BackendConfig:
    def __init__(self):
        self.HOST = "0.0.0.0"
        self.PORT = 8000
        self.ENV = "dev"
        self.DEBUG = True
        self.WORKERS = 1

    def update_with_args(self, args):
        self.PORT = args.port
        self.ENV = args.env
        self.DEBUG = self.ENV != "prod"  # 운영 환경이 아니면 디버그 모드
