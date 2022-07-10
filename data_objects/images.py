from pathlib import Path


def load_images():
    image_dir = Path('static', 'images')
    assert image_dir.exists(), f'Cannot find image directory {image_dir}'

    image_paths = list(image_dir.glob('*'))
    assert image_paths, f'No images found in {image_dir}'

    return [str(Path('..', 'static', 'images', image_path.name)) for image_path in image_paths]
