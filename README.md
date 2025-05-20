# Evaluating the Performance of Open-Vocabulary Object Detection in Low-quality Image

## Description
Dou to the scarcity of suitable image dataset online related to low-quality image, we created a new set of datasets for this study.  Low-quality image dataset is based on the MS COCO 2017 validation images, with images processed into four categories, including lossy compression, image intensity, image noise and image blur.  In total, the dataset comprises 100,000 processed images and is modified by humans to ensure that images are valid in the real world.
<p align="center">
  <img src="cover.png" height="200">
</p>




## Open-source resource
Everyone can download the dataset from [Kaggle](https://www.kaggle.com/datasets/pochihwu/low-quality-image-dataset) and [Google Drive]().
If you would like to create your own low-quality images, you can use our image processing code available on [Github](https://github.com/pochih-code/Low-quality-image-dataset/tree/main/image%20processing).

## Dataset format
- coco2017val image blur (25K images)
  - coco_average_4 (5K images)
  - coco_average_6 (5K images)
  - coco_average_8 (5K images)
  - coco_average_10 (5K images)
  - coco_average_12 (5K images)
- coco2017val lossy compression (25K images)
  - coco_compressed_0 (5K images)
  - coco_compressed_20 (5K images)
  - coco_compressed_40 (5K images)
  - coco_compressed_60 (5K images)
  - coco_compressed_80 (5K images)
- coco2017val gamma correction (25K images)
  - coco_gamma_4 (5K images)
  - coco_gamma_8 (5K images)
  - coco_gamma_12 (5K images)
  - coco_gamma_16 (5K images)
  - coco_gamma_20 (5K images)
- coco2017val image noise (25K images)
  - coco_gaussian_10 (5K images)
  - coco_gaussian_20 (5K images)
  - coco_gaussian_30 (5K images)
  - coco_gaussian_40 (5K images)
  - coco_gaussian_50 (5K images)

## Feedback
We sincerely welcome any feedback on this dataset. Please contact the authors by sending an email to `pochihwu1118 at gmail.com`.
## License and Copyright
The project is open source under `MIT` license. 