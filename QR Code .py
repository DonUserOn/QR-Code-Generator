# Professional QR Code Generator in Python

import os
import qrcode


OUTPUT_FOLDER = "output"


def create_output_folder():
    """
    Create the output folder if it does not already exist.
    """
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def get_url():
    """
    Get and validate the URL or text from the user.
    """
    while True:
        url = input("Enter the URL or text to generate QR code: ").strip()

        if url:
            return url

        print("Input cannot be empty. Please enter a valid URL or text.")


def get_file_name():
    """
    Get a valid file name from the user.
    """
    file_name = input("Enter output file name without extension: ").strip()

    if not file_name:
        file_name = "qrcode"

    return file_name + ".png"


def generate_qr_code(data, file_name):
    """
    Generate and save the QR code image.
    """
    create_output_folder()

    file_path = os.path.join(OUTPUT_FOLDER, file_name)

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_path)

    return file_path


def main():
    print("=" * 45)
    print("        Python QR Code Generator")
    print("=" * 45)

    data = get_url()
    file_name = get_file_name()

    try:
        saved_path = generate_qr_code(data, file_name)
        print("\nQR Code generated successfully!")
        print(f"Saved at: {saved_path}")

    except Exception as error:
        print("\nAn error occurred while generating the QR code.")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()