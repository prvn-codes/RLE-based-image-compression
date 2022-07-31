# Image compression using RLE Algorithm

Run Length Encoding is a type of lossless compression method. We have used it to reduce the size of the image matrix by removing redundancy of repeated intensity values in an image by counting the runs of repeated values in the image. Then the code matrix is created where each intensity value is followed by the frequency of its sequential occurrence. This is most useful when data contains multiple runs of repeated values. Text documents are compressed easily and efficiently using this technique.

## How to run

1) Just create the Virtual environment and install the necessary pip packages from `REQUIREMENTS.txt` file

2) Then run `Main.py` with command line arguments.

    ```md
    usage: Main.py [-h] [-e ENCODE] [-d DECODE] [-s SCANNING]

    RLE Encoder and Decoder.

    optional arguments:

    -h, Help,    --help                 show this help message and exit
    -e ENCODE,   --encode   ENCODE      Image to encode.
    -d DECODE,   --decode   DECODE      Compressed file to decode.
    -s SCANNING, --scanning SCANNING    Works if encoding is set. Can be R, RR, ZZ, C, CR.
    ```

## Sample compression Images

### Size Comparision

|Image         |Original|Compressed|Decompressed|
---------------|--------|----------|------------|
|lenna_4bit.bmp|![Original Lena_4bit](./images/lenna_4bit.bmp)128.12KB|88.53KB (Compressed File cannot be shown)   |![Decompressed Lena_4bit](./images/lenna_4bit-decomp.bmp)256.12KB    |
|lenna_8bit.bmp|![Original Lena_8bit](./images/lenna_8bit.bmp)257.05KB|155.6KB (Compressed File cannot be shown)   |![Decompressed Lena_8bit](./images/lenna_8bit-decomp.bmp)257.05KB    |
|lenna_BW.bmp  |![Original lenna_BW](./images/lenna_BW.bmp)32.06KB |15.48KB (Compressed File cannot be shown)   |![Decompressed lenna_BW](./images/lenna_BW-decomp.bmp)32.06KB     |
