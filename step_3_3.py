from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from step_1 import IN_DIR, OUT_DIR
from step_3_2 import read_text_translated

OUT_3_3 = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75

def read_text_and_fill_area(path: Path):
    parsed = read_text_translated(path)   # ← 4개 값 반환
    img = Image.open(path)
    draw = ImageDraw.Draw(img, "RGBA")    # 알파 채널 OK
    font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=60)

    for row in parsed:
        bbox, orig_text, trans_text, prob = row   # ← 여기 4개로 고쳐야 함!

        # 좌표 변환
        box = [(int(x), int(y)) for x, y in bbox]

        # 정확도에 따라 반투명 빨강/초록 채우기
        fill_color = (255, 0, 0, 100) if prob >= PROB else (0, 255, 0, 100)
        draw.polygon(box, fill=fill_color, outline=(255, 255, 255, 180), width=5)

        # 번역된 한글 텍스트 표시 (흰색으로 선명하게)
        draw.text(xy=box[0], text=trans_text, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))

    img.save(OUT_3_3)
    print(f"결과 저장됨: {OUT_3_3}")

if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_fill_area(path)