import sys
import os
import pypdf

scale_factor = 0.5 # 50%
new_width = 612 # px
new_height = 792 # px

# Take the first argument as the folder name, if not print usage
if len(sys.argv) < 3:
    print("Usage: python3 main.py [folder] [scale_factor]")
    print("  Example: python3 main.py /path/to/folder 0.5")
    print("Usage with specific size: python3 main.py [folder] [width] [height]")
    print("  Example: python3 main.py /path/to/folder 400 600")
    sys.exit(1)

if len(sys.argv) == 3:
    scale_factor = float(sys.argv[2])

if len(sys.argv) == 4:
    new_width = float(sys.argv[2])
    new_height = float(sys.argv[3])

# Find all the PDF files in the folder, excluding the scaled ones
folder = sys.argv[1]
pdfs = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".pdf") and not f.endswith("-scaled.pdf")]


# Loop through all the PDF files
for pdf in pdfs:
    reader = pypdf.PdfReader(pdf)
    writer = pypdf.PdfWriter()

    for page in reader.pages[0:]:
        if len(sys.argv) == 3:
            page.scale_by(scale_factor)
        else:
            page.scale_to(new_width, new_height)
        writer.add_page(page)

    # Save the new PDF with -scaled.pdf suffix
    with open(pdf.replace(".pdf", "-scaled.pdf"), "wb") as fp:
        writer.write(fp)
