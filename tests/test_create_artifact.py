import pytest
import wandb as wb
from wbutils import create_artifact


def test_create_artifact():
    artifact = create_artifact(artifact_name='dummy', artifact_type='dummy-type', description='Dummy artifact',
                               metadata={}, files={})
    assert isinstance(artifact, wb.Artifact)
