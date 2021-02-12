# Starscape-Module

## Introduction
The following Python Module is an Astronomy repository using ideas of Image Segmentation to filter/contour out images of stars from star clusters or any Astronomical data obtained by professional telescopes like VLT or the Hubble Space Telescope based on the brightness of stars, redshift and temperature.The project uses idea of Computer Vision and in all uses the OpenCV, Matalab and PIL package of Python to segment out the necessary data. 
 
 Data that can be studied using the module include both Raw Data and Processed data like:
 
![hd17](https://user-images.githubusercontent.com/77894161/105863173-9b8a2100-6016-11eb-8a16-509677bc07d6.jpg)

or, processed data like
![eso2](https://user-images.githubusercontent.com/77894161/105863682-23702b00-6017-11eb-925f-13e100039926.jpg)

## Segment Stars based on brightness
The module as mentioned above can be used to filter stars based on brightness. For the purpose we essentially take the required image from the user and convert the iamge to Binary scale. Correspondingly, we binarize the given image. The module asks the user to provide a threshold to binarize the image so that, other bright objects in the background like nebulas or other astronomical objects can be segmnted out from the binary image leaving us with just the stars. Foe example the image above has a lot of bright objects apart from the stars and it can be correspondingly be difficult to segment the stars with the raw iamge, hence we have to use sufficient threshold to binarize the data, to help us give the necessary output.

Now, note that without proper thresholding the image looks like this

![eso2binary](https://user-images.githubusercontent.com/77894161/105865385-e60c9d00-6018-11eb-908c-68e02a879d9f.jpg)

With proper thresholding the binarized image will look like this, that gives us sufficient data to segment out just the stars based on the brightness.

![eso2binary](https://user-images.githubusercontent.com/77894161/105866060-95497400-6019-11eb-90c7-c44dc5dc735d.jpg)

With the binary data, we estimate the number of pixels covered by a particular star and thereby, use that to segment the stars based on the brightness. The user is asked to input a range, in comparison to the brightest and the dimmest object in the picture and in reference to that we segment the stars within the reuired range. For a particular range inputed by the user the data, if the photo given by the user is this,

![ESO](https://user-images.githubusercontent.com/77894161/105866672-3cc6a680-601a-11eb-9346-5d7edb429bd7.jpg)

Then, we generate a contour around the stars, that are in the required range and we get this:

![Eso_bright](https://user-images.githubusercontent.com/77894161/105867390-0e959680-601b-11eb-830b-d0946ac4ae56.jpg)

Then, this output gets stored in the respective directory.

## Segment Stars based on Red Shift
The module further provides you an option to filter out stars in an image based on their redshift. It creates a necessary kernel corresponding to a mask to contour the specific stars in the photograph. The image like in the previous function is obatined from the user, and then it gets converted to the HSV format from the RGB format. Now, based on  the shift, we create a mask and a corresponding kernel. Using this kernel and the mask created, we draw contour around the objects that fall in range, now to prevent noise from being calibrated we run a loop to just contour the objects that are greater than a certain pixel length, the function correspondingly returns the count of the number of stars within that shift and also the contoured image.

Suppose, if we consider the previous image input by the user, then for a range [136,87,11] and [180,255, 255], the count is 147 and the image output is as follows,

![Eso_shift](https://user-images.githubusercontent.com/77894161/105868766-8617f580-601c-11eb-86bf-a38c353ece25.jpg)

## Segment Stars based on Temperature
Finally, using the module the user can give a temperature range and based on that temperature range, the module segments the regions on the photo that host that temperature range. The module does it by deriving the necessary B-V index from the Temperature using the formula:

![image](https://user-images.githubusercontent.com/77894161/105882504-ba46e280-602b-11eb-86e3-475bb957464d.png)
(source:wikipedia)

The obtained BV index is then calibrated to the corresponding RGB index, using the bv2rgb() function in the Python Module. Since, RGB index may vary due to differences in Telescopes used to click the picture, it must be calibrated to suit the system, because of this the module will ask if you want to calibrate the system to your required settings. For that you must know, the BV index of atleast two stars in the picture. After that, the system uses the BV index to calculate the RGB using the module specific function and compares it to the actua; RGB index of the star in the picture. Now, depending on the difference, it creates a Lagrange Interpolation to map the calculate RGB values to the Calibrated RGB values, thereby accounting for the error. If you are unawre of B-V index of any stars or astronomical objects in your system, you may proceed without Calibrating the Module to your specific settings. Below, I provide the difference in output when the module is calibrated and when it's not.

### Without Calibrating the Module:

![Eso_temperature](https://user-images.githubusercontent.com/77894161/105885336-06dfed00-602f-11eb-88cb-78c4559371a6.jpg)

### With Calibrating the Module:

![Eso_temperature](https://user-images.githubusercontent.com/77894161/105886306-41965500-6030-11eb-855c-1671800c26dd.jpg)

So, we can observe that calibration we can reduce significant error generated by the module, hence it is preference to calibrate the system before analysis.



 #### It also hosts a well calibrated database of star temperatures and corresponding RGB gradient. The temperaturedatabase() function maps cerain specific temeprature ranges to a specific RGB index generalised over many common telescopes.

This module can be used by students and professional alike to study, analyse and implement the necessary Astronomical data, to obtain required results.
