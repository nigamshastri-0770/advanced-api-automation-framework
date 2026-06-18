from core.config_reader import config


class JsonPlaceholderAPI:

    def __init__(self, client):
        self.client = client
        self.base_url = config["jsonplaceholder"]["base_url"]

    def get_posts(self):
        return self.client.get(f"{self.base_url}/posts")

    def get_post(self, post_id):
        return self.client.get(f"{self.base_url}/posts/{post_id}")