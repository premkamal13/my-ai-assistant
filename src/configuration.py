class Configuration:
    def __init__(self, assistant_name, user_name, wolfram_app_id):
        self.assistant_name = assistant_name
        self.user_name = user_name
        self.wolfram_app_id = wolfram_app_id

    def __call__(self):
        return [self.assistant_name, self.user_name, self.wolfram_app_id]
