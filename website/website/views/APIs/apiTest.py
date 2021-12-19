from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response


@api_view()
def test_view(request):
    comment = Comment(email='leila@example.com', content='foo bar')
    serializer = CommentSerializer(comment)
    # return Response(serializer.data)
    ret = {
        'resultCd': '0',
        'msg': 'Signup',
        'result': {}
    }
    ret["result"] = {"name": "Taro", "address": "Tokyo"}
    return Response(ret)


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)


class Comment(object):
    def __init__(self, email, content):
        self.email = email
        self.content = content
