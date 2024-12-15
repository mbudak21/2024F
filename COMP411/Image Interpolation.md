![[Pasted image 20241215235136.png]]
(a) Nearest-neighbor. (b) Bilinear. (c) Bicubic. (d) Original HR image


**Interpolation is the process of using known data to estimate values at unknown locations**. This works in two directions and tries to achieve the best approximation of a pixel’s intensity based on the values of surrounding pixels. As it’s an approximation method image will always lose some quality when interpolated.

**Image interpolation occurs especially when an image is resized or distorted(remapped) from a one-pixel grid to another.**

There are plenty of interpolation techniques. Interpolation algorithms can be grouped into two categories.

1. Adaptive
2. Non -adaptive

Adaptive methods change depending on what they are interpolating (sharp edges vs smooth texture) while non-adaptive methods treat all pixel values equally.

This article is mainly focused on non-adaptive methods. Out of the non-adaptive methods also I’m going to discuss

1. Nearest neighbor Interpolation

2. Bilinear Interpolation

3. Bicubic Interpolation

**Nearest Neighbor Interpolation**

This is the most basic form of interpolation. The nearest Neighbor algorithm only considers one pixel, the closest one to the interpolated point. This requires the least processing time of all the interpolation algorithms. And has the effect of simply making each pixel bigger.

**Bilinear Interpolation**

Considers the closest 2x2 neighborhood of known pixel values (total 4 pixels) surrounding the unknown pixel and then takes the weighted average of these values to assign the unknown pixel.

This will create smoother-looking images than the nearest neighbor and needs more processing time.

**Bicubic Interpolation**

Bicubic Interpolation Considers the closest 4x4 neighborhood of known pixel values (total of 16 pixels) surrounding the unknown pixels. Since the known pixels are at various distances from the unknown pixel, closer pixels will give higher weighting.

This produces noticeably sharper images than the nearest neighbor and bilinear interpolations. Bicubic interpolation is an ideal combination of processing time and output quality.
