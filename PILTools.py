from PIL import Image


class PILTools:
    @staticmethod
    def conv_img_array(image):
        width = image.size[0]
        height = image.size[1]

        result = []

        for x in range(0, width):
            result.append([])
            for y in range(0, height):
                result[x].append(
                    image.getpixel(
                        (x, y)
                    )
                )

        return result

    @staticmethod
    def compress(image, compress_factor):
        return image.resize(
            (
                int(image.size[0] / compress_factor),
                int(image.size[1] / compress_factor)
            ),
            Image.ANTIALIAS
        )
