from setuptools import setup, find_packages

setup(
    name="pcinotify",
    version="1.0.0.1",  # Version 1 of the library for the 1.0.0 spec
    packages=find_packages(),
    install_requires=[
        "coarnotify"
    ],
    urls=["https://coar-notify.net/", "https://peercommunityin.org/", "http://cottagelabs.com/"],
    author="Cottage Labs",
    author_email="richard@cottagelabs.com",
    description="PCI-specific COAR Notify patterns and workflow support",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license="Apache2",
    classifiers=[],
    extras_require={
        # 'docs': [
        #     'sphinx',
        #     'sphinx-autoapi'
        # ],
        # 'test': [
        #     "Flask>3.0.0"
        # ],
    }
)
