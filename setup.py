import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="hello",
    version="0.0.1",

    description="A sample CDK Python app with a CDK Pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Steven Smiley",

    package_dir={"": "hello"},
    packages=setuptools.find_packages(where="hello"),

    install_requires=[
        "aws-cdk.core~=1.73.0",
        "aws-cdk.aws_iam~=1.73.0",
        "aws-cdk.aws_sqs~=1.73.0",
        "aws-cdk.aws_sns~=1.73.0",
        "aws-cdk.aws_sns_subscriptions~=1.73.0",
        "aws-cdk.aws_s3~=1.73.0",
        "aws-cdk.pipelines~=1.73.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 1 - Planning",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",

        "Typing :: Typed",
    ],
)
