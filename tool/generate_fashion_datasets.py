import os
from shutil import copyfile
from pathlib import Path
from PIL import Image

def crop_image(img_dir, save_dir):
	img = Image.open(img_dir)
	imgcrop = img.crop((40, 0, 216, 256))
	imgcrop.save(save_dir)

# path for downloaded fashion images
root_fashion_dir = 'D:\\Archivos UADE\\PFI\\Desarrollos\\ADGAN\\deepfashion'
assert len(root_fashion_dir) > 0, 'please give the path of raw deep fashion dataset!'

train_images = []
train_f = open(os.path.join(root_fashion_dir,'train.lst'), 'r')
for lines in train_f:
	lines = lines.strip()
	if lines.endswith('.jpg'):
		train_images.append(lines)

test_images = []
test_f = open(os.path.join(root_fashion_dir,'test.lst'), 'r')
for lines in test_f:
	lines = lines.strip()
	if lines.endswith('.jpg'):
		test_images.append(lines)

train_path = os.path.join(root_fashion_dir,'train')
if not os.path.exists(train_path):
	os.mkdir(train_path)

for item in train_images:
	id_index = item.index("id_0")
	path = item.replace(item[id_index + 11 :], "\\" + item[id_index + 11 :])
	from_ = os.path.join(root_fashion_dir, path)
	from_ = from_.replace("\\", "/")
	to_ = os.path.join(train_path, path)
	to_ = to_.replace("\\", "/")
#	to_array = to_.split("/")
#	to_array.pop()
#	Path("/".join(to_array)).mkdir(parents=True, exist_ok=True)
	#os.system('copy %s %s' %(from_, to_))
#	copyfile(from_, to_)
	crop_image(from_, to_)

test_path = os.path.join(root_fashion_dir,'test')
if not os.path.exists(test_path):
	os.mkdir(test_path)

for item in test_images:
	id_index = item.index("id_0")
	path = item.replace(item[id_index + 11 :], "\\" + item[id_index + 11 :])
	from_ = os.path.join(root_fashion_dir, path)
	from_ = from_.replace("\\", "/")
	to_ = os.path.join(test_path, path)
	to_ = to_.replace("\\", "/")	
	#to_array = to_.split("/")
	#to_array.pop()
	#Path("/".join(to_array)).mkdir(parents=True, exist_ok=True)
	#os.system('copy %s %s' %(from_, to_))
	#copyfile(from_, to_)
	crop_image(from_, to_)