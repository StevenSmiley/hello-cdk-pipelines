import json
import pytest

from aws_cdk import core as cdk
from hello.hello_stack import HelloStack


def get_template():
    app = cdk.App()
    HelloStack(app, "hello")
    return json.dumps(app.synth().get_stack("hello").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
