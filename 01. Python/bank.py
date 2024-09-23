# 뱅킹 시스템에서 계좌 정보를 관리할 클래스
import joblib
import os

class Account:
    # Account 객체의 멤버 변수를 초기화할 생성자
    def __init__(self, owner, accNo, balance):
        self.__owner__ = owner
        self.__accNo__ = accNo
        self.__balance__ = balance

    # 잔고조회
    def getBalance(self):
        return self.__balance__

    # 입금
    def deposit(self, amount):
        self.__balance__ += amount

    # 계좌정보 조회
    def showAccountInfo(self):
        return f'소유주: {self.__owner__}, 계좌번호: {self.__accNo__}, 잔고: {self.__balance__}'

    # 출금
    def withdraw(self, amount):
        if self.__balance__ >= amount:
            self.__balance__ -= amount
        else:
            raise InvalidTransactionExpection('출금 잔고가 부족합니다.')

    # 이체
    def transfer(self, amount, target):
        if self.__balance__ >= amount:
            self.__balance__ -= amount
            target.deposit(amount)
        else:
            raise InvalidTransactionException('이체 잔고가 부족합니다.')

    # 계좌번호 조회
    def getAccNo(self):
        return self.__accNo__

    accNo = property(getAccNo)


# 뱅킹 시스템에서 부적절한 거래가 이뤄졌을때 발행할 사용자 예외
class InvalidTransactionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

# 뱅킹 시스템에서 업무 로직을 정의한 클래스
# 계좌 등록, 등록된 계좌 검색, 전체 계좌 목록 조회
class BankManager:
    def __init__(self):
        self.accountList = []

    # 계좌 등록
    def addAccount(self, a):
        self.accountList.append(a)


    # 등록된 계좌 검색
    # 리턴 값: 검색된 Account 객체. 단, 검색 결과가 없을 경우 None을 반환
    def searchAccount(self, accNo):
        result = None
        for a in self.accountList:
            if a.accNo == accNo:
                result = a
                break
        return result

    # 등록된 계좌 목록 반환
    def getAllAccountList(self):
        return self.accountList

    # 등록된 계좌 목록 파일 저장
    def saveData(self):
        joblib.dump(self.accountList, 'bank.dat')

    # 파일에 저장된 계좌 목록 정복 읽기
    def loadData(self):
        if os.path.exists('bank.dat'):
            self.accountList = joblib.load('bank.dat')
