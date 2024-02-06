import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="tr-nlp-pre-processing",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Oğuzhan Yenen",
    author_email="oguzhanyenen@gmail.com",
    description="Bu kütüphane doğal dil işleme problemlerinde metin önişleme adımlarını kolaylaştırmayı sağlayan bir kütüphanedir.",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
