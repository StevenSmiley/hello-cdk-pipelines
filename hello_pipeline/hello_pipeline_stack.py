from aws_cdk import (
    core as cdk,
    pipelines,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions
)

from hello.hello_stack import HelloStack


class Hello(cdk.Stage):
    def __init__(self, scope: cdk.Stage, id: str, *, env: cdk.Environment = None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)

        HelloStack(self, "Hello")


class HelloPipelineStack(cdk.Stack):
    def __init__(self, scope: cdk.Stack, id: str, *, description: str = None, env: cdk.Environment = None):
        super().__init__(scope, id, description=description, env=env)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CdkPipeline(
            self, "Pipeline",
            cloud_assembly_artifact=cloud_assembly_artifact,
            source_action=codepipeline_actions.GitHubSourceAction(
                action_name='GitHub',
                output=source_artifact,
                oauth_token=cdk.SecretValue.secrets_manager(
                    'GITHUB_TOKEN'),
                owner='StevenSmiley',
                repo='hello-cdk-pipelines',
                branch='main'),
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                build_command='pytest tests',
                synth_command='cdk synth'
            ))

        pipeline.add_application_stage(Hello(self, "TestEnvironment", env=cdk.Environment(
            account="123456789012", region="us-west-2")))
