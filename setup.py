import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aerialist",
    version="0.2.02",
    author="Sajad Khatiri",
    author_email="s.khatiri@gmail.com",
    description="UAV Test Bench",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skhatiri/Aerialist",
    project_urls={"Bug Tracker": "https://github.com/skhatiri/Aerialist/issues"},
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[
        "numpy==1.23.2",
        "similaritymeasures==0.5.0",
        "matplotlib==3.6.1",
        "pyulog==0.9.0",
        "mavsdk==1.4.1",
        "keyboard==0.13.5",
        "python-decouple==3.6",
        "csv-logger==1.3.0",
        "statsmodels==0.13.2",
        "webdav4==0.9.4",
        "ruptures==1.1.7",
        "shapely==1.8.4",
        "validators==0.20.0",
        "pyyaml==6.0",
        "munch==2.5.0",
        "rospkg==1.4.0",
        "defusedxml==0.7.1",
        "tslearn== 0.5.2",
        "h5py==3.9.0",
    ],
    entry_points={"console_scripts": ["aerialist=aerialist.entry:main"]},
)
