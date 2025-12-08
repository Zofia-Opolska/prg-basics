class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(self.username)
        for p in self.posts:
            print(p)

username_1='johndoe'
profil = SocialMediaProfile(username_1)
content_1 = 'Hello, world!'
content_2 = 'Had a great day at the park!'
content_3 = "What's up, Natalie? How are you?"
profil.add_post(content_1)
profil.add_post(content_2)
profil.add_post(content_3)
profil.display_timeline()

    