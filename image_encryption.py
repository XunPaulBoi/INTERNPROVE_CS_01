from PIL import Image


def encrypt_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Get the pixel data
        pixels = img.load()

        # Swap the red and blue pixel values
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)

        # Save the encrypted image
        img.save('encrypted_image.png')


def decrypt_image(image_path):
    # Open the encrypted image file
    with Image.open(image_path) as img:
        # Get the pixel data
        pixels = img.load()

        # Swap the red and blue pixel values (reverse of encryption)
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (b, g, r)

        # Save the decrypted image
        img.save('decrypted_image.png')


# Example usage
encrypt_image('original_image.png')
decrypt_image('encrypted_image.png')