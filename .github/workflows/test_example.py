name: Run Python Tests

on:
  push:
    branches:
      - main  # main 브랜치에 푸시될 때 워크플로우 실행
  pull_request:
    branches:
      - main  # PR이 main 브랜치로 만들어질 때 실행

jobs:
  test:
    runs-on: ubuntu-latest  # Ubuntu 환경에서 실행

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3  # 저장소 코드를 checkout

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'  # Python 버전 설정

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt  # requirements.txt에 정의된 패키지 설치

      - name: Run DataMaseryuk.py
        run: |
          python DataMaseryuk.py  # DataMaseryuk.py 파일 실행

      - name: Run tests
        run: |
          pytest tests  # tests 디렉토리 내 모든 테스트 실행
