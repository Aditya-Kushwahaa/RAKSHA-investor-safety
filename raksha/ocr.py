def extract_text_from_image(uploaded_file):
    """Best-effort OCR. Tesseract must be installed on the machine."""
    try:
        import pytesseract
        from PIL import Image
        image = Image.open(uploaded_file)
        return pytesseract.image_to_string(image).strip()
    except Exception:
        return ""
