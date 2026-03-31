import setuptools

__version__ = '0.0.0'

REPO_NAME = "ml_project"
AUTHOR_USER_NAME = "Sahupavan335"
SRC_REPO = "ml_project"
AUTHOR_EMAIL = "sahupavan335@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Machine Learning End to End Project",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
    