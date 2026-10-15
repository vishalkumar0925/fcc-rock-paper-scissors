import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    pdf_document = fitz.open(pdf_path)
    img_count = 0

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"extracted_page{page_num + 1}_img{img_index + 1}.{image_ext}"
            image_filepath = os.path.join(output_dir, image_name)

            with open(image_filepath, "wb") as f:
                f.write(image_bytes)
            img_count += 1

    print(f"Total {img_count} images extracted and saved in '{output_dir}'.")
