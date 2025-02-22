# ============================================================================================
# 파이썬에서 미리 만들어서 제공하는 클래스
# built in class 라고 한다.
# ex) 숫자, 문자 등을 저장할 수 있는 class(int, float, bool, list, tuple 등)
# ============================================================================================
# num = 12
# num.to_bytes()      # 우클릭, goto로 int class의 정보를 확인 할 수 있음.
# ============================================================================================
# 내 프로그램 혹은 프로젝트에서 데이터를 표현하는 class를 만든다. -> 사용자 정의 class
# 생성방법
# class 클래스명:
#       변수
#       메서드(함수) 등
# -> 이것은 class를 생성 한 것이지 메모리에 데이터를 저장한 것은 아니다.
# ============================================================================================
# ex) 계산기 프로그램을 만들고자 한다.
# -> 계산기 테이터 타입을 생성
#    계산기의 속성은 무엇이 있는가?, 연산기능 -> 메서드(함수, 클래스가 하는 역할, 기능)
#    데이터 -> 보통 변수 라고 함.(클래스가 나타내는 속성, 특징, 성질, 외형)
# 클래스명 : calculator
# 변수 : num_1, num_2
# 메서드 : plus(), minus(), multi(), div() 등
# ============================================================================================
class calculator:
    # num_1 = 0
    # num_2 = 0

    # 객체 생성자(constructor)
    # 클래스명()으로 객체 생성 시 호출되는 메서드
    # 파이썬에서 클래스 생성 시에 자주 사용하는 메서드를 미리 만들어서 제공하는 것임.
    # 형태 : def __메서드명__(self)
    # __init__ : 객체 생성 시 변수 생성 및 초기화 하는 경우 사용한다.
    # 즉, 위의 num_1, 2 선언을 해주지 않아도 됨
    def __init__(self, num_1, num_2):     # initialize(초기화)
        print(f'__init__')
        self.num_1 = num_1
        self.num_2 = num_2

    # class의 기능에 해당하는 메서드
    def plus(self, num_1, num_2):
        print(self.num_1 + self.num_2)
        print(num_1 + num_2)

    def minus(self, num_1, num_2):
        print(num_1 - num_2)

    def multi(self, num_1, num_2):
        print(num_1 * num_2)

    def div(self, num_1, num_2):
        print(num_1 / num_2)
# ============================================================================================
# 클래스 사용하기 -> 메모리에 데이터를 저장하겠다. -> 힙에 객체 저장
#       사용방법 -> class명() -> 객체 생성
# ============================================================================================
myapp = calculator(10, 5)
print(f'myapp, {type(myapp)}')
# 클래스 안에 존재하는 메서드 접근 -> 객체변수명,메서드()
myapp.plus(9, 5)
myapp.div(5, 3)


yourapp = calculator(5, 9)
yourapp.plus(1, 5)
# 즉, 필요할 때 마다 객체를 만들어 낼 수 있다.

