class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id

        MemberStore.members.append(member)

        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        result = None
        all_members = self.get_all()

        for member in all_members:
            if id == member.id:
                result = member
                break

        return result

    def entity_exists(self, member):
        return self.get_by_id(member.id) is None

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)


class PostStore:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = PostStore.last_id

        PostStore.posts.append(post)

        PostStore.last_id += 1

    def get_all(self):
        return PostStore.posts

    def get_by_id(self, id):
        for post in PostStore.posts:
            if id == post.id:
                return post
        return None

    def entity_exists(self, post):
        return self.get_by_id(post.id) is None

    def delete(self, id):
        post = self.get_by_id(id)
		PostStore.posts.remove(post)
