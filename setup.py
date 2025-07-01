from pathlib import Path

from setuptools import find_packages, setup

README_TEXT = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

MAINTAINER = "Konstantin Verner"
MAINTAINER_EMAIL = "konst.verner@gmail.com"
REQUIRED_PKGS = [
    "imageio==2.4.1",
    "librosa==0.10.1",
    "hydra-core==1.3.2",
    "moviepy==0.2.3.5",
    "numpy==2.3.0",
    "torch==2.7.0",
    "transformers==4.35.2"
]

print(find_packages("src"))

setup(
    name="subtitles-generator",
    version="0.0.1",
    description="",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url="",
    download_url="",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    package_data={"": ["*.json"]},
    install_requires=REQUIRED_PKGS,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="subtitles, nlp, generation",
    zip_safe=False,  # Required for mypy to find the py.typed file
)
