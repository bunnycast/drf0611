# ^R 전역테스트 / ^F 실패한 부분 테스트
from django.contrib.auth.models import User
from model_bakery import baker
from munch import Munch     # munch > 딕셔너리를 ^T > 4. Introduce Variable 로 변수로 객체화시켜 [],'' 등의 사용을 줄임, 생산성 향상
from rest_framework.test import APITestCase
from rest_framework import status


class UserTestCase(APITestCase):
    def setUp(self) -> None:    # 테스트 실행 전에 기본으로 세팅
        self.users = baker.make('auth.User', _quantity=3)   # model_bakery : 자동으로 모델을 생성해주는 모듈(테스트에 유익)

    def test_should_list(self):
        self.client.force_authenticate(user=self.users[0])      # 강제로 로그인한 상태로 테스트 진행
        response = self.client.get('/api/users')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for user_response, user in zip(response.data['results'], self.users[::-1]):     # pagination으로 결괏값이 역순이 되기 때문에 다시 뒤집어서 반복문 실
            response = Munch(user_response)
            self.assertEqual(response.id, user.id)
            self.assertEqual(response.username, user.username)

    def test_should_create(self):
        data = {'username': 'abc'}
        response = self.client.post('/api/users', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.username, data['username'])

    def test_should_get(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.get(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.username, user.username)

    def test_should_update(self):
        user = self.users[0]
        prev_username = user.username

        data = {'username': 'new'}
        self.client.force_authenticate(user=user)
        response = self.client.put(f'/api/users/{user.id}', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertNotEqual(user_response.username, prev_username)
        self.assertEqual(user_response.username, data['username'])

    def test_should_delete(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.delete(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=user.id).exists())      # 값이 실제로 삭제되었는지 확인
        # self.assertIsNone(response.data)

        # self.fail()  # 테스트 케이스 모두 성공할 시 마지막으로 에러코드 찍음
