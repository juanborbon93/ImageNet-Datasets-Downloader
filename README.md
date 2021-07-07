# ImageNet Downloader

This is ImageNet dataset downloader. **You can create new datasets from subsets of ImageNet by specifying how many 
classes you need and how many images per class you need.** 
This is achieved by using image urls provided by ImageNet API.

## Usage

Set up the environment using the vscode remote container extension
1. create a file `.devcontainer/devcontainer.env` and fill in the following variables (for s3 upload):
    ```
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    ```
2. Build and open the dev container environment. [more info in remote containers](https://code.visualstudio.com/docs/remote/remote-overview)

The following command will randomly select 100 of ImageNet classes with at least 200 images in them and start downloading:
```
python ./downloader.py \
    -data_root /data_root_folder/imagenet \
    -number_of_classes 100 \
    -images_per_class 200
```


The following command will download 500 images from each of selected class:
```
python ./downloader.py 
    -data_root /data_root_folder/imagenet \
    -use_class_list True \
    -class_list n09858165 n01539573 n03405111 \
    -images_per_class 500 
```
You can find class list in [this csv](https://github.com/mf1024/ImageNet-datasets-downloader/blob/master/classes_in_imagenet.csv) where I list every class that appear in the ImageNet with number of total urls and total flickr urls it that class.

# Uploading resulting images to S3

You can upload the downloaded images to an s3 directory by specifiying the `-s3_bucket` and `s3_dir_path` arguments. 

You can do something like this:

```
python ./downloader.py \
    -data_root /data_root_folder/imagenet \
    -number_of_classes 100 \
    -images_per_class 200 \
    -s3_bucket ilox-ml-data \
    -s3_dir_path beltid/other_images
```