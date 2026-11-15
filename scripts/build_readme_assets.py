"""Build the original Gabex README artwork with Pillow (pip install Pillow).

Run from any directory: python scripts/build_readme_assets.py
No downloaded fonts or external services are required. Windows system fonts are
preferred; DejaVu and Pillow's default font provide portable fallbacks.
The GIF deliberately has no loop extension: one four-second pass, then rest.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "readme"
WIDTH, HEIGHT = 1200, 460
SCALE = 2
COLORS = {
    "background": "#0B1119",
    "surface": "#111D28",
    "surface_2": "#152431",
    "grid": "#14212D",
    "line": "#2B3C49",
    "mint": "#B9F5C9",
    "ivory": "#F0F4EB",
    "muted": "#9BAFB9",
    "dim": "#5B7884",
    "button_ink": "#172B21",
}


@lru_cache(maxsize=None)
def font(size: int, role: str = "body") -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = {
        "display": [
            "C:/Windows/Fonts/bahnschrift.ttf",
            "C:/Windows/Fonts/segoeuib.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ],
        "body": [
            "C:/Windows/Fonts/segoeui.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ],
        "mono": [
            "C:/Windows/Fonts/consola.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        ],
    }[role]
    for candidate in candidates:
        if Path(candidate).is_file():
            return ImageFont.truetype(candidate, size * SCALE)
    return ImageFont.load_default(size=size * SCALE)


def box(coords: tuple[float, ...]) -> tuple[int, ...]:
    return tuple(round(value * SCALE) for value in coords)


def line(draw: ImageDraw.ImageDraw, points, fill: str, width: float = 1) -> None:
    draw.line([box(point) for point in points], fill=fill, width=max(1, round(width * SCALE)))


def text(draw, position, content, size=16, fill=None, role="body") -> None:
    draw.text(
        box(position), content, font=font(size, role),
        fill=fill or COLORS["ivory"], anchor="lt",
    )


def tracked(draw, position, content, size=11, tracking=1.8, fill=None) -> None:
    x, y = position
    current_font = font(size, "mono")
    for character in content:
        draw.text(box((x, y)), character, font=current_font,
                  fill=fill or COLORS["muted"], anchor="lt")
        x += draw.textlength(character, font=current_font) / SCALE + tracking


def panel(draw, coords, radius=12, fill=None, outline=None) -> None:
    draw.rounded_rectangle(
        box(coords), radius=round(radius * SCALE),
        fill=fill or COLORS["surface"], outline=outline or COLORS["line"], width=SCALE,
    )


def ease_out_cubic(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return 1 - (1 - value) ** 3


def back_out(value: float, overshoot=1.25) -> float:
    value = max(0.0, min(1.0, value)) - 1
    return 1 + (overshoot + 1) * value ** 3 + overshoot * value ** 2


def button_scale(seconds: float) -> float:
    if seconds < 1.55:
        return 1.0
    if seconds < 1.67:
        return 1 - 0.034 * ease_out_cubic((seconds - 1.55) / 0.12)
    if seconds < 2.23:
        return 0.966 + 0.034 * back_out((seconds - 1.67) / 0.56)
    return 1.0


def render(seconds: float, final=False) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), COLORS["background"])
    draw = ImageDraw.Draw(canvas)

    # Architectural rules: a quiet rhythm rather than texture or blur.
    for x in range(708, WIDTH, 28):
        line(draw, [(x, 24), (x, HEIGHT - 24)], COLORS["grid"], 0.6)
    for y in range(36, HEIGHT, 28):
        line(draw, [(708, y), (WIDTH - 24, y)], COLORS["grid"], 0.6)
    line(draw, [(48, 74), (1152, 74)], COLORS["line"])
    line(draw, [(48, 420), (1152, 420)], COLORS["line"])
    line(draw, [(692, 98), (692, 397)], COLORS["line"])

    # A simple original geometric G mark, paired with editable system typography.
    draw.rounded_rectangle(box((48, 30, 76, 58)), radius=5 * SCALE,
                           outline=COLORS["mint"], width=2 * SCALE)
    line(draw, [(68, 38), (57, 38), (57, 50), (68, 50), (68, 45), (63, 45)],
         COLORS["mint"], 1.6)
    tracked(draw, (92, 38), "GABEX / DESIGN DIRECTION", size=11, tracking=1.4)
    tracked(draw, (920, 38), "COLLECTION 01 / 2026", size=10, tracking=1.0)

    # Core labels never disappear or wait for the animation.
    text(draw, (45, 105), "GABEX", size=102, role="display")
    text(draw, (45, 205), "DESIGNS", size=102, role="display", fill=COLORS["mint"])
    text(draw, (49, 326), "UI/UX direction / motion with purpose.", size=22)
    text(draw, (49, 361), "36 original briefs. Distinct by design.", size=15,
         fill=COLORS["muted"])
    tracked(draw, (49, 395), "GABRIEL MARTINEZ PORTILLO", size=11,
            tracking=1.45, fill=COLORS["muted"])

    # The card shells settle once; text is present even in the first frame.
    settled = 1.0 if final else ease_out_cubic(seconds / 0.8)
    offset = 10 * (1 - settled)
    x, y = 740, 98 + offset
    panel(draw, (x, y, 1152, y + 116))
    text(draw, (762, y + 15), "36", size=65, role="display", fill=COLORS["mint"])
    line(draw, [(857, y + 24), (857, y + 90)], COLORS["line"])
    tracked(draw, (880, y + 29), "ORIGINAL BRIEFS", size=11, tracking=1.1)
    text(draw, (880, y + 57), "Ideas with a build plan.", size=16)
    text(draw, (880, y + 82), "LAYOUT / STATES / MOTION", size=10,
         role="mono", fill=COLORS["dim"])

    labels = [(740, "BUSINESS"), (882, "CORPORATE"), (1024, "GOVERNMENT")]
    for index, (chip_x, label) in enumerate(labels):
        local_progress = 1.0 if final else ease_out_cubic((seconds - index * 0.07) / 0.7)
        chip_y = 232 + 5 * (1 - local_progress)
        panel(draw, (chip_x, chip_y, chip_x + 128, chip_y + 33), radius=5,
              fill=COLORS["surface_2"])
        label_width = draw.textlength(label, font=font(10, "mono")) / SCALE
        text(draw, (chip_x + (128 - label_width) / 2, chip_y + 11), label,
             size=10, role="mono", fill=COLORS["ivory"])

    lower_y = 282 + 6 * (1 - settled)
    panel(draw, (740, lower_y, 1152, lower_y + 115))
    tracked(draw, (760, lower_y + 17), "MOTION / SPRING-STYLE", size=9, tracking=0.7)

    # A complete quiet reference curve is present; the mint trace draws once.
    curve = []
    for index in range(65):
        value = index / 64
        curve.append((1024 + value * 106, lower_y + 31 - back_out(value) * 18))
    line(draw, curve, COLORS["dim"], 1)
    progress = 1.0 if final else ease_out_cubic(seconds / 2.7)
    count = max(2, round(progress * (len(curve) - 1)) + 1)
    line(draw, curve[:count], COLORS["mint"], 1.5)

    # Only the button's visual face compresses. The containing panel is stable.
    face = Image.new("RGBA", (372 * SCALE, 48 * SCALE), (0, 0, 0, 0))
    face_draw = ImageDraw.Draw(face)
    face_draw.rounded_rectangle(box((0, 0, 371, 47)), radius=6 * SCALE,
                                fill=COLORS["mint"])
    text(face_draw, (19, 15), "Review direction", size=16, fill=COLORS["button_ink"])
    line(face_draw, [(332, 24), (352, 24)], COLORS["button_ink"], 1.6)
    line(face_draw, [(346, 18), (352, 24), (346, 30)], COLORS["button_ink"], 1.6)
    scale = 1.0 if final else button_scale(seconds)
    scaled = face.resize((round(face.width * scale), round(face.height * scale)),
                         Image.Resampling.LANCZOS)
    button_x = 760 * SCALE + (face.width - scaled.width) // 2
    button_y = round((lower_y + 49) * SCALE) + (face.height - scaled.height) // 2
    canvas.paste(scaled, (button_x, button_y), scaled)

    text(draw, (49, 435), "UI / UX  —  VISUAL SYSTEMS  —  GSAP CHOREOGRAPHY", size=10,
         role="mono", fill=COLORS["dim"])
    text(draw, (941, 435), "CRAFTED TO BE DISTINCT.", size=10,
         role="mono", fill=COLORS["muted"])
    return canvas.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def build_badges() -> None:
    labels = [
        ("36 DESIGN BRIEFS", 224),
        ("RESPONSIVE UI / UX", 262),
        ("GSAP MOTION SPECS", 264),
        ("ALL RIGHTS RESERVED", 286),
    ]
    x = 0
    items = []
    for label, width in labels:
        items.append(
            f'<rect x="{x}" y="2" width="{width}" height="38" rx="7" '
            'fill="#111D28" stroke="#2B3C49" />'
            f'<circle cx="{x + 17}" cy="21" r="3" fill="#B9F5C9" />'
            f'<text x="{x + 31}" y="26" font-size="12" fill="#F0F4EB" '
            'font-family="Consolas, monospace" letter-spacing="0.5">'
            f'{label}</text>'
        )
        x += width + 12
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="44" '
        'viewBox="0 0 1080 44" role="img" aria-labelledby="title">'
        '<title id="title">36 design briefs; responsive UI and UX; GSAP motion '
        'specifications; all rights reserved</title>' + ''.join(items) + '</svg>\n'
    )
    (OUT / "gabex-badges.svg").write_text(svg, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    static = render(4.0, final=True)

    # 40 moving frames at 80 ms, then a final 800 ms hold: exactly four seconds.
    frames = [render(index * 0.08) for index in range(40)] + [static]
    durations = [80] * 40 + [800]
    palette = static.quantize(colors=160, method=Image.Quantize.MEDIANCUT)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(
        OUT / "gabex-banner.gif", save_all=True, append_images=indexed[1:],
        duration=durations, optimize=True, disposal=1,
        # Intentionally omit `loop`: GIF players show one pass, then hold.
    )
    build_badges()
    with Image.open(OUT / "gabex-banner.gif") as animation:
        actual_frames = animation.n_frames
        total_duration = 0
        for index in range(actual_frames):
            animation.seek(index)
            total_duration += animation.info.get("duration", 0)
        # Use the exact decoded final frame for a seamless static alternative.
        animation.convert("RGB").save(OUT / "gabex-banner-static.png", optimize=True)
        print(f"GIF: {animation.size}, {actual_frames} frames, {total_duration} ms, "
              f"{(OUT / 'gabex-banner.gif').stat().st_size:,} bytes; "
              f"loop extension: {'loop' in animation.info}")
    print(f"Static: {WIDTH}x{HEIGHT}, {(OUT / 'gabex-banner-static.png').stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
