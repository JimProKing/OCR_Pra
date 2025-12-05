from pathlib import Path
from PIL import Image, ImageDraw
from step_1 import IN_DIR, OUT_DIR
from step_2_2 import read_text

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75

def read_text_and_draw_line(path: Path):
    parsed = read_text(path)  # EasyOCR 결과 가져오기
    img = Image.open(path)
    draw = ImageDraw.Draw(img)

    for raw in parsed:
        bbox, text, prob = raw  # 올바르게 unpack

        # bbox를 [(x1,y1), (x2,y2), ...] 형태로 변환
        box = [(int(point[0]), int(point[1])) for point in bbox]

        # 색상 결정 (정확도 75% 이상: 빨강, 이하: 초록)
        color = (255, 0, 0) if prob >= PROB else (0, 255, 0)
        draw.polygon(box, outline=color, width=10)

        # 텍스트 + 정확도 표시 (위쪽에)
        top_left = box[0]  # 좌상단 좌표
        label = f"{text} ({prob:.2f})"
        draw.text((top_left[0], top_left[1] - 30), label, fill=color)

    img.save(OUT_2_3)
    print(f"결과 저장됨: {OUT_2_3}")

if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_draw_line(path)