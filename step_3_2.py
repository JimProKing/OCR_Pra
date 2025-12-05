# step_2_5.py 또는 utils.py에 추가하세요
from pathlib import Path
from googletrans import Translator  # pip install googletrans==4.0.0-rc1

# 전역 번역기 (속도 빠르게 한 번만 생성)
translator = Translator()

def read_text_translated(path: Path) -> list:
    """
    기존 read_text() 결과를 받아서
    텍스트 부분만 한국어로 번역해서 반환!
    
    반환 형식:
    [(bbox, 원본_텍스트, 번역된_텍스트, 정확도), ...]
    """
    # 기존 read_text() 그대로 사용!
    from step_2_2 import read_text   # 또는 같은 파일에 있으면 생략
    results = read_text(path)        # ← 당신이 원하던 그 함수!

    translated_results = []
    
    for bbox, text, prob in results:
        # 이미 한글이면 번역 안 함
        if any('가' <= char <= '힣' for char in text):
            translated_text = text
        else:
            try:
                translated = translator.translate(text, src='en', dest='ko')
                translated_text = translated.text
            except:
                translated_text = text  # 실패하면 원본 유지
        
        translated_results.append((bbox, text, translated_text, prob))
    
    return translated_results


# 테스트용
if __name__ == "__main__":
    from step_1 import IN_DIR
    path = IN_DIR / "ocr.jpg"
    
    print("번역 전후 비교:")
    result = read_text_translated(path)
    print(result)
    # for bbox, orig, trans, prob in result:
    #     print(f"{orig} → {trans} (정확도: {prob:.1%})")