import numpy as np
from PIL import Image as pimg
from typing import List


def convert_image_to_ndarray(img: pimg.Image) -> np.ndarray:
    return np.array(
        object=img)


def convert_ndarray_to_image(nda: np.ndarray) -> pimg.Image:
    return pimg.fromarray(
        obj=nda)


def open_image_as_ndarray(path: str) -> np.ndarray:
    return convert_image_to_ndarray(
        pimg.open(
            fp=path))


def save_image(img: pimg.Image, path: str) -> None:
    img.save(path)


def get_layer(nda: np.ndarray, n_layer: int) -> np.ndarray:
    assert len(nda.shape) == 3

    l0 = nda.shape[0]
    l1 = nda.shape[1]
    return nda[:, :, n_layer].reshape(l0, l1, 1)


def stack_3d_layers(r: np.ndarray, g: np.ndarray, b: np.ndarray) -> np.ndarray:
    assert len(r.shape) == 3
    assert len(g.shape) == 3
    assert len(b.shape) == 3

    return np.dstack((r, g, b))


def convert_2d_to_3d(nda: np.ndarray) -> np.ndarray:
    assert len(nda.shape) == 2

    l0 = nda.shape[0]
    l1 = nda.shape[1]
    return nda.reshape(l0, l1, 1)


def extract_bayer_layers(nda: np.ndarray, convert_to_3d: bool) -> np.ndarray:

    assert len(nda.shape) == 2

    l0 = nda.shape[0]
    l1 = nda.shape[1]

    assert l0 % 2 == 0
    assert l1 % 2 == 0

    n0 = int(l0 / 2)
    n1 = int(l1 / 2)

    e00 = np.zeros(
        shape=(n0, n1),
        dtype=nda.dtype)

    e01 = np.zeros(
        shape=(n0, n1),
        dtype=nda.dtype)

    e10 = np.zeros(
        shape=(n0, n1),
        dtype=nda.dtype)

    e11 = np.zeros(
        shape=(n0, n1),
        dtype=nda.dtype)

    for a in range(n0):
        for b in range(n1):
            e00[a, b] = nda[2*a, 2*b]
            e01[a, b] = nda[2*a, 2*b+1]
            e10[a, b] = nda[2*a+1, 2*b]
            e11[a, b] = nda[2*a+1, 2*b+1]

    if convert_to_3d:
        return convert_2d_to_3d(e00), convert_2d_to_3d(e01), convert_2d_to_3d(e10), convert_2d_to_3d(e11)
    else:
        return e00, e01, e10, e11


def debayer_ndarray(nda: np.ndarray, mode: str) -> np.ndarray:

    modes = ['gbrg', 'grbg', 'bggr', 'rggb']

    assert mode in modes
    assert len(nda.shape) == 2

    l0 = nda.shape[0]
    l1 = nda.shape[1]

    assert l0 % 2 == 0
    assert l1 % 2 == 0

    e1, e2, e3, e4 = extract_bayer_layers(
        nda=nda,
        convert_to_3d=True)

    if mode == 'gbrg':
        return stack_3d_layers(
            r=e3,
            g=average_layers(e1, e4),
            b=e2)
    elif mode == 'grbg':
        return stack_3d_layers(
            r=e2,
            g=average_layers(e1, e4),
            b=e3)
    elif mode == 'bggr':
        return stack_3d_layers(
            r=e4,
            g=average_layers(e2, e3),
            b=e1)
    elif mode == 'rggb':
        return stack_3d_layers(
            r=e1,
            g=average_layers(e2, e3),
            b=e4)


def debayer_image(path: str, dest: str, mode: str) -> None:
    nda = open_image_as_ndarray(
        path=path)

    if nda.ndim == 3:
        nda=nda[:, :, 0]

    nda_color = debayer_ndarray(
        nda=nda, 
        mode=mode)

    save_image(
        img=convert_ndarray_to_image(
            nda=nda_color),
        path=dest)


def weighted_average_layers(layers: List[np.array], weights: List[float]) -> np.array:
    return np.average(
        a=layers,
        axis=0,
        weights=weights).astype(layers[0].dtype)


def average_layers(l1: np.array, l2: np.array) -> np.array:
    return weighted_average_layers(
        layers=[l1, l2],
        weights=[.5, .5])

