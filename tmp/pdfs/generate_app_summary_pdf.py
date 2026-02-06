from __future__ import annotations

from datetime import date
from pathlib import Path
import textwrap

PAGE_WIDTH = 612
PAGE_HEIGHT = 792
MARGIN_X = 48
TOP_Y = 760
BOTTOM_Y = 48
CONTENT_WIDTH = PAGE_WIDTH - (MARGIN_X * 2)


def esc(text: str) -> str:
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


ops: list[str] = []
y = TOP_Y


def draw_line(text: str, size: int = 10, bold: bool = False, leading: int = 12) -> None:
    global y
    font = '/F2' if bold else '/F1'
    ops.append(f"BT {font} {size} Tf 1 0 0 1 {MARGIN_X} {y} Tm ({esc(text)}) Tj ET")
    y -= leading


def draw_heading(text: str) -> None:
    global y
    draw_line(text, size=12, bold=True, leading=14)


def draw_paragraph(text: str, size: int = 10, max_chars: int = 92, leading: int = 12) -> None:
    wrapped = textwrap.wrap(text, width=max_chars)
    for line in wrapped:
        draw_line(line, size=size, bold=False, leading=leading)


def draw_bullet(text: str, size: int = 10, max_chars: int = 84, leading: int = 12) -> None:
    wrapped = textwrap.wrap(text, width=max_chars)
    if not wrapped:
        return
    draw_line(f"- {wrapped[0]}", size=size, bold=False, leading=leading)
    for line in wrapped[1:]:
        draw_line(f"  {line}", size=size, bold=False, leading=leading)


def spacer(amount: int = 6) -> None:
    global y
    y -= amount


draw_line('Travelingwebsite App Summary', size=18, bold=True, leading=22)
draw_line(f"Repository snapshot summary generated {date.today().isoformat()}", size=9, leading=14)
spacer(2)

draw_heading('What it is')
draw_paragraph(
    'A SvelteKit web app that presents a horizontally scrolling, section-based portfolio experience branded as Full Scope Media.'
)
draw_paragraph(
    'The repository is also configured as a packageable Svelte library, but the primary user-facing artifact here is the root route showcase page.'
)
spacer()

draw_heading("Who it's for")
draw_bullet(
    'Primary persona appears to be a traveling photographer or small creative studio owner (Ryan Champion / Full Scope Media) who needs a visual portfolio and booking-oriented landing page.'
)
spacer()

draw_heading('What it does')
for item in [
    'Renders a full-viewport horizontal rail of sections (hero, work, journal, services, schedule, testimonials, about, contact).',
    'Uses a fixed top navigation bar with section buttons that programmatically jump to section indices.',
    'Presents static content blocks for travel chapters and client testimonials with responsive card layouts.',
    'Implements custom wheel-to-horizontal scrolling behavior for desktop navigation.',
    'Supports keyboard navigation (Arrow keys, PageUp/PageDown, Home/End) across sections.',
    'Includes a styled contact form UI shell (name, phone, email) with no submit handler connected to backend routes.',
    'Uses reduced-motion preference checks and scroll snapping for smoother, accessible navigation behavior.'
]:
    draw_bullet(item)
spacer()

draw_heading('How it works (repo evidence only)')
for item in [
    'Route composition: `src/routes/+page.svelte` defines page sections and static arrays (`navLinks`, `cards`, `testimonials`) and nests everything inside `HorizontalScroller`.',
    'Component behavior: `src/lib/components/HorizontalScroller.svelte` owns the rail, maps wheel and keyboard events to horizontal movement, and uses `IntersectionObserver` to track the visible section.',
    'State/data flow: `src/lib/stores/scroller.ts` exposes `scrollerHandle` and `activeIndex`; the page reads `scrollerHandle` to call `scrollToIndex` when nav buttons are clicked.',
    'Styling stack: global Tailwind import plus custom CSS variables in `src/app.css`; route-level styles in `src/routes/+page.svelte`.',
    'Server/data layer: Drizzle + Postgres setup exists in `src/lib/server/db/index.ts` and `src/lib/server/db/schema.ts`, but no API routes or UI wiring to that DB were found in this repo.'
]:
    draw_bullet(item)
spacer()

draw_heading('How to run (minimal)')
for item in [
    'Install dependencies: `npm install`.',
    'Start local dev server: `npm run dev -- --open`.',
    'Optional quality check: `npm run check`.',
    'Node version requirement: Not found in repo. Production deploy URL/instructions: Not found in repo.'
]:
    draw_bullet(item)

if y < BOTTOM_Y:
    raise SystemExit(f'Content overflowed one page (final y={y}).')

content = "\n".join(ops).encode('latin-1', errors='replace')

objects: list[bytes] = []


def add_obj(data: bytes) -> int:
    objects.append(data)
    return len(objects)


catalog_id = add_obj(b"<< /Type /Catalog /Pages 2 0 R >>")
pages_id = add_obj(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
page_id = add_obj(
    b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>"
)
font1_id = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
font2_id = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
stream_obj = (
    b"<< /Length " + str(len(content)).encode('ascii') + b" >>\nstream\n" + content + b"\nendstream"
)
content_id = add_obj(stream_obj)

assert [catalog_id, pages_id, page_id, font1_id, font2_id, content_id] == [1, 2, 3, 4, 5, 6]

pdf = bytearray()
pdf.extend(b"%PDF-1.4\n")
offsets = [0]

for idx, obj in enumerate(objects, start=1):
    offsets.append(len(pdf))
    pdf.extend(f"{idx} 0 obj\n".encode('ascii'))
    pdf.extend(obj)
    pdf.extend(b"\nendobj\n")

xref_start = len(pdf)
pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode('ascii'))
pdf.extend(b"0000000000 65535 f \n")
for off in offsets[1:]:
    pdf.extend(f"{off:010d} 00000 n \n".encode('ascii'))

pdf.extend(
    (
        "trailer\n"
        f"<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        "startxref\n"
        f"{xref_start}\n"
        "%%EOF\n"
    ).encode('ascii')
)

output_path = Path('output/pdf/travelingwebsite-app-summary.pdf')
output_path.write_bytes(pdf)
print(output_path.resolve())
print(f'Final y={y}')
