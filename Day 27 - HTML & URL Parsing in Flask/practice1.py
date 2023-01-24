class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(user):
        if user.is_logged_in:
            function(user)
    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post!")


new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)