import json

from django.http import JsonResponse
from rest_framework.views import APIView
from etc.assginpdc import producer_primes

from alg.figureup import two_sum, three_sum, count_primes
from alg.verify import verify_url
__import__()


class FigureUp(APIView):
    @classmethod
    def figure(cls, api_two, api_three, nums, target):

        if api_two.get("exist"):
            stdout_data = two_sum(nums, target)
            return JsonResponse({"status:": 200, "data": stdout_data})
        if api_three.get("exist"):
            stdout_data = three_sum(nums, target, {})
            return JsonResponse({"status:": 200, "data": stdout_data})
        return JsonResponse({"status": 500, "msg": "url include three or two", "error:": "url is error"})

    def get(self, request):
        """

        @rtype: json
        """
        try:
            url = request.path
            nums = json.loads(request.GET.get("nums"))
            target = json.loads(request.GET.get("target"))

            api_two = verify_url(url=url, ver="/api/twosum/")
            api_three = verify_url(url=url, ver="/api/threesum/")
            return self.figure(api_two, api_three, nums, target)
        except Exception as e:
            return JsonResponse({"status": 500, "msg": f"{e}", "error:": "error argument"})

    def post(self, request):
        """

        @rtype: json
        """
        try:
            url = request.path
            nums = request.data['nums']
            target = request.data['target']

            api_two = verify_url(url=url, ver="/api/twosum/")
            api_three = verify_url(url=url, ver="/api/threesum/")
            return self.figure(api_two, api_three, nums, target)
        except Exception as e:
            return JsonResponse({"status": 500, "msg": f"{e}", "error:": "error argument"})


# class CountPrimes(APIView):
#     def get(self, request):
#
#         try:
#             _count_ls = dict()
#             loop_int = request.GET.getlist('primes')
#             loop_int = list(map(lambda x: int(x), loop_int))
#             for i in loop_int:
#                 _count_ls.update({i: count_primes(i)})
#         except Exception as e:
#             return JsonResponse({"status": 500, "msg": f"{e} ", "error:": "error argument"})
#         return JsonResponse({"status:": 200, "data": _count_ls})
#
#     def post(self, request):
#
#         try:
#             _count_ls = dict()
#             loop_int = request.data.get('primes')
#             print(loop_int)
#             loop_int = list(map(lambda x: int(x), loop_int))
#             for i in loop_int:
#                 _count_ls.update({i: count_primes(i)})
#         except Exception as e:
#             return JsonResponse({"status": 500, "msg": f"{e} ", "error:": "error argument"})
#         return JsonResponse({"status:": 200, "data": _count_ls})


class CountPrimes(APIView):
    def get(self, request):

        try:
            _count_ls = dict()
            loop_int = request.GET.getlist('primes')
            loop_int = list(map(lambda x: int(x), loop_int))
            if len(loop_int) > 10:
                for i in range(1, 3):
                    loop = loop_int[(i - 1) * 3: i * 3]
                    producer_primes(loop)
                loop_int = loop_int[3 * len(loop_int) // 3: ]
            for i in loop_int:
                _count_ls.update({i: count_primes(i)})
        except Exception as e:
            return JsonResponse({"status": 500, "msg": f"{e} ", "error:": "error argument"})
        return JsonResponse({"status:": 200, "data": _count_ls})

    def post(self, request):

        try:
            _count_ls = dict()
            loop_int = request.data.get('primes')
            print(loop_int)
            loop_int = list(map(lambda x: int(x), loop_int))
            for i in loop_int:
                _count_ls.update({i: count_primes(i)})
        except Exception as e:
            return JsonResponse({"status": 500, "msg": f"{e} ", "error:": "error argument"})
        return JsonResponse({"status:": 200, "data": _count_ls})
