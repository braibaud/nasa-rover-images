# NASA Rover Images Downloader

Allows downloading raw images taken by `Perseverance` and `Curiosity` rovers. The file `dl.py` is located in the `commands` folder.

```
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
