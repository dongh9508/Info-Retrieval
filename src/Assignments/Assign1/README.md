Assign1 - Stemming, Konlpy 실습
===
* Python3 설치.

* [Stemmer 패키지](https://pypi.org/project/stemming/1.0) 설치 (명령창에서 아래 명령 실행)

    `python -m pip install stemming`

* 다음 코드를 testStem.py 파일로 저장 후 명령창에서 python testStem.py 실행

    ```python
        from stemming.porter2 import stem
        print(stem('automates'))
    ```

* 다음 단어들의 스테밍 결과들이 출력되도록 위 코드(testStem.py)를 수정하시오.

    >automate, automated, automates, automating, automation, operate, operating, operates, operation, operative, operatives, operational

* 다음 문장에서 명사들을 추출하여 출력하는 코드(testNoun.py)를 작성하시오. (Konlpy의 Okt 사용할 것, [참조](https://konlpy-ko.readthedocs.io/ko/v0.5.1/api/konlpy.tag/#okt-class)

    > 뭄바이에서 발생한 테러와 관련하여 한국대사관에서는 한국인들의 사망과 부상 피해를 조사하고 있다.
