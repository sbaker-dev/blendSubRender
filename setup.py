# Copyright (C) 2020 Samuel Baker

DESCRIPTION = "Sub processing multiple instances of blender for rending"
LONG_DESCRIPTION = """
# blendSubRender

Sub processing multiple instances of blender for rendering. When rending the general principle is applying more 
resources and completely the current frame is faster approach to getting the end result. Most of the time this works, 
but there are a few, additively niece cases, when it can be faster to subprocess an animation. 

More information available on [github][repo]

[repo]: https://github.com/sbaker-dev/blendSubRender

"""
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

DISTNAME = 'blendSubRender'
MAINTAINER = 'Samuel Baker'
MAINTAINER_EMAIL = 'samuelbaker.researcher@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = "https://github.com/sbaker-dev/blendSubRender"
VERSION = "0.01.0"
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [

    ]

PACKAGES = [
    "blendSubRender",
]

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

if __name__ == "__main__":

    from setuptools import setup

    import sys

    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("blendSubRender requires python >= 3.7.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        license=LICENSE,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )
