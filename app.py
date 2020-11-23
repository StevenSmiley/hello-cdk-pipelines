#!/usr/bin/env python3

from aws_cdk import core as cdk
from hello_pipeline.hello_pipeline_stack import HelloPipelineStack


app = cdk.App()
HelloPipelineStack(app, id="Pipeline",
                   env=cdk.Environment(region='us-west-2'))

app.synth()
