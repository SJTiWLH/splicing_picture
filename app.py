import base64
from PIL import Image
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/<username>') #路由
def index(username):
    return "hello %s" % username

# @app.route('/splicing_picture, methods=['POST'], strict_slashes=False)
@app.route('/splicing_picture', methods=['POST'])
def splicing_picture():
    base64_image_data = request.form.get('base64_image_data')
    # 选择保存的文件格式和文件名
    # base64_image_data = im
    output_file_format = "png"  # 可以是 'png' 或 'jpg'
    output_file_name = f"output_image.{output_file_format}"

    image_data = base64.b64decode(base64_image_data)
    with open(output_file_name, "wb") as file:
        file.write(image_data)
    # print(f"图片已保存为 {output_file_name}")

    # 加载验证码图片
    image1 = Image.open('output_image.png')
    image2 = Image.open('k.png')
    # 获取图片的宽度和高度
    width1, height1 = image1.size
    width2, height2 = image2.size
    # 创建一个新的图片，宽度为原始图片的宽度，高度为所有图片高度之和
    total_width = max(width1, width2)
    total_height = height1 + height2
    new_image = Image.new('RGB', (total_width, total_height))

    # 将图片粘贴到新图片中
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, height1))

    # 保存拼接后的图片
    new_image.save('new_image.png')
    with open(f"new_image.png", "rb") as image_file:  # 转换为base64
        splicing_im = base64.b64encode(image_file.read()).decode()
    # print(splicing_im)
    return splicing_im

app.run(host='0.0.0.0', port=5000)

# with open(f"screenshot_row1_col1.png", "rb") as image_file:  # 转换为base64
#     im = base64.b64encode(image_file.read()).decode()
# print(im)
# newim = splicing_picture(im)
# print(newim)








