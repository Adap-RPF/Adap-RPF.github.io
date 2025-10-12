from pathlib import Path
from pdf2image import convert_from_path

SEARCH_DIR = Path("static/images")
DPI = 300
FORMAT = "PNG"

def convert_pdf_to_png(pdf_path: Path):
    print(f"🔍 Found PDF: {pdf_path.name}")
    try:
        pages = convert_from_path(pdf_path, dpi=DPI, fmt="png", use_cropbox=False)
        for i, page in enumerate(pages):
            output_file = pdf_path.with_suffix(f"_{i+1}.png") if len(pages) > 1 else pdf_path.with_suffix(".png")
            page.save(output_file, FORMAT)
            print(f"✅ Saved: {output_file.resolve()}")
    except Exception as e:
        print(f"❌ Error converting {pdf_path.name}: {e}")

def main():
    pdf_files = list(SEARCH_DIR.rglob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {SEARCH_DIR.resolve()}")
        return
    print(f"🚀 Starting conversion for {len(pdf_files)} PDF(s)...\\n")
    for pdf in pdf_files:
        convert_pdf_to_png(pdf)
    print("\\n🎉 Done! All PDFs converted without cropping.")

if __name__ == "__main__":
    main()

