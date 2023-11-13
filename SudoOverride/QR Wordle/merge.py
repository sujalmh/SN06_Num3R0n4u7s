from PIL import Image

def merge_images(save_path, correct_positions, output_path):
    ext=".jpg"
    img_path = save_path+correct_positions[0]+ext
    img = Image.open(img_path)
    
    # Calculate the size of the final merged image
    width, height = img.size
    img.close()
    merged_width = width * 8
    merged_height = height * 8
    # Create a new image with white background
    merged_image = Image.new("RGB", (merged_width, merged_height), "white")

    # Paste each image onto the merged image based on its position
    for i in range(8):
        for j in range(8):
            position = i * 8 + j
            img_path = save_path+correct_positions[int(position)]+ext
            print(correct_positions[int(position)],position)
            img = Image.open(img_path)
            merged_image.paste(img, box=(j * width, i * height))

    # Save the merged image
    merged_image.save(output_path)
    print(f"Merged image saved to {output_path}")

save_path = "images/"
output_path = "merged_image.png"

with open('positions.txt') as f:
    raw = f.readlines()

raw=raw[0][1:-1].split(',')
correct_positions={}
for i in raw:
    key, value=i.split(":")
    correct_positions[int(float(key.lstrip("w.")))]=value[2:-1]
print(len(correct_positions))

merge_images(save_path, correct_positions, output_path)