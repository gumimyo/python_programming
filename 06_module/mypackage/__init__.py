# 패키지 초기화 파일
# 페키지가 로드될 때 실행되는 초기화 파일

# 1. 패키지를 import할때 실행되어야하는 초기화 코드(환경 확인, 설정값 로드)
print("__init__")

# 2. 페키지 메타데이터 설정 (버전, 작성자 정보)
VERSION = "1.0.0"

# 3. 패키지 re-export
# from mypackage.mymath import add        #절때 임포트 • • • 단점은 패키지 이름 변환시 전부 다 변경해야함
from .mymath import add  # 상대 임포트
