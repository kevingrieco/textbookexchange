from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .models import Conversation, Message
from .views import view_conversation

# Create your tests here.

User = get_user_model()

class DirectMessageTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.recipient = User.objects.create_user(username="recipient", password="pass")
        self.client.login(username='user', password='pass')
        self.factory = RequestFactory()

    def test_message_user(self):
        conversation = Conversation(user_a=self.user, user_b=self.recipient)
        conversation.save()
        message = Message(
            content="Hello", 
            sender=self.user, 
            recipient=self.recipient,
            conversation=conversation
            )
        message.save()
        conversation.latest = message.time
        conversation.save()
        test_assert = conversation.get_latest_message().content
        self.assertEqual("Hello", test_assert)
    
    def test_create_conversation(self):
        conversation = Conversation(user_a=self.user, user_b=self.recipient)
        conversation.save()
        self.assertIsInstance(Conversation.objects.get(user_a=self.user, user_b=self.recipient), Conversation)

    def test_can_view_conversation(self):
        conversation = Conversation(user_a=self.user, user_b=self.recipient)
        conversation.save()
        request = self.factory.get('direct_message:view_conversation', pk=conversation.pk)
        request.user = self.user
        response = view_conversation(request, pk=conversation.pk)
        response.client = self.client
        self.assertEqual(response.status_code, 200)

    def test_redirect_for_other_conversation(self):
        user_c = User.objects.create_user(username="user_c", password="pass")
        user_d = User.objects.create_user(username="user_d", password="pass")
        conversation = Conversation(user_a=user_c, user_b=user_d)
        conversation.save()
        request = self.factory.get('direct_message:view_conversation', pk=conversation.pk)
        request.user = self.user
        response = view_conversation(request, pk=conversation.pk)
        response.client = self.client
        self.assertEqual(response.status_code, 302)
