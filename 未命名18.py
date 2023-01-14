import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string


def rndChar():
    """
    生成随机字母+数字
    :return:
    """
    return random.choice(string.ascii_lowercase + string.digits)

def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 130), random.randint(0, 130), random.randint(0, 130))


def check_code(width=180, height=60, char_length=5, font_file='micross.ttf', font_size=30):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype(font_file, font_size)
    # 创建Draw对象:
    draw = ImageDraw.Draw(img, mode='RGB')
    # # 填充每个像素:
    # for x in range(width):
    #     for y in range(height):
    #         draw.point((x, y), fill=rndColor())

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(10, 20)
        draw.text([i * 25+6, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(50):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())



    # 画干扰线
    for i in range(3):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line((x1, y1, x2, y2), fill=rndColor())

    # img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)


if __name__ == '__main__':
    # 1. 直接打开
    img,code = check_code()
    img.show()

    # 2. 写入文件
    # img, code = check_code()
    # print(code)
    # with open('code3.png','wb') as f:
    #     img.save(f, format='png')

    # 3. 写入内存(Python3)
    # from io import BytesIO
    # stream = BytesIO()
    # img.save(stream, 'png')
    # stream.getvalue()
    # print(stream.getvalue())