from .directory import get_wb_directory, get_artifacts_directory

TRAIN_SPLIT = 'train'
VAL_SPLIT = 'val'
TEST_SPLIT = 'test'
SPLITS = [TRAIN_SPLIT, VAL_SPLIT, TEST_SPLIT]

INCLUDE_STUBS = [
    '.py',
    '.ipynb',
    'requirements.txt',
    'README.md',
]

EXCLUDE_STUBS = [
    '.git',
    '.vscode',
    '.idea',
    get_wb_directory(),
    get_artifacts_directory()
]


def include_files(path: str) -> bool:
    """ Decide which file to include when code is logged """
    # See https://docs.wandb.ai/ref/python/run#log_code
    for stub in EXCLUDE_STUBS:
        if stub in path:
            return False

    for stub in INCLUDE_STUBS:
        if path.endswith(stub):
            return True
    return False
