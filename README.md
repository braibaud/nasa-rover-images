# NASA Rover Images

## Raw Image Downloader

Allows downloading raw images taken by `Perseverance` and `Curiosity` rovers. The file `dl.py` is located in the `commands` folder.

```bash
usage: dl.py [-h] [-c CACHE_LOCATION] [-r {perseverance, curiosity}] [-t] [-i]

NASA raw images downloader

optional arguments:

  -h                             Show this help message and exit.
                                 Same as --help

  -c CACHE_LOCATION              Location of the cache folder base.
                                 Same as --cache_location
                        
  -r {perseverance, curiosity}   Name of the rover.
                                 Same as --rover_name

  -t                             Set to download thumbnail images also.
                                 Only downloads full frames if not set.
                                 Same as --thumbnail

  -i                             Incremental updates only. 
                                 Stops at the first page with no more updates.
                                 Same as --incremental
```

The images will be saved in the `{CACHE_LOCATION}/{ROVER_NAME}` folder.

In this folder, an additional file named `images_{ROVER_NAME}.npz` keeps track of the images already downloaded.

## Post-Processing

### Notebook

The **Jupyter** notebook `NASA Rover Images Post-Processing - DEBAYERING.ipynb` provides some examples of image `DEBAYERING` using `python`.

![](samples/debayer.jpg)


### Stitched and Processed Images


#### A landscape panorama (Perseverance, Sol 4)

* **Full size image:** [samples/panorama-2.jpg](samples/panorama-2.jpg)
* **Resolution:** 7236x3074 (22MP)
* **Stitch:** 80 images
* **Source Credits:** NASA / JPL-Caltech

![](samples/panorama-2-small.jpg)


#### Another landscape panorama (Perseverance, Sol 4)

* **Full size image:** [samples/panorama-3.jpg](samples/panorama-3.jpg)
* **Resolution:** 5207x1048 (5MP)
* **Stitch:** 79 images
* **Source Credits:** NASA / JPL-Caltech

![](samples/panorama-3-small.jpg)


#### Landscape panorama (Curiosity, Sol 3042)

 * **Full size image:** [samples/panorama-5.jpg](samples/panorama-5.jpg)
 * **Resolution:** 9721x2082 (20MP)
 * **Stitch:** 72 images
 * **Source Credits:** NASA / JPL-Caltech

![](samples/panorama-5-small.jpg)


#### Close view of "Mt-Mercou" (Curiosity, Sol 3051)

 * **Full size image:** [samples/panorama-4.jpg](samples/panorama-4.jpg)
 * **Resolution:** 8697x2932 (25MP)
 * **Stitch:** 97 images
 * **Source Credits:** NASA / JPL-Caltech

![](samples/panorama-4-small.jpg)


#### Bottom-left view of "Mt-Mercou" (Curiosity, Sol 3058)

 * **Full size image:** [samples/view-1.jpg](samples/view-1.jpg)
 * **Resolution:** 4381x2436 (11MP)
 * **Stitch:** 40 images
 * **Source Credits:** NASA / JPL-Caltech

![](samples/view-1-small.jpg)

