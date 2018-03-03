import itertools
import copy


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
        return self.get_by_id(member.id) is not None

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def update(self, member):
        all_members = self.get_all()

        for index, current_member in enumerate(all_members):
            if member.id == current_member.id:
                all_members[index] = member
                break

    def get_by_name(self, name):
        return (member for member in self.get_all()

    def get_members_with_posts(self, posts):
        all_members = copy.deepcopy(self.get_all())
        all_product = itertools.product(all_members, posts)

        for member, post in all_product:
            if member.id == post.member_id:
                member.posts.append(post)

        return (member for member in all_members)

    def get_top_two(self, posts):
        members_with_posts = list(self.get_members_with_posts(posts))

        members_with_posts.sort(
            key=lambda member: len(member.posts), reverse=True)

        yield members_with_posts[0]
        yield members_with_posts[1]


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
        return self.get_by_id(post.id) is not None

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def update(self, post):
        all_posts = self.get_all()

        for index, current_post in enumerate(all_posts):
            if post.id == current_post.id:
                all_posts[index] = post
                break
