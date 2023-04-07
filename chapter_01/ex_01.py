import numpy as np

# BEGINS

print( np.__version__ ) # numpy 버전 확인하기

print( np.ndarray ) # 넘파이 다차원 배열의 클래스

print( np.ndarray.__name__ ) # 넘파이 다차원 배열의 클래스 객체의 이름

print( type( np.ndarray.var ) ) # 파이썬 내부에서 작성된 디스크립터( descripter )의 클래스 객체

# 다차원 배열 클래스에 정의된 속성이나 메소드를 확인하기 위해 이름공간( namespace )을 확인
for i in dir( np.ndarray ):
    if not i.startswith( "_" ):
        if type( np.ndarray.__dict__[ i ] != type( np.ndarray.var ) ):
            print( i )

# ENDS